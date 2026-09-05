"""Validated caption appearance shared by channel profiles and project overrides."""
import re
from .state import ProductionError

DEFAULT_STYLE = dict(font='Arial', font_size=44, color='#FFFFFF', outline_color='#080E15',
                     outline=3, bold=True, margin_bottom=225, margin_side=108, wrap_width=34)

def validate_style(style):
    if not isinstance(style, dict) or set(style) - set(DEFAULT_STYLE):
        raise ProductionError('CAPTION_STYLE', 'Caption style must contain only documented style fields')
    for key, value in style.items():
        if key == 'font':
            if not isinstance(value, str) or not re.fullmatch(r'[\w .-]{1,80}', value):
                raise ProductionError('CAPTION_STYLE', 'Use a plain installed font family name')
        elif key in ('color', 'outline_color'):
            if not isinstance(value, str) or not re.fullmatch(r'#[0-9a-fA-F]{6}', value):
                raise ProductionError('CAPTION_STYLE', f'{key} must be #RRGGBB')
        elif key == 'bold':
            if not isinstance(value, bool):
                raise ProductionError('CAPTION_STYLE', 'bold must be boolean')
        else:
            bounds = dict(font_size=(28,80), outline=(0,8), margin_bottom=(80,500),
                          margin_side=(40,250), wrap_width=(18,50))
            low, high = bounds[key]
            if isinstance(value, bool) or not isinstance(value, (int,float)) or not low <= value <= high:
                raise ProductionError('CAPTION_STYLE', f'{key} must be between {low} and {high}')
            if key == 'wrap_width' and not isinstance(value, int):
                raise ProductionError('CAPTION_STYLE', 'wrap_width must be an integer')
    return style

def resolve_style(profile=None, overrides=None):
    inherited = profile.get('identity', {}).get('captions', {}) if profile else {}
    return {**DEFAULT_STYLE, **validate_style(inherited), **validate_style({} if overrides is None else overrides)}

def ass_color(value):
    return '&H00'+value[5:7]+value[3:5]+value[1:3]
