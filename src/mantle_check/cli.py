"""The command (contracts/check-command.md)."""

from __future__ import annotations

import sys
from dataclasses import dataclass
from pathlib import Path

import typer
from PIL import Image, UnidentifiedImageError

from . import oldsample, roads
from .checks import Checker, Known
from .forms import WRONG_SCALE, City, Kit, read_city, read_kit, read_template
from .gamedata import NO_MOD, CannotRun, GameData, Source, parse_xml
from .ground import Ground, ground as fit_ground
from .pictures import (
    FINDING, PROBLEM, Painter, area_drawing, over_picture_cells, pieces_of, Piece, same_width, save, side_by_side,
    with_ruler,
)
from .report import Culture, Problem, Report

app = typer.Typer(add_completion=False, help="Check templates, kits and laid-out cities against RimWorld's Data/.")


def inside_repository(folder: Path) -> bool:
    folder = folder.resolve()
    return any((parent / ".git").exists() for parent in (folder, *folder.parents))


def holder_of(path: Path, mods: list[Source]) -> Source | None:
    resolved = path.resolve()
    for mod in mods:
        try:
            resolved.relative_to(mod.folder.resolve())
            return mod
        except ValueError:
            continue
    return None


def display(path: Path, holder: Source | None) -> str:
    if holder is not None:
        return f"{holder.folder.resolve().name}/{path.resolve().relative_to(holder.folder.resolve()).as_posix()}"
    return path.name


def parse_references(values: list[str]) -> dict[tuple[str, str], Path]:
    references = {}
    for value in values:
        if ":" not in value or "=" not in value.split(":", 1)[1]:
            raise CannotRun(f"--reference {value} is not in the form <name>:<label>=<picture>")
        name, rest = value.split(":", 1)
        label, path = rest.split("=", 1)
        references[(name.strip(), label.strip())] = Path(path)
    return references


# A reading's places to look again, its ground, and the old sample beside it (spec FR-052 to FR-057, SC-017 to
# SC-019; research R-20, R-24, R-27)


def parse_crops(values: list[str]) -> dict[tuple[str, str], tuple[int, int, int, int]]:
    crops = {}
    for value in values:
        try:
            name, rest = value.split(":", 1)
            label, box = rest.split("=", 1)
            x0, y0, x1, y1 = (int(v) for v in box.split(","))
        except ValueError as error:
            raise CannotRun(f"--crop {value} is not in the form <name>:<label>=x0,y0,x1,y1") from error
        if x0 > x1 or y0 > y1:
            raise CannotRun(f"--crop {value} has a minimum past its maximum")
        crops[(name.strip(), label.strip())] = (x0, y0, x1, y1)
    return crops


@dataclass
class OldSample:
    sample: oldsample.Sample
    mapping: oldsample.Mapping
    area: tuple[int, int, int, int]
    label: str


def kit_of_reading(city: City, known: Known) -> Kit | None:
    for name in sorted(known.templates):
        template = known.templates[name][0]
        if template.reference_name == city.reference and template.kit is not None:
            entry = known.kits.get(template.kit.name)
            return entry[0] if entry is not None else None
    return None


def measures(owner: str, found: roads.Findings) -> list[str]:
    lines = []
    if found.ends:
        ends = ", ".join(f"{grade} {kind} {count}" for (grade, kind), count in sorted(found.ends.items()))
        lines.append(f"- {owner}: road ends by grade and class: {ends}")
    for size in found.plot_sizes:
        lines.append(f"- {owner}: plot {size}")
    if found.shares:
        shares = ", ".join(f"{label} {share:.3f}" for label, share in found.shares)
        lines.append(f"- {owner}: shares of the land: {shares}")
    return lines


def picture_crop(picture: Image.Image, crop: tuple[int, int, int, int] | None, ground: Ground | None,
                 size: tuple[int, int]) -> tuple[int, int, int, int]:
    """The part of the picture an area is set beside: the given crop, or the box the reading's map takes on the
    picture through its ground fit, with a margin (contracts/check-command.md, --crop)."""
    if crop is not None:
        x0, y0, x1, y1 = crop
    elif ground is not None:
        corners = [ground.pixel(c) for c in ((0, 0), (size[0], 0), (size[0], size[1]), (0, size[1]))]
        x0 = int(min(c[0] for c in corners)) - 10
        y0 = int(min(c[1] for c in corners)) - 10
        x1 = int(max(c[0] for c in corners)) + 10
        y1 = int(max(c[1] for c in corners)) + 10
    else:
        x0, y0, x1, y1 = 0, 0, picture.width - 1, picture.height - 1
    return (max(0, x0), max(0, y0), min(picture.width - 1, x1), min(picture.height - 1, y1))


