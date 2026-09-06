#!/usr/bin/env python3
"""Measure current narration and optionally transcribe it; no automatic review verdict."""
import argparse
import json
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from mathtuber.audio_review import inspect_audio
from mathtuber.state import Project, ProductionError


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--project',required=True)
    parser.add_argument('--model',default='small.en')
    parser.add_argument('--language',default='en')
    parser.add_argument('--no-asr',action='store_true')
    parser.add_argument('--final',action='store_true',help='Also measure the current final soundtrack')
    args=parser.parse_args()
    try:
        project=Project(args.project)
        with project.lock():
            result=inspect_audio(project,args.model,args.language,not args.no_asr,args.final)
        print(json.dumps(result))
    except ProductionError as exc:
        print(str(exc),file=sys.stderr);return 1
    return 0


if __name__=='__main__':sys.exit(main())
