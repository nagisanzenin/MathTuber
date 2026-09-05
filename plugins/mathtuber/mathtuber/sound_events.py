"""Sparse original action sounds. Event times refer to measured speech cues."""
import math
import wave
from array import array
from .state import ProductionError

TIMBRES = {"tap": (330, .10), "settle": (660, .28), "reveal": (880, .38)}

def resolve_events(plan, timing, duration):
    if not isinstance(plan, list):
        raise ProductionError("SOUND_EVENTS", "Sound events must be a list")
    result = []
    for event in plan:
        try:
            kind = event["kind"]
            frequency, length = TIMBRES[kind]
            at = float(timing[event["scene"]][event["cue"]]) + float(event.get("offset", 0))
            gain = float(event.get("amplitude", .04))
            if not (math.isfinite(at) and 0 <= at and at + length <= duration and math.isfinite(gain) and 0 < gain <= .08):
                raise ValueError("Out-of-range time or amplitude")
        except (KeyError, TypeError, ValueError) as exc:
            raise ProductionError("SOUND_EVENTS", f"Invalid sound event: {exc}") from exc
        result.append({"time": at, "kind": kind, "frequency": frequency, "duration": length, "amplitude": gain})
    return result

def write_score(path, events, duration, rate=24000):
    samples = array("d", [0]) * math.ceil(duration * rate)
    for event in events:
        start = round(event["time"] * rate)
        for i in range(round(event["duration"] * rate)):
            t = i / rate
            envelope = min(t / .004, 1) * math.exp(-t / (event["duration"] / 5))
            value = event["amplitude"] * envelope * (math.sin(math.tau * event["frequency"] * t) + .15 * math.sin(math.tau * event["frequency"] * 2.76 * t))
            if start + i < len(samples):
                samples[start + i] += value
    if max(map(abs, samples), default=0) >= 1:
        raise ProductionError("SOUND_EVENTS", "Overlapping sounds would clip")
    pcm = array("h", (round(s * 32767) for s in samples))
    import sys
    if sys.byteorder != "little": pcm.byteswap()
    with wave.open(str(path), "wb") as output:
        output.setparams((1, 2, rate, 0, "NONE", "not compressed"))
        output.writeframes(pcm.tobytes())
