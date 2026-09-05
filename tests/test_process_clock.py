import math
from pathlib import Path
import sys
import unittest
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'plugins/mathtuber'))
from mathtuber.process_clock import ProcessClock


class ProcessClockTests(unittest.TestCase):
    def test_equal_elapsed_time_independent_of_frame_partition(self):
        a, b = ProcessClock(math.pi, -.5), ProcessClock(math.pi, -.5)
        for _ in range(300):
            a.advance(1 / 30)
        b.advance(10)
        self.assertAlmostEqual(a.value, b.value)

    def test_bound_time_survives_unobserved_intervals_and_pause_boundaries(self):
        now = [10.0]
        c = ProcessClock(2, time_source=lambda: now[0])
        now[0] = 11
        self.assertEqual(c.value, 2)
        now[0] = 12
        c.pause()
        now[0] = 20
        c.resume()
        now[0] = 21
        self.assertEqual(c.value, 6)
        self.assertEqual(c.value, 6)
        with self.assertRaises(ValueError):
            c.advance(1)
        now[0] = 19
        with self.assertRaises(ValueError):
            _ = c.value

    def test_pause_keeps_phase_without_catching_up(self):
        c = ProcessClock(2, 3)
        c.advance(1)
        c.pause()
        c.pause()
        c.advance(100)
        self.assertEqual(c.value, 5)
        c.resume()
        c.resume()
        c.advance(.25)
        self.assertEqual(c.value, 5.5)

    def test_invalid_time_cannot_corrupt_phase(self):
        c = ProcessClock()
        for x in [-1, float('nan'), float('inf'), True, '1']:
            with self.assertRaises(ValueError):
                c.advance(x)
            self.assertEqual(c.value, 0)
        for x in [-1, float('nan'), float('inf'), True]:
            with self.assertRaises(ValueError):
                ProcessClock(x)
        with self.assertRaises(ValueError):
            ProcessClock(initial=float('nan'))

    def test_overflow_is_rejected_atomically_and_zero_rate_is_stable(self):
        c = ProcessClock(1e308, 1e308)
        with self.assertRaises(ValueError):
            c.advance(2)
        self.assertEqual(c.value, 1e308)
        c = ProcessClock(0, 7)
        self.assertEqual(c.advance(100), 7)
