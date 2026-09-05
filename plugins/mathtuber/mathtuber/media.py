"""Measured, cached media operations. No creative model orchestration."""
import importlib.metadata
import json
import math
import os
from pathlib import Path
import shutil
import subprocess
import sys
import time
from .captions import make_ass
from .creative import validate_plan, soundtrack, validate_delivery
from .state import ProductionError, digest, file_hash, within, atomic_json

ROOT = Path(__file__).resolve().parents[1]

def run(args, timeout=600, env=None, cwd=None):
    started = time.monotonic()
    try:
        r = subprocess.run([str(a) for a in args], capture_output=True, text=True,
                           timeout=timeout, env=env, cwd=cwd)
    except subprocess.TimeoutExpired as exc:
        raise ProductionError("TIMEOUT", f"{Path(str(args[0])).name} exceeded {timeout}s") from exc
    if r.returncode:
        raise ProductionError("WORKER_FAILED", r.stderr[-5000:] or r.stdout[-5000:])
    return r.stdout, time.monotonic() - started

def python_executable():
    explicit = os.environ.get("MATHTUBER_PYTHON")
    if explicit:
        if not Path(explicit).is_file():
            raise ProductionError("MISSING_RUNTIME", explicit)
        return explicit
    home = Path(os.environ.get("MATHTUBER_RUNTIME_HOME", Path.home() / ".local/share/mathtuber"))
    candidate = home / "media" / ("Scripts/python.exe" if os.name == "nt" else "bin/python")
    if candidate.exists():
        return str(candidate)
    return sys.executable

def probe(path):
    output, _ = run(["ffprobe", "-v", "error", "-show_format", "-show_streams", "-of", "json", path])
    info = json.loads(output)
    info["duration"] = float(info["format"].get("duration", 0))
    if info["duration"] <= 0 or not math.isfinite(info["duration"]):
        raise ProductionError("INVALID_MEDIA", f"Invalid duration: {path}")
    return info

def audio_fingerprint(project, scene):
    imported = None
    if project.data.get("speech", {}).get("provider") == "wav":
        imported = file_hash(Path(scene["audio_source"]).expanduser())
    return digest({"narration": scene["narration"], "speech": project.data.get("speech", {}),
                   "imported": imported, "worker": file_hash(ROOT / "workers/speech.py")})

def audio_for(project, scene):
    result = project.artifact("audio:" + scene["id"], audio_fingerprint(project, scene))
    if not result:
        raise ProductionError("AUDIO_REQUIRED", f"Synthesize current narration for {scene['id']}")
    return result

def synthesize(project, sid):
    scenes = project.data["scenes"] if sid == "all" else [project.scene(sid)]
    pending, results = [], []
    for scene in scenes:
        fp = audio_fingerprint(project, scene)
        cached = project.artifact("audio:" + scene["id"], fp)
        if cached:
            results.append({"scene": scene["id"], "cached": True, "artifact": cached})
        else:
            pending.append({"scene": scene, "fingerprint": fp,
                            "output": str(project.root / "audio" / f"{scene['id']}-{fp[:12]}.wav")})
    if pending:
        request = project.root / ".mathtuber/speech-request.json"
        atomic_json(request, {"speech": project.data.get("speech", {}), "items": pending})
        _, elapsed = run([python_executable(), ROOT / "workers/speech.py", request], timeout=1800)
        for item in pending:
            info = probe(item["output"])
            timing_path = Path(item["output"]).with_suffix(".words.json")
            timing = json.loads(timing_path.read_text()) if timing_path.exists() else {"method":"unavailable","words":[]}
            metadata = {"duration": info["duration"], "word_timing": timing,
                        "narration": item["scene"]["narration"],
                        "speech": project.data.get("speech", {}), "batch_seconds": elapsed}
            artifact = project.record("audio:" + item["scene"]["id"], item["fingerprint"], item["output"], metadata)
            results.append({"scene": item["scene"]["id"], "cached": False, "artifact": artifact})
    return results

def render_fingerprint(project, scene, quality, execution=None):
    if execution is None:
        previous = project.artifact(f"render:{quality}:{scene['id']}")
        execution = previous["metadata"].get("execution", "native") if previous else "native"
    source = within(project.root, scene["source"])
    if not source.exists():
        raise ProductionError("SOURCE_REQUIRED", str(source))
    dependencies = {scene["source"]: file_hash(source)}
    for relative in scene.get("dependencies", []):
        path = within(project.root, relative)
        dependencies[relative] = file_hash(path)
    for pattern in ("scenes/_shared/**/*.py", "assets/**/*"):
        for path in project.root.glob(pattern):
            if path.is_file():
                dependencies[str(path.relative_to(project.root))] = file_hash(path)
    audio = audio_for(project, scene)
    return digest({"dependencies": dependencies, "audio": audio["sha256"], "scene": scene,
                   "format": project.data.get("format", {}), "quality": quality,
                   "worker": file_hash(ROOT / "workers/render.py"),
                   "components": file_hash(ROOT / "components.py"),
                   "runtime": runtime_versions(execution), "execution": execution})

