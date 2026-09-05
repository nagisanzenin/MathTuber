"""Geometry for authored focal staging; not a predictor of viewer attention."""
import math


def fit_scale(width, height, box_width, box_height):
    """Uniform scale to contain a nonempty object in a positive-sized rectangle.

    A vertical or horizontal line is valid. A point has no meaningful fit scale.
    The caller owns context, placement, typography and updater synchronization.
    """
    values = (width, height, box_width, box_height)
    if any(isinstance(v, bool) or not isinstance(v, (int, float)) or not math.isfinite(v) for v in values):
        raise ValueError("Framing dimensions must be finite numbers")
    if width < 0 or height < 0 or box_width <= 0 or box_height <= 0 or width == height == 0:
        raise ValueError("Framing requires a nonempty object and a positive box")
    return min(b / size for size, b in ((width, box_width), (height, box_height)) if size > 0)
