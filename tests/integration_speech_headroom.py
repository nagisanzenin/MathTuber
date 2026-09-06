"""Run with the media runtime; exercise the real worker's PCM write boundary."""
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

import numpy as np
import soundfile as sf

WORKER = Path(__file__).resolve().parents[1] / "plugins/mathtuber/workers/speech.py"


class SpeechHeadroomTests(unittest.TestCase):
    def test_float_peaks_are_attenuated_without_clipping_or_retiming(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for values in ([0, .5, 1.4, -.7, -1.2, 0], [0, .1, -.2, 0], [0, 0]):
                samples = np.array(values, dtype=np.float32)
                source, output = root / "input.wav", root / "output.wav"
                sf.write(source, samples, 24000, subtype="FLOAT")
                request = root / "request.json"
                request.write_text(json.dumps({
                    "speech": {"provider": "wav", "tail_seconds": 0},
                    "items": [{"scene": {"narration": "Test", "audio_source": str(source)},
                               "output": str(output)}],
                }))
                subprocess.run([sys.executable, str(WORKER), str(request)], check=True)
                actual, rate = sf.read(output)
                peak = float(np.max(np.abs(samples)))
                gain = min(1, .98 / peak) if peak else 1
                self.assertEqual(rate, 24000)
                self.assertEqual(len(actual), len(samples))
                np.testing.assert_allclose(actual, samples * gain, atol=1 / 32768)
                self.assertLessEqual(float(np.max(np.abs(actual))), .98004)
                metadata = json.loads(output.with_suffix('.words.json').read_text())
                self.assertAlmostEqual(metadata['pcm_headroom']['gain'], gain)
                self.assertEqual(metadata['words'], [])


if __name__ == '__main__':
    unittest.main()
