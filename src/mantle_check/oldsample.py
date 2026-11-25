"""The old project's sample of the town, set beside a reading as a comparison only: its codes sorted into the
reading's kinds, its same area as a reading's pieces for the findings and shares, and its mapping of the screenshot
(spec FR-057, SC-018; research R-27). Nothing of it is written into a reading (spec FR-053; constitution,
Principle II)."""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path

from .forms import Area, City
from .gamedata import CannotRun
from .ground import Matrix, apply, invert

# Each code of the sample's legend sorted into the reading's kinds (research R-27). Codes not listed are outside.
KINDS = {
    "M": "Road", "S": "Road", "l": "Road",
    "P": "Plaza", "m": "Plaza", "f": "Plaza",
    "B": "Bridge",
    "#": "House", "_": "House", "D": "House",
    "%": "AnnexOrAttic", ",": "AnnexOrAttic",
    "y": "Yard", "r": "YardPath",
    "w": "YardWall", "g": "YardWall",
    "o": "Garden", "q": "Garden", "c": "Garden", "T": "Tree", "t": "Tree",
    "J": "LargePiece",
    "W": "CityWall", "R": "CityWall", "U": "CityWall", "G": "CityWall", "d": "CityWall", "O": "CityWall",
    "=": "Water", "~": "Water",
    "z": "WorkshopYard", "v": "VineTrellis", "i": "Colonnade", "n": "Shrine", "p": "StockPen", "h": "Shed",
    "a": "FrontSteps", "s": "FrontSteps", "u": "Unclear",
}
GRADES = {"M": "MainStreet", "S": "SecondaryStreet", "l": "Lane"}


@dataclass
class Mapping:
    """The old project's mapping from a pixel of the screenshot to a cell of the sample: its eight coefficients take
    a pixel of its 1440×918 copy of the screenshot, which is the screenshot's pixel times `pixel_scale`."""

    to_cell: Matrix
    pixel_scale: float

    def cell(self, pixel: tuple[float, float]) -> tuple[float, float]:
        return apply(self.to_cell, (pixel[0] * self.pixel_scale, pixel[1] * self.pixel_scale))

    def pixel(self, cell: tuple[float, float]) -> tuple[float, float]:
        x, y = apply(invert(self.to_cell), cell)
        return (x / self.pixel_scale, y / self.pixel_scale)


@dataclass
class Sample:
    box: tuple[int, int, int, int]
    rows: list[str]

    def code(self, x: int, y: int) -> str:
        x0, y0 = self.box[0], self.box[1]
        if not (0 <= y - y0 < len(self.rows)) or not (0 <= x - x0 < len(self.rows[y - y0])):
            return "."
        return self.rows[y - y0][x - x0]


def load_sample(path: Path) -> Sample:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        box = tuple(int(v) for v in data["box"])
        rows = [str(r) for r in data["rows"]]
    except (OSError, ValueError, KeyError, TypeError) as error:
        raise CannotRun(f"the old sample {path} cannot be read: {error}") from error
    return Sample(box, rows)


def load_mapping(path: Path) -> Mapping:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        h = [float(v) for v in data["homography"]]
        scale = float(data["pixelScale"])
        if len(h) != 8 or scale <= 0:
            raise ValueError("eight coefficients and a positive pixelScale are needed")
    except (OSError, ValueError, KeyError, TypeError) as error:
        raise CannotRun(f"the old mapping {path} cannot be read: {error}") from error
    return Mapping([[h[0], h[1], h[2]], [h[3], h[4], h[5]], [h[6], h[7], 1.0]], scale)


def parse_area(value: str | None, sample: Sample) -> tuple[int, int, int, int]:
    if value is None:
        return (sample.box[0], sample.box[1], sample.box[0] + len(sample.rows[0]) - 1, sample.box[1] + len(sample.rows) - 1)
    try:
        x0, y0, x1, y1 = (int(v) for v in value.split(","))
    except ValueError as error:
        raise CannotRun(f"--old-area {value} is not x0,y0,x1,y1") from error
    if x0 > x1 or y0 > y1:
        raise CannotRun(f"--old-area {value} has a minimum past its maximum")
    return (x0, y0, x1, y1)


def kind_cells(sample: Sample, area: tuple[int, int, int, int]) -> dict[str, set[tuple[int, int]]]:
    """The area's cells by kind, in the reading's orientation: x east from the area's west edge, z north from its south
    edge (the sample counts y from the north)."""
    x0, y0, x1, y1 = area
    found: dict[str, set[tuple[int, int]]] = {}
    for y in range(y0, y1 + 1):
        for x in range(x0, x1 + 1):
            kind = KINDS.get(sample.code(x, y))
            if kind is not None:
                found.setdefault(kind, set()).add((x - x0, y1 - y))
    return found


def components(cells: set[tuple[int, int]]) -> list[set[tuple[int, int]]]:
    from .roads import components as split

    return split(cells)


def as_city(sample: Sample, area: tuple[int, int, int, int], file: str) -> City:
    """The old sample's same area as a reading's pieces, one piece for each joined run of cells of a kind, so that
    the same findings and shares can be counted for it (research R-27). Roads carry no line and no destination."""
    x0, y0, x1, y1 = area
    parts = []
    for kind, cells in sorted(kind_cells(sample, area).items()):
        for index, piece in enumerate(sorted(components(cells), key=lambda c: min(c)), start=1):
            rects = [(x, z, x, z) for x, z in sorted(piece)]
            parts.append(Area(f"{kind}{index}", rects, kind=kind))
    return City(file=file, is_reading=True, template=None, kit=None, reference=None,
                size=(x1 - x0 + 1, y1 - y0 + 1), terrain=[], roofs=[], things=[], parts=parts, features=[])
