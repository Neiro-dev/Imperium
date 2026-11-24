"""Reading the game's definitions in Data/ and the definitions of the mods given (research R-10)."""

from __future__ import annotations

import copy
import xml.etree.ElementTree as ET
from dataclasses import dataclass, field
from pathlib import Path

BASE_GAME = "ludeon.rimworld"
SUPPORTED_VERSION = "1.7"


class CannotRun(Exception):
    """The check cannot run: nothing is reported as passing (contracts/check-command.md, Exit status 2)."""


@dataclass
class Source:
    """The base game, an expansion or a mod: a folder with About/About.xml."""

    name: str
    package_id: str
    folder: Path
    requires: frozenset[str]
    is_mod: bool

    @property
    def key(self) -> str:
        return self.package_id.lower()


@dataclass
class Definition:
    type: str
    name: str
    source: Source
    origin: str
    file: Path
    raw: ET.Element
    _resolved: ET.Element | None = field(default=None, repr=False)

    @property
    def short_type(self) -> str:
        return self.type.rsplit(".", 1)[-1]

    @property
    def is_base_game(self) -> bool:
        return self.origin == BASE_GAME

    @property
    def is_expansion(self) -> bool:
        return not self.source.is_mod and not self.is_base_game

    @property
    def origin_name(self) -> str:
        return self.source.name


def parse_xml(path: Path) -> ET.Element:
    try:
        return ET.parse(path).getroot()
    except (ET.ParseError, UnicodeDecodeError) as error:
        raise CannotRun(f"{path.name} is not XML: {error}") from error
    except OSError as error:
        raise CannotRun(f"{path} cannot be read: {error.strerror}") from error


def read_about(folder: Path, is_mod: bool) -> Source:
    about = folder / "About" / "About.xml"
    if not about.is_file():
        raise CannotRun(f"{folder} has no About/About.xml")
    root = parse_xml(about)
    package_id = (root.findtext("packageId") or "").strip()
    if not package_id:
        raise CannotRun(f"{about} names no packageId")
    name = (root.findtext("name") or folder.name).strip()
    requires = frozenset(
        (li.findtext("packageId") or "").strip().lower()
        for li in root.findall("modDependencies/li")
        if (li.findtext("packageId") or "").strip()
    )
    return Source(name=name, package_id=package_id, folder=folder, requires=requires, is_mod=is_mod)


def check_version(data_dir: Path) -> str:
    if not data_dir.is_dir():
        raise CannotRun(f"Data/ not found at {data_dir}")
    version_file = data_dir.parent / "Version.txt"
    if not version_file.is_file():
        raise CannotRun(f"Version.txt not found beside {data_dir}")
    version = version_file.read_text(encoding="utf-8-sig").strip()
    if version.split(" ", 1)[0].split(".")[:2] != SUPPORTED_VERSION.split("."):
        raise CannotRun(f"Version.txt names {version}, not {SUPPORTED_VERSION}")
    return version


def may_require(element: ET.Element) -> set[str]:
    values = set()
    for attribute in ("MayRequire", "MayRequireAnyOf"):
        for value in (element.get(attribute) or "").split(","):
            if value.strip():
                values.add(value.strip().lower())
    return values


def merge(target: ET.Element, child: ET.Element) -> None:
    """Gives a child definition's fields over its parent's, as `Data/` inherits them (research R-10)."""
    for node in child:
        if not isinstance(node.tag, str):
            continue
        if node.tag == "li":
            target.append(copy.deepcopy(node))
            continue
        existing = target.find(node.tag)
        if existing is None:
            target.append(copy.deepcopy(node))
        elif (node.get("Inherit") or "").lower() == "false" or len(node) == 0:
            index = list(target).index(existing)
            target.remove(existing)
            target.insert(index, copy.deepcopy(node))
        else:
            merge(existing, node)
    for key, value in child.attrib.items():
        if key not in ("Name", "Abstract", "ParentName"):
            target.set(key, value)


