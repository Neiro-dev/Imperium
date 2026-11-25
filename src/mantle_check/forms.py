"""Reading templates, kits, laid-out cities and readings in the forms `Data/` writes (data-model.md, research R-3)."""

from __future__ import annotations

import re
import xml.etree.ElementTree as ET
from dataclasses import dataclass, field

from .gamedata import may_require
from .report import Problem, Rect

ROTATIONS = ("North", "East", "South", "West")
PART_KINDS = (
    "Core",
    "SecondaryCore",
    "PalaceQuarter",
    "Gate",
    "RiverGate",
    "WaterGate",
    "TowerChain",
    "Lifeline",
    "MainStreet",
    "SecondaryAxis",
    "District",
    "Acropolis",
    "Landmark",
    "Bridge",
    "WallLine",
    "Plaza",
    "PublicBuilding",
)
RELATION_NEEDS = {
    "Inside": ("a", "b"),
    "Adjoins": ("a", "b"),
    "Across": ("a", "b", "feature"),
    "SameSide": ("a", "b", "feature"),
    "Upstream": ("a", "b", "feature"),
    "Farther": ("a", "b", "than"),
}
MAX_MAP = 350
USES = ("Housing", "ShopFront", "Workshop", "Tavern", "Market", "Public", "AnnexOrAttic", "Unclear")
WRONG_SCALE = "wrong scale, region or use"
# The kinds of a piece of a reading from a picture (data-model.md, LaidOutCity `kind`; research R-21).
PIECE_KINDS = (
    "Road", "RouteLine", "Plaza", "Gate", "Bridge", "House", "AnnexOrAttic", "Plot", "Yard", "YardPath", "Porch",
    "CityWall", "YardWall", "LowWall", "Railing", "Fence", "LargePiece", "Tree", "Water", "Bank", "Ruin", "Unclear",
    "Garden", "VineTrellis", "Colonnade", "Shrine", "WorkshopYard", "StockPen", "Shed", "FrontSteps",
)
PLOT_CONTENTS = ("Garden", "VineTrellis", "Colonnade", "Shrine", "WorkshopYard", "StockPen", "Shed", "FrontSteps")
DEAD_ENDS = ("Allowed", "None")
# Attributes every element may carry: the game's own (research R-25; `Data/`, `ModUpdating.txt` lines 356-359).
ATTRIBUTES = frozenset({"MayRequire", "MayRequireAnyOf", "IgnoreIfNoMatchingField"})
DEF_ATTRIBUTES = ATTRIBUTES | {"Name", "ParentName", "Abstract", "Class"}
DEF_FIELDS = {"defName", "label", "description", "modExtensions"}
TEMPLATE_FIELDS = DEF_FIELDS | {
    "kit", "reference", "allowedBiomes", "allowedRivers", "naturalEnemy", "permanentEnemy", "minMapSize",
    "terrainShape", "skeleton", "things",
}
KIT_FIELDS = DEF_FIELDS | {
    "cultures", "nameMaker", "skeleton", "wallSettings", "groups", "fill", "roads", "households", "blockLibrary",
}
CITY_FIELDS = {"template", "kit", "reference", "size", "terrain", "roofs", "things", "parts", "features", "scale", "ground"}
AREA_FIELDS = {"name", "rects"}
READING_AREA_FIELDS = AREA_FIELDS | {
    "from", "use", "basis", "kind", "uncertain", "because", "grade", "width", "widthFrom", "line", "leadsTo",
    "wayInFrom", "household",
}

_INT = r"\s*(-?\d+)\s*"
RECT = re.compile(rf"^\({_INT},{_INT},{_INT},{_INT}\)$")
POSITION = re.compile(rf"^\({_INT},\s*0\s*,{_INT}\)$")
SIZE = re.compile(rf"^\({_INT},{_INT}\)$")
PIXEL = re.compile(rf"^\({_INT},{_INT}\)$")
_NUM = r"\s*(-?\d+(?:\.\d+)?)\s*"
NUMBER_PAIR = re.compile(rf"^\({_NUM},{_NUM}\)$")
MIN_MAP_SIZE = re.compile(rf"^\({_INT},\s*1\s*,{_INT}\)$")