def marks_of(numbered_problems, numbered_findings, file: str, owner: str) -> list:
    marks = []
    for number, problem in numbered_problems:
        if problem.file == file and problem.owner == owner and problem.cell is not None:
            marks.append((str(number), problem.cell, PROBLEM))
    for number, finding in numbered_findings:
        if finding.file == file and finding.owner == owner and finding.cell is not None:
            marks.append((number, finding.cell, FINDING))
    return marks


NOT_MARKED = "mismatches are not marked and no picture is reported as a match"


def regions_outside(city: City, file: str, owner: str, size: tuple[int, int]) -> list[Problem]:
    """A measured thing or a `from` whose pixels lie outside the reference picture, where the picture is given
    (data-model.md, What the check reports; spec FR-019, FR-048, FR-049)."""
    width, height = size
    problems = []
    found = [(f"scale measured {m.name or '#' + str(i)}", m.rect) for i, m in enumerate(city.scale.measured, 1)] if city.scale else []
    for area in city.parts + city.features:
        found.extend((f"{'parts' if area in city.parts else 'features'} {area.name} from", rect) for rect in area.from_rects)
    for where, rect in found:
        if rect is not None and (rect[0] < 0 or rect[1] < 0 or rect[2] >= width or rect[3] >= height):
            x1, z1, x2, z2 = rect
            problems.append(
                Problem(WRONG_SCALE, file, owner, where,
                        f"({x1},{z1},{x2},{z2}) lies outside the picture, {width}×{height} pixels")
            )
    return problems


def describe(culture: Culture, kit: Kit) -> None:
    """Names what a culture's kit holds that a copy changes: its file, the culture definitions it serves and its walls
    (spec FR-032, FR-034)."""
    culture.kit = kit.file
    culture.cultures = ", ".join(c.name for c in kit.cultures) or None
    culture.walls = kit.wall_def.name if kit.wall_def else None


