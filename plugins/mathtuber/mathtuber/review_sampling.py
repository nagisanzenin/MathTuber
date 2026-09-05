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
