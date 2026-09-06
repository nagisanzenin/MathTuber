import unittest
from mathtuber.curve_trace import CurveTrace

class TraceTests(unittest.TestCase):
    def test_linear_endpoint_rewind_and_cached_evaluation(self):
        calls=[]
        def f(t):
            calls.append(t)
            return (2*t,3-t,0)
        trace=CurveTrace(f,0,2,5)
        self.assertEqual(trace.through(1.3)[-1],(2.6,1.7,0))
        self.assertEqual(trace.through(.25)[-1],(.5,2.75,0))
        self.assertEqual(trace.through(2)[-1],(4,1,0))
        self.assertEqual(len(calls),5)
        self.assertEqual(len(trace.through(0)),2)
    def test_no_arc_length_claim(self):
        trace=CurveTrace(lambda t:(t*t,0,0),0,1,5)
        self.assertEqual(trace.through(.5)[-1],(.25,0,0))
    def test_reject_invalid_geometry_and_range(self):
        with self.assertRaises(ValueError):CurveTrace(lambda t:(t,float('nan'),0))
        with self.assertRaises(ValueError):CurveTrace(lambda t:(t,0))
        with self.assertRaises(ValueError):CurveTrace(lambda t:(t,0,0),samples=True)
        trace=CurveTrace(lambda t:(t,0,0))
        for x in [-.1,1.1,float('nan')]:
            with self.assertRaises(ValueError):trace.through(x)