@dataclass
class Named:
    """A name of a definition, where it stands and the expansions marked on it or around it."""

    name: str
    where: str
    marked: frozenset[str]


@dataclass
class LayerEntry:
    ref: Named
    rects: list[Rect]


@dataclass
class Area:
    name: str
    rects: list[Rect]
    flows_from: str | None = None
    # In a reading from a picture only: the pixel rects of the picture the piece was read from (data-model.md).
    from_rects: list[Rect] = field(default_factory=list)
    use: str | None = None
    basis: str | None = None
    # Typed pieces of a reading (data-model.md, LaidOutCity; research R-21).
    kind: str | None = None
    uncertain: bool = False
    because: str | None = None
    grade: str | None = None
    width: int | None = None
    width_from: Rect | None = None
    line: list[tuple[int, int]] = field(default_factory=list)
    leads_to: str | None = None
    way_in_from: list[Rect] = field(default_factory=list)
    household: str | None = None


@dataclass
class Part:
    name: str
    kind: str
    optional: bool


@dataclass
class Relation:
    kind: str
    a: str | None
    b: str | None
    feature: str | None
    than: str | None
    where: str

    def describe(self) -> str:
        extra = ""
        if self.kind in ("Across", "SameSide", "Upstream"):
            extra = f" by {self.feature}"
        elif self.kind == "Farther":
            extra = f" than {self.than}"
        return f"{self.kind}({self.a}, {self.b}){extra}"


@dataclass
class Skeleton:
    parts: list[Part] = field(default_factory=list)
    relations: list[Relation] = field(default_factory=list)


@dataclass
class Thing:
    ref: Named
    position: tuple[int, int] | None
    rotation: str
    stuff: Named | None
    rect: Rect | None
    where: str


@dataclass
class Group:
    name: str
    size: tuple[int, int] | None
    terrain: list[LayerEntry]
    things: list[Thing]
    where: str


@dataclass
class SpecCard:
    name: str
    size: tuple[int, int] | None
    terrain: list[LayerEntry]
    rooms: list[Area]
    things: list[Thing]


@dataclass
class Template:
    def_name: str
    label: str
    file: str
    kit: Named | None
    reference_name: str | None
    reference_pictures: list[str]
    allowed_biomes: list[Named]
    allowed_rivers: list[Named]
    natural_enemy: bool
    permanent_enemy: bool
    min_map_size: tuple[int, int] | None
    terrain: list[LayerEntry]
    rocks: list[LayerEntry]
    roofs: list[LayerEntry]
    features: list[Area]
    skeleton: Skeleton
    buildings: list[Thing] = field(default_factory=list)

    @property
    def owner(self) -> str:
        return f"template {self.def_name}"


@dataclass
class Kit:
    def_name: str
    label: str
    file: str
    skeleton: Skeleton
    wall_def: Named | None
    groups: list[Group]
    fill_wall: Named | None
    fill_door: Named | None
    fill_door_stuff: Named | None
    plots: list[Group]
    block_library: list[SpecCard]
    cultures: list[Named] = field(default_factory=list)
    roads: RoadSettings | None = None
    plot_each: bool | None = None

    @property
    def owner(self) -> str:
        return f"kit {self.def_name}"


@dataclass
class RoadSettings:
    """What a kit holds its culture's readings to beyond the shared road checks (data-model.md, KitDef.roads)."""

    grades: dict[str, tuple[int, ...]] = field(default_factory=dict)
    eight_directions: bool = False
    dead_ends: str = "Allowed"


@dataclass
class Measured:
    name: str
    rect: Rect | None


@dataclass
class Scale:
    """How a reading from a picture sizes one cell (spec FR-048): pixels one cell of the reference game is, the
    RimWorld cells it is, and the things it was measured from."""

    pixels_per_cell: float | None
    reference_cell: float | None
    measured: list[Measured]
    # The pixel of the picture where cell (0, 0)'s lower left corner lies; None puts it at the picture's lower left.
    origin: tuple[int, int] | None = None

    def usable(self) -> bool:
        return (
            self.pixels_per_cell is not None
            and self.reference_cell is not None
            and self.pixels_per_cell > 0
            and self.reference_cell > 0
        )

    def pixels_per_rimworld_cell(self) -> float:
        return self.pixels_per_cell / self.reference_cell


