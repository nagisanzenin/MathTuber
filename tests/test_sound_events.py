import sys
import tempfile
import unittest
import wave
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "plugins/mathtuber"))
from mathtuber.sound_events import resolve_events, write_score
from mathtuber.state import ProductionError

class SoundEventsTests(unittest.TestCase):
    def test_landing_offset(self):
        event = resolve_events([{"scene":"s01","cue":"land","kind":"tap","offset":.7}], {"s01":{"land":2}}, 5)[0]
        self.assertEqual(event["time"], 2.7)
    def test_invalid_events_fail(self):
        for changes in ({"cue":"missing"}, {"offset":-3}, {"offset":float("nan")}, {"amplitude":.5}, {"kind":"unknown"}, {"offset":3}):
            event = {"scene":"s01","cue":"land","kind":"tap", **changes}
            with self.assertRaises(ProductionError): resolve_events([event], {"s01":{"land":2}}, 5)
    def test_score_keeps_reasoning_silent(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "score.wav"
            events = resolve_events([{"scene":"s01","cue":"land","kind":"tap"}], {"s01":{"land":1}}, 2)
            write_score(path, events, 2)
            with wave.open(str(path)) as sound:
                self.assertEqual(sound.getnframes(), 48000)
                self.assertEqual(sound.readframes(24000), bytes(48000))
                self.assertNotEqual(sound.readframes(2400), bytes(4800))
                self.assertEqual(sound.readframes(21600), bytes(43200))
