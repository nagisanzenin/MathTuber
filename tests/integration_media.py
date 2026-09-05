"""Real TTS-import, render, assembly and cache integration with a generated tone fixture."""
import argparse
import json
import math
import os
from pathlib import Path
import shutil
import struct
import subprocess
import sys
import wave
p=argparse.ArgumentParser();p.add_argument('--project',required=True);p.add_argument('--execution',choices=['native','docker'],default='native');a=p.parse_args()
repo=Path(__file__).resolve().parents[1];engine=repo/'plugins/mathtuber/scripts/engine.py';root=Path(a.project).resolve();root.mkdir(parents=True,exist_ok=True)
audio=root/'tone.wav'
with wave.open(str(audio),'wb') as w:
 w.setparams((1,2,24000,0,'NONE','not compressed'))
 w.writeframes(b''.join(struct.pack('<h',round(1200*math.sin(2*math.pi*440*i/24000))) for i in range(4*24000)))
manifest={'schema_version':1,'brief':{'topic':'Integration fixture: one plus three','min_seconds':4,'max_seconds':5},'format':{'width':360,'height':640,'fps':15},'speech':{'provider':'wav','tail_seconds':0},'scenes':[{'id':'s01','source':'scenes/proof.py','class_name':'Proof','narration':'Technical fixture, not production narration.','audio_source':str(audio)}]}
path=root/'input.json';path.write_text(json.dumps(manifest))
def cli(*args):
 r=subprocess.run([sys.executable,str(engine),*args],text=True,capture_output=True)
 if r.returncode: raise RuntimeError(r.stdout+r.stderr)
 return json.loads(r.stdout)['result']
if not (root/'project.json').exists():cli('init','--project',str(root),'--manifest',str(path))
(root/'scenes/proof.py').write_text('''from components import *
class Proof(NarratedScene):
    def construct(self):
        self.heading("ODD NUMBERS", "One plus three makes a square")
        blocks=VGroup(*[Square(side_length=1,fill_opacity=.8,fill_color=BLUE if i==0 else GOLD).move_to([(i%2-.5)*1.05,(i//2-.5)*1.05,0]) for i in range(4)])
        self.play(FadeIn(blocks[0]),run_time=.4)
        self.play(LaggedStart(*[FadeIn(x) for x in blocks[1:]],lag_ratio=.3),run_time=1)
        self.play(Write(MathTex("1+3=2^2",color=INK).shift(DOWN*2)),run_time=.7)
        self.finish()
''')
cli('audio','--project',str(root),'--scene','all')
first=cli('render','--project',str(root),'--scene','s01','--quality','final','--execution',a.execution)
second=cli('render','--project',str(root),'--scene','s01','--quality','final','--execution',a.execution)
export=cli('assemble','--project',str(root));verified=cli('verify','--project',str(root));bundle=cli('review-bundle','--project',str(root))
report={'execution':a.execution,'fixture':'generated tone, not speech-quality validation','checks':{'render':bool(first['artifact']),'cache_reused':second['cached'],'assembly':bool(export['artifact']),'mechanical':verified['passed'],'evidence':len(bundle['frames'])>=3},'export':export['artifact']['absolute_path']}
report['passed']=all(report['checks'].values());(root/'integration-report.json').write_text(json.dumps(report,indent=2));print(json.dumps(report,indent=2))
raise SystemExit(0 if report['passed'] else 1)