@dataclass
class City:
    file: str
    is_reading: bool
    template: str | None
    kit: str | None
    reference: str | None
    size: tuple[int, int] | None
    terrain: list[LayerEntry]
    roofs: list[LayerEntry]
    things: list[Thing]
    parts: list[Area]
    features: list[Area]
    scale: Scale | None = None
    # A reading of a picture in perspective: pairs of a ground pixel and the cell corner it lies on (R-20).
    ground: list[tuple[tuple[float, float], tuple[float, float]]] = field(default_factory=list)

    @property
    def owner(self) -> str:
        return f"reading {self.file}" if self.is_reading else f"city {self.file}"


class Reader:
    """Reads one file's forms and collects the problems of form it finds (spec FR-014)."""

    def __init__(self, file: str):
        self.file = file
        self.problems: list[Problem] = []
        self.owner = ""

    def problem(self, kind: str, where: str, message: str, cell: Rect | None = None) -> None:
        self.problems.append(Problem(kind, self.file, self.owner, where, message, cell))

    def wrong_form(self, where: str, value: str, form: str) -> None:
        self.problem("wrong form", where, f"'{value}' is not in the form {form}")

    def only(self, node: ET.Element | None, fields: set[str] | frozenset[str], where: str,
             attributes: frozenset[str] = ATTRIBUTES) -> None:
        """Reports each child element and attribute the form does not hold, as the game reports a field its code
        does not hold, unless the element is marked IgnoreIfNoMatchingField (spec FR-014; research R-25)."""
        if node is None:
            return
        for name in sorted(node.attrib):
            if name not in attributes:
                self.problem("wrong form", where, f"the attribute {name} is not one this form holds")
        for child in node:
            if not isinstance(child.tag, str) or child.tag in fields:
                continue
            if (child.get("IgnoreIfNoMatchingField") or "").strip().lower() == "true":
                continue
            self.problem("wrong form", where, f"<{child.tag}> is not a field this form holds")

    def only_li(self, node: ET.Element | None, where: str) -> None:
        """A list holds only `li` elements."""
        self.only(node, {"li"}, where)

    def rect(self, value: str | None, where: str) -> Rect | None:
        match = RECT.match(value or "")
        if not match:
            self.wrong_form(where, value or "", "(minX,minZ,maxX,maxZ)")
            return None
        x1, z1, x2, z2 = (int(g) for g in match.groups())
        if x1 > x2 or z1 > z2:
            self.wrong_form(where, value or "", "(minX,minZ,maxX,maxZ) with each minimum at most its maximum")
            return None
        return (x1, z1, x2, z2)

    def rects(self, node: ET.Element | None, where: str) -> list[Rect]:
        if node is None:
            return []
        found = []
        for li in node.findall("rects/li"):
            rect = self.rect((li.text or "").strip(), f"{where} rects")
            if rect is not None:
                found.append(rect)
        return found

    def position(self, value: str | None, where: str) -> tuple[int, int] | None:
        match = POSITION.match(value or "")
        if not match:
            self.wrong_form(where, value or "", "(x, 0, z)")
            return None
        return (int(match.group(1)), int(match.group(2)))

    def size(self, value: str | None, where: str) -> tuple[int, int] | None:
        match = SIZE.match(value or "")
        if not match or int(match.group(1)) < 1 or int(match.group(2)) < 1:
            self.wrong_form(where, value or "", "(x, z) of whole cells")
            return None
        return (int(match.group(1)), int(match.group(2)))

    def min_map_size(self, value: str | None, where: str) -> tuple[int, int] | None:
        match = MIN_MAP_SIZE.match(value or "")
        if not match or int(match.group(1)) < 1 or int(match.group(2)) < 1:
            self.wrong_form(where, value or "", "(x, 1, z)")
            return None
        return (int(match.group(1)), int(match.group(2)))

    def rotation(self, value: str | None, where: str) -> str:
        value = (value or "").strip()
        if value not in ROTATIONS:
            self.wrong_form(where, value, "North, East, South or West")
            return "North"
        return value

    def boolean(self, node: ET.Element, tag: str) -> bool:
        value = node.findtext(tag)
        if value is None:
            return False
        if value.strip().lower() not in ("true", "false"):
            self.wrong_form(tag, value.strip(), "true or false")
            return False
        return value.strip().lower() == "true"

    def named(self, element: ET.Element | None, where: str, marked: frozenset[str]) -> Named | None:
        if element is None or not (element.text or "").strip():
            return None
        return Named((element.text or "").strip(), where, marked | may_require(element))

    def named_list(self, node: ET.Element, tag: str, marked: frozenset[str]) -> list[Named]:
        holder = node.find(tag)
        if holder is None:
            return []
        self.only_li(holder, tag)
        inner = marked | may_require(holder)
        found = []
        for li in holder.findall("li"):
            named = self.named(li, tag, inner)
            if named is not None:
                found.append(named)
        return found

    def layer(self, node: ET.Element | None, where: str, marked: frozenset[str]) -> list[LayerEntry]:
        if node is None:
            return []
        inner = marked | may_require(node)
        entries = []
        self.only(node, {e.tag for e in node if isinstance(e.tag, str)}, where)
        for element in node:
            if not isinstance(element.tag, str):
                continue
            ref = Named(element.tag, where, inner | may_require(element))
            self.only(element, {"rects"}, f"{where} {element.tag}")
            self.only_li(element.find("rects"), f"{where} {element.tag} rects")
            entries.append(LayerEntry(ref, self.rects(element, f"{where} {element.tag}")))
        return entries

    def areas(self, node: ET.Element | None, where: str, rivers: bool, reading: bool = False) -> list[Area]:
        if node is None:
            return []
        self.only_li(node, where)
        areas = []
        for li in node.findall("li"):
            name = (li.findtext("name") or "").strip()
            label = f"{where} {name}" if name else where
            fields = READING_AREA_FIELDS if reading else AREA_FIELDS
            self.only(li, fields | ({"flowsFrom"} if rivers else set()), label)
            self.only_li(li.find("rects"), f"{label} rects")
            if not name:
                self.problem("missing field", where, "an entry holds no name")
            flows = li.findtext("flowsFrom")
            flows_from = None
            if flows is not None:
                if not rivers:
                    self.problem("wrong kind", label, "only a terrain feature names flowsFrom")
                flows_from = self.rotation(flows, f"{label} flowsFrom")
            area = Area(name, self.rects(li, label), flows_from)
            if reading:
                self.region_and_use(li, label, area)
            areas.append(area)
        return areas

    def region_and_use(self, li: ET.Element, label: str, area: Area) -> None:
        """Reads what a reading from a picture records of a piece: its `from` region, its `use` and its `basis`."""
        for item in li.findall("from/li"):
            rect = self.rect((item.text or "").strip(), f"{label} from")
            if rect is not None:
                area.from_rects.append(rect)
        self.only_li(li.find("from"), f"{label} from")
        use = li.findtext("use")
        basis = (li.findtext("basis") or "").strip()
        if use is not None:
            area.use = use.strip()
            area.basis = basis or None
            if area.use not in USES:
                self.problem(WRONG_SCALE, f"{label} use", f"'{area.use}' is not one of the design's uses: {', '.join(USES)}")
            elif not basis:
                self.problem(WRONG_SCALE, f"{label} use", f"{area.use} is given with no basis, one sentence")
        self.piece(li, label, area)

    def piece(self, li: ET.Element, label: str, area: Area) -> None:
        """Reads what types a piece of a reading: its kind, whether the reader is unsure and why, a road's grade,
        width, line, destination and where its way in is seen, and the household a piece belongs to (data-model.md,
        LaidOutCity; spec FR-053 to FR-055; research R-21)."""
        kind = li.findtext("kind")
        if kind is not None:
            area.kind = kind.strip()
            if area.kind not in PIECE_KINDS:
                self.wrong_form(f"{label} kind", area.kind, "one of " + ", ".join(PIECE_KINDS))
                area.kind = None
        if li.find("uncertain") is not None:
            area.uncertain = self.boolean(li, "uncertain")
        area.because = (li.findtext("because") or "").strip() or None
        if area.uncertain and area.because is None:
            self.problem("missing field", f"{label} because", "an unsure piece says what makes it unsure, one sentence")
        household = li.findtext("household")
        if household is not None:
            area.household = household.strip() or None
        grade = li.findtext("grade")
        if grade is not None:
            area.grade = grade.strip() or None
        width = li.findtext("width")
        if width is not None:
            try:
                area.width = int(width.strip())
                if area.width < 1:
                    raise ValueError
            except ValueError:
                self.wrong_form(f"{label} width", width.strip(), "a whole number of cells, at least 1")
                area.width = None
        width_from = li.findtext("widthFrom")
        if width_from is not None:
            area.width_from = self.rect(width_from.strip(), f"{label} widthFrom")
        line = li.find("line")
        if line is not None:
            self.only_li(line, f"{label} line")
            for point in line.findall("li"):
                match = PIXEL.match((point.text or "").strip())
                if match:
                    area.line.append((int(match.group(1)), int(match.group(2))))
                else:
                    self.wrong_form(f"{label} line", (point.text or "").strip(), "(x,z) on a cell corner")
        leads = li.findtext("leadsTo")
        if leads is not None:
            area.leads_to = leads.strip() or None
        self.only_li(li.find("wayInFrom"), f"{label} wayInFrom")
        for item in li.findall("wayInFrom/li"):
            rect = self.rect((item.text or "").strip(), f"{label} wayInFrom")
            if rect is not None:
                area.way_in_from.append(rect)
        if area.kind in ("Road", "RouteLine"):
            if area.kind == "Road" and area.grade is None:
                self.problem("missing field", f"{label} grade", "a road holds its grade")
            if len(area.line) < 2:
                self.problem("missing field", f"{label} line", "a road holds its centre line, two points or more")
        elif area.grade is not None or line is not None or leads is not None:
            self.problem("wrong kind", label, "only a road holds a grade, a line and a destination")

    def number(self, node: ET.Element, tag: str, where: str) -> float | None:
        text = node.findtext(tag)
        try:
            value = float((text or "").strip())
        except ValueError:
            value = None
        if value is None or not value > 0 or value == float("inf"):
            self.problem(WRONG_SCALE, where, f"'{(text or '').strip()}' is not a positive number")
            return None
        return value

    def ground(self, node: ET.Element | None) -> list[tuple[tuple[float, float], tuple[float, float]]]:
        """A reading's ground pairs: a pixel of the picture's ground and the cell corner it lies on (R-20)."""
        if node is None:
            return []
        self.only(node, {"pairs"}, "ground")
        self.only_li(node.find("pairs"), "ground pairs")
        pairs = []
        for index, li in enumerate(node.findall("pairs/li"), start=1):
            label = f"ground pair #{index}"
            self.only(li, {"pixel", "cell"}, label)
            points = []
            for tag in ("pixel", "cell"):
                value = (li.findtext(tag) or "").strip()
                match = NUMBER_PAIR.match(value)
                if not match:
                    self.wrong_form(f"{label} {tag}", value, "(x,y) of two numbers")
                    break
                points.append((float(match.group(1)), float(match.group(2))))
            if len(points) == 2:
                pairs.append((points[0], points[1]))
        if len(pairs) < 4:
            self.problem(WRONG_SCALE, "ground", f"{len(pairs)} ground pairs are given; a perspective fit needs four or more")
        return pairs

    def scale(self, node: ET.Element | None) -> Scale | None:
        if node is None:
            return None
        self.only(node, {"pixelsPerCell", "referenceCell", "origin", "measured"}, "scale")
        self.only_li(node.find("measured"), "scale measured")
        for li in node.findall("measured/li"):
            self.only(li, {"name", "rect"}, "scale measured")
        scale = Scale(
            self.number(node, "pixelsPerCell", "scale pixelsPerCell"),
            self.number(node, "referenceCell", "scale referenceCell"),
            [],
        )
        origin_text = node.findtext("origin")
        if origin_text is not None:
            match = PIXEL.match(origin_text)
            if match:
                scale.origin = (int(match.group(1)), int(match.group(2)))
            else:
                self.wrong_form("scale origin", origin_text.strip(), "(x,y) in whole pixels")
        measured = node.findall("measured/li")
        if not measured:
            self.problem(WRONG_SCALE, "scale measured", "the scale holds no thing it was measured from, at least one")
        for index, li in enumerate(measured, start=1):
            name = (li.findtext("name") or "").strip()
            label = f"scale measured {name}" if name else f"scale measured #{index}"
            if not name:
                self.problem(WRONG_SCALE, label, "a measured thing holds no name")
            rect_text = li.findtext("rect")
            rect = self.rect(rect_text.strip(), f"{label} rect") if rect_text is not None else None
            if rect_text is None:
                self.problem(WRONG_SCALE, label, "a measured thing holds no rect in the picture's pixels")
            scale.measured.append(Measured(name, rect))
        return scale

    def things(self, node: ET.Element | None, where: str, marked: frozenset[str]) -> list[Thing]:
        if node is None:
            return []
        inner = marked | may_require(node)
        found = []
        for index, element in enumerate(node, start=1):
            if not isinstance(element.tag, str):
                continue
            label = f"{where} {element.tag} #{index}"
            own = inner | may_require(element)
            self.only(element, {"position", "rotation", "stuff", "rect"}, label)
            position_text = element.findtext("position")
            position = self.position(position_text.strip(), f"{label} position") if position_text else None
            if position_text is None:
                self.problem("missing field", label, "the thing holds no position")
            rotation_text = element.findtext("rotation")
            rotation = self.rotation(rotation_text, f"{label} rotation") if rotation_text is not None else "North"
            stuff = self.named(element.find("stuff"), f"{label} stuff", own)
            rect_text = element.findtext("rect")
            rect = self.rect(rect_text.strip(), f"{label} rect") if rect_text is not None else None
            found.append(Thing(Named(element.tag, label, own), position, rotation, stuff, rect, label))
        return found

    def skeleton(self, node: ET.Element | None) -> Skeleton:
        skeleton = Skeleton()
        if node is None:
            return skeleton
        self.only(node, {"parts", "relations"}, "skeleton")
        self.only_li(node.find("parts"), "skeleton parts")
        self.only_li(node.find("relations"), "skeleton relations")
        for li in node.findall("relations/li"):
            self.only(li, {"relation", "a", "b", "feature", "than"}, "skeleton relations")
        for li in node.findall("parts/li"):
            self.only(li, {"name", "kind", "optional"}, "skeleton parts")
            name = (li.findtext("name") or "").strip()
            kind = (li.findtext("kind") or "").strip()
            if not name:
                self.problem("missing field", "skeleton parts", "a part holds no name")
            optional = self.boolean(li, "optional")
            skeleton.parts.append(Part(name, kind, optional))
        for index, li in enumerate(node.findall("relations/li"), start=1):
            kind = (li.findtext("relation") or "").strip()
            values = {key: (li.findtext(key) or "").strip() or None for key in ("a", "b", "feature", "than")}
            skeleton.relations.append(
                Relation(kind, values["a"], values["b"], values["feature"], values["than"], f"relation #{index}")
            )
        return skeleton

    def group(self, li: ET.Element, where: str, marked: frozenset[str]) -> Group:
        name = (li.findtext("name") or "").strip()
        label = f"{where} {name}" if name else where
        self.only(li, {"name", "size", "terrain", "things"}, label)
        size_text = li.findtext("size")
        size = self.size(size_text.strip(), f"{label} size") if size_text is not None else None
        if size_text is None:
            self.problem("missing field", label, "the group holds no size")
        inner = marked | may_require(li)
        return Group(
            name,
            size,
            self.layer(li.find("terrain"), f"{label} terrain", inner),
            self.things(li.find("things"), f"{label} things", inner),
            label,
        )


