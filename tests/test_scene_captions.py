import sys
from pathlib import Path
import unittest
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'plugins/mathtuber'))
from mathtuber.captions import scene_srt
from mathtuber.state import ProductionError

class SceneCaptionTests(unittest.TestCase):
    def test_authored_line_breaks_keep_global_timing_and_numbering(self):
        scene={'id':'s02','narration':'One choice. Two paths.'}
        audio={'word_timing':{'words':[{'text':w,'start':a,'end':b} for w,a,b in
                [('One',0,.4),('choice.',.5,.9),('Two',1,1.3),('paths.',1.4,1.8)]]}}
        result=scene_srt(scene,audio,2,{'phrases':{'s02':['One choice.','Two\npaths.']}},offset=10,first_index=3)
        self.assertEqual(result,['3\n00:00:10,000 --> 00:00:10,900\nOne choice.\n',
                                 '4\n00:00:11,000 --> 00:00:11,800\nTwo\npaths.\n'])
        with self.assertRaises(ProductionError):
            scene_srt(scene,audio,2,{'phrases':{'s02':['One choice.']}})

    def test_section_fallback_keeps_complete_narration(self):
        self.assertEqual(scene_srt({'id':'s01','narration':'A complete explanation.'},{},4),
                         ['1\n00:00:00,000 --> 00:00:04,000\nA complete explanation.\n'])

if __name__=='__main__':unittest.main()
