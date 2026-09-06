#!/usr/bin/env python3
"""Extract portable final visual evidence; inspect returned sheets before reviewing."""
import argparse
import json
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from mathtuber.state import Project, ProductionError
from mathtuber.visual_review import extract


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--project',required=True)
    parser.add_argument('--cue-offset',type=float,default=1.7)
    args=parser.parse_args()
    try:
        project=Project(args.project)
        with project.lock():result=extract(project,args.cue_offset)
        print(json.dumps(result))
    except ProductionError as exc:
        print(str(exc),file=sys.stderr);return 1
    return 0


if __name__=='__main__':sys.exit(main())