def read_template(node: ET.Element, file: str) -> tuple[Template, list[Problem]]:
    reader = Reader(file)
    def_name = (node.findtext("defName") or "").strip()
    reader.owner = f"template {def_name}"
    marked = frozenset(may_require(node))
    reader.only(node, TEMPLATE_FIELDS, "template", DEF_ATTRIBUTES)
    reader.only(node.find("reference"), {"name", "pictures"}, "reference")
    reader.only_li(node.find("reference/pictures"), "reference pictures")
    reader.only(node.find("terrainShape"), {"terrain", "rocks", "roofs", "features", "things"}, "terrainShape")
    kit = reader.named(node.find("kit"), "kit", marked)
    if kit is None:
        reader.problem("missing field", "kit", "the template names no kit")
    min_text = node.findtext("minMapSize")
    min_map_size = None
    if min_text is None:
        reader.problem("missing field", "minMapSize", "the template states no smallest map")
    else:
        min_map_size = reader.min_map_size(min_text.strip(), "minMapSize")
        if min_map_size is not None and min_map_size[0] != min_map_size[1]:
            reader.problem("not square", "minMapSize", f"{min_text.strip()} is not square")
    reference = node.find("reference")
    shape = node.find("terrainShape")
    template = Template(
        def_name=def_name,
        label=(node.findtext("label") or def_name).strip(),
        file=file,
        kit=kit,
        reference_name=(reference.findtext("name") or "").strip() or None if reference is not None else None,
        reference_pictures=[
            (li.text or "").strip() for li in reference.findall("pictures/li") if (li.text or "").strip()
        ]
        if reference is not None
        else [],
        allowed_biomes=reader.named_list(node, "allowedBiomes", marked),
        allowed_rivers=reader.named_list(node, "allowedRivers", marked),
        natural_enemy=reader.boolean(node, "naturalEnemy"),
        permanent_enemy=reader.boolean(node, "permanentEnemy"),
        min_map_size=min_map_size,
        terrain=reader.layer(shape.find("terrain") if shape is not None else None, "terrainShape terrain", marked),
        rocks=reader.layer(shape.find("rocks") if shape is not None else None, "terrainShape rocks", marked),
        roofs=reader.layer(shape.find("roofs") if shape is not None else None, "terrainShape roofs", marked),
        features=reader.areas(shape.find("features") if shape is not None else None, "terrainShape features", True),
        skeleton=reader.skeleton(node.find("skeleton")),
        buildings=reader.things(node.find("things"), "things", marked)
        + reader.things(shape.find("things") if shape is not None else None, "terrainShape things", marked),
    )
    return template, reader.problems


