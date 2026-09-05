import sys
from pathlib import Path
import unittest
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'plugins/mathtuber'))
from mathtuber.framing import fit_scale


class FramingTests(unittest.TestCase):
    def test_fit_preserves_aspect_and_both_bounds(self):
        for w,h,bw,bh in [(12,3,6,7),(2,9,6,7),(0,8,6,7),(8,0,6,7),(.2,.1,6,7)]:
            s=fit_scale(w,h,bw,bh)
            self.assertLessEqual(w*s,bw+1e-10)
            self.assertLessEqual(h*s,bh+1e-10)
            self.assertTrue(abs(w*s-bw)<1e-10 or abs(h*s-bh)<1e-10)

    def test_invalid_extents_fail(self):
        for dimensions in [(0,0,6,7),(-1,2,6,7),(1,2,0,7),(1,2,6,-1),(float('nan'),2,6,7),(1,2,float('inf'),7),(True,2,6,7)]:
            with self.assertRaises(ValueError):
                fit_scale(*dimensions)


if __name__ == '__main__':
    unittest.main()
