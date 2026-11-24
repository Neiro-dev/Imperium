"""User Story 5: a culture added by copying one, with nothing shared changed (spec, User Story 5, scenarios 1-2;
SC-009; FR-033, FR-034)."""

import hashlib
from pathlib import Path

import pytest

from mantle_check import cli
from mantle_check.pictures import Painter

from conftest import FIXTURES, MODS

ROOT = Path(__file__).resolve().parent.parent
MANTLE = ROOT / "Mantle"
IMPERIUM = ROOT / "Imperium"
SHARED_PIECES = MODS / "SharedPieces"
PIECE_KIT = FIXTURES / "us5" / "TestPieceKit.xml"
KIT = IMPERIUM / "Defs/KitDefs/Kits_Empire.xml"
TEMPLATE = IMPERIUM / "Defs/TemplateDefs/Templates_Empire.xml"
SHARED = [ROOT / "src", MANTLE, IMPERIUM, SHARED_PIECES]

FARTHER = "<li><relation>Farther</relation><a>palaceQuarter</a><b>mainGate</b><than>{}</than></li>"

# The copy's changes: its name, its word list, its wall settings and one relation of its skeleton.
KIT_CHANGES = [
    ("<defName>Empire</defName>", "<defName>TestCulture</defName>"),
    ("<label>Empire</label>", "<label>test culture</label>"),
    ("<nameMaker>NamerSettlementEmpireImperium</nameMaker>", "<nameMaker>NamerSettlementOutlander</nameMaker>"),
    ("<wallSettings>\n      <wallDef>Wall</wallDef>", "<wallSettings>\n      <wallDef>TestPieceWall</wallDef>"),
    (FARTHER.format("core"), FARTHER.format("firstSquare")),
]
TEMPLATE_CHANGES = [
    ("<defName>RiverBendTown</defName>", "<defName>TestCultureTown</defName>"),
    ("<kit>Empire</kit>", "<kit>TestCulture</kit>"),
]


def copy_with(source: Path, target: Path, changes: list[tuple[str, str]]) -> Path:
    text = source.read_text(encoding="utf-8")
    for old, new in changes:
        assert text.count(old) == 1, old
        text = text.replace(old, new)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(text, encoding="utf-8", newline="\n")
    return target


def shared_files() -> dict[str, str]:
    found = {}
    for folder in SHARED:
        for path in sorted(folder.rglob("*")):
            if path.is_file() and "__pycache__" not in path.parts:
                found[str(path.relative_to(ROOT))] = hashlib.sha256(path.read_bytes()).hexdigest()
    return found


@pytest.fixture
def recorded(monkeypatch):
    """Keeps every painter the check makes, so that what it wrote can be read."""
    painters = []

    class Recording(Painter):
        def __init__(self, game):
            super().__init__(game)
            painters.append(self)

    monkeypatch.setattr(cli, "Painter", Recording)
    return painters


def culture_line(report: str, culture: str) -> str:
    lines = [line for line in report.splitlines() if line.startswith(f"- {culture}: ")]
    assert len(lines) == 1, report
    return lines[0]


def test_a_copied_culture_is_checked_and_drawn_under_its_new_name(run_check, make_picture, recorded, tmp_path):
    before = shared_files()
    screenshot = make_picture("screenshot.png", size=(60, 40))
    render = make_picture("render.png", size=(40, 40), colour=(200, 180, 120))
    references = [f"RiverBendTown:screenshot={screenshot}", f"RiverBendTown:render={render}"]

    original = run_check([KIT, TEMPLATE], mods=[MANTLE, IMPERIUM], references=references, out=tmp_path / "original")
    assert original.status == 0, original.report

    copies = tmp_path / "TestCulture"
    kit = copy_with(KIT, copies / "Defs/KitDefs/Kits_TestCulture.xml", KIT_CHANGES)
    template = copy_with(TEMPLATE, copies / "Defs/TemplateDefs/Templates_TestCulture.xml", TEMPLATE_CHANGES)
    copy = run_check([kit, template, PIECE_KIT], mods=[MANTLE, SHARED_PIECES], references=references,
                     out=tmp_path / "copy")

    assert copy.status == 0, copy.report
    assert copy.problems == []
    line = culture_line(copy.report, "TestCulture")
    assert "word list NamerSettlementOutlander" in line
    assert "walls TestPieceWall" in line
    assert line.endswith("templates TestCultureTown")
    assert "- Empire: " not in copy.report
    assert "walls Wall" in culture_line(original.report, "Empire")

    assert (copy.out / "TestCultureTown.png").is_file()
    assert (copy.out / "TestCultureTown.side-by-side.png").is_file()
    original_words, copy_words = recorded[0].written, recorded[1].written
    assert "template RiverBendTown: river-bend town (culture Empire)" in original_words
    assert "template TestCultureTown: river-bend town (culture TestCulture)" in copy_words
    assert "Farther than core" in original_words and "Farther than core" not in copy_words
    assert "Farther than firstSquare" in copy_words

    assert shared_files() == before


def test_a_new_culture_finds_a_piece_among_the_shared_pieces(run_check):
    found = run_check([PIECE_KIT], mods=[SHARED_PIECES])
    assert found.status == 0, found.report
    assert "walls TestPieceWall" in culture_line(found.report, "TestPieceCulture")

    missing = run_check([PIECE_KIT], out=found.out.parent / "missing")
    assert missing.status == 1
    assert {(p["kind"], p["where"]) for p in missing.problems} >= {("unknown definition", "wallSettings wallDef")}
    assert all("TestPieceWall" in p["message"] for p in missing.problems)
