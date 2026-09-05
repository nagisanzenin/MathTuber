import sys, unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"plugins/mathtuber"))
from mathtuber.review_sampling import interval_samples

class IntervalTests(unittest.TestCase):
    def plan(self, **changes):
        item=dict(id="late-mapping",start_cue="turn",end_cue="done",purpose="Check the landing",samples=3)
        item.update(changes)
        return {"intervals":[item]}
    def test_late_transition_includes_end(self):
        self.assertEqual(interval_samples(self.plan(end_offset=2),{"turn":40,"done":46},60)[0]["times"],[40,44,48])
    def test_invalid_ranges_do_not_silently_clip(self):
        for changes in [dict(start_offset=-50),dict(end_offset=20),dict(end_cue="missing"),dict(samples=True),dict(start_offset=float("nan")),dict(purpose="")]:
            with self.subTest(changes=changes), self.assertRaises(ValueError):
                interval_samples(self.plan(**changes),{"turn":40,"done":46},60)
    def test_duplicate_ids_rejected(self):
        p=self.plan();p["intervals"]*=2
        with self.assertRaises(ValueError):interval_samples(p,{"turn":40,"done":46},60)


class EndingTests(unittest.TestCase):
    def test_last_frame_and_full_ending_are_covered(self):
        from mathtuber.review_sampling import ending_samples
        times = ending_samples(60, seconds=15, samples=9, fps=30)
        self.assertEqual(times[0], 45)
        self.assertAlmostEqual(times[-1], 60 - 1/30)
        self.assertTrue(all(a < b for a, b in zip(times, times[1:])))
    def test_short_clip_never_seeks_past_media(self):
        from mathtuber.review_sampling import ending_samples
        for duration in (0.01, 1, 8):
            times = ending_samples(duration)
            self.assertEqual(times[0], 0)
            self.assertTrue(all(0 <= t < duration for t in times))
    def test_bad_inputs_rejected(self):
        from mathtuber.review_sampling import ending_samples
        for kwargs in ({"duration":0}, {"duration":float("nan")}, {"duration":True}, {"seconds":-1}, {"fps":0}, {"samples":True}, {"samples":2}):
            args = {"duration":60}; args.update(kwargs)
            with self.subTest(args=args), self.assertRaises(ValueError):
                ending_samples(**args)
