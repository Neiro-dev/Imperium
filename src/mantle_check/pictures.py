"""The pictures: a grid of cells with coordinates, a legend and the problems marked, set beside the reference
pictures (research R-11; spec FR-023, FR-025 to FR-028)."""

from __future__ import annotations

import hashlib
import math
from dataclasses import dataclass, field
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

from .forms import MAX_MAP, City, LayerEntry, Skeleton, Template, Thing
from .gamedata import Definition, GameData, parse_colour, text
from .report import Problem

MARGIN = 44
BACKGROUND = (250, 250, 247)
INK = (30, 30, 30)
THIN = (0, 0, 0, 38)
STRONG = (0, 0, 0, 110)
PROBLEM = (215, 25, 32)
AREA = (20, 70, 200)
FEATURE = (0, 130, 140)
# A reference picture laid over is enlarged by a whole number to about this many pixels on its longer side.
OVERLAY_SIZE = 1100


def font(size: int = 12):
    try:
        return ImageFont.load_default(size=size)
    except TypeError:
        return ImageFont.load_default()


def name_colour(name: str) -> tuple[int, int, int]:
    digest = hashlib.md5(name.encode("utf-8")).digest()
    return tuple(90 + digest[i] * 140 // 255 for i in range(3))


@dataclass
class Legend:
    entries: dict[tuple[str, str], tuple[tuple[int, int, int], str]] = field(default_factory=dict)

    def add(self, group: str, name: str, colour: tuple[int, int, int], label: str) -> None:
        self.entries.setdefault((group, name), (colour, label))


class Painter:
    def __init__(self, game: GameData):
        self.game = game
        # Every caption drawn, so that what a picture names can be read back without reading its pixels.
        self.written: list[str] = []

    def write(self, draw: ImageDraw.ImageDraw, place, caption: str, fill, size: int) -> None:
        self.written.append(caption)
        draw.text(place, caption, fill=fill, font=font(size))

    def colour_of(self, definition: Definition | None, name: str) -> tuple[int, int, int]:
        if definition is not None:
            resolved = self.game.resolved(definition)
            for path in ("color", "graphicData/color", "stuffProps/color"):
                colour = parse_colour(text(resolved, path))
                if colour is not None:
                    return colour
        return name_colour(name)

    def describe(self, definition: Definition | None, name: str) -> str:
        if definition is None:
            return f"{name} (unknown)"
        label = text(self.game.resolved(definition), "label") or name
        if definition.is_base_game:
            return label
        source = self.game.source_of(definition.origin)
        return f"{label} ({source.name if source is not None else definition.origin})"

    def definition(self, name: str, short_type: str) -> Definition | None:
        found = self.game.find(name, short_type)
        return found[-1] if found else None

    # The grid

    def grid(self, bounds: tuple[int, int], title: str) -> tuple[Image.Image, int]:
        w, h = bounds
        cell = max(4, min(24, 2100 // max(w, h)))
        image = Image.new("RGB", (w * cell + 2 * MARGIN, h * cell + 2 * MARGIN + 24), BACKGROUND)
        self.write(ImageDraw.Draw(image), (MARGIN, 6), title, INK, 14)
        return image, cell

    def origin(self) -> tuple[int, int]:
        return (MARGIN, MARGIN + 24)

    def box(self, cell: int, h: int, x: int, z: int) -> tuple[int, int, int, int]:
        ox, oy = self.origin()
        top = oy + (h - 1 - z) * cell
        left = ox + x * cell
        return (left, top, left + cell - 1, top + cell - 1)

    def rect_box(self, cell: int, h: int, rect) -> tuple[int, int, int, int]:
        x1, z1, x2, z2 = rect
        left, _, _, bottom = self.box(cell, h, x1, z1)
        _, top, right, _ = self.box(cell, h, x2, z2)
        return (left, top, right, bottom)

    def fill_layer(self, image, cell, bounds, layers: list[LayerEntry], short_type: str, legend: Legend, group: str,
                   blend: float = 1.0) -> None:
        w, h = bounds
        # A layer element written later covers the cells of one written earlier (data-model.md, Common forms).
        overlay = Image.new("RGBA", image.size, (0, 0, 0, 0))
        draw = ImageDraw.Draw(overlay)
        alpha = round(255 * blend)
        for entry in layers:
            definition = self.definition(entry.ref.name, short_type)
            colour = self.colour_of(definition, entry.ref.name)
            legend.add(group, entry.ref.name, colour, self.describe(definition, entry.ref.name))
            for x1, z1, x2, z2 in entry.rects:
                rect = (max(0, x1), max(0, z1), min(w - 1, x2), min(h - 1, z2))
                if rect[0] > rect[2] or rect[1] > rect[3]:
                    continue
                draw.rectangle(self.rect_box(cell, h, rect), fill=(*colour, alpha))
        image.paste(Image.alpha_composite(image.convert("RGBA"), overlay).convert("RGB"))

    def lines(self, image, cell, bounds) -> None:
        w, h = bounds
        overlay = Image.new("RGBA", image.size, (0, 0, 0, 0))
        draw = ImageDraw.Draw(overlay)
        ox, oy = self.origin()
        for x in range(w + 1):
            colour = STRONG if x % 10 == 0 or x == w else THIN
            draw.line([(ox + x * cell, oy), (ox + x * cell, oy + h * cell)], fill=colour)
        for z in range(h + 1):
            colour = STRONG if z % 10 == 0 or z == h else THIN
            y = oy + (h - z) * cell
            draw.line([(ox, y), (ox + w * cell, y)], fill=colour)
        image.paste(Image.alpha_composite(image.convert("RGBA"), overlay).convert("RGB"))
        draw = ImageDraw.Draw(image)
        for x in range(0, w, 10):
            px = ox + x * cell
            self.write(draw, (px, oy - 14), str(x), INK, 10)
            self.write(draw, (px, oy + h * cell + 3), str(x), INK, 10)
        for z in range(0, h, 10):
            py = oy + (h - 1 - z) * cell
            self.write(draw, (ox - 30, py), str(z), INK, 10)
            self.write(draw, (ox + w * cell + 4, py), str(z), INK, 10)
        self.write(draw, (ox + w * cell // 2 - 60, oy - 28), "x grows east, z grows north (top)", INK, 10)

    def things(self, image, cell, bounds, things: list[Thing], legend: Legend) -> None:
        w, h = bounds
        draw = ImageDraw.Draw(image)
        for thing in things:
            # A thing is filled with its own colour, and its material's colour shows in its middle.
            definition = self.definition(thing.ref.name, "ThingDef")
            stuff = self.definition(thing.stuff.name, "ThingDef") if thing.stuff is not None else None
            colour = self.colour_of(definition, thing.ref.name)
            legend.add("thing", thing.ref.name, colour, self.describe(definition, thing.ref.name))
            material = None
            if thing.stuff is not None:
                material = self.colour_of(stuff, thing.stuff.name)
                legend.add("material", thing.stuff.name, material, self.describe(stuff, thing.stuff.name))
            if thing.rect is not None:
                rect = thing.rect
            elif thing.position is not None:
                rect = (*thing.position, *thing.position)
            else:
                continue
            x1, z1, x2, z2 = rect
            rect = (max(0, x1), max(0, z1), min(w - 1, x2), min(h - 1, z2))
            if rect[0] > rect[2] or rect[1] > rect[3]:
                continue
            left, top, right, bottom = self.rect_box(cell, h, rect)
            inset = 1 if cell >= 6 else 0
            draw.rectangle([left + inset, top + inset, right - inset, bottom - inset], fill=colour, outline=INK)
            core = cell // 4
            if material is not None and cell >= 8:
                draw.rectangle([left + core, top + core, right - core, bottom - core], fill=material)

    def areas(self, image, cell, bounds, areas, colour) -> None:
        w, h = bounds
        draw = ImageDraw.Draw(image)
        ox, oy = self.origin()
        for area in sorted(areas, key=lambda a: a.name):
            # The outline of all its cells together, so that an area written as many rects reads as one.
            cells = set()
            for x1, z1, x2, z2 in area.rects:
                for x in range(max(0, x1), min(w - 1, x2) + 1):
                    for z in range(max(0, z1), min(h - 1, z2) + 1):
                        cells.add((x, z))
            for x, z in sorted(cells):
                left, top = ox + x * cell, oy + (h - 1 - z) * cell
                right, bottom = left + cell, top + cell
                if (x - 1, z) not in cells:
                    draw.line([(left, top), (left, bottom)], fill=colour, width=2)
                if (x + 1, z) not in cells:
                    draw.line([(right - 1, top), (right - 1, bottom)], fill=colour, width=2)
                if (x, z + 1) not in cells:
                    draw.line([(left, top), (right, top)], fill=colour, width=2)
                if (x, z - 1) not in cells:
                    draw.line([(left, bottom - 1), (right, bottom - 1)], fill=colour, width=2)
            if area.rects:
                x1, z1, x2, z2 = area.rects[0]
                left, top, _, _ = self.rect_box(cell, h, (max(0, x1), max(0, z1), min(w - 1, x2), min(h - 1, z2)))
                self.write(draw, (left + 3, top + 2), area.name, colour, 12)

    def problems(self, image, cell, bounds, numbered: list[tuple[int, Problem]]) -> None:
        w, h = bounds
        draw = ImageDraw.Draw(image)
        for number, problem in numbered:
            if problem.cell is None:
                continue
            x1, z1, x2, z2 = problem.cell
            rect = (max(0, x1), max(0, z1), min(w - 1, x2), min(h - 1, z2))
            if rect[0] > rect[2] or rect[1] > rect[3]:
                rect = (min(max(0, x1), w - 1), min(max(0, z1), h - 1)) * 2
            box = self.rect_box(cell, h, rect)
            draw.rectangle(box, outline=PROBLEM, width=2)
            self.write(draw, (box[0] + 2, box[1] - 14), f"{number}", PROBLEM, 12)

    def legend(self, image: Image.Image, legend: Legend, extra: list[str]) -> Image.Image:
        rows = sorted(legend.entries.items(), key=lambda item: (item[0][0], item[1][1], item[0][1]))
        height = 24 + 18 * (len(rows) + len(extra)) + 10
        out = Image.new("RGB", (max(image.width, 520), image.height + height), BACKGROUND)
        out.paste(image, (0, 0))
        draw = ImageDraw.Draw(out)
        y = image.height + 6
        self.write(draw, (MARGIN, y), "Legend", INK, 13)
        y += 20
        for (group, _), (colour, label) in rows:
            draw.rectangle([MARGIN, y + 2, MARGIN + 12, y + 14], fill=colour, outline=INK)
            self.write(draw, (MARGIN + 20, y), f"{group}: {label}", INK, 12)
            y += 18
        for line in extra:
            self.write(draw, (MARGIN, y), line, INK, 12)
            y += 18
        return out

    # Templates and cities

    def template(self, template: Template, numbered: list[tuple[int, Problem]], kit_skeleton: Skeleton | None) -> Image.Image:
        bounds = template.min_map_size or (MAX_MAP, MAX_MAP)
        bounds = (min(bounds[0], MAX_MAP), min(bounds[1], MAX_MAP))
        image, cell = self.grid(bounds, f"{template.owner}: {template.label} (culture {template.kit.name if template.kit else '-'})")
        legend = Legend()
        self.fill_layer(image, cell, bounds, template.terrain, "TerrainDef", legend, "terrain")
        self.fill_layer(image, cell, bounds, template.rocks, "ThingDef", legend, "rock")
        self.fill_layer(image, cell, bounds, template.roofs, "RoofDef", legend, "roof", blend=0.35)
        self.lines(image, cell, bounds)
        self.areas(image, cell, bounds, template.features, FEATURE)
        self.problems(image, cell, bounds, numbered)
        image = self.legend(image, legend, [])
        diagram = self.diagram(template.skeleton, kit_skeleton, [f.name for f in template.features], image.height)
        out = Image.new("RGB", (image.width + diagram.width, image.height), BACKGROUND)
        out.paste(image, (0, 0))
        out.paste(diagram, (image.width, 0))
        return out

    def city(self, city: City, numbered: list[tuple[int, Problem]]) -> Image.Image:
        bounds = city.size or (MAX_MAP, MAX_MAP)
        bounds = (min(bounds[0], MAX_MAP), min(bounds[1], MAX_MAP))
        if city.is_reading:
            title = f"{city.owner}: reading of {city.reference or '-'}"
        else:
            title = f"{city.owner}: template {city.template or '-'}, culture {city.kit or '-'}"
        image, cell = self.grid(bounds, title)
        legend = Legend()
        self.fill_layer(image, cell, bounds, city.terrain, "TerrainDef", legend, "terrain")
        self.fill_layer(image, cell, bounds, city.roofs, "RoofDef", legend, "roof", blend=0.35)
        self.lines(image, cell, bounds)
        self.things(image, cell, bounds, city.things, legend)
        self.areas(image, cell, bounds, city.features, FEATURE)
        self.areas(image, cell, bounds, city.parts, AREA)
        self.problems(image, cell, bounds, numbered)
        return self.legend(image, legend, ["Parts are outlined in blue, terrain features in teal, problems in red."])

    def over_picture(self, picture: Image.Image, city: City, numbered: list[tuple[int, Problem]]) -> Image.Image:
        """The reference picture with the reading's cells laid over it at the reading's scale: one cell is the
        scale's pixels per cell over its reference cell, cell (0, 0) at the picture's lower left corner and z growing
        up the picture, as in the drawing, or at the scale's `origin` where it has one. A small picture is first
        enlarged by a whole number so that the names, numbers and legend are drawn at a readable size. Each piece
        carries its name and number, an outline round all its cells, the problems at its cells their numbers, and a
        legend names the colours. Nothing is marked as matching or not (spec FR-051; research R-17)."""
        zoom = max(1, OVERLAY_SIZE // max(picture.size))
        if zoom > 1:
            picture = picture.resize((picture.width * zoom, picture.height * zoom), Image.Resampling.LANCZOS)
        side = city.scale.pixels_per_rimworld_cell() * zoom
        origin_x, origin_y = city.scale.origin if city.scale.origin is not None else (0, picture.height // zoom)
        origin_x, origin_y = origin_x * zoom, origin_y * zoom
        base = picture.convert("RGBA")
        overlay = Image.new("RGBA", base.size, (0, 0, 0, 0))
        draw = ImageDraw.Draw(overlay)

        def box(rect) -> tuple[int, int, int, int]:
            x1, z1, x2, z2 = rect
            return (round(origin_x + x1 * side), round(origin_y - (z2 + 1) * side),
                    round(origin_x + (x2 + 1) * side) - 1, round(origin_y - z1 * side) - 1)

        legend = Legend()
        for layers, short_type, blend in ((city.terrain, "TerrainDef", 0.35), (city.roofs, "RoofDef", 0.2)):
            for entry in layers:
                definition = self.definition(entry.ref.name, short_type)
                colour = self.colour_of(definition, entry.ref.name)
                legend.add(short_type[:-3].lower(), entry.ref.name, colour, self.describe(definition, entry.ref.name))
                for rect in entry.rects:
                    draw.rectangle(box(rect), fill=(*colour, round(255 * blend)))
        legend.add("feature", "feature", FEATURE, "terrain feature, outlined")
        legend.add("part", "part", AREA, "part, outlined and numbered")
        labels = []
        outlines = []
        for areas, colour in ((city.features, FEATURE), (city.parts, AREA)):
            for number, area in enumerate(sorted(areas, key=lambda a: a.name), start=1):
                cells = set()
                for rect in area.rects:
                    draw.rectangle(box(rect), fill=(*colour, 110))
                    x1, z1, x2, z2 = rect
                    cells.update((x, z) for x in range(x1, x2 + 1) for z in range(z1, z2 + 1))
                if area.rects:
                    labels.append((box(area.rects[0]), f"{number} {area.name}", colour))
                    outlines.append((cells, colour))
        for thing in city.things:
            rect = thing.rect or ((*thing.position, *thing.position) if thing.position is not None else None)
            if rect is not None:
                definition = self.definition(thing.ref.name, "ThingDef")
                colour = self.colour_of(definition, thing.ref.name)
                legend.add("thing", thing.ref.name, colour, self.describe(definition, thing.ref.name))
                draw.rectangle(box(rect), fill=(*colour, 220), outline=INK)
        image = Image.alpha_composite(base, overlay).convert("RGB")
        draw = ImageDraw.Draw(image)
        for cells, colour in outlines:
            # The outline of all a piece's cells together, so that a piece written as many rects reads as one.
            for x, z in sorted(cells):
                left, top, right, bottom = box((x, z, x, z))
                if (x - 1, z) not in cells:
                    draw.line([(left, top), (left, bottom)], fill=colour, width=2)
                if (x + 1, z) not in cells:
                    draw.line([(right, top), (right, bottom)], fill=colour, width=2)
                if (x, z + 1) not in cells:
                    draw.line([(left, top), (right, top)], fill=colour, width=2)
                if (x, z - 1) not in cells:
                    draw.line([(left, bottom), (right, bottom)], fill=colour, width=2)
        for (left, top, _, _), caption, colour in labels:
            # On a plain label so that it reads over the picture.
            text = draw.textbbox((left + 3, top + 2), caption, font=font(12))
            draw.rectangle((text[0] - 1, text[1] - 1, text[2] + 1, text[3] + 1), fill=BACKGROUND)
            self.write(draw, (left + 3, top + 2), caption, colour, 12)
        for number, problem in numbered:
            if problem.cell is not None:
                left, top, right, bottom = box(problem.cell)
                draw.rectangle((left, top, right, bottom), outline=PROBLEM, width=2)
                self.write(draw, (left + 2, top - 14), f"{number}", PROBLEM, 12)
        self.legend_on(image, legend)
        return image

    def legend_on(self, image: Image.Image, legend: Legend) -> None:
        """A legend of the colours used, in the picture's top left corner, with nothing added to the picture's size."""
        rows = [f"{group}: {label}" for (group, _), (_, label) in sorted(legend.entries.items(), key=lambda i: (i[0][0], i[1][1], i[0][1]))]
        colours = [colour for _, (colour, _) in sorted(legend.entries.items(), key=lambda i: (i[0][0], i[1][1], i[0][1]))]
        if not rows:
            return
        draw = ImageDraw.Draw(image)
        small = font(11)
        width = max(draw.textbbox((0, 0), row, font=small)[2] for row in rows) + 28
        draw.rectangle([4, 4, 4 + width, 8 + 15 * len(rows)], fill=BACKGROUND, outline=INK)
        for index, (row, colour) in enumerate(zip(rows, colours)):
            y = 7 + 15 * index
            draw.rectangle([8, y + 1, 18, y + 11], fill=colour, outline=INK)
            self.write(draw, (22, y), row, INK, 11)

    def diagram(self, skeleton: Skeleton, kit_skeleton: Skeleton | None, features: list[str], height: int) -> Image.Image:
        parts = {}
        for part in (kit_skeleton.parts if kit_skeleton is not None else []) + skeleton.parts:
            if part.name:
                parts[part.name] = part.kind
        relations = (kit_skeleton.relations if kit_skeleton is not None else []) + skeleton.relations
        nodes = sorted(parts) + sorted(f for f in features if f not in parts)
        size = max(520, min(height, 900))
        image = Image.new("RGB", (size, max(height, size)), BACKGROUND)
        draw = ImageDraw.Draw(image)
        self.write(draw, (16, 6), "Skeleton: parts, features and relations", INK, 14)
        if not nodes:
            return image
        cx, cy, radius = size // 2, size // 2 + 10, size // 2 - 110
        places = {}
        for index, name in enumerate(nodes):
            angle = 2 * math.pi * index / len(nodes) - math.pi / 2
            places[name] = (round(cx + radius * math.cos(angle)), round(cy + radius * math.sin(angle)))
        small = font(11)
        for relation in relations:
            ends = [n for n in (relation.a, relation.b) if n in places]
            if len(ends) != 2:
                continue
            (x1, y1), (x2, y2) = places[ends[0]], places[ends[1]]
            draw.line([(x1, y1), (x2, y2)], fill=(120, 120, 120), width=1)
            label = relation.kind
            if relation.feature:
                label += f" by {relation.feature}"
            if relation.than:
                label += f" than {relation.than}"
            self.write(draw, ((x1 + x2) // 2 + 3, (y1 + y2) // 2 - 6), label, (90, 90, 90), 11)
        for name in nodes:
            x, y = places[name]
            caption = f"{name} ({parts[name]})" if name in parts else f"{name} (feature)"
            colour = AREA if name in parts else FEATURE
            box = draw.textbbox((0, 0), caption, font=small)
            width = box[2] - box[0]
            draw.rectangle([x - width // 2 - 4, y - 9, x + width // 2 + 4, y + 9], fill=BACKGROUND, outline=colour)
            self.write(draw, (x - width // 2, y - 7), caption, colour, 11)
        return image


def side_by_side(drawing: Image.Image, pictures: list[Image.Image]) -> Image.Image:
    height = drawing.height
    scaled = [drawing]
    for picture in pictures:
        picture = picture.convert("RGB")
        width = max(1, round(picture.width * height / picture.height))
        scaled.append(picture.resize((width, height), Image.Resampling.LANCZOS))
    gap = 16
    out = Image.new("RGB", (sum(p.width for p in scaled) + gap * (len(scaled) - 1), height), BACKGROUND)
    x = 0
    for picture in scaled:
        out.paste(picture, (x, 0))
        x += picture.width + gap
    return out


def save(image: Image.Image, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    image.save(path, format="PNG", optimize=False)


# A reading's pieces by kind, the old sample beside it, and the screenshot's area (spec FR-053, FR-057, SC-018;
# research R-24, R-27). The same colours serve the new reading and the old sample, so that the two compare by eye.

KIND_COLOURS = {
    "Road": (135, 135, 135), "RouteLine": (160, 160, 160), "Plaza": (205, 200, 190), "Gate": (150, 110, 70),
    "Bridge": (150, 110, 70), "House": (214, 170, 120), "AnnexOrAttic": (185, 175, 210), "Plot": (238, 230, 205),
    "Yard": (226, 205, 150), "YardPath": (212, 192, 140), "Porch": (200, 182, 150), "CityWall": (95, 85, 75),
    "YardWall": (125, 95, 65), "LowWall": (125, 95, 65), "Railing": (150, 120, 90), "Fence": (150, 120, 90),
    "LargePiece": (232, 192, 64), "Tree": (88, 140, 72), "Garden": (150, 190, 110), "Water": (72, 122, 172),
    "Bank": (182, 172, 142), "Ruin": (150, 150, 150), "Unclear": (235, 120, 200), "VineTrellis": (170, 190, 120),
    "Colonnade": (220, 215, 200), "Shrine": (200, 170, 200), "WorkshopYard": (190, 170, 120),
    "StockPen": (175, 160, 110), "Shed": (170, 150, 120), "FrontSteps": (220, 210, 190),
}
# Kinds drawn first are covered by those drawn later, so that a house shows over its plot.
KIND_ORDER = (
    "Plot", "Garden", "VineTrellis", "WorkshopYard", "StockPen", "Shed", "Colonnade", "Shrine", "FrontSteps", "Yard",
    "YardPath", "Porch", "Bank", "Water", "Plaza", "Road", "Bridge", "Gate", "Tree", "Ruin", "Unclear", "LargePiece",
    "AnnexOrAttic", "House", "YardWall", "LowWall", "Railing", "Fence", "CityWall",
)
FINDING = (240, 130, 0)
UNSURE = (200, 0, 160)


def kind_rank(kind: str | None) -> int:
    return KIND_ORDER.index(kind) if kind in KIND_ORDER else len(KIND_ORDER)


def dashed(draw: ImageDraw.ImageDraw, start, end, fill, width: int = 1, dash: int = 4) -> None:
    (x0, y0), (x1, y1) = start, end
    length = math.hypot(x1 - x0, y1 - y0)
    if length == 0:
        return
    steps = max(1, int(length // dash))
    for i in range(0, steps, 2):
        a, b = i / steps, min(1.0, (i + 1) / steps)
        draw.line([(x0 + (x1 - x0) * a, y0 + (y1 - y0) * a), (x0 + (x1 - x0) * b, y0 + (y1 - y0) * b)],
                  fill=fill, width=width)


def outline_edges(cells: set):
    """The edges of a set of cells that face no other cell of it, as pairs of cell corners."""
    for x, z in sorted(cells):
        if (x - 1, z) not in cells:
            yield (x, z), (x, z + 1)
        if (x + 1, z) not in cells:
            yield (x + 1, z), (x + 1, z + 1)
        if (x, z - 1) not in cells:
            yield (x, z), (x + 1, z)
        if (x, z + 1) not in cells:
            yield (x, z + 1), (x + 1, z + 1)


def household_colour(name: str) -> tuple[int, int, int]:
    digest = hashlib.md5(("household " + name).encode("utf-8")).digest()
    return tuple(40 + digest[i] * 150 // 255 for i in range(3))


@dataclass
class Piece:
    """What is drawn of one piece: its cells, kind, name, household, and whether the reader is unsure of it."""

    cells: set
    kind: str
    name: str = ""
    household: str | None = None
    unsure: bool = False
    grade: str | None = None
    line: list = field(default_factory=list)


def pieces_of(city: City, road_cells: dict) -> list[Piece]:
    from .roads import area_cells

    size = city.size or (MAX_MAP, MAX_MAP)
    found = []
    for area in city.parts + city.features:
        if area.kind is None:
            continue
        if area.kind == "Road" and area.name in road_cells:
            cells = road_cells[area.name]
        else:
            cells = area_cells(area, size)
        found.append(Piece(cells, area.kind, area.name, area.household, area.uncertain, area.grade, list(area.line)))
    return found


class KindPainter:
    """Draws pieces by kind on a grid of cells (spec FR-053)."""

    def __init__(self, size: tuple[int, int], cell: int):
        self.w, self.h = size
        self.cell = cell
        self.top = 30

    def corner(self, x: float, z: float) -> tuple[float, float]:
        return (MARGIN + x * self.cell, self.top + (self.h - z) * self.cell)

    def draw(self, pieces: list[Piece], title: str, households: bool, marks: list) -> Image.Image:
        image = Image.new("RGB", (self.w * self.cell + 2 * MARGIN, self.h * self.cell + self.top + MARGIN), BACKGROUND)
        draw = ImageDraw.Draw(image)
        draw.text((MARGIN, 8), title, fill=INK, font=font(14))
        for piece in sorted(pieces, key=lambda p: kind_rank(p.kind)):
            if piece.kind == "RouteLine":
                continue
            colour = KIND_COLOURS.get(piece.kind, (200, 200, 200))
            if households and piece.household and piece.kind in ("House", "AnnexOrAttic"):
                base = household_colour(piece.household)
                colour = tuple((c + 2 * b) // 3 for c, b in zip(colour, base))
            for x, z in piece.cells:
                left, top = self.corner(x, z + 1)
                draw.rectangle([left, top, left + self.cell - 1, top + self.cell - 1], fill=colour)
        # A thin line every 10 cells, so that sizes read without hiding the pieces.
        for x in range(0, self.w + 1, 10):
            draw.line([self.corner(x, 0), self.corner(x, self.h)], fill=(200, 200, 195))
            draw.text((self.corner(x, self.h)[0], self.top - 12), str(x), fill=INK, font=font(9))
        for z in range(0, self.h + 1, 10):
            draw.line([self.corner(0, z), self.corner(self.w, z)], fill=(200, 200, 195))
            draw.text((MARGIN - 22, self.corner(0, z)[1] - 6), str(z), fill=INK, font=font(9))
        for piece in pieces:
            self.piece_lines(draw, piece, households)
        for label, rect, colour in marks:
            x1, z1, x2, z2 = rect
            left, top = self.corner(x1, z2 + 1)
            right, bottom = self.corner(x2 + 1, z1)
            draw.rectangle([left, top, right, bottom], outline=colour, width=2)
            draw.text((left + 2, top - 12), label, fill=colour, font=font(11))
        return image

    def piece_lines(self, draw, piece: Piece, households: bool) -> None:
        if piece.kind == "RouteLine":
            for a, b in zip(piece.line, piece.line[1:]):
                dashed(draw, self.corner(a[0] + 0.5, a[1] + 0.5), self.corner(b[0] + 0.5, b[1] + 0.5),
                       (110, 110, 110), 2)
            return
        colour = household_colour(piece.household) if households and piece.household else INK
        width, dash = 0, False
        if piece.kind == "Plot" and households:
            width = 3
        elif piece.kind in ("House", "AnnexOrAttic", "LargePiece"):
            width = 1
            if not (households and piece.household):
                colour = (70, 45, 25)
        elif piece.kind in ("Yard", "YardPath") and households:
            width, dash = 1, True
        if piece.unsure:
            colour, width, dash = UNSURE, 2, True
        if width:
            for a, b in outline_edges(piece.cells):
                if dash:
                    dashed(draw, self.corner(*a), self.corner(*b), colour, width, 3)
                else:
                    draw.line([self.corner(*a), self.corner(*b)], fill=colour, width=width)
        if piece.cells and ((piece.kind == "Plot" and households) or piece.unsure):
            x1 = min(c[0] for c in piece.cells)
            z2 = max(c[1] for c in piece.cells)
            label = (piece.household or piece.name) + (" ?" if piece.unsure else "")
            left, top = self.corner(x1, z2 + 1)
            draw.text((left + 2, top + 1), label, fill=colour, font=font(10))
        if piece.kind == "Road" and piece.grade and len(piece.line) >= 2:
            a, b = piece.line[(len(piece.line) - 1) // 2], piece.line[(len(piece.line) - 1) // 2 + 1]
            place = self.corner((a[0] + b[0]) / 2 + 0.5, (a[1] + b[1]) / 2 + 0.5)
            text_box = draw.textbbox(place, piece.grade, font=font(10))
            draw.rectangle(text_box, fill=BACKGROUND)
            draw.text(place, piece.grade, fill=INK, font=font(10))


def legend_counts(pieces: list[Piece], extra: list[str]) -> Image.Image:
    counts: dict = {}
    for piece in pieces:
        counts[piece.kind] = counts.get(piece.kind, 0) + 1
    rows = [(kind, counts[kind]) for kind in sorted(counts, key=kind_rank)]
    image = Image.new("RGB", (620, 22 + 16 * (len(rows) + len(extra)) + 8), BACKGROUND)
    draw = ImageDraw.Draw(image)
    draw.text((8, 4), "Legend: pieces by kind, with how many", fill=INK, font=font(12))
    y = 22
    for kind, count in rows:
        draw.rectangle([8, y + 2, 20, y + 13], fill=KIND_COLOURS.get(kind, (200, 200, 200)), outline=INK)
        draw.text((26, y), f"{kind}: {count}", fill=INK, font=font(11))
        y += 16
    for line in extra:
        draw.text((8, y), line, fill=INK, font=font(11))
        y += 16
    return image


def below(image: Image.Image, under: Image.Image) -> Image.Image:
    out = Image.new("RGB", (max(image.width, under.width), image.height + under.height), BACKGROUND)
    out.paste(image, (0, 0))
    out.paste(under, (0, image.height))
    return out


def area_drawing(pieces: list[Piece], size: tuple[int, int], title: str, households: bool, marks: list,
                 extra: list[str]) -> Image.Image:
    cell = max(3, min(12, 1000 // max(size)))
    image = KindPainter(size, cell).draw(pieces, title, households, marks)
    return below(image, legend_counts(pieces, extra))


def zoom_of(crop: tuple[int, int, int, int]) -> int:
    x0, y0, x1, y1 = crop
    return max(1, OVERLAY_SIZE // max(1, max(x1 - x0, y1 - y0)))


def over_picture_cells(picture: Image.Image, crop: tuple[int, int, int, int], to_pixel, pieces: list[Piece],
                       households: bool, marks: list, title: str) -> Image.Image:
    """The picture's area, enlarged by a whole number, with each piece's cells laid over it where `to_pixel` puts the
    cell corners: pieces filled lightly in their kind's colour and outlined, findings and problems boxed with their
    numbers. Nothing is marked as matching or not (spec FR-051, FR-052)."""
    x0, y0, x1, y1 = crop
    zoom = zoom_of(crop)
    base = picture.crop((x0, y0, x1 + 1, y1 + 1)).resize(((x1 - x0 + 1) * zoom, (y1 - y0 + 1) * zoom),
                                                            Image.Resampling.LANCZOS).convert("RGBA")
    overlay = Image.new("RGBA", base.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)

    def place(x: float, z: float) -> tuple[float, float]:
        px, py = to_pixel((x, z))
        return ((px - x0) * zoom, (py - y0) * zoom)

    for piece in sorted(pieces, key=lambda p: kind_rank(p.kind)):
        if piece.kind == "RouteLine":
            continue
        colour = KIND_COLOURS.get(piece.kind, (200, 200, 200))
        for x, z in piece.cells:
            draw.polygon([place(x, z), place(x + 1, z), place(x + 1, z + 1), place(x, z + 1)], fill=(*colour, 70))
    image = Image.alpha_composite(base, overlay).convert("RGB")
    draw = ImageDraw.Draw(image)
    for piece in pieces:
        if piece.kind == "RouteLine":
            for a, b in zip(piece.line, piece.line[1:]):
                dashed(draw, place(a[0] + 0.5, a[1] + 0.5), place(b[0] + 0.5, b[1] + 0.5), (235, 235, 235), 2)
            continue
        colour = KIND_COLOURS.get(piece.kind, (200, 200, 200))
        if households and piece.household and piece.kind in ("Plot", "House", "AnnexOrAttic"):
            colour = household_colour(piece.household)
        width = 3 if piece.kind in ("House", "AnnexOrAttic", "LargePiece") else 2 if piece.kind == "Plot" else 1
        if piece.kind in ("House", "AnnexOrAttic", "LargePiece") and not (households and piece.household):
            colour = (255, 245, 220)
        for a, b in outline_edges(piece.cells):
            if piece.unsure or piece.kind in ("Yard", "YardPath"):
                dashed(draw, place(*a), place(*b), UNSURE if piece.unsure else colour, width, 4)
            else:
                draw.line([place(*a), place(*b)], fill=colour, width=width)
    for label, rect, colour in marks:
        xa, za, xb, zb = rect
        corners = [place(xa, za), place(xb + 1, za), place(xb + 1, zb + 1), place(xa, zb + 1)]
        draw.polygon(corners, outline=colour, width=2)
        left = min(c[0] for c in corners)
        top = min(c[1] for c in corners)
        draw.text((left + 2, top - 13), label, fill=colour, font=font(12))
    box = draw.textbbox((6, 4), title, font=font(13))
    draw.rectangle([0, 0, box[2] + 4, box[3] + 4], fill=BACKGROUND)
    draw.text((6, 4), title, fill=INK, font=font(13))
    return image


def with_ruler(picture: Image.Image, crop: tuple[int, int, int, int], title: str) -> Image.Image:
    """The screenshot's area, enlarged as over_picture_cells enlarges it, with a ruler of its own pixels on two
    sides (spec FR-053)."""
    x0, y0, x1, y1 = crop
    zoom = zoom_of(crop)
    base = picture.crop((x0, y0, x1 + 1, y1 + 1)).resize(((x1 - x0 + 1) * zoom, (y1 - y0 + 1) * zoom),
                                                            Image.Resampling.LANCZOS)
    pad = 34
    out = Image.new("RGB", (base.width + pad, base.height + pad), BACKGROUND)
    out.paste(base, (pad, pad))
    draw = ImageDraw.Draw(out)
    for x in range((x0 // 10 + 1) * 10, x1 + 1, 10):
        px = pad + (x - x0) * zoom
        long = x % 50 == 0
        draw.line([(px, pad - (10 if long else 5)), (px, pad)], fill=INK)
        if long:
            draw.text((px + 2, 4), str(x), fill=INK, font=font(10))
    for y in range((y0 // 10 + 1) * 10, y1 + 1, 10):
        py = pad + (y - y0) * zoom
        long = y % 50 == 0
        draw.line([(pad - (10 if long else 5), py), (pad, py)], fill=INK)
        if long:
            draw.text((2, py + 2), str(y), fill=INK, font=font(10))
    box = draw.textbbox((pad + 4, pad + 4), title, font=font(13))
    draw.rectangle(box, fill=BACKGROUND)
    draw.text((pad + 4, pad + 4), title, fill=INK, font=font(13))
    return out


def same_width(images: list[Image.Image], width: int, gap: int = 16) -> Image.Image:
    """The pictures side by side, each scaled to the same width, so that an area's proportions compare by eye
    (spec FR-053, SC-018)."""
    scaled = [image.resize((width, max(1, round(image.height * width / image.width))), Image.Resampling.LANCZOS)
              for image in images]
    out = Image.new("RGB", (width * len(scaled) + gap * (len(scaled) - 1), max(i.height for i in scaled)), BACKGROUND)
    for index, image in enumerate(scaled):
        out.paste(image, (index * (width + gap), 0))
    return out
