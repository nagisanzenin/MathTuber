"""Reproduce the films' finite checks with Python's standard library.

Run without -O. These assertions supplement the arguments and scope limits in
each project's math-verification.json; enumeration is not a general proof.
"""
from fractions import Fraction
from itertools import product
from math import isclose, log10


pairs = {(n % 3, n % 5): n for n in range(15)}
assert len(pairs) == 15 and pairs[2, 3] == 8
for start in range(-45, 46):
    assert sum((n % 3, n % 5) == (2, 3) for n in range(start, start + 15)) == 1
for a, b in product(range(-60, 61), repeat=2):
    assert ((a % 3, a % 5) == (b % 3, b % 5)) == ((a - b) % 15 == 0)
print('Remainders: PASS')


def differences(row):
    return [right - left for left, right in zip(row, row[1:])]


row = [2, 2, 2, 8, 8, 8, 2, 2]
shifted = [2, 2, 2, 2, 8, 8, 8, 2]
assert differences(row) == [0, 0, 6, 0, 0, -6, 0]
assert differences(shifted) == [0, 0, 0, 6, 0, 0, -6]
assert differences([value + 1 for value in shifted]) == differences(shifted)
print('Signed image filter: PASS')

assert [10 * log10(power) for power in [1, 10, 100, 1000]] == [0, 10, 20, 30]
assert isclose(10 * log10(2) + 10 * log10(5), 10, abs_tol=1e-12)
assert 10 * log10(.1) == -10
print('Power levels relative to 1 mW: PASS')

fixed = Fraction(2, 3)


def update(probability):
    return Fraction(3, 4) * probability + Fraction(1, 2) * (1 - probability)


assert fixed / 4 == (1 - fixed) / 2 == Fraction(1, 6)
assert update(fixed) == fixed
assert update(Fraction(1)) == Fraction(3, 4)
assert update(Fraction(3, 4)) == Fraction(11, 16)
for numerator in range(101):
    p = Fraction(numerator, 100)
    assert update(p) - fixed == (p - fixed) / 4
print('Two-state probability chain: PASS')

edges = [('S', 'A'), ('S', 'B'), ('A', 'T'), ('A', 'B'), ('B', 'T')]
for middle, optimum, route in [(1, 6, [3, 3, 2, 1, 4]), (2, 7, [4, 3, 2, 2, 5])]:
    capacities = [4, 3, 2, middle, 5]
    assert all(0 <= flow <= capacity for flow, capacity in zip(route, capacities))
    assert route[0] == route[2] + route[3] and route[1] + route[3] == route[4]
    feasible = [f[0] + f[1] for f in product(*[range(c + 1) for c in capacities])
                if f[0] == f[2] + f[3] and f[1] + f[3] == f[4]]
    cuts = []
    for interior in [set(), {'A'}, {'B'}, {'A', 'B'}]:
        source_side = {'S'} | interior
        cuts.append(sum(c for (u, v), c in zip(edges, capacities)
                        if u in source_side and v not in source_side))
    assert max(feasible) == min(cuts) == optimum == sum(route[:2])
print('Attained network cut bounds: PASS')
