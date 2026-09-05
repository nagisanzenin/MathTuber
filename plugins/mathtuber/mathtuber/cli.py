"""Agent-facing JSON CLI; all creative choices stay in the host agent."""
import argparse
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import time
import uuid
from . import __version__
from .state import Project, ProductionError, read_json, atomic_json, create, digest, file_hash
from . import media
from .creative import validate_plan
from . import profiles


def doctor():
    result = {"version": __version__, "engine_python": sys.version.split()[0],
              "media_python": media.python_executable(), "reasoning_api_required": False,
              "executables": {k: shutil.which(k) for k in ("ffmpeg", "ffprobe", "latex", "dvisvgm", "uv")},
              "render_isolation": "docker: restricted mounts and no network; native: trusted code, no OS sandbox"}
    try:
        result["media_versions"] = media.runtime_versions()
    except ProductionError as exc:
        result["media_error"] = str(exc)
    result["ready"] = all(result["executables"][k] for k in ("ffmpeg","ffprobe","latex","dvisvgm")) and "media_versions" in result
    return result

def status(project):
    rows = []
    for scene in project.data["scenes"]:
        sid = scene["id"]
        state = {"id": sid, "audio": bool(project.artifact("audio:"+sid, media.audio_fingerprint(project,scene)))}
        for quality in ("preview","final"):
            try:
                state[quality] = bool(project.artifact(f"render:{quality}:{sid}", media.render_fingerprint(project,scene,quality)))
            except ProductionError:
                state[quality] = False
        rows.append(state)
    export = None
    try:
        export = project.artifact("export", media.assembly_fingerprint(project))
    except ProductionError:
        pass
    snapshot = project.snapshot()
    with project.connect() as db:
        reviews = [json.loads(r[0]) for r in db.execute("SELECT payload FROM reviews WHERE snapshot=?",(snapshot,))]
    accepted = any(r.get("scope") == "final" and r.get("verdict") == "accept" for r in reviews)
    next_actions = []
    if any(not r["audio"] for r in rows): next_actions.append("synthesize narration")
    if any(not r["preview"] for r in rows): next_actions.append("write scene code and render previews")
    if any(not r["final"] for r in rows): next_actions.append("inspect evidence, revise and render final scenes")
    if not export: next_actions.append("assemble complete current timeline")
    elif not accepted: next_actions.append("verify, inspect final review bundle and record semantic/acoustic review")
    else: next_actions.append("deliver export; publish only if requested")
    return {"project": str(project.root), "scenes": rows, "export": export,
            "snapshot": snapshot, "accepted": accepted, "next_actions": next_actions}

def record_review(project, data):
    if data.get("snapshot") != project.snapshot():
        raise ProductionError("STALE_REVIEW", "Artifacts changed since this evidence was generated")
    if data.get("verdict") not in ("accept","revise"):
        raise ProductionError("INVALID_REVIEW", "verdict must be accept or revise")
    for key in ("reviewer", "scope", "evidence", "checks", "findings"):
        if key not in data:
            raise ProductionError("INVALID_REVIEW", f"Missing {key}")
    if not isinstance(data["evidence"],list) or not data["evidence"]:
        raise ProductionError("INVALID_REVIEW", "List the actual inspected media evidence")
    for item in data["evidence"]:
        path = Path(item["path"]).resolve()
        if not path.is_relative_to(project.root) or not path.is_file() or file_hash(path) != item["sha256"]:
            raise ProductionError("INVALID_EVIDENCE", "Evidence path/hash mismatch")
    if project.data.get("creative"):
        methods = data.get("methods", {})
        for domain in ("math", "visual", "timing", "audio"):
            method = methods.get(domain, {})
            if not method.get("method") or not method.get("coverage") or not isinstance(method.get("limitations"), list):
                raise ProductionError("REVIEW_PROVENANCE", "Creative projects require method, coverage and limitations for each review domain")
        if not isinstance(data.get("audience_validation"), str) or not data["audience_validation"].strip():
            raise ProductionError("REVIEW_PROVENANCE", "State whether actual audience outcomes have been measured")
    if project.data.get("channel_profile"):
        profiles.check(project)
        fit = data.get("profile_review", {})
        if not isinstance(fit, dict) or any(not isinstance(fit.get(k), str) or not fit[k].strip() for k in ("identity", "variation", "exceptions", "limitations")):
            raise ProductionError("PROFILE_REVIEW_REQUIRED", "Describe identity, variation, exceptions and limitations; do not infer audience recognition")
    if data["verdict"] == "accept":
        if data["findings"]:
            raise ProductionError("UNRESOLVED_FINDINGS", "Resolve findings before acceptance")
        required = ("math", "visual", "timing", "audio")
        if any(data["checks"].get(k) != "pass" for k in required):
            raise ProductionError("REVIEW_INCOMPLETE", "Math, visual, timing, and audio checks must pass; unavailable is not pass")
        if data["scope"] == "final":
            media.verify(project)
    with project.connect() as db:
        db.execute("INSERT INTO reviews(snapshot,payload,created) VALUES(?,?,?)",(data["snapshot"],json.dumps(data),time.time()))
    return {"recorded": True, "verdict": data["verdict"], "scope": data["scope"]}

