#!/usr/bin/env python3
"""Independently read batch publication state without creating or updating videos."""
import argparse
from datetime import datetime, timezone
import json
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from mathtuber import media
from mathtuber.state import Project, ProductionError, atomic_json, digest, read_json


def inspect(batch_path,credentials):
    path=Path(batch_path).resolve();entries=read_json(path).get('projects',[])
    if not entries:raise ProductionError('EMPTY_BATCH','Provide a batch with projects and intent paths')
    rows=[]
    for entry in entries:
        project=Project(path.parent/entry['project'])
        intent=read_json(path.parent/entry['intent'])
        with project.lock():
            export=project.artifact('export',media.assembly_fingerprint(project))
            if not export:
                rows.append({'project':project.root.name,'state':'no_current_export','complete':False})
                continue
            identity=digest({'sha256':export['sha256'],'channel_id':intent['channel_id']})
            receipt=project.root/'.mathtuber'/f'upload-{identity}.json'
            if not receipt.exists():
                result={'state':'not_uploaded'}
            else:
                request=project.root/'.mathtuber/publication-status-request.json'
                atomic_json(request,{'intent':intent,'receipt':str(receipt),'status_only':True,
                            'credentials_config':str(Path(credentials).expanduser().resolve())})
                raw,_=media.run([media.python_executable(),media.ROOT/'workers/youtube.py',request],timeout=120)
                result=json.loads(raw)
            result.update(project=project.root.name,export_sha256=export['sha256'],
                          requested_privacy=intent['privacy'])
            result['complete']=(result.get('state')=='observed' and result.get('privacy')==intent['privacy']
                                and result.get('processing')=='succeeded')
            rows.append(result)
    return {'checked_at':datetime.now(timezone.utc).isoformat(),'complete':all(row['complete'] for row in rows),
            'completed':sum(row['complete'] for row in rows),'total':len(rows),'videos':rows,
            'method':'Read-only YouTube status and processing queries for exact current-export receipts; no video insert or update.'}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--batch',required=True);parser.add_argument('--credentials',required=True)
    parser.add_argument('--output');parser.add_argument('--require-complete',action='store_true')
    args=parser.parse_args()
    try:
        report=inspect(args.batch,args.credentials)
        if args.output:atomic_json(Path(args.output).expanduser().resolve(),report)
        print(json.dumps(report))
        return 2 if args.require_complete and not report['complete'] else 0
    except ProductionError as exc:
        print(str(exc),file=sys.stderr);return 1


if __name__=='__main__':sys.exit(main())
