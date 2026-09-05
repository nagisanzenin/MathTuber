import sys
from pathlib import Path
import unittest
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'plugins/mathtuber'))
from mathtuber.caption_style import resolve_style
from mathtuber.captions import make_ass,caption_groups,phrase_wrap
from mathtuber.state import ProductionError

class CaptionStyleTests(unittest.TestCase):
    def test_profile_style_and_project_override_reach_ass(self):
        profile={'identity':{'captions':{'font':'Avenir Next','color':'#243944','bold':False}}}
        style=resolve_style(profile,{'font_size':50})
        ass=make_ass('1\n00:00:00,000 --> 00:00:02,000\nA quiet curve.\n',style=style)
        self.assertIn('Default,Avenir Next,50,&H00443924',ass)
        self.assertIn('&H80150E08,0,0,0,0',ass)
        self.assertEqual(resolve_style()['font'],'Arial')

    def test_reject_injected_or_invalid_style(self):
        for bad in [{'font':'Arial\n[Events]'}, {'color':'white'}, {'outline':float('nan')},
                    {'font_size':True},{'wrap_width':34.5},{'typo':4},[]]:
            with self.subTest(bad=bad), self.assertRaises(ProductionError):
                resolve_style(overrides=bad)

    def test_authored_line_break_survives_ass_and_matches_speech(self):
        text='Left heavy, right heavy,\nor balanced.'
        words=[dict(text=w,start=i,end=i+1) for i,w in enumerate(text.split())]
        self.assertEqual(len(caption_groups(words,[text])),1)
        ass=make_ass('1\n00:00:00,000 --> 00:00:04,000\n'+text+'\n')
        self.assertIn(r'Left heavy, right heavy,\Nor balanced.',ass)
        with self.assertRaises(ProductionError):phrase_wrap('one\ntwo\nthree')
        with self.assertRaises(ProductionError):phrase_wrap('a'*35+'\nshort')
