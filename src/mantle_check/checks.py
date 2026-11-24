"""The problems the check reports (data-model.md, What the check reports)."""

from __future__ import annotations

from dataclasses import dataclass, field

from . import relations as rel
from .forms import (
    MAX_MAP,
    PART_KINDS,
    RELATION_NEEDS,
    City,
    Group,
    Kit,
    LayerEntry,
    Named,
    Skeleton,
    SpecCard,
    Template,
    Thing,
)
from .gamedata import NO_MOD, Definition, GameData, Source, is_true, list_values, text
from .report import Problem, Rect, RelationResult


@dataclass
class Known:
    """The templates and kits the check knows: those in the given mods' Defs/ and in the files given."""

    templates: dict[str, tuple[Template, Source]] = field(default_factory=dict)
    kits: dict[str, tuple[Kit, Source]] = field(default_factory=dict)

    def holder_of_reading(self, reference: str | None) -> Source:
        for name in sorted(self.templates):
            template, holder = self.templates[name]
            if reference is not None and template.reference_name == reference:
                return holder
        return NO_MOD


class Checker:
    def __init__(self, game: GameData, known: Known):
        self.game = game
        self.known = known
        self.problems: list[Problem] = []
        self.relations: list[RelationResult] = []
        self.file = ""
        self.owner = ""
        self.holder: Source = NO_MOD

    # Reporting

    def problem(self, kind: str, where: str, message: str, cell: Rect | None = None) -> None:
        self.problems.append(Problem(kind, self.file, self.owner, where, message, cell))

    def start(self, file: str, owner: str, holder: Source) -> None:
        self.file, self.owner, self.holder = file, owner, holder

    # Names (FR-013, FR-014, FR-015)

    def expansion_name(self, origin: str) -> str:
        source = self.game.source_of(origin)
        return source.name if source is not None else origin

    def lookup(self, named: Named, short_type: str, what: str, cell: Rect | None = None) -> Definition | None:
        found = self.game.find(named.name)
        if not found:
            self.problem("unknown definition", named.where, f"{named.name} is in neither Data/ nor the mods given", cell)
            return None
        typed = [d for d in found if d.short_type == short_type]
        if not typed:
            kinds = ", ".join(sorted({d.short_type for d in found}))
            self.problem("wrong kind", named.where, f"{named.name} is a {kinds}, not {what}", cell)
            return None
        definition = typed[-1]
        self.other_expansion(named, definition, cell)
        return definition

    def other_expansion(self, named: Named, definition: Definition, cell: Rect | None = None) -> None:
        if not definition.is_expansion:
            return
        if definition.origin in self.holder.requires or definition.origin in named.marked:
            return
        source = self.game.source_of(definition.origin)
        package = source.package_id if source is not None else definition.origin
        expansion = self.expansion_name(definition.origin)
        if self.holder is NO_MOD:
            held = f"{expansion} content in a file no mod holds, which requires no expansion,"
        else:
            held = f"{expansion} content, which {self.holder.name} does not require,"
        self.problem(
            "other expansion", named.where, f'{named.name} is {held} and is not marked MayRequire="{package}"', cell
        )

    def terrain(self, named: Named, natural_only: bool, cell: Rect | None = None) -> Definition | None:
        definition = self.lookup(named, "TerrainDef", "a terrain", cell)
        if definition is not None and natural_only:
            if not is_true(text(self.game.resolved(definition), "natural")):
                self.problem("wrong kind", named.where, f"{named.name} is not natural terrain", cell)
        return definition

    def rock(self, named: Named, cell: Rect | None = None) -> None:
        definition = self.lookup(named, "ThingDef", "a rock", cell)
        if definition is not None and not is_true(text(self.game.resolved(definition), "building/isNaturalRock")):
            self.problem("wrong kind", named.where, f"{named.name} is not natural rock: a template holds no building", cell)

    def roof(self, named: Named, natural_only: bool, cell: Rect | None = None) -> None:
        definition = self.lookup(named, "RoofDef", "a roof", cell)
        if definition is not None and natural_only:
            if not is_true(text(self.game.resolved(definition), "isNatural")):
                self.problem("wrong kind", named.where, f"{named.name} is not a natural roof", cell)

    def wall(self, named: Named | None, where: str) -> None:
        if named is None:
            self.problem("missing field", where, "no wall is named")
            return
        definition = self.lookup(named, "ThingDef", "a wall")
        if definition is not None and not is_true(text(self.game.resolved(definition), "building/isWall")):
            self.problem("wrong kind", named.where, f"{named.name} is not a wall")

    def material(self, thing: Thing, definition: Definition, cell: Rect | None = None) -> Definition | None:
        resolved = self.game.resolved(definition)
        categories = set(list_values(resolved, "stuffCategories"))
        if thing.stuff is None:
            if categories:
                self.problem("material", thing.where, f"{definition.name} takes a material and none is given", cell)
            return None
        stuff = self.lookup(thing.stuff, "ThingDef", "a material", cell)
        if stuff is None:
            return None
        stuff_categories = set(list_values(self.game.resolved(stuff), "stuffProps/categories"))
        if not categories:
            self.problem("material", thing.stuff.where, f"{definition.name} takes no material", cell)
        elif not categories & stuff_categories:
            self.problem("material", thing.stuff.where, f"{definition.name} does not take {stuff.name}", cell)
        return stuff

    # Cells (FR-007, FR-016)

    def outside(self, rects: list[Rect], bounds: tuple[int, int], where: str, past: str) -> None:
        w, h = bounds
        for rect in rects:
            x1, z1, x2, z2 = rect
            if x1 < 0 or z1 < 0 or x2 >= w or z2 >= h:
                self.problem("outside the map", where, f"cells reach past {past}", rect)

    def no_terrain(self, layers: list[LayerEntry], bounds: tuple[int, int], where: str) -> None:
        w, h = bounds
        covered = bytearray(w * h)
        for entry in layers:
            for x1, z1, x2, z2 in entry.rects:
                for z in range(max(0, z1), min(h - 1, z2) + 1):
                    start, end = max(0, x1), min(w - 1, x2)
                    if start <= end:
                        covered[z * w + start : z * w + end + 1] = b"\x01" * (end - start + 1)
        for rect in uncovered_rects(covered, w, h):
            self.problem("no terrain", where, "cells inside the map have no terrain", rect)

    # Skeletons (FR-005, FR-017)

    def skeleton(
        self, skeleton: Skeleton, kit_skeleton: Skeleton | None, features: dict[str, object] | None, kit_known: bool = True
    ) -> None:
        """Checks a skeleton's names. While a template's kit is unknown, a name that may be the kit's part is not
        reported: the missing or unknown kit is."""
        kit_parts = {p.name: p.kind for p in kit_skeleton.parts} if kit_skeleton is not None else {}
        own: dict[str, str] = {}
        for part in skeleton.parts:
            where = f"skeleton part {part.name}"
            if part.kind not in PART_KINDS:
                self.problem("wrong kind", where, f"'{part.kind}' is not a part kind")
            if not part.name:
                continue
            if part.name in own:
                self.problem("unknown name", where, f"{part.name} is named twice")
            elif part.name in kit_parts and kit_parts[part.name] != part.kind:
                self.problem("unknown name", where, f"{part.name} is the kit's {kit_parts[part.name]}, not {part.kind}")
            own[part.name] = part.kind
        names = set(own) | set(kit_parts)
        feature_names = set(features or {})
        for name in sorted(feature_names & names):
            self.problem("unknown name", f"feature {name}", f"{name} names both a part and a feature")
        for relation in skeleton.relations:
            where = f"skeleton {relation.where}"
            if relation.kind not in RELATION_NEEDS:
                self.problem("wrong kind", where, f"'{relation.kind}' is not a relation kind")
                continue
            for needed in RELATION_NEEDS[relation.kind]:
                if getattr(relation, needed) is None:
                    self.problem("wrong kind", where, f"{relation.kind} needs {needed}")
            for key in ("a", "b", "than"):
                value = getattr(relation, key)
                if value is not None and value not in names and value not in feature_names and kit_known:
                    holder = "the skeletons and the terrain shape hold" if features is not None else "the kit holds"
                    self.problem("unknown name", where, f"{key} names {value}, which no part {holder} is")
            if relation.feature is not None and RELATION_NEEDS[relation.kind].count("feature"):
                if features is None or relation.feature not in feature_names:
                    self.problem("unknown name", where, f"feature names {relation.feature}, which the terrain shape does not hold")
                elif relation.kind == "Upstream" and getattr(features[relation.feature], "flows_from", None) is None:
                    self.problem("wrong kind", where, f"{relation.feature} is not a river: it names no flowsFrom")

    # Templates

    def template(self, template: Template, holder: Source) -> None:
        self.start(template.file, template.owner, holder)
        kit = None
        if template.kit is not None:
            entry = self.known.kits.get(template.kit.name)
            if entry is None:
                others = self.game.find(template.kit.name)
                if others and not any(d.short_type == "KitDef" for d in others):
                    kinds = ", ".join(sorted({d.short_type for d in others}))
                    self.problem("wrong kind", "kit", f"{template.kit.name} is a {kinds}, not a kit")
                else:
                    self.problem("no kit", "kit", f"no kit {template.kit.name} exists")
            else:
                kit = entry[0]
        for named in template.allowed_biomes:
            self.lookup(named, "BiomeDef", "a biome")
        for named in template.allowed_rivers:
            self.lookup(named, "RiverDef", "a river")
        for entry in template.terrain:
            self.terrain(entry.ref, natural_only=True, cell=bounding_rects(entry.rects))
        for entry in template.rocks:
            self.rock(entry.ref, cell=bounding_rects(entry.rects))
        for entry in template.roofs:
            self.roof(entry.ref, natural_only=True, cell=bounding_rects(entry.rects))
        for thing in template.buildings:
            cell = (*thing.position, *thing.position) if thing.position is not None else thing.rect
            self.problem("wrong kind", thing.where, f"{thing.ref.name} is placed on the template's cells: a template "
                         "holds no building", cell)
        if template.min_map_size is None:
            # With no smallest map stated, only the largest map bounds the cells; the missing or wrong minMapSize is
            # reported, and cells without terrain cannot be told.
            bounds, past = (MAX_MAP, MAX_MAP), f"the largest map ({MAX_MAP}×{MAX_MAP})"
        else:
            bounds = template.min_map_size
            if bounds[0] > MAX_MAP or bounds[1] > MAX_MAP:
                self.problem("outside the map", "minMapSize", f"the smallest map is larger than {MAX_MAP}×{MAX_MAP}")
            past = f"the smallest map ({bounds[0]}×{bounds[1]})"
        for layer in (template.terrain, template.rocks, template.roofs):
            for entry in layer:
                self.outside(entry.rects, bounds, entry.ref.where + " " + entry.ref.name, past)
        for feature in template.features:
            self.outside(feature.rects, bounds, f"feature {feature.name}", past)
        # A template whose terrain holds no cell leaves the land to generation and has none to report (FR-004, FR-016).
        if template.min_map_size is not None and any(entry.rects for entry in template.terrain):
            self.no_terrain(template.terrain, (min(bounds[0], MAX_MAP), min(bounds[1], MAX_MAP)), "terrainShape terrain")
        features = {}
        for feature in template.features:
            if feature.name in features:
                self.problem("unknown name", f"feature {feature.name}", f"{feature.name} is named twice")
            features[feature.name] = feature
        self.skeleton(template.skeleton, kit.skeleton if kit is not None else None, features, kit_known=kit is not None)

    # Kits

    def kit(self, kit: Kit, holder: Source) -> None:
        self.start(kit.file, kit.owner, holder)
        if kit.name_maker is None:
            self.problem("missing field", "nameMaker", "the kit names no word list")
        else:
            self.lookup(kit.name_maker, "RulePackDef", "a word list (RulePackDef)")
        self.wall(kit.wall_def, "wallSettings wallDef")
        for group in kit.groups:
            self.group(group)
        if kit.fill_wall is not None or kit.fill_door is not None or kit.fill_door_stuff is not None or kit.plots:
            self.wall(kit.fill_wall, "fill wallDef")
            door = None
            if kit.fill_door is not None:
                door = self.lookup(kit.fill_door, "ThingDef", "a door")
            if kit.fill_door_stuff is not None:
                stuff = self.lookup(kit.fill_door_stuff, "ThingDef", "a material")
                if door is not None and stuff is not None:
                    takes = set(list_values(self.game.resolved(door), "stuffCategories"))
                    has = set(list_values(self.game.resolved(stuff), "stuffProps/categories"))
                    if not takes & has:
                        self.problem("wrong kind", kit.fill_door_stuff.where, f"{door.name} does not take {stuff.name}")
            for plot in kit.plots:
                self.group(plot)
        self.skeleton(kit.skeleton, None, None)
        for card in kit.block_library:
            self.spec_card(card)

    def placed_things(self, things: list[Thing], bounds: tuple[int, int] | None, past: str) -> None:
        for thing in things:
            cell = (*thing.position, *thing.position) if thing.position is not None else thing.rect
            definition = self.lookup(thing.ref, "ThingDef", "a thing", cell)
            if definition is not None:
                self.material(thing, definition, cell)
                self.thing_size(thing, definition)
            if bounds is None:
                continue
            if thing.position is not None:
                x, z = thing.position
                self.outside([(x, z, x, z)], bounds, thing.where, past)
            if thing.rect is not None:
                self.outside([thing.rect], bounds, thing.where, past)

    def thing_size(self, thing: Thing, definition: Definition) -> None:
        """A thing's rect matches its definition's size, turned by its rotation (data-model.md, Thing; R-7)."""
        wide, deep = parse_size(text(self.game.resolved(definition), "size"))
        if thing.rotation in ("East", "West"):
            wide, deep = deep, wide
        if thing.rect is not None:
            x1, z1, x2, z2 = thing.rect
            if (x2 - x1 + 1, z2 - z1 + 1) != (wide, deep):
                self.problem(
                    "size", thing.where, f"rect covers {x2 - x1 + 1}×{z2 - z1 + 1} cells, {definition.name} turned "
                    f"{thing.rotation} covers {wide}×{deep}", thing.rect
                )
        elif (wide, deep) != (1, 1):
            cell = (*thing.position, *thing.position) if thing.position is not None else None
            self.problem("size", thing.where, f"{definition.name} covers {wide}×{deep} cells and no rect is given", cell)

    def group(self, group: Group) -> None:
        for entry in group.terrain:
            self.terrain(entry.ref, natural_only=False, cell=bounding_rects(entry.rects))
            if group.size is not None:
                self.outside(entry.rects, group.size, f"{entry.ref.where} {entry.ref.name}", "the group's size")
        self.placed_things(group.things, group.size, "the group's size")

    def spec_card(self, card: SpecCard) -> None:
        past = "its plot"
        for entry in card.terrain:
            self.terrain(entry.ref, natural_only=False, cell=bounding_rects(entry.rects))
            if card.size is not None:
                self.outside(entry.rects, card.size, f"{entry.ref.where} {entry.ref.name}", past)
        for room in card.rooms:
            if card.size is not None:
                self.outside(room.rects, card.size, f"spec card {card.name} room {room.name}", past)
        self.placed_things(card.things, card.size, past)

    # Laid-out cities and readings (FR-008, FR-016 to FR-018, FR-029)

    def city(self, city: City) -> None:
        template = kit = None
        if city.is_reading:
            holder = self.known.holder_of_reading(city.reference)
        else:
            entry = self.known.templates.get(city.template or "")
            holder = entry[1] if entry is not None else NO_MOD
            template = entry[0] if entry is not None else None
        self.start(city.file, city.owner, holder)
        if not city.is_reading:
            if city.template is not None and template is None:
                self.problem("no kit", "template", f"no template {city.template} exists")
            kit_entry = self.known.kits.get(city.kit or "")
            if city.kit is not None and kit_entry is None:
                self.problem("no kit", "kit", f"no kit {city.kit} exists")
            kit = kit_entry[0] if kit_entry is not None else None
            if template is not None and template.kit is not None and city.kit is not None:
                if template.kit.name != city.kit:
                    self.problem("no kit", "kit", f"{city.kit} is not the kit of {template.def_name}, {template.kit.name}")
        size = city.size or (MAX_MAP, MAX_MAP)
        if size[0] > MAX_MAP or size[1] > MAX_MAP:
            self.problem("outside the map", "size", f"the map is larger than {MAX_MAP}×{MAX_MAP}")
        past = f"the map ({size[0]}×{size[1]})"
        terrain_defs: list[Definition | None] = []
        for entry in city.terrain:
            terrain_defs.append(self.terrain(entry.ref, natural_only=False, cell=bounding_rects(entry.rects)))
            self.outside(entry.rects, size, f"{entry.ref.where} {entry.ref.name}", past)
        for entry in city.roofs:
            self.roof(entry.ref, natural_only=False, cell=bounding_rects(entry.rects))
            self.outside(entry.rects, size, f"{entry.ref.where} {entry.ref.name}", past)
        for area in city.parts + city.features:
            self.outside(area.rects, size, f"{area.name}", past)
        bounds = (min(size[0], MAX_MAP), min(size[1], MAX_MAP))
        self.no_terrain(city.terrain, bounds, "terrain")
        grid = terrain_grid(city.terrain, bounds)
        for thing in city.things:
            self.city_thing(thing, size, past, grid, terrain_defs, city.terrain)
        if not city.is_reading:
            self.city_skeleton(city, template, kit, bounds)

    def city_thing(self, thing, size, past, grid, terrain_defs, layers) -> None:
        cell = thing.rect if thing.rect is not None else (
            (*thing.position, *thing.position) if thing.position is not None else None
        )
        definition = self.lookup(thing.ref, "ThingDef", "a thing", cell)
        stuff = self.material(thing, definition, cell) if definition is not None else None
        cells: list[tuple[int, int]] = []
        if thing.rect is not None:
            self.outside([thing.rect], size, thing.where, past)
            x1, z1, x2, z2 = thing.rect
            cells = [(x, z) for z in range(z1, z2 + 1) for x in range(x1, x2 + 1)]
        elif thing.position is not None:
            self.outside([thing.position * 2], size, thing.where, past)
            cells = [thing.position]
        if definition is None:
            return
        self.thing_size(thing, definition)
        resolved = self.game.resolved(definition)
        need = text(resolved, "terrainAffordanceNeeded")
        if is_true(text(resolved, "useStuffTerrainAffordance")) and stuff is not None:
            need = text(self.game.resolved(stuff), "terrainAffordanceNeeded") or need
        if not need:
            return
        w, h = size
        for cell in cells:
            x, z = cell
            if not (0 <= x < min(w, MAX_MAP) and 0 <= z < min(h, MAX_MAP)):
                continue
            index = grid[z * min(w, MAX_MAP) + x]
            if index < 0 or terrain_defs[index] is None:
                continue
            affordances = list_values(self.game.resolved(terrain_defs[index]), "affordances")
            if need not in affordances:
                self.problem(
                    "affordance", thing.where,
                    f"{definition.name} needs {need}, which {layers[index].ref.name} does not give",
                    (x, z, x, z),
                )
                return

    def city_skeleton(self, city: City, template: Template | None, kit: Kit | None, size: tuple[int, int]) -> None:
        if template is None:
            return
        parts = {}
        for part in (kit.skeleton.parts if kit is not None else []) + template.skeleton.parts:
            if part.name:
                parts[part.name] = part
        areas = {a.name: rel.cells_of(a.rects) for a in city.parts}
        features = {a.name: a for a in city.features}
        feature_cells = {name: rel.cells_of(a.rects) for name, a in features.items()}
        for name in sorted(parts):
            if not parts[name].optional and not areas.get(name):
                self.problem("missing part", f"part {name}", f"{name} is not optional and has no cells")
        named_features = {r.feature for r in template.skeleton.relations if r.feature}
        named_features |= {
            v for r in template.skeleton.relations for v in (r.a, r.b, r.than) if v and v not in parts
        }
        for name in sorted(named_features):
            if not feature_cells.get(name):
                self.problem("missing part", f"feature {name}", f"the skeleton names {name} and it has no cells")
        relations = (kit.skeleton.relations if kit is not None else []) + template.skeleton.relations
        for relation in relations:
            self.measure(city, relation, parts, areas, features, feature_cells, size)

    def measure(self, city, relation, parts, areas, features, feature_cells, size) -> None:
        label = relation.describe()
        if relation.kind not in RELATION_NEEDS or any(
            getattr(relation, k) is None for k in RELATION_NEEDS[relation.kind]
        ):
            return
        involved = [relation.a, relation.b] + ([relation.than] if relation.kind == "Farther" else [])

        def cells(name):
            return areas.get(name) or feature_cells.get(name) or set()

        for name in involved:
            if not cells(name):
                why = "an optional part left out" if name in parts and parts[name].optional else f"{name} has no cells"
                self.relations.append(RelationResult(self.file, self.owner, label, "not measured", why))
                return
        a, b = cells(relation.a), cells(relation.b)
        result: bool | None
        if relation.kind == "Inside":
            result = rel.inside(a, b, size)
        elif relation.kind == "Adjoins":
            result = rel.adjoins(a, b)
        elif relation.kind in ("Across", "SameSide"):
            feature = feature_cells.get(relation.feature or "", set())
            if not feature:
                self.relations.append(RelationResult(self.file, self.owner, label, "not measured", "no feature cells"))
                return
            joined = rel.same_side(a, b, feature, size)
            result = joined if relation.kind == "SameSide" else not joined
        elif relation.kind == "Upstream":
            river = features.get(relation.feature or "")
            result = None
            if river is not None:
                result = rel.upstream(a, b, feature_cells[relation.feature], river.flows_from, size)
            if result is None:
                self.relations.append(
                    RelationResult(self.file, self.owner, label, "not measured", "the river names no edge it enters by")
                )
                return
        else:
            result = rel.farther(a, b, cells(relation.than))
        if result:
            self.relations.append(RelationResult(self.file, self.owner, label, "holds"))
            return
        where = "; ".join(f"{n} at {bounding_text(cells(n))}" for n in involved)
        self.relations.append(RelationResult(self.file, self.owner, label, "broken", where))
        self.problem("broken relation", relation.where, f"{label} does not hold: {where}", bounding(a))