def read_kit(node: ET.Element, file: str) -> tuple[Kit, list[Problem]]:
    reader = Reader(file)
    def_name = (node.findtext("defName") or "").strip()
    reader.owner = f"kit {def_name}"
    marked = frozenset(may_require(node))
    reader.only(node, KIT_FIELDS, "kit", DEF_ATTRIBUTES)
    reader.only(node.find("wallSettings"), {"wallDef"}, "wallSettings")
    reader.only(node.find("fill"), {"wallDef", "doorDef", "doorStuffDef", "plots"}, "fill")
    for tag in ("groups", "fill/plots", "blockLibrary"):
        reader.only_li(node.find(tag), tag.replace("/", " "))
    for li in node.findall("blockLibrary/li"):
        reader.only(li, {"name", "size", "terrain", "rooms", "things"}, "spec card")
    if node.find("nameMaker") is not None:
        reader.problem(
            "deprecated field", "nameMaker",
            "a kit holds no word list: a settlement takes its faction's own settlementNameMaker (spec FR-006)",
        )
    fill = node.find("fill")
    fill_marked = marked | may_require(fill) if fill is not None else marked
    cards = []
    for index, li in enumerate(node.findall("blockLibrary/li"), start=1):
        name = (li.findtext("name") or "").strip() or f"#{index}"
        label = f"spec card {name}"
        size_text = li.findtext("size")
        size = reader.size(size_text.strip(), f"{label} size") if size_text is not None else None
        if size_text is None:
            reader.problem("missing field", label, "the spec card holds no size, its plot")
        inner = marked | may_require(li)
        cards.append(
            SpecCard(
                name,
                size,
                reader.layer(li.find("terrain"), f"{label} terrain", inner),
                reader.areas(li.find("rooms"), f"{label} rooms", False),
                reader.things(li.find("things"), f"{label} things", inner),
            )
        )
    kit = Kit(
        def_name=def_name,
        label=(node.findtext("label") or def_name).strip(),
        file=file,
        skeleton=reader.skeleton(node.find("skeleton")),
        wall_def=reader.named(node.find("wallSettings/wallDef"), "wallSettings wallDef", marked),
        groups=[reader.group(li, "groups", marked) for li in node.findall("groups/li")],
        fill_wall=reader.named(fill.find("wallDef") if fill is not None else None, "fill wallDef", fill_marked),
        fill_door=reader.named(fill.find("doorDef") if fill is not None else None, "fill doorDef", fill_marked),
        fill_door_stuff=reader.named(
            fill.find("doorStuffDef") if fill is not None else None, "fill doorStuffDef", fill_marked
        ),
        plots=[reader.group(li, "fill plots", fill_marked) for li in fill.findall("plots/li")] if fill is not None else [],
        block_library=cards,
        cultures=reader.named_list(node, "cultures", marked),
        roads=read_roads(reader, node.find("roads")),
        plot_each=read_households(reader, node.find("households")),
    )
    return kit, reader.problems


