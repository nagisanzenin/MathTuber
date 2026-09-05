import sys
from pathlib import Path
import unittest
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'plugins/mathtuber'))
from mathtuber.captions import ass_time,make_ass
class CaptionTests(unittest.TestCase):
 def test_centisecond_carry(self):self.assertEqual(ass_time('00:00:59,999'),'0:01:00.00')
 def test_override_text_is_not_executable(self):
  ass=make_ass('1\n00:00:00,100 --> 00:00:01,200\nHello , {\\pos(1,2)} world.\n')
  self.assertNotIn('{\\pos',ass);self.assertIn('Hello,',ass);self.assertIn('0:00:00.10,0:00:01.20',ass)
 def test_punctuation_only_cue_extends_previous_caption(self):
  ass=make_ass('1\n00:00:01,000 --> 00:00:02,000\nCount six\n\n2\n00:00:02,000 --> 00:00:02,150\n.\n\n3\n00:00:02,150 --> 00:00:03,000\nNow count twelve.\n')
  cues=[x for x in ass.splitlines() if x.startswith('Dialogue:')]
  self.assertEqual(len(cues),2)
  self.assertIn('0:00:01.00,0:00:02.15',cues[0]);self.assertTrue(cues[0].endswith('Count six.'))
 def test_leading_punctuation_does_not_create_a_caption(self):
  self.assertNotIn('Dialogue:',make_ass('1\n00:00:00,000 --> 00:00:00,100\n.\n'))
if __name__=='__main__':unittest.main()

class LeadingPunctuationTests(__import__('unittest').TestCase):
    def test_leading_comma_attaches_to_previous_caption(self):
        from mathtuber.captions import make_ass
        result=make_ass('1\n00:00:00,000 --> 00:00:01,000\nCount them\n\n2\n00:00:01,000 --> 00:00:02,000\n, not tile them.\n')
        self.assertIn('Count them,',result)
        self.assertIn(',,not tile them.',result)
        self.assertNotIn(',,\u002c not tile',result)