_VERSION_CACHE = {}
def runtime_versions(execution="native"):
    if execution == "docker":
        output, _ = run(["docker", "image", "inspect", "manimcommunity/manim:v0.20.1", "--format", "{{.Id}}"])
        return {"image_id": output.strip()}
    py = python_executable()
    if py not in _VERSION_CACHE:
        out, _ = run([py, "-c", "import importlib.metadata,json; print(json.dumps({k:importlib.metadata.version(k) for k in ['manim','numpy']}))"])
        _VERSION_CACHE[py] = json.loads(out)
    return _VERSION_CACHE[py]

def render(project, sid, quality, execution):
    scene = project.scene(sid)
    fp = render_fingerprint(project, scene, quality, execution)
    key = f"render:{quality}:{sid}"
    cached = project.artifact(key, fp)
    if cached:
        return {"cached": True, "artifact": cached}
    audio = audio_for(project, scene)
    fmt = project.data.get("format", {})
    fps = fmt.get("fps", 30) if quality == "final" else min(15, fmt.get("fps", 30))
    width, height = fmt.get("width", 1080), fmt.get("height", 1920)
    if quality == "preview":
        ratio = min(1, 640 / max(width, height))
        width, height = max(2, round(width * ratio / 2) * 2), max(2, round(height * ratio / 2) * 2)
    frames = math.ceil(audio["metadata"]["duration"] * fps)
    target = frames / fps
    output_dir = project.root / "renders" / sid / quality / fp[:12]
    output_dir.mkdir(parents=True, exist_ok=True)
    request = project.root / ".mathtuber/render-request.json"
    atomic_json(request, {"source": str(within(project.root, scene["source"])), "class_name": scene["class_name"],
                          "duration": target, "width": width, "height": height, "fps": fps,
                          "media_dir": str(output_dir), "components": str(ROOT), "project": str(project.root)})
    timeout = project.data.get("budgets", {}).get("render_timeout_seconds", 600)
    if execution == "docker":
        payload = json.loads(request.read_text())
        payload.update(source="/input/"+scene["source"], components="/plugin", project="/input", media_dir="/output")
        atomic_json(request, payload)
        _, elapsed = run(["docker", "run", "--rm", "--network", "none", "--read-only",
                          "--cap-drop", "ALL", "--security-opt", "no-new-privileges",
                          "--pids-limit", "128", "--memory", "4g", "--cpus", "2",
                          "--user", f"{os.getuid()}:{os.getgid()}",
                          "--tmpfs", "/tmp:rw,size=512m", "-e", "HOME=/tmp",
                          "-v", f"{ROOT}:/plugin:ro", "-v", f"{request}:/request.json:ro",
                          "-v", f"{project.root / 'scenes'}:/input/scenes:ro",
                          "-v", f"{project.root / 'assets'}:/input/assets:ro",
                          "-v", f"{output_dir}:/output:rw", "-w", "/output",
                          "--entrypoint", "python", "manimcommunity/manim:v0.20.1",
                          "/plugin/workers/render.py", "/request.json"], timeout=timeout)
    else:
        # Native mode is trusted-code only, not filesystem isolation.
        env = {k: v for k, v in os.environ.items() if k in ("PATH", "HOME", "TMPDIR", "LANG", "LC_ALL", "SYSTEMROOT")}
        env["PYTHONPATH"] = os.pathsep.join([str(ROOT), str(project.root)])
        _, elapsed = run([python_executable(), ROOT / "workers/render.py", request], timeout=timeout, env=env, cwd=project.root)
    candidates = [p for p in output_dir.rglob("scene.mp4") if "partial_movie_files" not in p.parts]
    if len(candidates) != 1:
        raise ProductionError("RENDER_OUTPUT_MISSING", f"Expected one scene.mp4, found {len(candidates)}")
    path = candidates[0]
    info = probe(path)
    if abs(info["duration"] - target) > max(.15, 2/fps):
        raise ProductionError("TIMING_MISMATCH", f"Scene {sid}: rendered {info['duration']:.3f}s, narration schedule {target:.3f}s; revise cue timing")
    artifact = project.record(key, fp, path, {"duration": info["duration"], "target_duration": target,
                                           "width": width, "height": height, "fps": fps,
                                           "render_seconds": elapsed, "execution": execution})
    return {"cached": False, "artifact": artifact}

