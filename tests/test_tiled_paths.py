import itertools
import math
import unittest
from collections import Counter
from mathtuber.tiled_paths import tile_arcs, connected_paths


class TilePathTests(unittest.TestCase):
    def test_every_three_by_three_field_partitions_without_dead_ends(self):
        # Exhaust all 512 fields, not just the film's attractive random seed.
        for values in itertools.product((0, 1), repeat=9):
            rows = [values[i:i+3] for i in range(0, 9, 3)]
            paths = connected_paths(rows)
            arcs = [a for p in paths for a in p.arcs]
            expected = [a for r in range(3) for c in range(3) for a in tile_arcs(c, r, rows[r][c])]
            canonical = lambda a: tuple(sorted((a.start, a.end)))
            self.assertEqual(Counter(map(canonical, arcs)), Counter(map(canonical, expected)))
            degree = Counter(n for a in arcs for n in (a.start, a.end))
            for node, count in degree.items():
                self.assertEqual(count, 1 if 0 in node or 6 in node else 2)
            for p in paths:
                for a, b in zip(p.arcs, p.arcs[1:]):
                    self.assertEqual(a.end, b.start)
                    self.assertEqual(a.point(1), b.point(0))
                    # Consistent directed tangents across every tile join.
                    u = [x-y for x,y in zip(a.point(1), a.point(1-1e-6))]
                    v = [x-y for x,y in zip(b.point(1e-6), b.point(0))]
                    cosine = sum(x*y for x,y in zip(u,v))/math.sqrt(sum(x*x for x in u)*sum(x*x for x in v))
                    self.assertGreater(cosine, .999999)
                if not p.closed:
                    for node in (p.arcs[0].start, p.arcs[-1].end):
                        self.assertTrue(0 in node or 6 in node)

    def test_single_tile_endpoints_and_equal_arc_distance(self):
        for orientation in (0, 1):
            arcs = tile_arcs(0, 0, orientation)
            self.assertEqual({n for a in arcs for n in (a.start, a.end)}, {(1,2),(2,1),(1,0),(0,1)})
            for a in arcs:
                distances=[]
                for i in range(100):
                    p,q=a.point(i/100),a.point((i+1)/100)
                    self.assertAlmostEqual(math.dist(p, (*a.center,0)), .5)
                    distances.append(math.dist(p,q))
                self.assertLess(max(distances)-min(distances),1e-14)
        for p in connected_paths([[0,1],[1,0]]):
            self.assertEqual(p.point(0),p.arcs[0].point(0))
            self.assertEqual(p.point(1),p.arcs[-1].point(1))
        self.assertTrue(any(p.closed for p in connected_paths([[0,1],[1,0]])))

    def test_invalid_fields_and_parameters(self):
        for rows in ([],[[]],[[0],[0,1]],[[2]],[[True]],[[.0]]):
            with self.assertRaises(ValueError): connected_paths(rows)
        p=connected_paths([[0]])[0]
        for t in (-.1,1.1,float('nan')):
            with self.assertRaises(ValueError):p.point(t)
            with self.assertRaises(ValueError):p.arcs[0].point(t)
