"""Roads and households of a reading from a picture: their cells, the places to look again, the road ends by class,
the plots' sizes and the shares of the land (spec FR-053 to FR-055, SC-019; research R-21, R-24).

Nothing here is a problem: every case found is a finding, a place to look again beside the pictures, and none passes
or fails a reading (spec SC-017, SC-019)."""

from __future__ import annotations

import math
from collections import Counter, defaultdict
from dataclasses import dataclass, field

from .forms import PLOT_CONTENTS, Area, City, Kit
from .report import Problem, Rect

Cell = tuple[int, int]

ROAD_LIKE = ("Road", "Gate", "Bridge")
NETWORK = ("Road", "Gate", "Bridge", "Plaza")
BUILDING = ("House", "AnnexOrAttic", "LargePiece")
YARDS = ("Yard", "YardPath")
FRONTAGE = ("Road", "Plaza", "Yard", "YardPath", "Porch", "Gate", "Bridge")
WALLS = ("CityWall", "YardWall", "LowWall", "Railing", "Fence")
END_CLASSES = ("through", "way in", "at a plaza", "into a yard", "dead end", "dangling")
# The shares of FR-053, each cell counted once in this order (research R-21).
SHARE_ORDER = (
    ("water", ("Water", "Bank")),
    ("walls", WALLS),
    ("houses", BUILDING),
    ("yards and yard paths", YARDS),
    ("rest of the plots", ("Plot",) + PLOT_CONTENTS),
    ("roads and plazas", ("Road", "Plaza", "Gate", "Bridge", "Porch")),
    ("gardens and trees", ("Tree",)),
    ("unclear", ("Unclear", "Ruin", "RouteLine")),
)
ROAD_KIND = "road"
HOUSEHOLD_KIND = "household"


@dataclass
class Findings:
    findings: list[Problem] = field(default_factory=list)
    ends: Counter = field(default_factory=Counter)
    plot_sizes: list[str] = field(default_factory=list)
    shares: list[tuple[str, float]] = field(default_factory=list)
    road_cells: dict[str, set[Cell]] = field(default_factory=dict)


def area_cells(area: Area, size: tuple[int, int]) -> set[Cell]:
    w, h = size
    cells = set()
    for x1, z1, x2, z2 in area.rects:
        for x in range(max(0, x1), min(w - 1, x2) + 1):
            for z in range(max(0, z1), min(h - 1, z2) + 1):
                cells.add((x, z))
    return cells


def road_width(road: Area, kit: Kit | None) -> int:
    if road.width is not None:
        return road.width
    if kit is not None and kit.roads is not None and road.grade in kit.roads.grades:
        widths = kit.roads.grades[road.grade]
        if widths:
            return widths[0]
    return 1


def band(points: list[Cell], width: int, size: tuple[int, int]) -> set[Cell]:
    """The cells of a road laid from its centre line and its width. A point of the line names the cell whose lower
    left corner it is, and the road is centred on the cells the line runs through; an odd width is centred, an even
    one takes its extra cell to the east or north (research R-21). A cell belongs to the road where its centre lies
    within the road's half width of a segment, measured square to it."""
    w, h = size
    cells = set()
    half = width / 2
    for (x0, z0), (x1, z1) in zip(points, points[1:]):
        dx, dz = x1 - x0, z1 - z0
        length = math.hypot(dx, dz)
        if length == 0:
            continue
        ux, uz = dx / length, dz / length
        # The normal pointing north, or east for a north-south segment.
        nx, nz = -uz, ux
        if nz < 0 or (nz == 0 and nx < 0):
            nx, nz = -nx, -nz
        reach = int(math.ceil(half)) + 1
        for x in range(min(x0, x1) - reach, max(x0, x1) + reach + 1):
            for z in range(min(z0, z1) - reach, max(z0, z1) + reach + 1):
                if not (0 <= x < w and 0 <= z < h):
                    continue
                px, pz = x - x0, z - z0
                along = px * ux + pz * uz
                if along < -0.5 or along > length + 0.5:
                    continue
                across = px * nx + pz * nz
                if width % 2 == 1:
                    inside = abs(across) <= half - 0.5 + 1e-9
                else:
                    inside = -half + 1 - 1e-9 <= across <= half + 1e-9
                if inside:
                    cells.add((x, z))
    return cells


def neighbours(cell: Cell) -> list[Cell]:
    x, z = cell
    return [(x + 1, z), (x - 1, z), (x, z + 1), (x, z - 1)]


def touches(cells: set[Cell], others: set[Cell]) -> bool:
    return any(c in others or any(n in others for n in neighbours(c)) for c in cells)


