from pathlib import Path
import sys,json,math
import numpy as np
import soundfile as sf
sys.path.insert(0,str(Path(__file__).resolve().parents[2]/'plugins/mathtuber'))
from mathtuber.state import Project,atomic_json
from mathtuber.media import audio_for
p=Project(sys.argv[1]);a=audio_for(p,p.scene('s01'));pauses=a['metadata']['word_timing']['paragraph_pauses'];rate=48000;duration=math.ceil(a['metadata']['duration']*30)/30
signal=np.zeros(round(rate*duration));windows=[]
for index,frequencies in [(0,[220,221]),(3,[220,220.5])]:
 gap=pauses[index];start=gap['start']+.15;end=gap['end']-.15;n=round((end-start)*rate);t=np.arange(n)/rate;fade=np.minimum(1,np.minimum(t/.08,(len(t)/rate-t)/.08));chunk=.09*sum(np.cos(2*np.pi*f*t) for f in frequencies)*fade
 k=round(start*rate);signal[k:k+n]+=chunk;windows.append(dict(start=k/rate,end=(k+n)/rate,frequencies=frequencies,beat_hz=abs(frequencies[1]-frequencies[0]),peak=float(np.max(np.abs(chunk))),fade_seconds=.08))
sf.write(p.root/'assets/score.wav',signal,rate,subtype='PCM_16');atomic_json(p.root/'assets/sound-design.json',dict(license='Original mathematical sine synthesis; CC0',windows=windows,subjective_listening='Not established; signal and audiovisual timing require separate checks.'))
p.data['soundtrack']=dict(path='assets/score.wav',gain_db=0,license='Original mathematical sine synthesis; CC0');atomic_json(p.manifest_path,p.data)
print('Generated two original listening windows',windows)
