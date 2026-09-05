#!/usr/bin/env python3
"""Inspect narration and captions on a current scene preview before final rendering."""
import argparse
import json
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from mathtuber.state import Project, ProductionError
from mathtuber.prototype import captioned_preview

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--project',required=True)
    parser.add_argument('--scene',required=True)
    args=parser.parse_args()
    try:
        project=Project(args.project)
        with project.lock():result=captioned_preview(project,args.scene)
        print(json.dumps(result))
    except ProductionError as exc:
        print(str(exc),file=sys.stderr);return 1
    return 0

if __name__=='__main__':sys.exit(main())
