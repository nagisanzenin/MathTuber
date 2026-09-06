"""Portable final-frame evidence, including authored cues and complete intervals."""
import json
import math
from fractions import Fraction
from pathlib import Path
from . import media
from .review_sampling import interval_samples, ending_samples
from .state import ProductionError, atomic_json, digest, file_hash, read_json


def sample_groups(scenes, timing, plan, duration, fps, cue_offset=1.7):
    """Map scene-local cues to concatenated export time without clipping bad plans."""
    if not math.isfinite(cue_offset) or cue_offset < 0:
        raise ValueError('Cue offset must be finite and nonnegative')
    end=max(0,duration-1/fps)
    groups=[{'id':'contact','purpose':'Distributed final frames','times':[end*i/11 for i in range(12)]},
            {'id':'opening','purpose':'Opening motion samples','times':[min(end,3)*i/7 for i in range(8)]}]
    offsets={};offset=0
    for scene,length in scenes:
        if not math.isfinite(length) or length<=0:raise ValueError('Invalid scene duration')
        offsets[scene]=(offset,length);offset+=length
    if abs(offset-duration)>.25:raise ValueError('Scene timeline differs from final video')
    cues=[]
    for scene,(offset,length) in offsets.items():
        mapping=timing.get(scene)
        if not isinstance(mapping,dict) or not mapping:raise ValueError('Every scene needs compiled cues')
        for cue,time in mapping.items():
            if isinstance(time,bool) or not isinstance(time,(int,float)) or not math.isfinite(time) or not 0<=time<length:
                raise ValueError('Cue must lie within its scene')
            cues.append(min(offset+time+cue_offset,offset+length-1/fps,end))
    groups.append({'id':'cues','purpose':f'Every authored cue sampled {cue_offset}s afterward, bounded by its scene','times':cues})
    intervals=plan.get('intervals',[])
    if not intervals:raise ValueError('At least one authored critical interval is required')
    seen=set()
    for index,item in enumerate(intervals):
        scene=item.get('scene',scenes[0][0] if len(scenes)==1 else None)
        if scene not in offsets:raise ValueError('Multi-scene review intervals must name a known scene')
        identity=(scene,item.get('id'))
        if identity in seen:raise ValueError('Duplicate review interval in scene')
        seen.add(identity)
        offset,length=offsets[scene]
        resolved=interval_samples({'intervals':[item]},timing[scene],length)[0]
        groups.append({'id':f'interval-{index+1}','source_id':item['id'],'scene':scene,
                       'purpose':resolved['purpose'],'times':[offset+t for t in resolved['times']]})
    groups.append({'id':'ending','purpose':'Last fifteen seconds through final decodable frame',
                   'times':ending_samples(duration,15,9,fps)})
    return groups


def extract(project,cue_offset=1.7):
    export=project.artifact('export',media.assembly_fingerprint(project))
    if not export:raise ProductionError('EXPORT_REQUIRED','Assemble a current final export')
    info=media.probe(export['absolute_path'])
    video=next(s for s in info['streams'] if s.get('codec_type')=='video')
    fps=float(Fraction(video['avg_frame_rate']))
    frames=video.get('nb_frames')
    duration=int(frames)/fps if frames and frames!='N/A' else float(video['duration'])
    scenes=[(scene['id'],render['metadata']['duration']) for scene,render,_ in media.current_renders(project)]
    try:
        timing=read_json(project.root/'assets/timing.json');plan=read_json(project.root/'assets/review-plan.json')
        groups=sample_groups(scenes,timing,plan,duration,fps,cue_offset)
    except (ValueError,FileNotFoundError) as exc:
        raise ProductionError('REVIEW_PLAN_REQUIRED',str(exc)) from exc
    worker=media.ROOT/'workers/visual_review.py'
    fingerprint=digest({'export':export['sha256'],'groups':groups,'worker':file_hash(worker)})
    out=project.root/'reviews/visual-evidence'/fingerprint[:12]
    report=out/'evidence.json'
    if report.exists():
        old=read_json(report)
        files=[record for group in old.get('groups',[]) for key in ('frames','sheets') for record in group[key]]
        if old.get('fingerprint')==fingerprint and files and all(Path(r['path']).is_file() and file_hash(Path(r['path']))==r['sha256'] for r in files):
            return {'cached':True,'path':str(report),'automatic_acceptance':False}
    request=project.root/'.mathtuber/visual-evidence-request.json'
    atomic_json(request,{'export':export['absolute_path'],'export_sha256':export['sha256'],
                         'groups':groups,'fingerprint':fingerprint,'output':str(out)})
    output,_=media.run([media.python_executable(),worker,request],timeout=1800)
    return json.loads(output)
