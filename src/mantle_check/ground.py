"""The ground of a picture in perspective laid onto the cells: a projective mapping fitted to the reading's ground
pairs, each pair's error in cells, and the mapping both ways (spec FR-052; research R-20).

Points of one flat ground seen through one camera are related by a projective mapping, which four points fix; more
points are fitted by least squares. Only Python's own library is used (research R-9)."""

from __future__ import annotations

import math
from dataclasses import dataclass

Point = tuple[float, float]
Matrix = list[list[float]]


def solve(a: Matrix, b: list[float]) -> list[float]:
    """Solves a x = b by Gaussian elimination with partial pivoting."""
    n = len(b)
    m = [row[:] + [b[i]] for i, row in enumerate(a)]
    for col in range(n):
        pivot = max(range(col, n), key=lambda r: abs(m[r][col]))
        if abs(m[pivot][col]) < 1e-12:
            raise ValueError("the ground pairs do not fix a mapping: three of them may lie on one line")
        m[col], m[pivot] = m[pivot], m[col]
        for r in range(col + 1, n):
            factor = m[r][col] / m[col][col]
            for c in range(col, n + 1):
                m[r][c] -= factor * m[col][c]
    x = [0.0] * n
    for r in range(n - 1, -1, -1):
        x[r] = (m[r][n] - sum(m[r][c] * x[c] for c in range(r + 1, n))) / m[r][r]
    return x


def normalising(points: list[Point]) -> Matrix:
    """The similarity that moves points to their centroid and scales them to a mean distance of √2 (Hartley)."""
    cx = sum(p[0] for p in points) / len(points)
    cy = sum(p[1] for p in points) / len(points)
    mean = sum(math.hypot(p[0] - cx, p[1] - cy) for p in points) / len(points) or 1.0
    s = math.sqrt(2) / mean
    return [[s, 0, -s * cx], [0, s, -s * cy], [0, 0, 1]]


def multiply(a: Matrix, b: Matrix) -> Matrix:
    return [[sum(a[i][k] * b[k][j] for k in range(3)) for j in range(3)] for i in range(3)]


def invert(m: Matrix) -> Matrix:
    (a, b, c), (d, e, f), (g, h, i) = m
    det = a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)
    if abs(det) < 1e-15:
        raise ValueError("the mapping cannot be inverted")
    return [
        [(e * i - f * h) / det, (c * h - b * i) / det, (b * f - c * e) / det],
        [(f * g - d * i) / det, (a * i - c * g) / det, (c * d - a * f) / det],
        [(d * h - e * g) / det, (b * g - a * h) / det, (a * e - b * d) / det],
    ]


def apply(m: Matrix, point: Point) -> Point:
    x, y = point
    w = m[2][0] * x + m[2][1] * y + m[2][2]
    return ((m[0][0] * x + m[0][1] * y + m[0][2]) / w, (m[1][0] * x + m[1][1] * y + m[1][2]) / w)


def fit(sources: list[Point], targets: list[Point]) -> Matrix:
    """The projective mapping that takes each source point to its target, by least squares over four or more."""
    if len(sources) < 4:
        raise ValueError("a perspective fit needs four ground pairs or more")
    ns, nt = normalising(sources), normalising(targets)
    s = [apply(ns, p) for p in sources]
    t = [apply(nt, p) for p in targets]
    rows, values = [], []
    for (x, y), (u, v) in zip(s, t):
        rows.append([x, y, 1, 0, 0, 0, -u * x, -u * y])
        values.append(u)
        rows.append([0, 0, 0, x, y, 1, -v * x, -v * y])
        values.append(v)
    normal = [[sum(r[i] * r[j] for r in rows) for j in range(8)] for i in range(8)]
    right = [sum(r[i] * value for r, value in zip(rows, values)) for i in range(8)]
    h = solve(normal, right)
    fitted = [[h[0], h[1], h[2]], [h[3], h[4], h[5]], [h[6], h[7], 1.0]]
    return multiply(invert(nt), multiply(fitted, ns))


@dataclass
class Ground:
    """A reading's ground: pixel to cell, cell to pixel, and each pair's error in cells."""

    to_cell: Matrix
    to_pixel: Matrix
    errors: list[float]

    def cell(self, pixel: Point) -> Point:
        return apply(self.to_cell, pixel)

    def pixel(self, cell: Point) -> Point:
        return apply(self.to_pixel, cell)


def ground(pairs: list[tuple[Point, Point]]) -> Ground:
    pixels = [p for p, _ in pairs]
    cells = [c for _, c in pairs]
    to_cell = fit(pixels, cells)
    to_pixel = invert(to_cell)
    errors = [math.dist(apply(to_cell, p), c) for p, c in pairs]
    return Ground(to_cell, to_pixel, errors)
