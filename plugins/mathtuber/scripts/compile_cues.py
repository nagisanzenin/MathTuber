#!/usr/bin/env python3
"""Resolve literal scene at(...) cues against current synthesized word timings."""
import argparse
from pathlib import Path
import re
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from mathtuber.state import Project,ProductionError,atomic_json,within
from mathtuber.media import audio_for

def resolve_cues(source,words):
    tokens=[]
    for word in words:
        tokens.extend((token,word['start']) for token in re.findall(r'[a-z0-9]+',word['text'].lower()))
    result={}
    for phrase in re.findall(r"self\.at\(['\"](.+?)['\"]\)",source):
        needle=re.findall(r'[a-z0-9]+',phrase.lower())
        matches=[i for i in range(len(tokens)) if [x[0] for x in tokens[i:i+len(needle)]]==needle]
        if len(matches)!=1:
            raise ProductionError('CUE_AMBIGUOUS',f'Expected one spoken match for {phrase!r}, found {len(matches)}; use a longer unique phrase')
        result[phrase]=round(tokens[matches[0]][1],3)
    return result

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--project',required=True);args=parser.parse_args();project=Project(args.project)
    with project.lock():
        timing={}
        for scene in project.data['scenes']:
            artifact=audio_for(project,scene);words=artifact['metadata'].get('word_timing',{}).get('words',[])
            if not words:raise ProductionError('TIMING_REQUIRED','Provider did not return word timings')
            timing[scene['id']]=resolve_cues(within(project.root,scene['source']).read_text(),words)
        atomic_json(project.root/'assets/timing.json',timing)
    print('Compiled measured speech cues for',len(timing),'scenes')
if __name__=='__main__':main()
