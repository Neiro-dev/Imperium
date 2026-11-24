"""User Story 1: templates and kits checked against the game (spec, User Story 1, scenarios 1-6; SC-001, SC-004)."""

import pytest

from mantle_check.report import FINAL_STATEMENT

from conftest import FIXTURES, NEEDS_ROYALTY, NO_EXPANSION

US1 = FIXTURES / "us1"

# Each fixture holds one problem: its kind, the cell reported where it has one, and a word of its message.
ONE_PROBLEM = {
    "unknown-terrain.xml": ("unknown definition", "(30, 30)-(35, 35)", "Quicksilver"),
    "terrain-not-natural.xml": ("wrong kind", "(30, 30)-(35, 35)", "not natural terrain"),
    "kit-wall-not-wall.xml": ("wrong kind", None, "Door is not a wall"),
    "kit-fill-wall-not-wall.xml": ("wrong kind", None, "Door is not a wall"),
    "kit-door-stuff.xml": ("wrong kind", None, "Door does not take Cloth"),
    "biome-not-biome.xml": ("wrong kind", None, "not a biome"),
    "river-not-river.xml": ("wrong kind", None, "not a river"),
    "kit-namer-not-namer.xml": ("wrong kind", None, "not a word list"),
    "part-kind.xml": ("wrong kind", None, "'Castle' is not a part kind"),
    "relation-kind.xml": ("wrong kind", None, "'Near' is not a relation kind"),
    "relation-field.xml": ("wrong kind", None, "Across needs feature"),
    "attitude-form.xml": ("wrong form", None, "'yes'"),
    "min-map-size-form.xml": ("wrong form", None, "(x, 1, z)"),
    "flows-from-form.xml": ("wrong form", None, "'Up'"),
    "kit-rotation-form.xml": ("wrong form", None, "'Up'"),
    "not-square.xml": ("not square", None, "(40, 1, 50)"),
    "no-kit-field.xml": ("missing field", None, "names no kit"),
    "no-min-map-size.xml": ("missing field", None, "no smallest map"),
    "reading-no-reference.xml": ("missing field", None, "names no reference city"),
    "odyssey-unmarked.xml": ("other expansion", "(30, 30)-(35, 35)", 'MayRequire="Ludeon.RimWorld.Odyssey"'),
    "kit-biotech-unmarked.xml": ("other expansion", "(1, 1)", 'MayRequire="Ludeon.RimWorld.Biotech"'),
    "reading-biotech-unmarked.xml": ("other expansion", "(5, 5)", "a file no mod holds"),
    "outside-the-map.xml": ("outside the map", "(30, 30)-(45, 45)", "the smallest map (40×40)"),
    "kit-group-outside.xml": ("outside the map", "(6, 2)", "the group's size"),
    "no-terrain.xml": ("no terrain", "(0, 35)-(4, 39)", "no terrain"),
    "unknown-name.xml": ("unknown name", None, "temple"),
    "kit-unknown-name.xml": ("unknown name", None, "forum"),
    "duplicate-name.xml": ("unknown name", None, "ford is named twice"),
    "no-kit.xml": ("no kit", None, "no kit Atlantis exists"),
    "building-in-rocks.xml": ("wrong kind", "(0, 30)-(5, 39)", "a template holds no building"),
    "building-in-things.xml": ("wrong kind", "(10, 10)", "a template holds no building"),
}

NO_PROBLEM = ["odyssey-marked.xml", "kit-biotech-marked.xml"]


@pytest.mark.parametrize("name", sorted(ONE_PROBLEM))
def test_each_fixture_gives_exactly_its_problem(run_check, name):
    kind, cell, words = ONE_PROBLEM[name]
    result = run_check([US1 / name], mods=[NO_EXPANSION])
    assert result.status == 1, result.report
    assert len(result.problems) == 1, result.report
    problem = result.problems[0]
    assert problem["kind"] == kind
    assert problem["file"] == name
    assert problem["cell"] == cell
    assert words in problem["message"], problem["message"]
    assert result.report.rstrip("\n").endswith(FINAL_STATEMENT)


@pytest.mark.parametrize("name", NO_PROBLEM)
def test_a_marked_expansion_definition_is_accepted(run_check, name):
    result = run_check([US1 / name], mods=[NO_EXPANSION])
    assert result.status == 0, result.report
    assert result.problems == []


def test_royalty_is_reported_only_where_the_mod_does_not_require_it(run_check):
    files = [
        NO_EXPANSION / "Defs/KitDefs/RoyaltyNamer.xml",
        NEEDS_ROYALTY / "Defs/KitDefs/RoyaltyNamer.xml",
    ]
    result = run_check(files, mods=[NO_EXPANSION, NEEDS_ROYALTY])
    assert result.status == 1, result.report
    assert len(result.problems) == 1, result.report
    problem = result.problems[0]
    assert problem["kind"] == "other expansion"
    assert problem["file"] == "NoExpansion/Defs/KitDefs/RoyaltyNamer.xml"
    assert "NamerSettlementEmpire" in problem["message"]
    assert "Test mod requiring no expansion does not require" in problem["message"]


def test_the_clean_template_and_kit_give_no_problem(run_check, make_picture):
    picture = make_picture()
    files = [
        NO_EXPANSION / "Defs/KitDefs/TestTribal.xml",
        NO_EXPANSION / "Defs/TemplateDefs/TestHillfort.xml",
    ]
    result = run_check(files, mods=[NO_EXPANSION], references=[f"TestHillfort:screenshot={picture}"])
    assert result.status == 0, result.report
    assert result.problems == []
    assert "Problems: none found." in result.report
    assert result.report.rstrip("\n").endswith(FINAL_STATEMENT)
    assert (result.out / "TestHillfort.png").is_file()
    assert (result.out / "TestHillfort.side-by-side.png").is_file()
