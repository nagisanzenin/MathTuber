"""Captioned scene previews for inspection; never a publishable export."""
from pathlib import Path
from .state import ProductionError, digest, file_hash
from .media import audio_for, render_fingerprint, run, probe
from .captions import scene_srt, make_ass
from .caption_style import resolve_style
from .profiles import load

def captioned_preview(project, sid):
    scene = project.scene(sid)
    render = project.artifact(f'render:preview:{sid}', render_fingerprint(project, scene, 'preview'))
    if render is None:
        raise ProductionError('PREVIEW_REQUIRED', f'Render the current preview for {sid} first')
    audio = audio_for(project, scene)
    settings = project.data.get('captions', {})
    style = resolve_style(load(project), settings.get('style') if isinstance(settings, dict) else None)
    package = Path(__file__).parent
    fingerprint = digest(dict(render=render['sha256'], audio=audio['sha256'], settings=settings,
                              style=style, workers={n:file_hash(package/n) for n in
                              ('prototype.py','captions.py','caption_style.py')}))
    key = f'prototype:captioned:{sid}'
    cached = project.artifact(key, fingerprint)
    if cached:
        return dict(cached=True, artifact=cached, publishable=False)
    folder = project.root/'reviews'/'captioned-previews'/sid/fingerprint[:12]
    folder.mkdir(parents=True, exist_ok=True)
    duration = render['metadata']['duration']
    info = probe(render['absolute_path'])
    video = next(s for s in info['streams'] if s['codec_type']=='video')
    srt = '\n'.join(scene_srt(scene, audio['metadata'], duration, settings))
    (folder/'captions.srt').write_text(srt)
    (folder/'captions.ass').write_text(make_ass(srt, video['width'], video['height'], style))
    _, elapsed = run(['ffmpeg','-y','-v','error','-i',render['absolute_path'],'-i',audio['absolute_path'],
                     '-map','0:v:0','-map','1:a:0','-vf','ass=captions.ass','-af','apad',
                     '-t',str(duration),'-c:v','libx264','-preset','veryfast','-crf','23',
                     '-pix_fmt','yuv420p','-c:a','aac','-movflags','+faststart','preview.mp4'],
                    cwd=folder, timeout=1800)
    output = folder/'preview.mp4'; delivery = probe(output)
    if abs(delivery['duration']-duration)>.25:
        raise ProductionError('PROTOTYPE_DURATION', 'Captioned prototype lost part of the scene')
    artifact = project.record(key, fingerprint, output, dict(duration=delivery['duration'],
                              width=video['width'],height=video['height'],seconds=elapsed,
                              scope='scene prototype with narration and captions; no soundtrack or final review'))
    return dict(cached=False, artifact=artifact, publishable=False)
