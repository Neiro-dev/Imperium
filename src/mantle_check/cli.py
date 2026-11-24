"""The command (contracts/check-command.md)."""

from __future__ import annotations

import sys
from pathlib import Path

import typer
from PIL import Image, UnidentifiedImageError

from .checks import Checker, Known
from .forms import WRONG_SCALE, City, Kit, read_city, read_kit, read_template
from .gamedata import NO_MOD, CannotRun, GameData, Source, parse_xml
from .pictures import Painter, save, side_by_side
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
    """Names what a culture's kit holds that a copy changes: its file, word list and walls (spec FR-034)."""
    culture.kit = kit.file
    culture.word_list = kit.name_maker.name if kit.name_maker else None
    culture.walls = kit.wall_def.name if kit.wall_def else None


def run(files: list[Path], data: Path, out: Path, mods: list[Path], references: list[str]) -> int:
    try:
        if inside_repository(out):
            raise CannotRun(f"the output folder {out} lies inside a repository")
        for folder in mods:
            if not (folder / "About" / "About.xml").is_file():
                raise CannotRun(f"the mod folder {folder} has no About/About.xml")
        pictures_given = parse_references(references)
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

    staged = []
    for kind, item in drawings:
        pictures, reference_name, labels = [], None, []
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
        staged.append((kind, item, owner, file, stem, pictures))

    numbered = report.numbered()
    painter = Painter(game)
    for kind, item, owner, file, stem, pictures in staged:
        marked = [(n, p) for n, p in numbered if p.file == file and p.owner == owner]
        if kind == "template":
            kit = known.kits.get(item.kit.name if item.kit else "")
            image = painter.template(item, marked, kit[0].skeleton if kit else None)
        else:
            image = painter.city(item, marked)
            if pictures and item.is_reading and item.scale is not None and item.scale.usable():
                pictures = [painter.over_picture(pictures[0], item), *pictures[1:]]
        save(image, out / f"{stem}.png")
        if pictures:
            save(side_by_side(image, pictures), out / f"{stem}.side-by-side.png")

    print(report.write(out), end="")
    return 1 if report.numbered() else 0


@app.command()
def check(
    files: list[Path] = typer.Argument(..., help="Definition files, laid-out cities and readings."),
    data: Path = typer.Option(..., "--data", help="The game's Data/ folder."),
    out: Path = typer.Option(..., "--out", help="The folder for the report and pictures, outside the repository."),
    mod: list[Path] = typer.Option([], "--mod", help="A mod folder whose definitions are read; repeatable."),
    reference: list[str] = typer.Option(
        [], "--reference", help="A reference picture as <name>:<label>=<picture>; repeatable."
    ),
) -> None:
    raise typer.Exit(run(files, data, out, mod, reference))


def main() -> None:
    app()
