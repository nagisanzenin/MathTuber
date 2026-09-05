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

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--project", required=True)
    args = parser.parse_args()
    project = Project(args.project)
    with project.lock():
        timing = json.loads((project.root / "assets/timing.json").read_text())
        absolute = {}
        offset = 0
        fps = project.data["format"]["fps"]
        for scene in project.data["scenes"]:
            absolute[scene["id"]] = {key: value + offset for key, value in timing[scene["id"]].items()}
            offset += math.ceil(audio_for(project, scene)["metadata"]["duration"] * fps) / fps
        plan = json.loads((project.root / "assets/sound-events.json").read_text())
        events = resolve_events(plan, absolute, offset)
        write_score(project.root / "assets/score.wav", events, offset)
        atomic_json(project.root / "assets/sound-design.json", {"license": "Original synthesis; CC0", "events": events, "subjective_listening": "Not established by synthesis or signal validation; record separately during review."})
        project.data["soundtrack"] = {"path": "assets/score.wav", "gain_db": 0, "license": "Original synthesis; CC0"}
        atomic_json(project.manifest_path, project.data)
    print("Compiled", len(events), "action sounds")

if __name__ == "__main__": main()