def read_roads(reader: Reader, node: ET.Element | None) -> RoadSettings | None:
    """A kit's road settings: its grades with their widths, eight directions and dead ends (data-model.md, KitDef)."""
    if node is None:
        return None
    reader.only(node, {"grades", "eightDirections", "deadEnds"}, "roads")
    reader.only_li(node.find("grades"), "roads grades")
    settings = RoadSettings()
    for li in node.findall("grades/li"):
        reader.only(li, {"name", "widths"}, "roads grades")
        reader.only_li(li.find("widths"), "roads grades widths")
        name = (li.findtext("name") or "").strip()
        if not name:
            reader.problem("missing field", "roads grades", "a grade holds no name")
            continue
        widths = []
        for width in li.findall("widths/li"):
            value = (width.text or "").strip()
            if value.isdigit() and int(value) > 0:
                widths.append(int(value))
            else:
                reader.wrong_form(f"roads grades {name} widths", value, "a whole number of cells, at least 1")
        if not widths:
            reader.problem("missing field", f"roads grades {name}", "a grade holds its widths")
        settings.grades[name] = tuple(widths)
    settings.eight_directions = reader.boolean(node, "eightDirections")
    dead_ends = node.findtext("deadEnds")
    if dead_ends is not None:
        if dead_ends.strip() in DEAD_ENDS:
            settings.dead_ends = dead_ends.strip()
        else:
            reader.wrong_form("roads deadEnds", dead_ends.strip(), "Allowed or None")
    return settings


