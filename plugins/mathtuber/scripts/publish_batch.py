#!/usr/bin/env python3
"""Review all batch members before any upload; defaults to a read-only plan."""
import argparse
import json
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from mathtuber.state import Project, ProductionError, read_json
from mathtuber.cli import status, publish


def prepare(batch_file):
    path = Path(batch_file).resolve()
    entries = read_json(path).get('projects', [])
    if not entries:
        raise ProductionError('EMPTY_BATCH', 'Provide projects with project, intent and editorial paths')
    prepared, seen = [], set()
    for entry in entries:
        project = Project(path.parent / entry['project'])
        if project.root in seen:
            raise ProductionError('DUPLICATE_PROJECT', 'Each project belongs in the batch once')
        seen.add(project.root)
        state = status(project)
        if not state['accepted'] or not state['export']:
            raise ProductionError('BATCH_NOT_READY', f'{project.root.name}: current accepted export required')
        editorial = read_json(path.parent / entry['editorial'])
        if editorial.get('snapshot') != state['snapshot'] or editorial.get('export_sha256') != state['export']['sha256']:
            raise ProductionError('STALE_EDITORIAL', f'{project.root.name}: editorial evidence is stale')
        required = ('opening', 'mechanism', 'readability', 'pacing', 'sound', 'remaining_weaknesses', 'audience_evidence')
        if editorial.get('decision') != 'release' or any(not isinstance(editorial.get(k),str) or not editorial[k].strip() for k in required):
            raise ProductionError('EDITORIAL_REQUIRED', 'Separate written editorial judgment is required; not a numeric score')
        intent = read_json(path.parent / entry['intent'])
        plan = publish(project, intent, None, True)
        prepared.append((project, intent, plan))
    return prepared


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--batch',required=True)
    parser.add_argument('--publish',action='store_true')
    parser.add_argument('--credentials')
    args=parser.parse_args()
    try:
        ready=prepare(args.batch)
        if args.publish and not args.credentials:parser.error('--publish requires --credentials')
        print(json.dumps({'all_reviewed_before_upload':True,'plans':[x[2] for x in ready]}),flush=True)
        if args.publish:
            for index in range(len(ready)):
                # Recheck the entire batch: a changed member stops later uploads too.
                current=prepare(args.batch)
                if [x[2] for x in current] != [x[2] for x in ready]:
                    raise ProductionError('BATCH_CHANGED','Batch changed after initial readiness check')
                project,intent,_=current[index]
                with project.lock():result=publish(project,intent,args.credentials,False)
                print(json.dumps({'project':project.root.name,'result':result}),flush=True)
    except ProductionError as exc:
        print(str(exc),file=sys.stderr);sys.exit(1)

if __name__=='__main__':main()
