#!/usr/bin/env python3
"""Original CC0 boundary tones; reasoning passages intentionally have no score."""
import argparse,json,wave,math
from pathlib import Path
import numpy as np
p=argparse.ArgumentParser();p.add_argument('--project',required=True);args=p.parse_args();root=Path(args.project)
manifest=json.loads((root/'project.json').read_text())
import sqlite3
with sqlite3.connect(root/'.mathtuber/state.sqlite') as db:row=db.execute("SELECT metadata FROM artifacts WHERE key='audio:s01'").fetchone()
duration=json.loads(row[0])['duration'];rate=24000;signal=np.zeros(math.ceil(duration*rate));events=[]
for start,freq in [(.08,440),(.24,660),(duration-.72,440),(duration-.5,660)]:
 length=min(.28,duration-start);t=np.arange(int(length*rate))/rate;env=(1-np.exp(-t*100))*np.exp(-t*18);tone=.018*env*(np.sin(2*np.pi*freq*t)+.2*np.sin(2*np.pi*freq*2*t));offset=int(start*rate);signal[offset:offset+len(tone)]+=tone;events.append(dict(start=round(start,3),duration=length,frequency=freq))
with wave.open(str(root/'assets/score.wav'),'wb') as wav:wav.setnchannels(1);wav.setsampwidth(2);wav.setframerate(rate);wav.writeframes((signal*32767).astype('<i2').tobytes())
(root/'assets/sound-design.json').write_text(json.dumps(dict(license='Original synthesized tones: CC0',intent='Two quiet boundary notes; no bed or effects during proof. Artistic listening not measured.',events=events),indent=2))
manifest['soundtrack']={'path':'assets/score.wav','gain_db':0,'license':'Original CC0 synthesized boundary tones'}
(root/'project.json').write_text(json.dumps(manifest,indent=2)+'\n')