def parse_size(value: str | None) -> tuple[int, int]:
    if not value:
        return (1, 1)
    parts = value.strip().strip("()").split(",")
    try:
        return (int(parts[0]), int(parts[-1]))
    except (ValueError, IndexError):
        return (1, 1)


def terrain_grid(layers: list[LayerEntry], bounds: tuple[int, int]) -> list[int]:
    w, h = bounds
    grid = [-1] * (w * h)
    for index, entry in enumerate(layers):
        for x1, z1, x2, z2 in entry.rects:
            for z in range(max(0, z1), min(h - 1, z2) + 1):
                start, end = max(0, x1), min(w - 1, x2)
                if start <= end:
                    grid[z * w + start : z * w + end + 1] = [index] * (end - start + 1)
    return grid


def uncovered_rects(covered: bytearray, w: int, h: int) -> list[Rect]:
    """The cells left uncovered, gathered into rectangles: runs along x, joined across z where they match."""
    open_runs: dict[tuple[int, int], int] = {}
    rects: list[Rect] = []
    for z in range(h + 1):
        runs = set()
        if z < h:
            x = 0
            while x < w:
                if not covered[z * w + x]:
                    start = x
                    while x < w and not covered[z * w + x]:
                        x += 1
                    runs.add((start, x - 1))
                else:
                    x += 1
        for run in list(open_runs):
            if run not in runs:
                rects.append((run[0], open_runs.pop(run), run[1], z - 1))
        for run in runs:
            open_runs.setdefault(run, z)
    return sorted(rects, key=lambda r: (r[1], r[0], r[3], r[2]))


def bounding_rects(rects: list[Rect]) -> Rect | None:
    if not rects:
        return None
    return (min(r[0] for r in rects), min(r[1] for r in rects), max(r[2] for r in rects), max(r[3] for r in rects))


def bounding(cells: set[tuple[int, int]]) -> Rect | None:
    if not cells:
        return None
    xs = [c[0] for c in cells]
    zs = [c[1] for c in cells]
    return (min(xs), min(zs), max(xs), max(zs))


def bounding_text(cells: set[tuple[int, int]]) -> str:
    rect = bounding(cells)
    if rect is None:
        return "no cells"
    return f"({rect[0]}, {rect[1]})-({rect[2]}, {rect[3]})"