class GameData:
    """Every definition in Data/ and in the Defs/ of the mods given, by name."""

    def __init__(self, data_dir: Path, mod_dirs: list[Path]):
        self.version = check_version(data_dir)
        self.sources: list[Source] = []
        for folder in sorted(p for p in data_dir.iterdir() if (p / "About" / "About.xml").is_file()):
            self.sources.append(read_about(folder, is_mod=False))
        self.sources.sort(key=lambda s: (s.key != BASE_GAME, s.key))
        if not any(s.key == BASE_GAME for s in self.sources):
            raise CannotRun(f"{data_dir} holds no base game (Core)")
        self.mods: list[Source] = [read_about(folder, is_mod=True) for folder in mod_dirs]
        self.by_name: dict[str, list[Definition]] = {}
        self._parents: dict[tuple[str, str], list[tuple[Source, ET.Element]]] = {}
        for source in self.sources + self.mods:
            defs = source.folder / "Defs"
            if defs.is_dir():
                for path in sorted(defs.rglob("*.xml")):
                    self.add_file(path, source)

    def add_file(self, path: Path, source: Source | None, root: ET.Element | None = None) -> None:
        if root is None:
            root = parse_xml(path)
        if root.tag != "Defs":
            return
        holder = source or NO_MOD
        for node in root:
            if not isinstance(node.tag, str):
                continue
            name_attr = node.get("Name")
            if name_attr:
                self._parents.setdefault((node.tag, name_attr), []).append((holder, node))
            def_name = (node.findtext("defName") or "").strip()
            if not def_name or (node.get("Abstract") or "").lower() == "true":
                continue
            marked = may_require(node)
            origin = sorted(marked)[0] if marked and not holder.is_mod else holder.key
            definition = Definition(
                type=node.tag, name=def_name, source=holder, origin=origin, file=path, raw=node
            )
            self.by_name.setdefault(def_name, []).append(definition)

    def source_of(self, package_id: str) -> Source | None:
        for source in self.sources + self.mods:
            if source.key == package_id:
                return source
        return None

    def find(self, name: str, short_type: str | None = None) -> list[Definition]:
        found = self.by_name.get(name, [])
        if short_type is None:
            return found
        return [d for d in found if d.short_type == short_type]

    def resolved(self, definition: Definition) -> ET.Element:
        if definition._resolved is None:
            definition._resolved = self._resolve(definition.raw, definition.source, set())
        return definition._resolved

    def _resolve(self, node: ET.Element, source: Source, seen: set[int]) -> ET.Element:
        parent_name = node.get("ParentName")
        if not parent_name or id(node) in seen:
            return copy.deepcopy(node)
        seen = seen | {id(node)}
        candidates = self._parents.get((node.tag, parent_name), [])
        if not candidates:
            return copy.deepcopy(node)
        same = [c for c in candidates if c[0] is source]
        parent_source, parent = (same or candidates)[-1]
        result = self._resolve(parent, parent_source, seen)
        result.attrib.pop("Abstract", None)
        result.attrib.pop("Name", None)
        merge(result, node)
        return result


NO_MOD = Source(name="no mod", package_id="", folder=Path(), requires=frozenset(), is_mod=True)


def text(node: ET.Element | None, path: str) -> str | None:
    if node is None:
        return None
    value = node.findtext(path)
    return value.strip() if value is not None else None


def is_true(value: str | None) -> bool:
    return (value or "").strip().lower() == "true"


def list_values(node: ET.Element | None, path: str) -> list[str]:
    if node is None:
        return []
    holder = node.find(path)
    if holder is None:
        return []
    return [(li.text or "").strip() for li in holder.findall("li") if (li.text or "").strip()]


def parse_colour(value: str | None) -> tuple[int, int, int] | None:
    if not value:
        return None
    parts = value.strip().strip("()").split(",")
    if len(parts) < 3:
        return None
    try:
        numbers = [float(p) for p in parts[:3]]
    except ValueError:
        return None
    if all(n <= 1.0 for n in numbers):
        numbers = [n * 255 for n in numbers]
    return tuple(max(0, min(255, round(n))) for n in numbers)
