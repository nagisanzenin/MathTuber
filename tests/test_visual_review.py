from pathlib import Path
import sys
import unittest
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'plugins/mathtuber'))
from mathtuber.visual_review import sample_groups


class VisualSamplingTests(unittest.TestCase):
    def interval(self,**kw):
        return dict(id='mapping',start_cue='begin',end_cue='end',purpose='Compare the changed relation',samples=3,**kw)

    def test_multiscene_intervals_follow_export_offsets(self):
        groups=sample_groups([('s01',10),('s02',20)],{'s01':{'first':1},'s02':{'begin':2,'end':8}},
                             {'intervals':[self.interval(scene='s02')]},30,30)
        interval=next(g for g in groups if g['id']=='interval-1')
        self.assertEqual(interval['times'],[12,15,18])
        self.assertAlmostEqual(groups[-1]['times'][-1],30-1/30)
        self.assertEqual(len(groups[2]['times']),3)

    def test_missing_scene_is_not_silently_mapped_to_first(self):
        with self.assertRaisesRegex(ValueError,'must name'):
            sample_groups([('s01',10),('s02',10)],{'s01':{'begin':1,'end':8},'s02':{'begin':1,'end':8}},
                          {'intervals':[self.interval()]},20,30)

    def test_legacy_single_scene_plan_and_bounded_cue_samples(self):
        groups=sample_groups([('s01',10)],{'s01':{'begin':1,'end':9.9}},
                             {'intervals':[self.interval()]},10,30)
        self.assertAlmostEqual(groups[2]['times'][-1],10-1/30)
        self.assertEqual(groups[3]['times'][-1],9.9)

    def test_bad_interval_cannot_be_clipped_into_valid_coverage(self):
        with self.assertRaisesRegex(ValueError,'wholly within'):
            sample_groups([('s01',10)],{'s01':{'begin':1,'end':9}},
                          {'intervals':[self.interval(end_offset=2)]},10,30)

    def test_invalid_cue_and_missing_plan_are_rejected(self):
        for timing,plan in [({'s01':{'begin':-1}},{}),({'s01':{'begin':1}},{})]:
            with self.subTest(timing=timing),self.assertRaises(ValueError):
                sample_groups([('s01',10)],timing,plan,10,30)


if __name__=='__main__':unittest.main()
