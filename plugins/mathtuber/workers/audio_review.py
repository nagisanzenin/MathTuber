"""Optional local ASR plus full audio signal measurements. No acceptance authority."""
import argparse
import difflib
import json
from pathlib import Path
import re
import subprocess
import sys
import numpy as np
import soundfile as sf
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from mathtuber.state import atomic_json, file_hash


def signal(samples, rate):
    samples=np.asarray(samples,dtype=np.float64)
    if not samples.size or not np.isfinite(samples).all() or rate <= 0:
        raise ValueError('Audio must contain finite samples at a positive sample rate')
    if samples.ndim==1:samples=samples[:,None]
    # Examine every channel; averaging channels first could hide clipping.
    size=max(1,int(rate*.1));longest=run=0
    for start in range(0,len(samples),size):
        window=samples[start:start+size]
        quiet=np.sqrt(np.mean(window**2))<.002
        run=run+len(window) if quiet else 0
        longest=max(longest,run)
    return {'peak':float(np.max(np.abs(samples))),
            'clipped_sample_fraction':float(np.mean(np.abs(samples)>=.999)),
            'rms_dbfs':float(20*np.log10(np.sqrt(np.mean(samples**2))+1e-12)),
            'longest_low_energy_seconds':longest/rate,
            'duration':len(samples)/rate,'channels':samples.shape[1],
            'sample_rate':rate,'low_energy_definition':'RMS below .002 in 100ms windows; approximate silence'}


def compare(expected, recognized):
    tokens=lambda text:re.findall(r'\w+',text.lower(),flags=re.UNICODE)
    left,right=tokens(expected),tokens(recognized)
    matcher=difflib.SequenceMatcher(None,left,right,autojunk=False)
    return {'token_similarity':matcher.ratio(),
            'differences':[{'expected':' '.join(left[i:j]),'recognized':' '.join(right[k:l])}
                for tag,i,j,k,l in matcher.get_opcodes() if tag!='equal']}


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('request')
    request=json.loads(Path(parser.parse_args().request).read_text())
    model=None
    if request['asr']:
        try:from faster_whisper import WhisperModel
        except ImportError:
            raise SystemExit('ASR_UNAVAILABLE: run scripts/setup.py --with-review or request --no-asr; unavailable is not pass')
        model=WhisperModel(request['model'],device='cpu',compute_type='int8',cpu_threads=4)
    scenes=[]
    for item in request['items']:
        if file_hash(Path(item['path']))!=item['sha256']:
            raise SystemExit('STALE_AUDIO: audio changed after inspection request')
        samples,rate=sf.read(item['path'],always_2d=True)
        row={'scene':item['scene'],'audio_sha256':item['sha256'],'expected':item['expected'],
             'signal':signal(samples,rate),'transcription_status':'unavailable'}
        if model:
            segments,_=model.transcribe(item['path'],language=request['language'],beam_size=5,
                                       vad_filter=True,condition_on_previous_text=False)
            segments=[{'start':s.start,'end':s.end,'text':s.text.strip()} for s in segments]
            recognized=' '.join(s['text'] for s in segments)
            row.update(recognized=recognized,segments=segments,transcription_status='performed',
                       **compare(item['expected'],recognized))
        scenes.append(row)
    final=None
    if request['export']:
        export=request['export']
        if file_hash(Path(export['path']))!=export['sha256']:
            raise SystemExit('STALE_EXPORT: export changed after inspection request')
        # Deliveries are stereo; preserve both channels instead of hiding opposing peaks.
        raw=subprocess.run(['ffmpeg','-v','error','-i',export['path'],'-vn','-f','f32le',
                            '-ac','2','-ar','24000','pipe:1'],capture_output=True,check=True).stdout
        final={'export_sha256':export['sha256'],'signal':signal(np.frombuffer(raw,dtype='<f4').reshape(-1,2),24000),
               'transcription_status':'not performed; independent ASR covers narration sources'}
    report={'schema_version':1,'fingerprint':request['fingerprint'],'automatic_acceptance':False,
            'method':'Full source signal measurements; optional independent local faster-whisper ASR',
            'asr':{'enabled':request['asr'],'model':request['model'] if model else None,'language':request['language']},
            'scenes':scenes,'final':final,
            'limitations':['ASR can misrecognize correct speech, especially mathematical terms and number formatting.',
                          'Token similarity is a diagnostic, not an accuracy or acceptance threshold.',
                          'No subjective listening, prosody, mix-quality or audience validation.']}
    out=Path(request['output']);atomic_json(out,report)
    print(json.dumps({'cached':False,'path':str(out),'sha256':file_hash(out),'automatic_acceptance':False}))


if __name__=='__main__':main()
