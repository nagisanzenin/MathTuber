#!/usr/bin/env python3
"""Retrieve a small set of production repair notes without a model or network."""
import argparse
import json
from pathlib import Path
import re

ROOT=Path(__file__).resolve().parents[1]

def retrieve(entries,query='',stage=None,limit=3):
    terms=set(re.findall(r'[a-z0-9]+',query.lower()))
    ranked=[]
    for entry in entries:
        if stage and entry['stage']!=stage:continue
        primary=set(re.findall(r'[a-z0-9]+',' '.join([entry['id'],*entry['tags']]).lower()))
        body=set(re.findall(r'[a-z0-9]+',(entry['symptom']+' '+entry['cause']).lower()))
        score=3*len(terms & primary)+len(terms & body)
        if not terms or score:ranked.append((score,entry['id'],entry))
    return [entry for _,_,entry in sorted(ranked,key=lambda x:(-x[0],x[1]))[:limit]]

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--query',default='');parser.add_argument('--stage')
    parser.add_argument('--id');parser.add_argument('--limit',type=int,default=3)
    args=parser.parse_args()
    if not 1<=args.limit<=8:parser.error('--limit must be between 1 and 8')
    data=json.loads((ROOT/'knowledge/repairs.json').read_text())
    entries=[e for e in data['entries'] if e['id']==args.id] if args.id else retrieve(data['entries'],args.query,args.stage,args.limit)
    print(json.dumps({'scope':data['scope'],'matches':entries,'no_match_guidance':'Read the stage guide and inspect the actual error; do not invent a repair.' if not entries else None},indent=2))

if __name__=='__main__':main()
