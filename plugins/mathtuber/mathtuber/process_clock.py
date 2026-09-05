"""A process phase independent of the duration of individual scene animations."""
import math


def _finite(value, name, nonnegative=False):
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError(f"{name} must be a finite number")
    if not math.isfinite(value) or (nonnegative and value < 0):
        raise ValueError(f"{name} must be finite" + (" and nonnegative" if nonnegative else ""))
    return float(value)


class ProcessClock:
    """Accumulate phase at a fixed rate; explicit inspection pauses retain phase.

    Units belong to the author (seconds, radians, distance). This is presentation
    time, not a numerical physics integrator. Paused wall time is never caught up.
    """
    def __init__(self, rate=1.0, initial=0.0, time_source=None):
        self._rate = _finite(rate, "rate", True)
        self._value = _finite(initial, "initial")
        self._paused = False
        self._time_source = time_source
        self._last_time = _finite(time_source(), "time", True) if time_source else None

    @property
    def value(self):
        self._sync()
        return self._value

    @property
    def rate(self):
        return self._rate

    @property
    def paused(self):
        return self._paused

    def _sync(self):
        if self._time_source is not None:
            now = _finite(self._time_source(), "time", True)
            dt = now - self._last_time
            self._advance(dt)
            self._last_time = now

    def advance(self, dt):
        if self._time_source is not None:
            raise ValueError("bound clocks read their time source; do not advance manually")
        return self._advance(dt)

    def _advance(self, dt):
        dt = _finite(dt, "dt", True)
        if not self._paused:
            candidate = self._value + self._rate * dt
            if not math.isfinite(candidate):
                raise ValueError("process phase overflow")
            self._value = candidate
        return self._value

    def pause(self):
        self._sync()
        self._paused = True

    def resume(self):
        self._sync()
        self._paused = False
