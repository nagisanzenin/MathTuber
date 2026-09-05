"""Resolve agent-authored review intervals. Sampling is not a review verdict."""
import math

def interval_samples(plan, cues, duration):
    if not math.isfinite(duration) or duration <= 0:
        raise ValueError("Invalid media duration")
    result = []
    seen = set()
    intervals = plan.get("intervals", [])
    if not intervals:
        raise ValueError("At least one review interval is required")
    for item in intervals:
        key = item.get("id")
        if not isinstance(key, str) or not key or key in seen:
            raise ValueError("Review interval IDs must be unique nonempty strings")
        seen.add(key)
        if not isinstance(item.get("purpose"), str) or not item["purpose"].strip():
            raise ValueError("An interval must state its review purpose")
        try:
            start = float(cues[item["start_cue"]]) + float(item.get("start_offset", 0))
            end = float(cues[item["end_cue"]]) + float(item.get("end_offset", 0))
        except (KeyError, TypeError, ValueError) as exc:
            raise ValueError("Unknown cue or invalid offset") from exc
        n = item.get("samples", 9)
        if type(n) is not int or not 3 <= n <= 121:
            raise ValueError("An interval requires 3 to 121 samples")
        if not (math.isfinite(start) and math.isfinite(end) and 0 <= start < end < duration):
            raise ValueError("Review interval must lie wholly within the media")
        result.append({"id": key, "purpose": item["purpose"],
                       "times": [start + (end-start)*i/(n-1) for i in range(n)]})
    return result


def ending_samples(duration, seconds=15, samples=9, fps=30):
    """Sample the ending through its last decodable frame, including short films.

    This is evidence coverage, never an automatic judgment of pacing or quality.
    """
    for name, value in (("duration", duration), ("seconds", seconds), ("fps", fps)):
        if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value) or value <= 0:
            raise ValueError(f"{name} must be a finite positive number")
    if type(samples) is not int or not 3 <= samples <= 121:
        raise ValueError("An ending requires 3 to 121 samples")
    end = max(0.0, duration - 1 / fps)
    start = max(0.0, duration - seconds)
    start = min(start, end)
    return [start + (end - start) * i / (samples - 1) for i in range(samples)]
