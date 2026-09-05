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
if __name__=='__main__':unittest.main()
