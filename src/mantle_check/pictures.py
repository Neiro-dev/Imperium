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
        up the picture, as in the drawing, or at the scale's `origin` where it has one. Each piece carries its name and
        number, the problems at its cells their numbers, and a legend names the colours. Nothing is marked as matching
        or not (spec FR-051; research R-17)."""
        side = city.scale.pixels_per_rimworld_cell()
        origin_x, origin_y = city.scale.origin if city.scale.origin is not None else (0, picture.height)
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
        for areas, colour in ((city.features, FEATURE), (city.parts, AREA)):
            for number, area in enumerate(sorted(areas, key=lambda a: a.name), start=1):
                for rect in area.rects:
                    draw.rectangle(box(rect), fill=(*colour, 110), outline=(*colour, 255))
                if area.rects:
                    labels.append((box(area.rects[0]), f"{number} {area.name}", colour))
        for thing in city.things:
            rect = thing.rect or ((*thing.position, *thing.position) if thing.position is not None else None)
            if rect is not None:
                definition = self.definition(thing.ref.name, "ThingDef")
                colour = self.colour_of(definition, thing.ref.name)
                legend.add("thing", thing.ref.name, colour, self.describe(definition, thing.ref.name))
                draw.rectangle(box(rect), fill=(*colour, 220), outline=INK)
        image = Image.alpha_composite(base, overlay).convert("RGB")
        draw = ImageDraw.Draw(image)
        for (left, top, _, _), caption, colour in labels:
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
