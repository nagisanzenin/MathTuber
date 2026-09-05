"""Readable portrait captions, generated from measured SRT timing."""
import re
import textwrap

def ass_time(value):
    hours,minutes,seconds=value.replace(',', '.').split(':')
    total=round((int(hours)*3600+int(minutes)*60+float(seconds))*100)
    h,total=divmod(total,360000);m,total=divmod(total,6000);s,cs=divmod(total,100)
    return f'{h}:{m:02}:{s:02}.{cs:02}'

def make_ass(srt,width=1080,height=1920):
    fontsize=round(height*44/1920);margin=round(height*225/1920)
    lines=['[Script Info]','ScriptType: v4.00+',f'PlayResX: {width}',f'PlayResY: {height}','WrapStyle: 2','',
           '[V4+ Styles]',
           'Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding',
           f'Style: Default,Arial,{fontsize},&H00FFFFFF,&H00FFFFFF,&H00150E08,&H80150E08,-1,0,0,0,100,100,0,0,1,3,0,2,{round(width*.1)},{round(width*.1)},{margin},1','',
           '[Events]','Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text']
    cues = []
    for block in re.split(r'\n\s*\n',srt.strip()):
        parts=block.splitlines()
        if len(parts)<3:continue
        start,end=parts[1].split(' --> ')
        text=' '.join(parts[2:]).strip()
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
        text=r'\N'.join(textwrap.wrap(text,width=34,break_long_words=False,break_on_hyphens=False))
        lines.append(f'Dialogue: 0,{ass_time(start)},{ass_time(end)},Default,,0,0,0,,{text}')
    return '\n'.join(lines)+'\n'
