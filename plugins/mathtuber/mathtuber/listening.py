"""Explicit explanatory tones, confined to measured speech-free boundaries."""
import math
from .state import ProductionError


def number(value, name, low, high):
    if (isinstance(value, bool) or not isinstance(value, (int, float))
            or not math.isfinite(value) or not low <= value <= high):
        raise ValueError(f"{name} must be finite in [{low}, {high}]")
    return value


def resolve_windows(plan, pauses, duration):
    """Pause indices are zero based; times in pauses are already scene-offset."""
    try:
        number(duration, "duration", .001, 86400)
        if not isinstance(plan, list):
            raise ValueError("Listening windows must be a list")
        result, ids = [], set()
        for item in plan:
            identity = item["id"]
            if not isinstance(identity, str) or not identity.strip() or identity in ids:
                raise ValueError("Window ids must be unique nonempty strings")
            ids.add(identity)
            meaning = item["meaning"]
            if not isinstance(meaning, str) or not meaning.strip():
                raise ValueError("A window needs an explanatory meaning")
            index = item["paragraph_pause"]
            if isinstance(index, bool) or not isinstance(index, int) or index < 0:
                raise ValueError("paragraph_pause must be a nonnegative integer")
            gap = pauses[item["scene"]][index]
            left = number(gap["start"], "pause start", 0, duration)
            right = number(gap["end"], "pause end", left, duration)
            offset = number(item.get("offset", .15), "offset", 0, duration)
            length = number(item["duration"], "window duration", .05, 10)
            start = left + offset
            if start + length > right + 1e-9:
                raise ValueError("Listening window extends beyond measured speech pause")
            fade = number(item.get("fade_seconds", .05), "fade", .005, length / 2)
            tones = item["tones"]
            if not isinstance(tones, list) or not 1 <= len(tones) <= 16:
                raise ValueError("Specify one to sixteen tones")
            tones = [{"frequency_hz": number(t["frequency_hz"], "frequency", 30, 8000),
                      "amplitude": number(t["amplitude"], "amplitude", .0001, .2)} for t in tones]
            if sum(t["amplitude"] for t in tones) > .4:
                raise ValueError("Sum of tone amplitudes exceeds .4")
            result.append(dict(id=identity, meaning=meaning, time=start, duration=length,
                               fade_seconds=fade, tones=tones))
        result.sort(key=lambda w: w["time"])
        for previous, current in zip(result, result[1:]):
            if current["time"] < previous["time"] + previous["duration"] - 1e-9:
                raise ValueError("Listening windows overlap")
        return result
    except (KeyError, TypeError, ValueError, IndexError) as exc:
        raise ProductionError("LISTENING_WINDOWS", str(exc)) from exc


def add_windows(samples, windows, rate):
    """Analytic sine tones with raised-cosine edges; no recorded instrument claim."""
    for window in windows:
        start = round(window["time"] * rate)
        count = round(window["duration"] * rate)
        fade = max(1, round(window["fade_seconds"] * rate))
        for i in range(count):
            edge = min(1, i / fade, (count - 1 - i) / fade)
            envelope = .5 - .5 * math.cos(math.pi * edge)
            sample = envelope * sum(t["amplitude"] * math.sin(math.tau * t["frequency_hz"] * i / rate)
                                    for t in window["tones"])
            if start + i >= len(samples):
                raise ProductionError("LISTENING_WINDOWS", "Quantized window exceeds score")
            samples[start + i] += sample
