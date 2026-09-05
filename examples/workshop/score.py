from pathlib import Path
import json,sys,wave,math
import numpy as np
sys.path.insert(0,str(Path(__file__).resolve().parents[2]/'plugins/mathtuber'))
from mathtuber.state import Project,atomic_json
from mathtuber.media import audio_for
import argparse
parser=argparse.ArgumentParser();parser.add_argument('--project',required=True);args=parser.parse_args()
for folder in [Path(args.project).resolve()]:
 p=Project(folder);timing=json.loads((folder/'assets/timing.json').read_text());durations=[math.ceil(audio_for(p,s)['metadata']['duration']*30)/30 for s in p.data['scenes']];length=sum(durations);rate=24000;audio=np.zeros((math.ceil(length*rate),2));events=[]
 def tone(at,freq,dur=.25,amp=.06,wood=False):
  n=int(dur*rate);t=np.arange(n)/rate;env=np.minimum(t/.006,1)*np.exp(-t/(.035 if wood else dur*.25));waveform=np.sin(TAU*freq*t)+.18*np.sin(TAU*freq*2.76*t);sound=amp*env*waveform
  start=max(0,int(at*rate));end=min(start+n,len(audio));audio[start:end,0]+=sound[:end-start];audio[start:end,1]+=sound[:end-start]*.92;events.append({'time':round(at,3),'frequency':freq,'duration':dur,'type':'wood tap' if wood else 'glass resonance'})
 TAU=2*np.pi
 base=next((v for k,v in [('Chessboard',220),('Coin',330),('Area',440),('Balls',262),('Six',294)] if k in p.data['brief']['topic']),262)
 for i,mult in enumerate([1,1.5,2]):tone(.15+i*.28,base*mult,.6,.045)
 offset=0
 for j,(s,d) in enumerate(zip(p.data['scenes'],durations)):
  if 'Balls' in p.data['brief']['topic'] and j in [1,2]:offset+=d;continue
  cues=list(timing[s['id']].values())
  for k,cue in enumerate(cues[:2]):tone(offset+cue,base*(2+k/2),.12,.055,True)
  offset+=d
 for i,mult in enumerate([1.5,2,2.5]):tone(length-2.8+i*.22,base*mult,.8,.05)
 target=folder/'assets/score.wav'
 with wave.open(str(target),'wb') as w:w.setparams((2,2,rate,0,'NONE','not compressed'));w.writeframes((np.clip(audio,-1,1)*32767).astype('<i2').tobytes())
 atomic_json(folder/'assets/sound-design.json',{'license':'Original synthesis; CC0','profile':'Workshop timbre family; episode-specific register, brief motifs and tactile events. No continuous bed.','subjective_listening':'Not performed by text/image host','events':events})
 p.data['soundtrack']={'path':'assets/score.wav','gain_db':0,'license':'Original MathTuber workshop synthesis; CC0'};atomic_json(p.manifest_path,p.data)
 print('SCORE',folder.name,round(length,2))
