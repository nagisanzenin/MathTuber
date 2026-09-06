"""Capability dependency reporting, distinct from model or account verification."""
PACKAGES=('manim','numpy','soundfile','kokoro','en-core-web-sm','Pillow','faster-whisper',
          'google-api-python-client','google-auth','google-auth-oauthlib')


def capabilities(executables, packages, pacific_timezone):
    requirements={
        'render':(('ffmpeg','ffprobe','latex','dvisvgm'),('manim','numpy')),
        'narration':(('espeak-ng',),('kokoro','en-core-web-sm','soundfile','numpy')),
        'imported_audio':((),('soundfile','numpy')),
        'assembly':(('ffmpeg','ffprobe'),()),
        'visual_review':(('ffmpeg','ffprobe'),('Pillow',)),
        'audio_signal_review':(('ffmpeg',),('numpy','soundfile')),
        'independent_asr':((),('faster-whisper','numpy','soundfile')),
        'youtube':((),('google-api-python-client','google-auth','google-auth-oauthlib')),
    }
    result={}
    for name,(commands,distributions) in requirements.items():
        missing=[f'executable:{x}' for x in commands if not executables.get(x)]
        missing += [f'package:{x}' for x in distributions if not packages.get(x)]
        if name=='youtube' and not pacific_timezone:missing.append('timezone:America/Los_Angeles (install tzdata)')
        result[name]={'dependencies_ready':not missing,'missing':missing}
    return result
