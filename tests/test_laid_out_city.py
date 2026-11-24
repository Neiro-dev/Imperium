"""User Story 2: a laid-out city checked, its relations measured and drawn beside its reference (spec, User Story 2,
scenarios 1-4; Edge Cases)."""

import re

import pytest

from conftest import FIXTURES

US2 = FIXTURES / "us2"
CITIES = US2 / "cities"
DEFS = [US2 / "TestTown.xml", US2 / "TestRiverTown.xml", US2 / "TestOtherKit.xml"]

RELATIONS = [
    "Across(westBank, eastBank) by river",
    "Adjoins(bridge, westBank)",
    "Adjoins(gate, walls)",
    "Farther(palace, gate) than core",
    "Inside(square, core)",
    "SameSide(core, westBank) by river",
    "Upstream(palace, core) by river",
]

# Each city: the one problem it holds (kind, cell, words of the message), or None; and the relations that do not hold.
CITY = {
    "clean.xml": (None, {}),
    "wood-wall-on-marsh.xml": (None, {}),
    "granite-wall-on-marsh.xml": (("affordance", "(31, 31)", "Wall needs Heavy, which MarshyTerrain does not give"), {}),
    "rect-not-size.xml": (("size", "(10, 20)", "Bed turned North covers 1×2"), {}),
    "material-not-taken.xml": (("material", "(4, 5)", "Wall does not take Cloth"), {}),
    "missing-part.xml": (
        ("missing part", None, "square is not optional"),
        {"Inside(square, core)": "not measured"},
    ),
    "optional-left-out.xml": (None, {"Adjoins(gate, walls)": "not measured"}),
    "broken-inside.xml": (("broken relation", "(13, 12)-(15, 14)", "Inside(square, core)"), {"Inside(square, core)": "broken"}),
    "broken-adjoins.xml": (
        ("broken relation", "(19, 20)-(22, 22)", "Adjoins(bridge, westBank)"),
        {"Adjoins(bridge, westBank)": "broken"},
    ),
    "broken-across.xml": (
        ("broken relation", "(0, 0)-(17, 39)", "Across(westBank, eastBank)"),
        {"Across(westBank, eastBank) by river": "broken"},
    ),
    "broken-sameside.xml": (
        ("broken relation", "(25, 10)-(32, 17)", "SameSide(core, westBank)"),
        {"SameSide(core, westBank) by river": "broken"},
    ),
    "broken-upstream.xml": (
        ("broken relation", "(6, 1)-(12, 6)", "Upstream(palace, core)"),
        {"Upstream(palace, core) by river": "broken"},
    ),
    "broken-farther.xml": (
        ("broken relation", "(2, 15)-(4, 18)", "Farther(palace, gate)"),
        {"Farther(palace, gate) than core": "broken"},
    ),
}


def relation_results(report: str, city: str) -> dict[str, str]:
    results = {}
    prefix = f"- {city}, city {city}: "
    for line in report.splitlines():
        if line.startswith(prefix):
            match = re.match(r"^(?P<relation>.+): (?P<result>holds|broken|not measured)(?: \(.*\))?$", line[len(prefix):])
            assert match, line
            results[match["relation"]] = match["result"]
    return results


@pytest.fixture
def picture(make_picture):
    return make_picture("plan.png", size=(64, 48))


@pytest.mark.parametrize("name", sorted(CITY))
def test_each_city_gives_its_problem_and_relations(run_check, picture, name):
    problem, not_holding = CITY[name]
    result = run_check(DEFS + [CITIES / name], references=[f"TestRiverTown:plan={picture}"])
    found = [p for p in result.problems if p["file"] == name]
    assert len(found) == len(result.problems), result.report
    if problem is None:
        assert result.status == 0, result.report
        assert found == []
    else:
        kind, cell, words = problem
        assert result.status == 1, result.report
        assert len(found) == 1, result.report
        assert (found[0]["kind"], found[0]["cell"]) == (kind, cell)
        assert words in found[0]["message"]
    expected = {relation: not_holding.get(relation, "holds") for relation in RELATIONS}
    assert relation_results(result.report, name) == expected


@pytest.mark.parametrize(
    "name, words",
    [("no-template.xml", "no template Nowhere exists"), ("wrong-kit.xml", "TestOtherKit is not the kit of TestRiverTown")],
)
def test_a_city_whose_template_or_kit_is_wrong(run_check, picture, name, words):
    result = run_check(DEFS + [CITIES / name], references=[f"TestRiverTown:plan={picture}"])
    assert result.status == 1
    assert [(p["kind"], p["file"]) for p in result.problems] == [("no kit", name)]
    assert words in result.problems[0]["message"]


def test_a_city_given_its_reference_is_drawn_beside_it(run_check, picture):
    result = run_check(DEFS + [CITIES / "clean.xml"], references=[f"TestRiverTown:plan={picture}"])
    assert result.status == 0, result.report
    assert (result.out / "clean.png").is_file()
    assert (result.out / "clean.side-by-side.png").is_file()
    assert "- city clean.xml: set beside plan" in result.report


def test_a_missing_picture_is_reported_and_the_run_goes_on(run_check):
    result = run_check(DEFS + [CITIES / "clean.xml"])
    kinds = sorted((p["kind"], p["owner"]) for p in result.problems)
    assert kinds == [("no comparison", "city clean.xml"), ("no comparison", "template TestRiverTown")]
    assert (result.out / "clean.png").is_file()
    assert not (result.out / "clean.side-by-side.png").exists()
    assert relation_results(result.report, "clean.xml") == {relation: "holds" for relation in RELATIONS}


def test_an_unreadable_picture_is_reported_and_the_run_goes_on(run_check, tmp_path):
    broken = tmp_path / "plan.png"
    broken.write_bytes(b"not a picture")
    result = run_check(DEFS + [CITIES / "clean.xml"], references=[f"TestRiverTown:plan={broken}"])
    city = [p for p in result.problems if p["owner"] == "city clean.xml"]
    assert [p["kind"] for p in city] == ["no comparison"]
    assert "cannot be read" in city[0]["message"]
    assert (result.out / "clean.png").is_file()
