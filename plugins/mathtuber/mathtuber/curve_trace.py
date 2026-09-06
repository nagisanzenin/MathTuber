"""Cached parameter-space polyline traces; no assumption of constant path speed."""
import bisect
import math

class CurveTrace:
    def __init__(self, point_at, start=0.0, end=1.0, samples=601):
        if isinstance(samples, bool) or not isinstance(samples, int) or samples < 2:
            raise ValueError('A trace needs at least two samples')
        if not math.isfinite(start) or not math.isfinite(end) or end <= start:
            raise ValueError('Trace bounds must be finite and increasing')
        self.parameters = [start+(end-start)*i/(samples-1) for i in range(samples)]
        self.points = [tuple(float(v) for v in point_at(t)) for t in self.parameters]
        if any(len(p) != 3 or not all(math.isfinite(v) for v in p) for p in self.points):
            raise ValueError('Trace points must have three finite coordinates')

    def through(self, parameter):
        """Return cached vertices plus an interpolated endpoint, allowing rewinds.

        Sampling is uniform in the supplied parameter, not arc length. A zero
        extent returns a degenerate two-point line for rendering compatibility.
        """
        if not math.isfinite(parameter) or not self.parameters[0] <= parameter <= self.parameters[-1]:
            raise ValueError('Trace parameter is outside its sampled bounds')
        i = bisect.bisect_right(self.parameters, parameter)-1
        points = list(self.points[:i+1])
        if parameter > self.parameters[i] and i+1 < len(self.points):
            weight=(parameter-self.parameters[i])/(self.parameters[i+1]-self.parameters[i])
            points.append(tuple(a+(b-a)*weight for a,b in zip(self.points[i],self.points[i+1])))
        return points if len(points)>1 else points*2