def components(cells: set[Cell]) -> list[set[Cell]]:
    left, found = set(cells), []
    while left:
        start = left.pop()
        piece, stack = {start}, [start]
        while stack:
            for n in neighbours(stack.pop()):
                if n in left:
                    left.remove(n)
                    piece.add(n)
                    stack.append(n)
        found.append(piece)
    return found


def bounding(cells: set[Cell]) -> Rect | None:
    if not cells:
        return None
    xs, zs = [c[0] for c in cells], [c[1] for c in cells]
    return (min(xs), min(zs), max(xs), max(zs))


class Reader:
    """Finds the places to look again in one reading."""

    def __init__(self, city: City, kit: Kit | None, owner: str | None = None):
        self.city = city
        self.kit = kit
        self.size = city.size or (350, 350)
        self.owner = owner or city.owner
        self.result = Findings()
        self.pieces = [p for p in city.parts + city.features if p.kind is not None]
        self.cells = {id(p): area_cells(p, self.size) for p in self.pieces}
        self.by_name = {p.name: p for p in self.pieces if p.name}

    def find(self, kind: str, where: str, message: str, cell: Rect | None = None) -> None:
        self.result.findings.append(Problem(kind, self.city.file, self.owner, where, message, cell))

    def of_kind(self, *kinds: str) -> set[Cell]:
        found = set()
        for piece in self.pieces:
            if piece.kind in kinds:
                found |= self.cell_set(piece)
        return found

    def cell_set(self, piece: Area) -> set[Cell]:
        if piece.kind == "Road" and piece.name in self.result.road_cells:
            return self.result.road_cells[piece.name]
        return self.cells[id(piece)]

    def household_cells(self, household: str | None, *kinds: str) -> set[Cell]:
        found = set()
        for piece in self.pieces:
            if piece.household == household and household is not None and piece.kind in kinds:
                found |= self.cell_set(piece)
        return found

    def run(self) -> Findings:
        roads = [p for p in self.pieces if p.kind == "Road"]
        for road in roads:
            if len(road.line) >= 2:
                self.result.road_cells[road.name] = band(road.line, road_width(road, self.kit), self.size)
        lined = [road for road in roads if len(road.line) >= 2]
        for road in lined:
            self.road_form(road)
        self.network()
        for road in lined:
            self.road_ends(road)
            self.destination(road)
        self.households()
        self.shares()
        return self.result

    # Roads (FR-054)

    def road_form(self, road: Area) -> None:
        where = f"parts {road.name}"
        settings = self.kit.roads if self.kit is not None else None
        cells = self.result.road_cells.get(road.name, set())
        if settings is not None and road.grade is not None:
            widths = settings.grades.get(road.grade)
            if widths is None:
                self.find(ROAD_KIND, where, f"{road.grade} is not one of the kit's grades: {', '.join(settings.grades)}",
                          bounding(cells))
            elif road.width is None and len(widths) > 1:
                self.find(ROAD_KIND, where, f"{road.grade} is {' or '.join(map(str, widths))} cells wide; the road states which",
                          bounding(cells))
            elif road.width is not None and road.width not in widths:
                even_ok = (road.width % 2 == 0 and road.width_from is not None
                           and any(abs(road.width - w) <= 1 for w in widths))
                if not even_ok:
                    self.find(ROAD_KIND, where, f"{road.width} cells is not a width of {road.grade} "
                              f"({' or '.join(map(str, widths))}), and no pixel width from the picture allows it",
                              bounding(cells))
        if settings is not None and settings.eight_directions:
            for (x0, z0), (x1, z1) in zip(road.line, road.line[1:]):
                dx, dz = x1 - x0, z1 - z0
                if dx != 0 and dz != 0 and abs(dx) != abs(dz):
                    self.find(ROAD_KIND, where, f"the segment from ({x0},{z0}) to ({x1},{z1}) is off the eight directions",
                              (min(x0, x1), min(z0, z1), max(x0, x1), max(z0, z1)))
        blocked = cells & self.of_kind("House", "Plot")
        if blocked:
            self.find(ROAD_KIND, where, "the road lies on a house or plot cell, and a cell holds one piece", bounding(blocked))

    def network(self) -> None:
        cells = self.of_kind(*NETWORK)
        if not cells:
            return
        pieces = sorted(components(cells), key=lambda c: (-len(c), bounding(c)))
        w, h = self.size
        if not any(x in (0, w - 1) or z in (0, h - 1) for piece in pieces for x, z in piece):
            self.find(ROAD_KIND, "the road network", "the roads, gates and plazas reach no edge of the reading's map",
                      bounding(cells))
        for piece in pieces[1:]:
            self.find(ROAD_KIND, "the road network", f"this piece of {len(piece)} cells is not joined to the main "
                      f"network of {len(pieces[0])} cells", bounding(piece))

    def end_region(self, road: Area, at_start: bool) -> tuple[set[Cell], set[Cell]]:
        """The road's cells at one end, and its 2-cell extension beyond that end in the direction of its last
        segment, stopping at the first house it meets (FR-054)."""
        points = road.line if not at_start else list(reversed(road.line))
        (x0, z0), (x1, z1) = points[-2], points[-1]
        width = road_width(road, self.kit)
        own = self.result.road_cells.get(road.name, set())
        tip = band([(x1, z1), (x1, z1)], width, self.size) | {
            c for c in own if math.hypot(c[0] - x1, c[1] - z1) <= width / 2 + 0.5}
        dx, dz = (x1 > x0) - (x1 < x0), (z1 > z0) - (z1 < z0)
        houses = self.of_kind(*BUILDING)
        extension = set()
        for step in (1, 2):
            moved = {(x + dx * step, z + dz * step) for x, z in tip}
            moved -= own
            if moved & houses:
                break
            extension |= moved
        return tip, extension

    def road_ends(self, road: Area) -> None:
        if len(road.line) < 2 or road.name not in self.result.road_cells:
            return
        own = self.result.road_cells[road.name]
        others = self.of_kind(*ROAD_LIKE) - own
        plazas = self.of_kind("Plaza")
        buildings = self.of_kind(*BUILDING)
        yards = self.of_kind(*YARDS)
        target = self.destination_cells(road)
        w, h = self.size
        for at_start in (True, False):
            tip, extension = self.end_region(road, at_start)
            region = tip | extension
            edge = any(x in (0, w - 1) or z in (0, h - 1) for x, z in region)
            if touches(region, others) or edge:
                kind = "through"
            elif target and touches(region, target):
                kind = "way in"
            elif touches(region, plazas):
                kind = "at a plaza"
            elif region & yards:
                kind = "into a yard"
            elif touches(region, buildings) or touches(region, yards):
                kind = "dead end"
            else:
                kind = "dangling"
            self.result.ends[(road.grade or "-", kind)] += 1
            point = road.line[0] if at_start else road.line[-1]
            where = f"parts {road.name} end at ({point[0]},{point[1]})"
            if kind == "dangling":
                self.find(ROAD_KIND, where, "the end, with its 2-cell extension, touches no road, plaza, gate, bridge, "
                          "building, yard or edge of the map: a dangling road", bounding(tip))
            elif kind in ("dead end", "into a yard") and self.kit is not None and self.kit.roads is not None \
                    and self.kit.roads.dead_ends == "None":
                self.find(ROAD_KIND, where, f"the end is {kind}: it touches no other road, gate or map edge and is not "
                          "at its destination, and the kit allows no dead ends", bounding(tip))

    def destination_cells(self, road: Area) -> set[Cell]:
        if road.leads_to is None:
            return set()
        piece = self.by_name.get(road.leads_to)
        household = road.leads_to if piece is None else piece.household
        found = set(self.cell_set(piece)) if piece is not None else set()
        if household is not None:
            found |= self.household_cells(household, *BUILDING, *YARDS, "Plot", *PLOT_CONTENTS)
        return found

    def destination(self, road: Area) -> None:
        where = f"parts {road.name}"
        cells = self.result.road_cells.get(road.name, set())
        if road.leads_to is None:
            self.find(ROAD_KIND, where, "the road names no building, household or plaza it leads to", bounding(cells))
            return
        target = self.destination_cells(road)
        if not target:
            self.find(ROAD_KIND, where, f"it leads to {road.leads_to}, which the reading does not hold", bounding(cells))
            return
        reach = set(cells)
        if len(road.line) >= 2:
            for at_start in (True, False):
                reach |= self.end_region(road, at_start)[1]
        if not touches(reach, target):
            self.find(ROAD_KIND, where, f"{road.leads_to} touches neither the road nor its 2-cell extension",
                      bounding(cells))
        if not road.way_in_from and not road.uncertain:
            self.find(ROAD_KIND, where, f"it names no region where the way in to {road.leads_to} is seen, and is not "
                      "marked unsure (the old project once moved a destination only so that its check passed)",
                      bounding(cells))

    # Households (FR-054, FR-055)

    def households(self) -> None:
        frontage = self.of_kind(*FRONTAGE)
        by_household: dict[str, list[Area]] = defaultdict(list)
        for piece in self.pieces:
            if piece.household is not None:
                by_household[piece.household].append(piece)
        for piece in self.pieces:
            if piece.kind != "House":
                continue
            building = self.household_cells(piece.household, *BUILDING) if piece.household else set()
            building |= self.cells[id(piece)]
            if not touches(building, frontage):
                self.find(HOUSEHOLD_KIND, f"parts {piece.name}", "the building has no side against a road, plaza, yard "
                          "or porch, so no way in", bounding(building))
            elif piece.household is not None and self.kit is not None and self.kit.plot_each:
                own = self.household_cells(piece.household, *YARDS, "Porch") | self.of_kind(*NETWORK)
                if not touches(building, own):
                    self.find(HOUSEHOLD_KIND, f"parts {piece.name}", "the building is reached only through another "
                              "household's yard or path", bounding(building))
        buildings = self.of_kind(*BUILDING)
        for piece in self.pieces:
            if piece.kind == "Yard" and not touches(self.cells[id(piece)], buildings):
                self.find(HOUSEHOLD_KIND, f"parts {piece.name}", "the yard touches no house: cut off from the house it "
                          "belongs to", bounding(self.cells[id(piece)]))
        if self.kit is None or not self.kit.plot_each:
            return
        plots_of: dict[str, set[Cell]] = {}
        owners: dict[Cell, set[str]] = defaultdict(set)
        for name, pieces in sorted(by_household.items()):
            plots = [p for p in pieces if p.kind == "Plot"]
            cells = set().union(*(self.cells[id(p)] for p in plots)) if plots else set()
            plots_of[name] = cells
            for cell in cells:
                owners[cell].add(name)
            houses = [p for p in pieces if p.kind == "House"]
            if houses and not plots:
                self.find(HOUSEHOLD_KIND, f"household {name}", "the household has no plot",
                          bounding(set().union(*(self.cells[id(p)] for p in houses))))
            if len(plots) > 1:
                self.find(HOUSEHOLD_KIND, f"household {name}", f"the household has {len(plots)} plots, not one",
                          bounding(cells))
            if not plots:
                continue
            for piece in pieces:
                if piece.kind in ("House", "AnnexOrAttic", *YARDS, *PLOT_CONTENTS):
                    outside = self.cells[id(piece)] - cells
                    if outside:
                        self.find(HOUSEHOLD_KIND, f"parts {piece.name}", f"{len(outside)} cells of this "
                                  f"{piece.kind} lie outside household {name}'s plot", bounding(outside))
            self.plot_size(name, plots, cells, pieces)
        shared = {cell for cell, names in owners.items() if len(names) > 1}
        if shared:
            for piece in components(shared):
                names = sorted(set().union(*(owners[c] for c in piece)))
                self.find(HOUSEHOLD_KIND, "plots", f"{len(piece)} cells lie in the plots of {' and '.join(names)}",
                          bounding(piece))

    def plot_size(self, name: str, plots: list[Area], cells: set[Cell], pieces: list[Area]) -> None:
        """A residence's plot measured in estates of the reference game: 3 by 3 reference cells, or 4 by 4 set
        diagonally, times the reading's referenceCell squared; a plot over one and a half is listed for the
        maintainer to look at (FR-055). A plot filling less than three quarters of its bounding box is taken as set
        diagonally, since a square turned by 45° fills half of its box."""
        scale = self.city.scale
        residence = any(p.kind == "House" and p.use in (None, "Housing") for p in pieces)
        if scale is None or not scale.usable() or not residence or not cells:
            return
        x1, z1, x2, z2 = bounding(cells)
        fill = len(cells) / ((x2 - x1 + 1) * (z2 - z1 + 1))
        side = 3 if fill >= 0.75 else 4
        estate = (side * scale.reference_cell) ** 2
        estates = len(cells) / estate
        self.result.plot_sizes.append(
            f"{name}: {len(cells)} cells, {len(cells) / scale.reference_cell ** 2:.1f} reference cells, "
            f"{estates:.2f} estates of {side}×{side}"
        )
        if estates > 1.5:
            self.find(HOUSEHOLD_KIND, f"household {name}", f"the plot is {estates:.2f} estates of {side}×{side} "
                      "reference cells, over one and a half: two households may be read as one", bounding(cells))

    # Shares (FR-053)

    def shares(self) -> None:
        w, h = self.size
        taken: dict[Cell, str] = {}
        for label, kinds in SHARE_ORDER:
            for cell in self.of_kind(*kinds):
                taken.setdefault(cell, label)
        counts = Counter(taken.values())
        total = w * h
        for label, _ in SHARE_ORDER:
            self.result.shares.append((label, counts.get(label, 0) / total))
        self.result.shares.append(("nothing traced", (total - len(taken)) / total))


def read(city: City, kit: Kit | None) -> Findings:
    return Reader(city, kit).run()