def current_renders(project, quality="final"):
    results = []
    for scene in project.data["scenes"]:
        fp = render_fingerprint(project, scene, quality)
        artifact = project.artifact(f"render:{quality}:{scene['id']}", fp)
        if artifact is None:
            raise ProductionError("RENDER_REQUIRED", f"Current {quality} render required for {scene['id']}")
        results.append((scene, artifact, audio_for(project, scene)))
    return results

def assembly_fingerprint(project):
    rows = current_renders(project)
    return digest({"scenes": [(s["id"], r["sha256"], a["sha256"]) for s,r,a in rows],
                   "soundtrack": soundtrack(project), "sound_worker": file_hash(ROOT / "mathtuber/creative.py"),
                   "format": project.data.get("format", {}), "captions": project.data.get("captions", True),
                   "worker": file_hash(Path(__file__)), "caption_worker": file_hash(ROOT / "mathtuber/captions.py")})

def srt_time(seconds):
    ms = round(seconds * 1000)
    h, ms = divmod(ms, 3600000)
    m, ms = divmod(ms, 60000)
    s, ms = divmod(ms, 1000)
    return f"{h:02}:{m:02}:{s:02},{ms:03}"

def assemble(project):
    validate_plan(project)
    rows = current_renders(project)
    fp = assembly_fingerprint(project)
    cached = project.artifact("export", fp)
    if cached:
        return {"cached": True, "artifact": cached}
    export_dir = project.root / "exports" / fp[:12]
    export_dir.mkdir(parents=True, exist_ok=True)
    clips, captions, offset = [], [], 0.0
    for scene, render_artifact, audio in rows:
        sid = scene["id"]
        clip = export_dir / f"{sid}.mp4"
        duration = render_artifact["metadata"]["duration"]
        run(["ffmpeg", "-y", "-v", "error", "-i", render_artifact["absolute_path"], "-i", audio["absolute_path"],
             "-map", "0:v:0", "-map", "1:a:0", "-c:v", "copy", "-af", "apad", "-t", str(duration), "-c:a", "aac", "-ar", "48000", clip])
        clips.append(clip)
        words = audio["metadata"].get("word_timing", {}).get("words", [])
        if words:
            group = []
            for index, word in enumerate(words):
                group.append(word)
                if len(group) >= 7 or word["text"].endswith((".", "?", "!", ";")) or index == len(words)-1:
                    start = offset + max(0, min(duration, group[0]["start"]))
                    end = offset + min(duration, max(group[-1]["end"], group[0]["start"]+.1))
                    text = " ".join(w["text"] for w in group)
                    captions.append(f"{len(captions)+1}\n{srt_time(start)} --> {srt_time(end)}\n{text}\n")
                    group = []
        else:
            captions.append(f"{len(captions)+1}\n{srt_time(offset)} --> {srt_time(offset+duration)}\n{scene['narration']}\n")
        offset += duration
    listing = export_dir / "concat.txt"
    # Clip basenames are safe validated identifiers, avoiding ffconcat quoting issues.
    listing.write_text("".join(f"file '{p.name}'\n" for p in clips))
    final = export_dir / "video.mp4"
    _, elapsed = run(["ffmpeg", "-y", "-v", "error", "-f", "concat", "-safe", "1", "-i", listing,
                      "-c", "copy", "-movflags", "+faststart", final])
    caption_path = export_dir / "captions.srt"
    caption_path.write_text("\n".join(captions))
    score = soundtrack(project)
    if score:
        run(["ffmpeg", "-y", "-v", "error", "-i", "video.mp4", "-i", score["path"],
             "-filter_complex", f"[0:a]asplit=2[voice][side];[1:a]volume={score['gain_db']}dB,apad[bed];[bed][side]sidechaincompress=threshold=0.025:ratio=6:attack=15:release=250[duck];[voice][duck]amix=inputs=2:duration=first:normalize=0,loudnorm=I=-16:LRA=7:TP=-1.5[out]",
             "-map", "0:v:0", "-map", "[out]", "-c:v", "copy", "-c:a", "aac", "-ar", "48000", "-b:a", "192k", "-t", str(offset), "mixed.mp4"], timeout=1800, cwd=export_dir)
        os.replace(export_dir / "mixed.mp4", final)
    caption_settings = project.data.get("captions", {})
    if isinstance(caption_settings, dict) and caption_settings.get("burn_in"):
        fmt = project.data.get("format", {})
        (export_dir / "captions.ass").write_text(make_ass(caption_path.read_text(), fmt.get("width",1080), fmt.get("height",1920)))
        burned = export_dir / "captioned.mp4"
        run(["ffmpeg", "-y", "-v", "error", "-i", "video.mp4", "-vf", "ass=captions.ass",
             "-af", "loudnorm=I=-16:LRA=7:TP=-1.5", "-ar", "48000", "-c:v", "libx264", "-preset", "fast",
             "-crf", "19", "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "160k", "-movflags", "+faststart",
             "captioned.mp4"], timeout=1800, cwd=export_dir)
        os.replace(burned, final)
    info = probe(final)
    if abs(info["duration"] - offset) > .25:
        raise ProductionError("ASSEMBLY_DURATION", "Assembled timeline differs from the complete scene timeline")
    validate_delivery(project, info["duration"])
    maximum = project.data.get("brief", {}).get("max_seconds", 180)
    minimum = project.data.get("brief", {}).get("min_seconds", 0)
    if not minimum <= info["duration"] <= maximum:
        raise ProductionError("DURATION_BUDGET", f"Export {info['duration']:.2f}s outside {minimum}–{maximum}s; revise narration")
    project.record("captions", fp, caption_path, {"timing": "synthesis_predicted_or_section_fallback", "count": len(captions)})
    artifact = project.record("export", fp, final, {"duration": info["duration"], "scene_count": len(rows),
                                                  "assembly_seconds": elapsed, "captions": str(caption_path)})
    return {"cached": False, "artifact": artifact}

