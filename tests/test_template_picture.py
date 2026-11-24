"""User Story 3: a template drawn as its site, with its skeleton, beside its reference pictures (spec, User Story 3,
scenarios 1-3)."""

import pytest
from PIL import Image

from mantle_check import cli
from mantle_check.gamedata import GameData
from mantle_check.pictures import MARGIN, PROBLEM, Painter, name_colour

from conftest import FIXTURES

TEMPLATE = FIXTURES / "us3" / "TestPalaceTown.xml"
SIZE = 30


@pytest.fixture
def drawn(run_check, make_picture, monkeypatch):
    """Checks the template with both reference pictures and keeps the painter that drew it."""
    painters = []

    class Recording(Painter):
        def __init__(self, game):
            super().__init__(game)
            painters.append(self)

    monkeypatch.setattr(cli, "Painter", Recording)
    screenshot = make_picture("screenshot.png", size=(60, 40))
    render = make_picture("render.webp", size=(30, 50), colour=(200, 180, 120))
    result = run_check(
        [TEMPLATE], references=[f"TestPalaceTown:screenshot={screenshot}", f"TestPalaceTown:render={render}"]
    )
    return result, painters[0]


def cell_centre(x: int, z: int) -> tuple[int, int]:
    cell = max(4, min(24, 2100 // SIZE))
    left = MARGIN + x * cell
    top = MARGIN + 24 + (SIZE - 1 - z) * cell
    return (left + cell // 2, top + cell // 2)


def test_each_cell_has_its_terrain_colour(drawn, data_dir):
    result, painter = drawn
    image = Image.open(result.out / "TestPalaceTown.png").convert("RGB")
    game = GameData(data_dir, [])
    expected = {
        (1, 20): painter.colour_of(game.find("Soil", "TerrainDef")[-1], "Soil"),
        (13, 10): painter.colour_of(game.find("WaterMovingShallow", "TerrainDef")[-1], "WaterMovingShallow"),
        (22, 22): painter.colour_of(game.find("Gravel", "TerrainDef")[-1], "Gravel"),
        (3, 3): name_colour("Quicksilver"),
    }
    for (x, z), colour in expected.items():
        assert image.getpixel(cell_centre(x, z)) == colour, (x, z)
    assert len(set(expected.values())) == len(expected)


def test_coordinates_run_along_all_four_edges(drawn):
    _, painter = drawn
    for number in ("0", "10", "20"):
        assert painter.written.count(number) == 4, number
    assert "x grows east, z grows north (top)" in painter.written


def test_the_problem_is_marked_at_its_cell_with_its_number(drawn):
    result, painter = drawn
    assert [(p["number"], p["kind"], p["cell"]) for p in result.problems] == [
        ("1", "unknown definition", "(3, 3)-(4, 4)")
    ]
    assert "1" in painter.written
    image = Image.open(result.out / "TestPalaceTown.png").convert("RGB")
    cell = max(4, min(24, 2100 // SIZE))
    left = MARGIN + 3 * cell
    top = MARGIN + 24 + (SIZE - 1 - 4) * cell
    assert image.getpixel((left, top + cell)) == PROBLEM


def test_the_parts_and_relations_are_named(drawn):
    _, painter = drawn
    for caption in ("palace (PalaceQuarter)", "westBank (District)", "core (Core)", "river (feature)",
                    "Upstream by river", "SameSide by river", "river"):
        assert caption in painter.written, caption


def test_reference_pictures_are_set_beside_it(drawn):
    result, _ = drawn
    side = Image.open(result.out / "TestPalaceTown.side-by-side.png")
    alone = Image.open(result.out / "TestPalaceTown.png")
    assert side.height == alone.height
    assert side.width > alone.width
    assert "- template TestPalaceTown: set beside render" in result.report
    assert "- template TestPalaceTown: set beside screenshot" in result.report