def read_households(reader: Reader, node: ET.Element | None) -> bool | None:
    if node is None:
        return None
    reader.only(node, {"plotEach"}, "households")
    return reader.boolean(node, "plotEach")


def read_city(root: ET.Element, file: str) -> tuple[City, list[Problem]]:
    reader = Reader(file)
    reference = (root.findtext("reference") or "").strip() or None
    template = (root.findtext("template") or "").strip() or None
    kit = (root.findtext("kit") or "").strip() or None
    is_reading = reference is not None or (template is None and kit is None)
    reader.owner = f"reading {file}" if is_reading else f"city {file}"
    if is_reading:
        if reference is None:
            reader.problem("missing field", "reference", "the reading names no reference city")
    else:
        if template is None:
            reader.problem("missing field", "template", "the city names no template")
        if kit is None:
            reader.problem("missing field", "kit", "the city names no kit")
    size_text = root.findtext("size")
    size = None
    if size_text is None:
        reader.problem("missing field", "size", "no map size is given")
    else:
        size = reader.size(size_text.strip(), "size")
        if size is not None and size[0] != size[1]:
            reader.problem("not square", "size", f"{size_text.strip()} is not square")
    marked = frozenset(may_require(root))
    reader.only(root, CITY_FIELDS, "the file")
    city = City(
        file=file,
        is_reading=is_reading,
        template=template,
        kit=kit,
        reference=reference,
        size=size,
        terrain=reader.layer(root.find("terrain"), "terrain", marked),
        roofs=reader.layer(root.find("roofs"), "roofs", marked),
        things=reader.things(root.find("things"), "things", marked),
        parts=reader.areas(root.find("parts"), "parts", False, is_reading),
        features=reader.areas(root.find("features"), "features", True, is_reading),
        scale=reader.scale(root.find("scale")) if is_reading else None,
        ground=reader.ground(root.find("ground")) if is_reading else [],
    )
    if not is_reading:
        for tag in ("scale", "ground"):
            if root.find(tag) is not None:
                reader.problem("wrong kind", tag, f"only a reading holds {tag}")
    return city, reader.problems
