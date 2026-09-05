"""Data-only speech worker. One model load per section batch."""
import json
import os
from pathlib import Path
import sys
import shutil
import numpy as np
import soundfile as sf

request = json.loads(Path(sys.argv[1]).read_text())
settings = request.get("speech", {})
provider = settings.get("provider", "kokoro")
if provider == "kokoro":
    # Some macOS espeak wheels embed the build machine's data path.
    # Prefer an explicitly installed system espeak-ng when available.
    espeak = shutil.which("espeak-ng")
    if espeak and sys.platform == "darwin":
        import espeakng_loader
        prefix = Path(espeak).resolve().parents[1]
        library = prefix / "lib/libespeak-ng.dylib"
        data = prefix / "share/espeak-ng-data"
        if library.exists() and data.exists():
            espeakng_loader.get_library_path = lambda: str(library)
            espeakng_loader.get_data_path = lambda: str(data)
    from kokoro import KPipeline
    pipeline = KPipeline(lang_code=settings.get("language", "a"), repo_id="hexgrad/Kokoro-82M")
    def synthesize(text):
        arrays, words, offset = [], [], 0.0
        for result in pipeline(text, voice=settings.get("voice", "af_heart"), speed=settings.get("speed", 1.0)):
            chunk = np.asarray(result.audio)
            for token in result.tokens or []:
                if token.start_ts is not None and token.end_ts is not None:
                    words.append({"text": token.text, "start": offset+token.start_ts, "end": offset+token.end_ts})
            arrays.append(chunk)
            offset += len(chunk)/24000
        if not arrays:
            raise RuntimeError("TTS returned no speech")
        return np.concatenate(arrays), 24000, words
elif provider == "mlx":
    from mlx_audio.tts.utils import load_model
    model = load_model(settings["model"])
    def synthesize(text):
        results = list(model.generate(text=text, voice=settings.get("voice", "af_heart"), speed=settings.get("speed",1.0)))
        return np.concatenate([np.asarray(r.audio) for r in results]), results[0].sample_rate, []
elif provider == "wav":
    def synthesize(text):
        raise RuntimeError("wav import handled per item")
else:
    raise ValueError(f"Unsupported speech provider: {provider}")
for item in request["items"]:
    if provider == "wav":
        audio, rate = sf.read(item["scene"]["audio_source"])
        words = []
    else:
        audio, rate, words = synthesize(item["scene"]["narration"])
    if not np.isfinite(audio).all() or len(audio) == 0:
        raise ValueError("Invalid speech samples")
    # Add a short intentional breathing margin at the end.
    silence = np.zeros((int(rate * settings.get("tail_seconds", .25)),) + audio.shape[1:])
    audio = np.concatenate([audio, silence])
    path = Path(item["output"])
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(".tmp.wav")
    sf.write(tmp, audio, rate, subtype="PCM_16")
    os.replace(tmp, path)
    timing = {"method": "synthesis_predicted" if words else "unavailable", "words": words}
    path.with_suffix(".words.json").write_text(json.dumps(timing, indent=2))