def run(files: list[Path], data: Path, out: Path, mods: list[Path], references: list[str],
        crops: list[str] = (), old_sample: Path | None = None, old_mapping: Path | None = None,
        old_area: str | None = None) -> int:
    try:
        if inside_repository(out):
            raise CannotRun(f"the output folder {out} lies inside a repository")
        for folder in mods:
            if not (folder / "About" / "About.xml").is_file():
                raise CannotRun(f"the mod folder {folder} has no About/About.xml")
        pictures_given = parse_references(references)
        crops_given = parse_crops(list(crops))
        old = None
        if (old_sample is None) != (old_mapping is None):
            raise CannotRun("--old-sample and --old-mapping are given together")
        if old_sample is not None:
            sample = oldsample.load_sample(old_sample)
            old = OldSample(sample, oldsample.load_mapping(old_mapping), oldsample.parse_area(old_area, sample),
                            old_sample.name)
        game = GameData(data, mods)
        given = []
        for path in files:
            root = parse_xml(path)
            if root.tag not in ("Defs", "LaidOutCity"):
                raise CannotRun(f"{path.name} is neither a Defs file nor a laid-out city")
            holder = holder_of(path, game.mods)
            if root.tag == "Defs" and holder is None:
                game.add_file(path, None, root)
            given.append((display(path, holder), path, root, holder))
    except CannotRun as error:
        print(f"The check could not run: {error}", file=sys.stderr)
        print("Nothing is reported as passing.", file=sys.stderr)
        return 2

    known = Known()
    for name in sorted(game.by_name):
        for definition in game.by_name[name]:
            holder = definition.source
            label = display(definition.file, holder if holder is not NO_MOD else None)
            if definition.short_type == "TemplateDef" and definition.type.startswith("Mantle."):
                known.templates[name] = (read_template(definition.raw, label)[0], holder)
            elif definition.short_type == "KitDef" and definition.type.startswith("Mantle."):
                known.kits[name] = (read_kit(definition.raw, label)[0], holder)

    report = Report()
    checker = Checker(game, known)
    drawings = []
    for label, path, root, holder in sorted(given, key=lambda g: g[0]):
        report.checked.append(label)
        if root.tag == "Defs":
            for node in root:
                if node.tag == "Mantle.TemplateDef":
                    template, problems = read_template(node, label)
                    report.problems.extend(problems)
                    checker.template(template, holder or NO_MOD)
                    if template.kit is not None:
                        report.culture(template.kit.name).templates.add(template.def_name)
                    drawings.append(("template", template))
                elif node.tag == "Mantle.KitDef":
                    kit, problems = read_kit(node, label)
                    report.problems.extend(problems)
                    checker.kit(kit, holder or NO_MOD)
                    describe(report.culture(kit.def_name), kit)
        else:
            city, problems = read_city(root, label)
            report.problems.extend(problems)
            checker.city(city)
            drawings.append(("city", city))
    for culture in report.cultures.values():
        if culture.kit is None and culture.name in known.kits:
            describe(culture, known.kits[culture.name][0])
    report.problems.extend(checker.problems)
    report.relations.extend(checker.relations)

    # Readings from a picture: their places to look again, ground fit and the old sample beside them (R-20, R-24,
    # R-27). None of it is a problem.
    typed = {}
    for kind, item in drawings:
        if kind != "city" or not item.is_reading:
            continue
        fitted = None
        if len(item.ground) >= 4:
            try:
                fitted = fit_ground(item.ground)
                for index, error in enumerate(fitted.errors, start=1):
                    report.measures.append(f"- {item.owner}: ground pair #{index} lies {error:.2f} cells from its cell corner")
            except ValueError as error:
                report.problems.append(Problem(WRONG_SCALE, item.file, item.owner, "ground", str(error)))
        if not any(area.kind is not None for area in item.parts + item.features):
            typed[id(item)] = (None, fitted, None)
            continue
        found = roads.read(item, kit_of_reading(item, known))
        report.findings.extend(found.findings)
        report.measures.extend(measures(item.owner, found))
        old_found = old_city = None
        if old is not None:
            old_city = oldsample.as_city(old.sample, old.area, old.label)
            old_found = roads.Reader(old_city, None, owner="old sample").run()
            report.findings.extend(old_found.findings)
            report.measures.extend(measures(f"old sample {old.label} {old.area}", old_found))
        typed[id(item)] = (found, fitted, (old_city, old_found))

    staged = []
    for kind, item in drawings:
        pictures, reference_name, labels, shown = [], None, [], []
        if kind == "template":
            reference_name, labels = item.reference_name, item.reference_pictures
            owner, file, stem = item.owner, item.file, item.def_name
        else:
            owner, file, stem = item.owner, item.file, Path(item.file).stem
            template = known.templates.get(item.template or "")
            if item.is_reading:
                reference_name = item.reference
                matching = [t for t, _ in known.templates.values() if t.reference_name == item.reference]
                labels = matching[0].reference_pictures if matching else sorted(
                    label for name, label in pictures_given if name == item.reference
                )
            elif template is not None:
                reference_name, labels = template[0].reference_name, template[0].reference_pictures
        scaled = kind == "city" and item.is_reading and item.scale is not None and item.scale.usable()
        if scaled:
            report.pictures.append(f"{owner}: its cells are laid over its first reference picture at its scale; {NOT_MARKED}")
        first = True
        for picture_label in labels:
            path = pictures_given.get((reference_name or "", picture_label))
            if path is None:
                report.problems.append(
                    Problem("no comparison", file, owner, f"reference {picture_label}",
                            f"no picture was given for {reference_name}:{picture_label}")
                )
                report.pictures.append(f"{owner}: {picture_label} missing")
                continue
            try:
                with Image.open(path) as picture:
                    picture.load()
                    pictures.append(picture.convert("RGB"))
                    shown.append((reference_name or "", picture_label))
                if first and kind == "city" and item.is_reading:
                    report.problems.extend(regions_outside(item, file, owner, pictures[0].size))
                first = False
                report.pictures.append(f"{owner}: set beside {picture_label}")
            except (OSError, UnidentifiedImageError):
                report.problems.append(
                    Problem("no comparison", file, owner, f"reference {picture_label}",
                            f"the picture for {reference_name}:{picture_label} cannot be read")
                )
                report.pictures.append(f"{owner}: {picture_label} cannot be read")
        staged.append((kind, item, owner, file, stem, list(zip(shown, pictures))))

    numbered = report.numbered()
    numbered_findings = report.numbered_findings()
    painter = Painter(game)
    for kind, item, owner, file, stem, labelled in staged:
        pictures = [picture for _, picture in labelled]
        marked = [(n, p) for n, p in numbered if p.file == file and p.owner == owner]
        if kind == "city" and id(item) in typed and (typed[id(item)][0] is not None or typed[id(item)][1] is not None):
            draw_reading(item, typed[id(item)], labelled, crops_given, old, numbered, numbered_findings, out, stem)
            continue
        if kind == "template":
            kit = known.kits.get(item.kit.name if item.kit else "")
            image = painter.template(item, marked, kit[0].skeleton if kit else None)
        else:
            image = painter.city(item, marked)
            if pictures and item.is_reading and item.scale is not None and item.scale.usable():
                pictures = [painter.over_picture(pictures[0], item, marked), *pictures[1:]]
        save(image, out / f"{stem}.png")
        if pictures:
            save(side_by_side(image, pictures), out / f"{stem}.side-by-side.png")

    print(report.write(out), end="")
    return 1 if report.numbered() else 0


