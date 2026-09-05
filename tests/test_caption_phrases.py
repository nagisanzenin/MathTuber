import unittest,sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'plugins/mathtuber'))
from mathtuber.captions import caption_groups,phrase_wrap
from mathtuber.state import ProductionError
class PhraseTests(unittest.TestCase):
 def words(self,text):return [dict(text=x,start=i*.2,end=(i+1)*.2) for i,x in enumerate(text.split())]
 def test_orphan_article_regression(self):
  g=caption_groups(self.words('Four bugs chase each other around a square .'))
  self.assertEqual(len(g),1);self.assertEqual(g[0][-1]['text'],'square.');self.assertAlmostEqual(g[0][-1]['end'],1.8)
 def test_exact_phrases_keep_timestamps_and_order(self):
  w=self.words('Move the touching point again . The equality survives .');g=caption_groups(w,['Move the touching point again.','The equality survives.'])
  self.assertEqual(g[1][0]['start'],w[6]['start']);self.assertEqual(g[-1][-1]['end'],w[-1]['end'])
 def test_stale_or_omitted_or_reordered_words_fail(self):
  for phrases in [['Move it.'],['Move the point again.'],['Move point the.'],[]]:
   with self.subTest(phrases=phrases),self.assertRaises(ProductionError):caption_groups(self.words('Move the point .'),phrases)
 def test_line_break_keeps_article_with_noun(self):
  x=phrase_wrap('We are aiming to get a better television service.',34)
  self.assertNotIn(' a'+r'\N',x);self.assertIn(r'\N',x)
 def test_punctuation_not_discarded_between_phrases(self):
  g=caption_groups(self.words('Yes ! No ?'),['Yes!','No?']);self.assertEqual([x[-1]['text'] for x in g],['Yes!','No?'])
