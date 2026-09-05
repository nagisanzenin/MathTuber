import sys,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'plugins/mathtuber'))
from mathtuber.speech_segments import paragraph_plan, pause_plan
class ParagraphPlanTests(unittest.TestCase):
    def test_default_preserves_existing_text_and_chunking(self):
        text='One line.\n\nAnother paragraph.'
        self.assertEqual(paragraph_plan(text),[text])
    def test_only_blank_lines_are_boundaries(self):
        self.assertEqual(paragraph_plan('First\nline.\n \nSecond.\n\n\nThird.',1),['First\nline.','Second.','Third.'])
    def test_invalid_pause_rejected(self):
        for value in [-1,11,float('inf'),float('nan'),True,'1']:
            with self.subTest(value=value),self.assertRaises(ValueError):paragraph_plan('text',value)
    def test_empty_segmented_narration_rejected(self):
        with self.assertRaises(ValueError):paragraph_plan(' \n\n ',1)

class SelectivePauseTests(unittest.TestCase):
    def test_explicit_zero_still_segments(self):
        self.assertEqual(pause_plan('One.\n\nTwo.',0,[0]),(['One.','Two.'],[0]))
    def test_one_duration_per_boundary(self):
        self.assertEqual(pause_plan('One.\n\nTwo.\n\nThree.',.4,[4,.2])[1],[4,.2])
        for values in [[],[1],[1,2,3],{},[True,0],[float('nan'),0],[-1,0]]:
            with self.subTest(values=values),self.assertRaises(ValueError):
                pause_plan('One.\n\nTwo.\n\nThree.',.4,values)

    def test_pause_edits_invalidate_cached_audio(self):
        from types import SimpleNamespace
        from mathtuber.media import audio_fingerprint
        project=SimpleNamespace(data={})
        scene=dict(narration='One.\n\nTwo.',paragraph_pauses=[1])
        before=audio_fingerprint(project,scene)
        scene['paragraph_pauses']=[3]
        self.assertNotEqual(before,audio_fingerprint(project,scene))
