"""Exact midpoint topology and quarter-circle geometry for square Truchet tiles.

Rows run bottom to top. A finite rectangular field has closed loops and/or
boundary-to-boundary paths, never interior dead ends. No random generator or
rendering dependency: the host agent supplies the tile choices and composition.
"""
from dataclasses import dataclass
from math import atan2, cos, sin, pi, isfinite


@dataclass(frozen=True)
class TileArc:
    start: tuple[int, int]  # doubled coordinates, avoiding float graph keys
    end: tuple[int, int]
    center: tuple[float, float]

    def reversed(self):
        return TileArc(self.end, self.start, self.center)

    def point(self, fraction):
        if not isfinite(fraction) or not 0 <= fraction <= 1:
            raise ValueError('Arc fraction must be finite and in [0, 1]')
        # Return exact joins, not the roundoff of sin(pi).
        if fraction in (0, 1):
            node = self.start if fraction == 0 else self.end
            return (node[0] / 2, node[1] / 2, 0.0)
        x, y = self.center
        a = atan2(self.start[1] / 2 - y, self.start[0] / 2 - x)
        b = atan2(self.end[1] / 2 - y, self.end[0] / 2 - x)
        delta = (b - a + pi) % (2 * pi) - pi
        return (x + .5 * cos(a + fraction * delta),
                y + .5 * sin(a + fraction * delta), 0.0)


@dataclass(frozen=True)
class TilePath:
    arcs: tuple[TileArc, ...]

    @property
    def closed(self):
        return self.arcs[0].start == self.arcs[-1].end

    def point(self, fraction):
        """Constant arc-distance parameter: all component arcs have equal length."""
        if not isfinite(fraction) or not 0 <= fraction <= 1:
            raise ValueError('Path fraction must be finite and in [0, 1]')
        position = fraction * len(self.arcs)
        index = min(int(position), len(self.arcs) - 1)
        return self.arcs[index].point(position - index)


def tile_arcs(column, row, orientation):
    if any(type(v) is not int for v in (column, row, orientation)) or orientation not in (0, 1):
        raise ValueError('Integer tile coordinates and orientation 0 or 1 required')
    n, e = (2 * column + 1, 2 * row + 2), (2 * column + 2, 2 * row + 1)
    s, w = (2 * column + 1, 2 * row), (2 * column, 2 * row + 1)
    if orientation == 0:
        return (TileArc(n, e, (column + 1, row + 1)),
                TileArc(s, w, (column, row)))
    return (TileArc(n, w, (column, row + 1)),
            TileArc(s, e, (column + 1, row)))


def connected_paths(rows):
    """Partition all tile arcs exactly once, returning oriented continuous paths."""
    rows = tuple(tuple(row) for row in rows)
    if not rows or not rows[0] or any(len(row) != len(rows[0]) for row in rows):
        raise ValueError('Nonempty rectangular tile field required')
    edges = [arc for r, row in enumerate(rows) for c, value in enumerate(row)
             for arc in tile_arcs(c, r, value)]
    adjacent = {}
    for i, arc in enumerate(edges):
        for node in (arc.start, arc.end):
            adjacent.setdefault(node, []).append(i)
    unused = set(range(len(edges)))
    paths = []

    def walk(node):
        ordered = []
        while True:
            available = [i for i in adjacent[node] if i in unused]
            if not available:
                break
            i = available[0]
            unused.remove(i)
            arc = edges[i] if edges[i].start == node else edges[i].reversed()
            ordered.append(arc)
            node = arc.end
        if ordered:
            paths.append(TilePath(tuple(ordered)))

    for node in sorted(adjacent):
        if len(adjacent[node]) == 1:
            walk(node)
    while unused:
        walk(edges[min(unused)].start)
    return tuple(paths)
