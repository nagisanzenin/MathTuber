import copy
import json
from contextlib import nullcontext
from unittest.mock import patch
import math
import sys
import tempfile
import unittest
import wave
from array import array
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'plugins/mathtuber'))
from mathtuber.listening import resolve_windows
from mathtuber.sound_events import write_score
from mathtuber.state import ProductionError


class ListeningTests(unittest.TestCase):
    def setUp(self):
        self.item = dict(id='bottle', scene='s02', paragraph_pause=0, offset=.1,
                         duration=.8, meaning='Smaller air volume raises resonance',
                         tones=[dict(frequency_hz=400, amplitude=.1)])
        self.pauses = {'s02': [dict(start=2, end=3)]}

    def test_measured_absolute_pause(self):
        result = resolve_windows([self.item], self.pauses, 4)
        self.assertEqual(result[0]['time'], 2.1)
        self.assertEqual(result[0]['duration'], .8)

    def test_invalid_and_spoken_overlap_fail(self):
        for changes in [dict(duration=1), dict(offset=-1), dict(paragraph_pause=-1),
                        dict(paragraph_pause=True), dict(paragraph_pause=1), dict(scene='absent'),
                        dict(duration=float('nan')), dict(fade_seconds=0), dict(meaning=''),
                        dict(tones=[]), dict(tones=[dict(frequency_hz=24000, amplitude=.1)]),
                        dict(tones=[dict(frequency_hz=True, amplitude=.1)]),
                        dict(tones=[dict(frequency_hz=400, amplitude=float('inf'))])]:
            with self.subTest(changes=changes), self.assertRaises(ProductionError):
                resolve_windows([{**self.item, **changes}], self.pauses, 4)

    def test_duplicate_and_overlap(self):
        for other in [self.item, {**self.item, 'id': 'other'}]:
            with self.assertRaises(ProductionError):
                resolve_windows([self.item, other], self.pauses, 4)

    def test_silence_frequency_and_reproducibility(self):
        windows = resolve_windows([self.item], self.pauses, 4)
        with tempfile.TemporaryDirectory() as directory:
            a, b = [Path(directory) / name for name in ['a.wav', 'b.wav']]
            write_score(a, [], 4, windows=windows)
            write_score(b, [], 4, windows=windows)
            self.assertEqual(a.read_bytes(), b.read_bytes())
            with wave.open(str(a)) as sound:
                self.assertEqual(sound.getnframes(), 96000)
                samples = array('h', sound.readframes(96000))
                if sys.byteorder != 'little': samples.byteswap()
            self.assertFalse(any(samples[:50400]))
            self.assertFalse(any(samples[69600:]))
            self.assertEqual(samples[50400], 0)
            self.assertEqual(samples[69599], 0)
            # Stable plateau spans exactly 0.5 sec: 200 positive crossings at 400 Hz.
            plateau = samples[55200:67201]
            crossings = sum(a <= 0 < b for a, b in zip(plateau, plateau[1:]))
            self.assertEqual(crossings, 200)
            self.assertLessEqual(max(map(abs, samples)), 3277)

    def test_action_sounds_cannot_mask_listening(self):
        windows = resolve_windows([self.item], self.pauses, 4)
        event = dict(time=2.2, duration=.1, frequency=330, amplitude=.04)
        with tempfile.TemporaryDirectory() as directory, self.assertRaises(ProductionError):
            write_score(Path(directory) / 'x.wav', [event], 4, windows=windows)

    def test_compiler_preserves_both_plans_and_scene_offsets(self):
        from scripts import score_events
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / 'assets').mkdir()
            (root / 'assets/timing.json').write_text(json.dumps({'s01': {'tap': .1}, 's02': {}}))
            (root / 'assets/sound-events.json').write_text(json.dumps([dict(scene='s01', cue='tap', kind='tap')]))
            (root / 'assets/listening-windows.json').write_text(json.dumps([self.item]))
            class FakeProject:
                manifest_path = root / 'project.json'
                data = {'format': {'fps': 30}, 'scenes': [{'id': 's01'}, {'id': 's02'}]}
                def lock(self): return nullcontext()
            project = FakeProject()
            project.root = root
            def audio(project, scene):
                metadata = dict(duration=1.01) if scene['id'] == 's01' else dict(duration=4, word_timing=dict(paragraph_pauses=[dict(start=2, end=3)]))
                return dict(metadata=metadata)
            with patch.object(score_events, 'Project', return_value=project), patch.object(score_events, 'audio_for', side_effect=audio), patch.object(sys, 'argv', ['score_events', '--project', directory]):
                score_events.main()
            report = json.loads((root / 'assets/sound-design.json').read_text())
            self.assertEqual(len(report['events']), 1)
            self.assertAlmostEqual(report['windows'][0]['time'], 31/30 + 2.1)
            self.assertEqual(project.data['soundtrack']['path'], 'assets/score.wav')
            with wave.open(str(root / 'assets/score.wav')) as sound:
                self.assertEqual(sound.getframerate(), 48000)
                self.assertEqual(sound.getnframes(), 241600)


if __name__ == '__main__':
    unittest.main()
