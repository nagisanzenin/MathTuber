"""Optional paragraph pauses with a single trustworthy speech timeline."""
import math
import re

def paragraph_plan(text, seconds=0):
    if isinstance(seconds, bool) or not isinstance(seconds, (int, float)) or not math.isfinite(seconds) or not 0 <= seconds <= 10:
        raise ValueError('paragraph_pause_seconds must be a finite number from 0 to 10')
    if seconds == 0:
        return [text]
    parts = [p.strip() for p in re.split(r'\n\s*\n', text) if p.strip()]
    if not parts:
        raise ValueError('Narration has no spoken paragraphs')
    return parts

def synthesize_paragraphs(text, synthesize, seconds=0):
    """Keep timings in sample time, including silence between paragraphs only."""
    import numpy as np
    parts = paragraph_plan(text, seconds)
    arrays, words, pauses = [], [], []
    rate = None
    offset_samples = 0
    shape = None
    for i, part in enumerate(parts):
        audio, chunk_rate, tokens = synthesize(part)
        audio = np.asarray(audio)
        if audio.ndim not in (1, 2) or not len(audio) or not np.isfinite(audio).all():
            raise ValueError('Invalid paragraph audio')
        if isinstance(chunk_rate, bool) or not isinstance(chunk_rate, (int, float)) or not math.isfinite(chunk_rate) or chunk_rate <= 0 or int(chunk_rate) != chunk_rate:
            raise ValueError('Invalid paragraph sample rate')
        chunk_rate = int(chunk_rate)
        if rate is None:
            rate, shape = chunk_rate, audio.shape[1:]
        elif chunk_rate != rate or audio.shape[1:] != shape:
            raise ValueError('Paragraph audio formats differ')
        if i:
            n = round(seconds * rate)
            pauses.append({'start': offset_samples/rate, 'end': (offset_samples+n)/rate, 'after_paragraph': i})
            arrays.append(np.zeros((n,) + shape, dtype=audio.dtype))
            offset_samples += n
        offset = offset_samples / rate
        for token in tokens:
            start, end = token['start'], token['end']
            if not math.isfinite(start) or not math.isfinite(end) or start < 0 or end < start or end > len(audio)/rate + .1:
                raise ValueError('Invalid paragraph word timing')
            words.append(dict(token, start=start+offset, end=end+offset))
        arrays.append(audio)
        offset_samples += len(audio)
    return np.concatenate(arrays), rate, words, pauses