def publish(project, intent, credentials, dry_run):
    if not status(project)["accepted"]:
        raise ProductionError("REVIEW_REQUIRED", "Current final export needs complete accepted review")
    export = project.artifact("export", media.assembly_fingerprint(project))
    required = ("channel_id","title","privacy","authorized")
    if any(k not in intent for k in required) or intent["authorized"] is not True:
        raise ProductionError("PUBLISH_INTENT_REQUIRED", "Provide authorized channel, title and visibility")
    if intent["privacy"] not in ("private","unlisted","public"):
        raise ProductionError("INVALID_PRIVACY", "private, unlisted or public required")
    if not 1 <= len(intent["title"]) <= 100:
        raise ProductionError("INVALID_TITLE", "Title must contain 1–100 characters")
    identity = digest({"sha256":export["sha256"],"channel_id":intent["channel_id"]})
    if dry_run:
        return {"dry_run":True,"intent_id":identity,"export_sha256":export["sha256"],"intent":intent}
    request = project.root / ".mathtuber/publish-request.json"
    atomic_json(request,{"video":export["absolute_path"],"intent":intent,"intent_id":identity,
                         "credentials_config":str(Path(credentials).expanduser().resolve()),
                         "receipt":str(project.root / ".mathtuber" / f"upload-{identity}.json")})
    output,_ = media.run([media.python_executable(),media.ROOT / "workers/youtube.py",request],timeout=1800)
    result = json.loads(output)
    with project.connect() as db:
        db.execute("INSERT OR REPLACE INTO publications VALUES(?,?)",(identity,json.dumps(result)))
    return result

def perform(args):
    if args.command == "doctor": return doctor()
    if args.command == "profile-list": return profiles.catalog()
    if args.command == "init": return create(args.project,read_json(args.manifest))
    project = Project(args.project)
    if args.command in ("status","next"): return status(project)
    if args.command == "plan-check": return validate_plan(project)
    if args.command == "profile-check": return profiles.check(project)
    if args.command == "job-status":
        path = project.root / ".mathtuber/jobs" / f"{args.job}.json"
        data = read_json(path)
        if data.get("state") == "running":
            try: os.kill(data["pid"],0)
            except ProcessLookupError:
                data["state"] = "interrupted"
                atomic_json(path,data)
        return data
    with project.lock():
        if args.command == "profile-bind": return profiles.bind(project,args.profile,args.replace)
        if args.command == "audio": return media.synthesize(project,args.scene)
        if args.command == "render": return media.render(project,args.scene,args.quality,args.execution)
        if args.command == "assemble": return media.assemble(project)
        if args.command == "verify": return media.verify(project)
        if args.command == "review-bundle": return media.bundle(project,args.scene,args.quality)
        if args.command == "review-record": return record_review(project,read_json(args.file))
        if args.command == "publish": return publish(project,read_json(args.intent),args.credentials,args.dry_run)
    raise ProductionError("UNKNOWN_COMMAND",args.command)

def parser():
    p = argparse.ArgumentParser(description="MathTuber: deterministic tools for native agentic math-video production")
    p.add_argument("--version",action="version",version=__version__)
    subs=p.add_subparsers(dest="command",required=True)
    subs.add_parser("doctor")
    subs.add_parser("profile-list")
    for name in ("profile-bind","profile-check","init","status","next","plan-check","audio","render","assemble","verify","review-bundle","review-record","publish","job-status"):
        sub=subs.add_parser(name)
        sub.add_argument("--project",required=True)
        if name == "profile-bind":
            sub.add_argument("--profile",required=True)
            sub.add_argument("--replace",action="store_true")
        if name == "init": sub.add_argument("--manifest",required=True)
        if name in ("audio","render","review-bundle"):
            sub.add_argument("--scene",required=name=="render",default="all" if name=="audio" else None)
        if name in ("render","review-bundle"):
            sub.add_argument("--quality",choices=("preview","final"),default="preview")
        if name == "render": sub.add_argument("--execution",choices=("native","docker"),required=True)
        if name in ("audio","render","assemble"):
            sub.add_argument("--background",action="store_true")
        if name == "review-record": sub.add_argument("--file",required=True)
        if name == "publish":
            sub.add_argument("--intent",required=True)
            sub.add_argument("--credentials",default="")
            sub.add_argument("--dry-run",action="store_true")
        if name == "job-status": sub.add_argument("--job",required=True)
    return p

def main(argv=None):
    args = parser().parse_args(argv)
    started=time.monotonic()
    job_receipt = os.environ.get("MATHTUBER_JOB_RECEIPT")
    try:
        if getattr(args,"background",False):
            Project(args.project)
            job=uuid.uuid4().hex
            folder=Path(args.project).resolve()/".mathtuber/jobs"
            folder.mkdir(parents=True,exist_ok=True)
            path=folder/f"{job}.json"
            env=os.environ.copy()
            env["MATHTUBER_JOB_RECEIPT"]=str(path)
            command=[sys.executable,str(media.ROOT/"scripts/engine.py")]+[a for a in (argv or sys.argv[1:]) if a != "--background"]
            with (folder/f"{job}.log").open("w") as log:
                process=subprocess.Popen(command,stdout=log,stderr=log,env=env,start_new_session=True)
            result={"job":job,"pid":process.pid,"state":"running","command":args.command}
            # Child owns the receipt; avoid overwriting a very fast completion.
            print(json.dumps({"ok":True,"result":result}))
            return 0
        if job_receipt: atomic_json(job_receipt,{"state":"running","pid":os.getpid(),"command":args.command})
        result=perform(args)
        response={"ok":True,"result":result,"elapsed_seconds":round(time.monotonic()-started,3)}
        if job_receipt: atomic_json(job_receipt,{"state":"completed",**response})
        print(json.dumps(response,ensure_ascii=False))
        return 0
    except (ProductionError,ValueError,KeyError,FileNotFoundError) as exc:
        response={"ok":False,"error":{"code":getattr(exc,"code","INVALID_INPUT"),"message":str(exc)}}
        if job_receipt: atomic_json(job_receipt,{"state":"failed",**response})
        print(json.dumps(response,ensure_ascii=False))
        return 1

if __name__ == "__main__":
    raise SystemExit(main())
