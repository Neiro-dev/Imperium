"""Measuring a skeleton's relations on a laid-out city's cells (research R-6)."""

from __future__ import annotations

import math
from collections import deque

from .report import Rect

Cell = tuple[int, int]
NEIGHBOURS = ((1, 0), (-1, 0), (0, 1), (0, -1))


def cells_of(rects: list[Rect]) -> set[Cell]:
    cells: set[Cell] = set()
    for x1, z1, x2, z2 in rects:
        for x in range(x1, x2 + 1):
            for z in range(z1, z2 + 1):
                cells.add((x, z))
    return cells


def _inside_map(cell: Cell, size: tuple[int, int]) -> bool:
    return 0 <= cell[0] < size[0] and 0 <= cell[1] < size[1]


def _reachable(starts: set[Cell], blocked: set[Cell], size: tuple[int, int]) -> set[Cell]:
    seen = {c for c in starts if c not in blocked and _inside_map(c, size)}
    queue = deque(sorted(seen))
    while queue:
        x, z = queue.popleft()
        for dx, dz in NEIGHBOURS:
            nxt = (x + dx, z + dz)
            if nxt not in seen and nxt not in blocked and _inside_map(nxt, size):
                seen.add(nxt)
                queue.append(nxt)
    return seen


def _edge_cells(size: tuple[int, int]) -> set[Cell]:
    w, h = size
    edge = {(x, 0) for x in range(w)} | {(x, h - 1) for x in range(w)}
    edge |= {(0, z) for z in range(h)} | {(w - 1, z) for z in range(h)}
    return edge


def inside(a: set[Cell], b: set[Cell], size: tuple[int, int]) -> bool:
    """Every cell of a is a cell of b or enclosed by b: no path leads from it to the map's edge without crossing b."""
    rest = a - b
    if not rest:
        return True
    outside = _reachable(_edge_cells(size), b, size)
    return not (rest & outside)


def adjoins(a: set[Cell], b: set[Cell]) -> bool:
    if a & b:
        return True
    return any((x + dx, z + dz) in b for x, z in a for dx, dz in NEIGHBOURS)


def same_side(a: set[Cell], b: set[Cell], feature: set[Cell], size: tuple[int, int]) -> bool:
    """A path of neighbouring cells outside the feature joins a and b."""
    starts = a - feature
    targets = b - feature
    if not starts or not targets:
        return False
    return bool(_reachable(starts, feature, size) & targets)


def _steps_from_edge(river: set[Cell], flows_from: str, size: tuple[int, int]) -> dict[Cell, int]:
    w, h = size
    if flows_from == "North":
        starts = {c for c in river if c[1] == h - 1}
    elif flows_from == "South":
        starts = {c for c in river if c[1] == 0}
    elif flows_from == "East":
        starts = {c for c in river if c[0] == w - 1}
    else:
        starts = {c for c in river if c[0] == 0}
    steps = {c: 0 for c in starts}
    queue = deque(sorted(starts))
    while queue:
        x, z = queue.popleft()
        for dx, dz in NEIGHBOURS:
            nxt = (x + dx, z + dz)
            if nxt in river and nxt not in steps:
                steps[nxt] = steps[(x, z)] + 1
                queue.append(nxt)
    return steps


def _nearest(cells: set[Cell], targets: set[Cell]) -> tuple[float, Cell | None]:
    """The target cell nearest any cell of `cells`, by distance between cell centres; ties go to the lowest cell."""
    best: tuple[float, Cell | None] = (math.inf, None)
    if not cells or not targets:
        return best
    buckets: dict[Cell, list[Cell]] = {}
    span = 16
    for t in targets:
        buckets.setdefault((t[0] // span, t[1] // span), []).append(t)
    keys = list(buckets)
    outline = {c for c in cells if any((c[0] + dx, c[1] + dz) not in cells for dx, dz in NEIGHBOURS)}
    for c in sorted(outline):
        bx, bz = c[0] // span, c[1] // span
        last_ring = max(max(abs(k[0] - bx), abs(k[1] - bz)) for k in keys)
        ring = 0
        while ring <= last_ring:
            for ix in range(bx - ring, bx + ring + 1):
                for iz in range(bz - ring, bz + ring + 1):
                    if max(abs(ix - bx), abs(iz - bz)) != ring:
                        continue
                    for t in buckets.get((ix, iz), ()):
                        candidate = (math.dist(c, t), t)
                        if best[1] is None or candidate < best:
                            best = candidate
            # Every target in a farther ring lies at least ring * span cells away.
            if best[0] <= ring * span:
                break
            ring += 1
    return best


def distance(a: set[Cell], b: set[Cell]) -> float:
    if a & b:
        return 0.0
    return _nearest(a, b)[0]


def upstream(a: set[Cell], b: set[Cell], river: set[Cell], flows_from: str | None, size: tuple[int, int]) -> bool | None:
    if flows_from is None:
        return None
    steps = _steps_from_edge(river, flows_from, size)
    if not steps:
        return None
    reached = set(steps)
    _, near_a = _nearest(a, reached)
    _, near_b = _nearest(b, reached)
    if near_a is None or near_b is None:
        return None
    return steps[near_a] < steps[near_b]


def farther(a: set[Cell], b: set[Cell], than: set[Cell]) -> bool:
    return distance(a, b) > distance(than, b)