def verify(project):
    fp = assembly_fingerprint(project)
    artifact = project.artifact("export", fp)
    if not artifact:
        raise ProductionError("ASSEMBLY_REQUIRED", "Assemble the current complete timeline")
    info = probe(artifact["absolute_path"])
    validate_delivery(project, info["duration"])
    brief = project.data.get("brief", {})
    if not brief.get("min_seconds", 0) <= info["duration"] <= brief.get("max_seconds", 180):
        raise ProductionError("DURATION_BUDGET", "Export duration does not meet the current brief")
    video = [s for s in info["streams"] if s["codec_type"] == "video"]
    audio = [s for s in info["streams"] if s["codec_type"] == "audio"]
    fmt = project.data.get("format", {})
    if len(video) != 1 or len(audio) != 1:
        raise ProductionError("INVALID_STREAMS", "Expected one video and one narration stream")
    if (video[0]["width"], video[0]["height"]) != (fmt.get("width",1080), fmt.get("height",1920)):
        raise ProductionError("INVALID_DIMENSIONS", "Wrong export dimensions")
    run(["ffmpeg", "-v", "error", "-xerror", "-i", artifact["absolute_path"], "-f", "null", "-"], timeout=600)
    report = {"passed": True, "scope": "mechanical; semantic and acoustic review still required",
              "export_sha256": artifact["sha256"], "snapshot": project.snapshot(),
              "duration": info["duration"], "scenes": len(project.data["scenes"])}
    atomic_json(project.root / "reviews/mechanical.json", report)
    return report

def bundle(project, sid=None, quality="preview"):
    if sid:
        scene = project.scene(sid)
        fp = render_fingerprint(project, scene, quality)
        artifact = project.artifact(f"render:{quality}:{sid}", fp)
        if not artifact:
            raise ProductionError("RENDER_REQUIRED", sid)
        audio = audio_for(project, scene)["absolute_path"]
    else:
        fp = assembly_fingerprint(project)
        artifact = project.artifact("export", fp)
        audio = artifact["absolute_path"] if artifact else None
    if not artifact:
        raise ProductionError("ASSEMBLY_REQUIRED", "No current export")
    folder = project.root / "reviews" / (sid or "final") / artifact["sha256"][:12]
    folder.mkdir(parents=True, exist_ok=True)
    duration = probe(artifact["absolute_path"])["duration"]
    if sid:
        times = project.scene(sid).get("review_times", [0.1, duration*.25, duration*.5, duration*.75, max(0,duration-.1)])
    else:
        times, offset = [], 0
        for scene, rendered, _ in current_renders(project):
            dur = rendered["metadata"]["duration"]
            times.extend([offset+.1, offset+dur/2, offset+max(0,dur-.1)])
            offset += dur
    frames = []
    for i, timestamp in enumerate(times):
        if not isinstance(timestamp, (float,int)) or not 0 <= timestamp < duration:
            raise ProductionError("INVALID_CUE", f"Review timestamp outside clip: {timestamp}")
        path = folder / f"frame-{i:03}.png"
        run(["ffmpeg", "-y", "-v", "error", "-ss", str(timestamp), "-i", artifact["absolute_path"], "-frames:v", "1", path])
        frames.append({"time": timestamp, "path": str(path), "sha256": file_hash(path)})
    result = {"schema_version": 1, "scope": sid or "final", "snapshot": project.snapshot(),
              "video": artifact["absolute_path"], "video_sha256": artifact["sha256"],
              "audio": audio, "frames": frames, "coverage": "sampled frames; inspect motion/audio separately",
              "narration": [s["narration"] for s in project.data["scenes"] if not sid or s["id"] == sid]}
    atomic_json(folder / "bundle.json", result)
    return result