def draw_reading(city: City, typed, labelled, crops, old: OldSample | None, numbered, numbered_findings, out: Path,
                 stem: str) -> None:
    """A reading from a picture drawn as FR-053 sets, laid over its first picture through its ground fit or scale,
    set beside its pictures' areas at one width, and, with the old sample, the two comparisons of SC-018."""
    found, fitted, old_part = typed
    size = city.size or (350, 350)
    road_cells = found.road_cells if found is not None else {}
    pieces = pieces_of(city, road_cells)
    marks = marks_of(numbered, numbered_findings, city.file, city.owner)
    extra = ["Plots thick, houses thin, yards dashed, each household in its colour; unsure pieces dashed in purple;",
             "problems in red, places to look again (findings) in orange. Nothing is marked as matching or not."]
    drawing = area_drawing(pieces, size, f"{city.owner}: reading of {city.reference or '-'}", True, marks, extra)
    save(drawing, out / f"{stem}.png")
    if not labelled:
        return
    (name, label), screenshot = labelled[0]
    crop = picture_crop(screenshot, crops.get((name, label)), fitted, size)
    if fitted is not None:
        to_pixel = fitted.pixel
    elif city.scale is not None and city.scale.usable():
        side = city.scale.pixels_per_rimworld_cell()
        ox, oy = city.scale.origin if city.scale.origin is not None else (0, screenshot.height)
        to_pixel = lambda c: (ox + c[0] * side, oy - c[1] * side)
    else:
        to_pixel = None
    panels = [drawing]
    over = None
    if to_pixel is not None:
        over = over_picture_cells(screenshot, crop, to_pixel, pieces, True, marks,
                                  f"{city.owner} laid over {label}: {NOT_MARKED}")
        panels.append(over)
    panels.append(with_ruler(screenshot, crop, f"{label}, pixels {crop}"))
    for (other_name, other_label), picture in labelled[1:]:
        other_crop = crops.get((other_name, other_label), (0, 0, picture.width - 1, picture.height - 1))
        panels.append(with_ruler(picture, other_crop, f"{other_label}, pixels {other_crop}"))
    save(same_width(panels, 900), out / f"{stem}.side-by-side.png")
    if old is None or old_part is None or old_part[0] is None:
        return
    old_city, old_found = old_part
    x0, y0, x1, y1 = old.area
    old_pieces = pieces_of(old_city, {})
    old_marks = [(n, f.cell, FINDING) for n, f in numbered_findings if f.owner == "old sample" and f.cell is not None]
    old_drawing = area_drawing(old_pieces, old_city.size, f"old sample {old.label}, cells {old.area}", False,
                               old_marks, ["The old project's sample: a comparison only; nothing of it is in the reading."])
    old_to_pixel = lambda c: old.mapping.pixel((x0 + c[0], y1 + 1 - c[1]))
    old_over = over_picture_cells(screenshot, crop, old_to_pixel, old_pieces, False, old_marks,
                                  f"old sample laid over {label} through the old project's mapping")
    if over is not None:
        save(same_width([over, old_over], 1100), out / f"{stem}.compare-over.png")
    save(same_width([drawing, old_drawing, with_ruler(screenshot, crop, f"{label}, pixels {crop}")], 900),
         out / f"{stem}.compare.png")


@app.command()
def check(
    files: list[Path] = typer.Argument(..., help="Definition files, laid-out cities and readings."),
    data: Path = typer.Option(..., "--data", help="The game's Data/ folder."),
    out: Path = typer.Option(..., "--out", help="The folder for the report and pictures, outside the repository."),
    mod: list[Path] = typer.Option([], "--mod", help="A mod folder whose definitions are read; repeatable."),
    reference: list[str] = typer.Option(
        [], "--reference", help="A reference picture as <name>:<label>=<picture>; repeatable."
    ),
    crop: list[str] = typer.Option(
        [], "--crop", help="The part of a reference picture an area is set beside, <name>:<label>=x0,y0,x1,y1."
    ),
    old_sample: Path = typer.Option(None, "--old-sample", help="The old project's sample (样张格.json), outside the repository."),
    old_mapping: Path = typer.Option(None, "--old-mapping", help="The old project's mapping of the screenshot, as JSON."),
    old_area: str = typer.Option(None, "--old-area", help="The box of the old sample's cells an area takes, x0,y0,x1,y1."),
) -> None:
    raise typer.Exit(run(files, data, out, mod, reference, crop, old_sample, old_mapping, old_area))


def main() -> None:
    app()
