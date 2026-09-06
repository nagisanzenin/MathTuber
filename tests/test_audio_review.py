import json
from pathlib import Path
import sys
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import patch

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'plugins/mathtuber'))
from mathtuber.audio_review import inspect_audio
from mathtuber.state import ProductionError


class AudioReviewTests(unittest.TestCase):
    def test_cache_is_bound_to_audio_text_and_requested_asr(self):
        with tempfile.TemporaryDirectory() as directory:
            root=Path(directory);(root/'reviews').mkdir()
            project=SimpleNamespace(root=root,data={'scenes':[{'id':'s01','narration':'Two thirds'}]})
            audio={'absolute_path':'fixture.wav','sha256':'first'}
            def run(*args,**kw):
                request=json.loads((root/'.mathtuber/audio-inspection-request.json').read_text())
                (root/'reviews/audio-inspection.json').write_text(json.dumps({'fingerprint':request['fingerprint']}))
                return json.dumps({'cached':False,'automatic_acceptance':False}),0
            with patch('mathtuber.audio_review.media.audio_for',return_value=audio),patch('mathtuber.audio_review.media.run',side_effect=run) as worker:
                self.assertFalse(inspect_audio(project)['cached'])
                self.assertTrue(inspect_audio(project)['cached'])
                audio['sha256']='second'
                self.assertFalse(inspect_audio(project)['cached'])
                project.data['scenes'][0]['narration']='One third'
                self.assertFalse(inspect_audio(project)['cached'])
                self.assertFalse(inspect_audio(project,asr=False)['cached'])
                self.assertEqual(worker.call_count,4)

    def test_missing_current_audio_prevents_review(self):
        project=SimpleNamespace(data={'scenes':[{'id':'s01'}]})
        with patch('mathtuber.audio_review.media.audio_for',side_effect=ProductionError('AUDIO_REQUIRED','Stale')),patch('mathtuber.audio_review.media.run') as run:
            with self.assertRaises(ProductionError):inspect_audio(project)
            run.assert_not_called()


if __name__=='__main__':unittest.main()
