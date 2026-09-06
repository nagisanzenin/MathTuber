"""Exercise real audio inspection and stale-input refusal without ASR downloads."""
import hashlib
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
import numpy as np
import soundfile as sf

WORKER=Path(__file__).resolve().parents[1]/'plugins/mathtuber/workers/audio_review.py'
spec=importlib.util.spec_from_file_location('audio_review_worker',WORKER)
worker=importlib.util.module_from_spec(spec);spec.loader.exec_module(worker)


class AudioInspectionTests(unittest.TestCase):
    def test_opposing_stereo_peaks_cannot_cancel_clipping(self):
        samples=np.array([[1.2,-1.2],[0,0],[.2,-.2]])
        result=worker.signal(samples,24000)
        self.assertAlmostEqual(result['peak'],1.2)
        self.assertAlmostEqual(result['clipped_sample_fraction'],1/3)
        self.assertEqual(result['duration'],3/24000)
        with self.assertRaises(ValueError):worker.signal([float('nan')],24000)

    def test_comparison_reports_changed_math_without_passing_it(self):
        result=worker.compare('The probability is two thirds.','The probability is one third.')
        self.assertEqual(result['differences'],[{'expected':'two thirds','recognized':'one third'}])

    def test_worker_reports_missing_asr_and_rejects_changed_input(self):
        with tempfile.TemporaryDirectory() as directory:
            root=Path(directory);audio=root/'signal.wav';out=root/'report.json';request=root/'request.json'
            sf.write(audio,np.zeros(2400),24000)
            data={'items':[{'scene':'s01','path':str(audio),'sha256':hashlib.sha256(audio.read_bytes()).hexdigest(),'expected':'A pause'}],
                  'asr':False,'model':'small.en','language':'en','export':None,'fingerprint':'fixture','output':str(out)}
            request.write_text(json.dumps(data))
            subprocess.run([sys.executable,str(WORKER),str(request)],check=True,capture_output=True)
            report=json.loads(out.read_text())
            self.assertFalse(report['automatic_acceptance'])
            self.assertEqual(report['scenes'][0]['transcription_status'],'unavailable')
            self.assertAlmostEqual(report['scenes'][0]['signal']['longest_low_energy_seconds'],.1)
            self.assertNotIn('verdict',report)
            sf.write(audio,np.ones(2400)*.3,24000)
            result=subprocess.run([sys.executable,str(WORKER),str(request)],capture_output=True,text=True)
            self.assertNotEqual(result.returncode,0)
            self.assertIn('STALE_AUDIO',result.stderr)


if __name__=='__main__':unittest.main()
