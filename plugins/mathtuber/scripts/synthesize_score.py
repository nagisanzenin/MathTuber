#!/usr/bin/env python3
"""Generate an original sparse CC0 score from measured scene cues. Run with the media Python."""
from pathlib import Path
import argparse,json,sys,wave
import numpy as np
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from mathtuber.state import Project,atomic_json
from mathtuber.media import audio_for
parser=argparse.ArgumentParser();parser.add_argument('--project',required=True);args=parser.parse_args()
p=Project(args.project);folder=p.root
with p.lock():
 timing=json.loads((folder/'assets/timing.json').read_text())
 durations=[audio_for(p,s)['metadata']['duration'] for s in p.data['scenes']]
 rate=24000;length=sum(durations)+1;audio=np.zeros((int(length*rate),2));offset=0;events=[]
 def tone(at,freq,dur,amp,kind):
  n=int(dur*rate);t=np.arange(n)/rate
  env=np.minimum(t/.015,1)*np.exp(-t/(dur*.23));sound=amp*env*(np.sin(2*np.pi*freq*t)+.2*np.sin(2*np.pi*freq*2*t))
  start=int(at*rate);end=min(start+n,len(audio));audio[start:end,0]+=sound[:end-start];audio[start:end,1]+=sound[:end-start]*.93
  events.append({'at':round(at,3),'duration':dur,'frequency':freq,'kind':kind})
 # Original short opening motif; no background bed during derivations.
 for i,freq in enumerate([261.63,392,523.25]):tone(.25+i*.27,freq,.65,.035,'original opening motif')
 for i,(scene,duration) in enumerate(zip(p.data['scenes'],durations)):
  # Only two faint tactile cues per beat; active speech ducks these further.
  cues=list(timing[scene['id']].values())
  for j,at in enumerate(cues[:2]):tone(offset+at,650+180*j,.09,.024,'tactile cue')
  offset+=duration
 for i,freq in enumerate([392,523.25,659.25]):tone(max(0,length-3)+i*.22,freq,.9,.025,'original closing motif')
 target=folder/'assets/score.wav'
 with wave.open(str(target),'wb') as out:out.setnchannels(2);out.setsampwidth(2);out.setframerate(rate);out.writeframes((np.clip(audio,-1,1)*32767).astype('<i2').tobytes())
 atomic_json(folder/'assets/sound-design.json',{'authorship':'Original mathematical tone synthesis by MathTuber; CC0','music_policy':'Brief opening and closing motifs; no sustained bed; derivations primarily dry speech','events':events})
 print('Generated original sparse score:', target)
