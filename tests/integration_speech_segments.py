"""Run with the media runtime: sample-accurate pauses feed cues and captions."""
from pathlib import Path
import sys,unittest
import numpy as np
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'plugins/mathtuber'))
from mathtuber.speech_segments import synthesize_paragraphs
from mathtuber.captions import scene_srt
from scripts.compile_cues import resolve_cues
class SpeechTimelineTests(unittest.TestCase):
    def test_silence_samples_words_cues_and_captions_agree(self):
        def synth(text):return np.ones(1000),1000,[dict(text=text,start=.1,end=.9)]
        audio,rate,words,pauses=synthesize_paragraphs('First.\n\nSecond.\n\nThird.',synth,1.2345)
        self.assertEqual(len(audio),3000+2*1234)
        self.assertTrue(np.all(audio[1000:2234]==0))
        self.assertTrue(np.all(audio[2234:3234]==1))
        self.assertAlmostEqual(words[1]['start'],2.334)
        self.assertAlmostEqual(words[2]['end'],5.368)
        self.assertEqual(pauses[0],dict(start=1,end=2.234,after_paragraph=1))
        cues=resolve_cues("self.at('Second')",words);self.assertEqual(cues['Second'],2.334)
        srt=scene_srt(dict(id='s01',narration='First. Second. Third.'),{'word_timing':{'words':words}},len(audio)/rate)
        self.assertIn('00:00:02,334 --> 00:00:03,134',srt[1])
    def test_incompatible_chunks_rejected(self):
        for bad in ['rate','channels','timing']:
            def synth(text):
                rate=2000 if bad=='rate' and text=='Second.' else 1000
                data=np.ones((1000,2)) if bad=='channels' and text=='Second.' else np.ones(1000)
                return data,rate,[dict(text=text,start=0,end=5 if bad=='timing' else .4)]
            with self.subTest(bad=bad),self.assertRaises(ValueError):synthesize_paragraphs('First.\n\nSecond.',synth,1)
    def test_single_paragraph_adds_no_leading_or_trailing_silence(self):
        data=np.array([.2,.3,.4])
        audio,rate,words,pauses=synthesize_paragraphs('Only.',lambda _: (data,1000,[]),1)
        np.testing.assert_array_equal(data,audio);self.assertEqual(pauses,[])
if __name__=='__main__':unittest.main()
