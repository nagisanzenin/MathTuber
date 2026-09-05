#!/usr/bin/env python3
"""Compile assets/sound-events.json after measured speech cues are available."""
import argparse
import json
import math
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from mathtuber.state import Project, atomic_json
from mathtuber.media import audio_for
from mathtuber.sound_events import resolve_events, write_score
from mathtuber.listening import resolve_windows

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--project", required=True)
    args = parser.parse_args()
    project = Project(args.project)
    with project.lock():
        timing = json.loads((project.root / "assets/timing.json").read_text())
        absolute = {}
        pauses = {}
        offset = 0
        fps = project.data["format"]["fps"]
        for scene in project.data["scenes"]:
            absolute[scene["id"]] = {key: value + offset for key, value in timing[scene["id"]].items()}
            metadata = audio_for(project, scene)["metadata"]
            pauses[scene["id"]] = [{"start": p["start"] + offset, "end": p["end"] + offset}
                                   for p in metadata.get("word_timing", {}).get("paragraph_pauses", [])]
            offset += math.ceil(metadata["duration"] * fps) / fps
        event_path = project.root / "assets/sound-events.json"
        plan = json.loads(event_path.read_text()) if event_path.exists() else []
        events = resolve_events(plan, absolute, offset)
        listening_path = project.root / "assets/listening-windows.json"
        windows = resolve_windows(json.loads(listening_path.read_text()), pauses, offset) if listening_path.exists() else []
        write_score(project.root / "assets/score.wav", events, offset, rate=48000 if windows else 24000, windows=windows)
        atomic_json(project.root / "assets/sound-design.json", {"license": "Original synthesis; CC0", "events": events, "windows": windows, "subjective_listening": "Not established by synthesis or signal validation; record separately during review."})
        project.data["soundtrack"] = {"path": "assets/score.wav", "gain_db": 0, "license": "Original synthesis; CC0"}
        atomic_json(project.manifest_path, project.data)
    print("Compiled", len(events), "action sounds and", len(windows), "listening windows")

if __name__ == "__main__": main()
