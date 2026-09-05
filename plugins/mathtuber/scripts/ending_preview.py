#!/usr/bin/env python3
"""Extract an export-bound ending sheet. Inspect it; extraction is not acceptance."""
import argparse, math, subprocess, sys
from fractions import Fraction
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from mathtuber.state import Project, atomic_json, file_hash
from mathtuber.media import assembly_fingerprint, probe
from mathtuber.review_sampling import ending_samples

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project", required=True)
    parser.add_argument("--seconds", type=float, default=15)
    parser.add_argument("--samples", type=int, default=9)
    args = parser.parse_args()
    from PIL import Image, ImageDraw
    project = Project(Path(args.project).resolve())
    export = project.artifact("export", assembly_fingerprint(project))
    if not export:
        parser.error("A current assembled export is required")
    # Container duration may include an AAC tail beyond the last video frame.
    video = next(s for s in probe(export["absolute_path"])["streams"] if s.get("codec_type") == "video")
    fps = float(Fraction(video["avg_frame_rate"]))
    count = video.get("nb_frames")
    duration = int(count) / fps if count and count != "N/A" else float(video["duration"])
    times = ending_samples(duration, args.seconds, args.samples, fps)
    out = Path(args.project).resolve()/"reviews"/"ending"
    out.mkdir(parents=True, exist_ok=True)
    sheet = Image.new("RGB", (1080, 667*math.ceil(len(times)/3)), "white")
    records = []
    for i, timestamp in enumerate(times):
        frame = out/f"frame-{i:03}.jpg"
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", str(timestamp), "-i", export["absolute_path"], "-frames:v", "1", "-vf", "scale=360:640,format=yuvj420p", str(frame)], check=True)
        tile = Image.new("RGB", (360, 667), "white")
        tile.paste(Image.open(frame), (0, 27))
        ImageDraw.Draw(tile).text((8, 7), f"{timestamp:.3f}s", fill="black")
        sheet.paste(tile, ((i%3)*360, (i//3)*667))
        records.append(dict(path=str(frame), sha256=file_hash(frame), time=timestamp))
    path = out/"sheet.jpg"
    sheet.save(path, quality=92)
    atomic_json(out/"evidence.json", dict(export_sha256=export["sha256"], video_duration=duration, fps=fps, frames=records, sheet_sha256=file_hash(path), coverage="Sampled final section only; not continuous audiovisual viewing or a review verdict."))
    print(path)
if __name__ == "__main__":
    main()
