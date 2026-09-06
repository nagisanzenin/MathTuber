"""Build a hash-bound audio inspection request; never produce a review verdict."""
import json
from pathlib import Path
from . import media
from .state import atomic_json, digest, file_hash


def inspect_audio(project, model='small.en', language='en', asr=True, final=False):
    items=[]
    for scene in project.data['scenes']:
        audio=media.audio_for(project,scene)
        items.append({'scene':scene['id'],'path':audio['absolute_path'],
                      'sha256':audio['sha256'],'expected':scene['narration']})
    export=None
    if final:
        export=project.artifact('export',media.assembly_fingerprint(project))
        if not export:
            from .state import ProductionError
            raise ProductionError('EXPORT_REQUIRED','Assemble the current final export first')
        export={'path':export['absolute_path'],'sha256':export['sha256']}
    worker=media.ROOT/'workers/audio_review.py'
    request={'items':items,'export':export,'asr':asr,'model':model,'language':language}
    fingerprint=digest({**request,'worker':file_hash(worker),'request_builder':file_hash(Path(__file__))})
    report=project.root/'reviews/audio-inspection.json'
    if report.exists():
        previous=json.loads(report.read_text())
        if previous.get('fingerprint')==fingerprint:
            return {'cached':True,'path':str(report),'sha256':file_hash(report),
                    'automatic_acceptance':False}
    request.update(fingerprint=fingerprint,output=str(report))
    request_path=project.root/'.mathtuber/audio-inspection-request.json'
    atomic_json(request_path,request)
    output,_=media.run([media.python_executable(),worker,request_path],timeout=1800)
    return json.loads(output)
