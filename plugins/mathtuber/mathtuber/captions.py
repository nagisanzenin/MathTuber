"""Readable portrait captions, generated from measured SRT timing."""
import re
import textwrap
from .state import ProductionError
from .caption_style import resolve_style, ass_color

def ass_time(value):
    hours,minutes,seconds=value.replace(',', '.').split(':')
    total=round((int(hours)*3600+int(minutes)*60+float(seconds))*100)
    h,total=divmod(total,360000);m,total=divmod(total,6000);s,cs=divmod(total,100)
    return f'{h}:{m:02}:{s:02}.{cs:02}'

def scene_srt(scene, audio, duration, settings=None, offset=0, first_index=1):
    """One caption source for final assembly and captioned scene prototypes."""
    def stamp(seconds):
        ms = round(seconds * 1000)
        h, ms = divmod(ms, 3600000); m, ms = divmod(ms, 60000); s, ms = divmod(ms, 1000)
        return f'{h:02}:{m:02}:{s:02},{ms:03}'
    words = audio.get('word_timing', {}).get('words', [])
    if not words:
        return [f"{first_index}\n{stamp(offset)} --> {stamp(offset+duration)}\n{scene['narration']}\n"]
    phrasing = settings.get('phrases', {}) if isinstance(settings, dict) else {}
    if not isinstance(phrasing, dict):
        raise ProductionError('CAPTION_PHRASES', 'captions.phrases must map scene IDs to phrase lists')
    sid = scene['id']; result = []
    for i, group in enumerate(caption_groups(words, phrasing.get(sid))):
        start = offset + max(0, min(duration, group[0]['start']))
        end = offset + min(duration, max(group[-1]['end'], group[0]['start']+.1))
        text = phrasing[sid][i] if sid in phrasing else ' '.join(w['text'] for w in group)
        result.append(f'{first_index+i}\n{stamp(start)} --> {stamp(end)}\n{text}\n')
    return result

def make_ass(srt,width=1080,height=1920,style=None):
    style=resolve_style(overrides=style)
    fontsize=round(height*style['font_size']/1920);margin=round(height*style['margin_bottom']/1920)
    side=round(width*style['margin_side']/1080)
    color=ass_color(style['color']);outline_color=ass_color(style['outline_color'])
    lines=['[Script Info]','ScriptType: v4.00+',f'PlayResX: {width}',f'PlayResY: {height}','WrapStyle: 2','',
           '[V4+ Styles]',
           'Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding',
           f"Style: Default,{style['font']},{fontsize},{color},{color},{outline_color},&H80150E08,{-1 if style['bold'] else 0},0,0,0,100,100,0,0,1,{style['outline']*height/1920:g},0,2,{side},{side},{margin},1",'',
           '[Events]','Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text']
    cues = []
    for block in re.split(r'\n\s*\n',srt.strip()):
        parts=block.splitlines()
        if len(parts)<3:continue
        start,end=parts[1].split(' --> ')
        text='\n'.join(parts[2:]).strip()
        # Synthesis can emit punctuation as a separate token at a chunk boundary.
        leading = re.match(r'^([.,!?;:…]+)\s*', text)
        if leading:
            if cues:
                cues[-1][2] += leading.group(1)
            text = text[leading.end():]
            if not text:
                if cues:
                    cues[-1][1] = end
                continue
        cues.append([start,end,text])
    for start,end,text in cues:
        text=re.sub(r'\s+([,.!?;:])',r'\1',text)
        text=text.replace('\\','/').replace('{','(').replace('}',')')
        text=phrase_wrap(text,style['wrap_width'])
        lines.append(f'Dialogue: 0,{ass_time(start)},{ass_time(end)},Default,,0,0,0,,{text}')
    return '\n'.join(lines)+'\n'


# A small English fallback, not a syntactic parser. Agents can supply exact phrases.
_DEPENDENT = {"a", "an", "the", "of", "to", "from", "with", "at", "by", "for", "and", "or", "but", "than", "this", "that", "these", "those", "its", "your", "our"}

def _lexical(text):
    return re.findall(r"[^\W_]+", text.casefold(), flags=re.UNICODE)

def caption_groups(words, phrases=None):
    """Preserve all spoken words and their timing; never silently accept stale prose."""
    units = []
    for word in words:
        if not _lexical(word["text"]):
            if units:
                units[-1]["text"] += word["text"].strip()
                units[-1]["end"] = max(units[-1]["end"], word["end"])
            continue
        units.append(dict(word))
    if phrases is not None:
        if not isinstance(phrases, list) or not phrases or any(not isinstance(x, str) or not _lexical(x) for x in phrases):
            raise ProductionError("CAPTION_PHRASES", "Supply a nonempty list of complete spoken phrases")
        groups, cursor = [], 0
        for phrase in phrases:
            wanted = _lexical(phrase); got = []; start = cursor
            while cursor < len(units) and len(got) < len(wanted):
                got += _lexical(units[cursor]["text"]); cursor += 1
            if got != wanted:
                raise ProductionError("CAPTION_PHRASES", "Authored phrases must match the current speech words in order")
            groups.append(units[start:cursor])
        if cursor != len(units):
            raise ProductionError("CAPTION_PHRASES", "Authored phrases omit spoken words")
        return groups
    groups, current = [], []
    for i, word in enumerate(units):
        current.append(word)
        terminal = bool(re.search(r"[.!?;][\"’']?$", word["text"]))
        count = sum(len(_lexical(w["text"])) for w in current)
        if terminal or (count >= 7 and _lexical(word["text"])[-1] not in _DEPENDENT) or count >= 11 or i == len(units)-1:
            groups.append(current); current = []
    return groups

def phrase_wrap(text, width=34):
    """Prefer a two-line phrase boundary; bounded heuristic, with safe long-text fallback."""
    if '\n' in text:
        lines=text.split('\n')
        if len(lines)>2 or any(not x.strip() or len(x.strip())>width for x in lines):
            raise ProductionError('CAPTION_LINES', 'Explicit captions need one or two nonempty lines within wrap_width')
        return r"\N".join(x.strip() for x in lines)
    words = text.split()
    if len(text) <= width:
        return text
    candidates = []
    for i in range(1, len(words)):
        a, b = ' '.join(words[:i]), ' '.join(words[i:])
        if max(len(a), len(b)) > width:
            continue
        lexical = _lexical(words[i-1])
        penalty = 100 if lexical and lexical[-1] in _DEPENDENT else 0
        penalty += 35 if min(i,len(words)-i) == 1 else 0
        candidates.append((penalty + abs(len(a)-len(b)), a, b))
    if candidates:
        _, a, b = min(candidates)
        return a + r"\N" + b
    return r"\N".join(textwrap.wrap(text,width=width,break_long_words=False,break_on_hyphens=False))
