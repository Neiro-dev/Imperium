"""Roads and households of a reading: places to look again, never problems (spec FR-054, FR-055, SC-019; research
R-21, R-24)."""

import xml.etree.ElementTree as ET

import pytest

from mantle_check import roads
from mantle_check.forms import read_city, read_kit

from conftest import FIXTURES

ROADS = FIXTURES / "us2" / "roads"
KIT_FILE = ROADS / "TestRoadKit.xml"

# Each variant of the clean reading and a word of the finding it must give, with the piece it is found at.
ONE_FINDING = {
    "network-in-pieces": ("parts plaza", "joins no road, gate or bridge"),
    "road-on-house": ("parts lane", "lies on a house or plot cell"),
    "dangling": ("parts spur end at (34,4)", "a dangling road"),
    "no-way-in": ("parts street", "no region where the way in"),
    "no-leads-to": ("parts street", "names no building, household or plaza"),
    "yard-outside-plot": ("parts westYard", "outside household west's plot"),
    "plot-too-large": ("household west", "over one and a half"),
    "no-plot": ("household east", "has no plot"),
    "off-eight-directions": ("parts lane", "off the eight directions"),
    "wrong-grade": ("parts street", "Avenue is not one of the kit's grades"),
    "yard-cut-off": ("parts looseYard", "touches no house"),
    "route-line-is-no-road": ("parts plaza", "joins no road, gate or bridge"),
}


def kit():
    node = next(n for n in ET.parse(KIT_FILE).getroot() if n.tag == "Mantle.KitDef")
    return read_kit(node, KIT_FILE.name)[0]


def findings(name: str):
    city, problems = read_city(ET.parse(ROADS / f"{name}.xml").getroot(), f"{name}.xml")
    assert problems == []
    return roads.read(city, kit())


def test_the_clean_reading_has_no_place_to_look_again():
    found = findings("clean")
    assert found.findings == []
    assert dict(found.ends) == {("Street", "through"): 2, ("Lane", "through"): 2}


@pytest.mark.parametrize("name", sorted(ONE_FINDING))
def test_each_variant_gives_its_finding_with_its_cells(name):
    where, words = ONE_FINDING[name]
    found = findings(name).findings
    matching = [f for f in found if f.where == where and words in f.message]
    assert matching, [(f.where, f.message) for f in found]
    assert all(f.cell is not None for f in matching)


def test_a_route_line_is_no_road():
    found = findings("route-line-is-no-road")
    assert all(f.where != "parts path" for f in found.findings)
    assert ("-", "through") not in found.ends


def test_the_shares_add_up_to_one_and_plots_are_measured_in_estates():
    found = findings("clean")
    assert abs(sum(share for _, share in found.shares) - 1) < 1e-9
    assert found.plot_sizes == ["east: 100 cells, 11.1 reference cells, 1.23 estates of 3×3",
                                "west: 100 cells, 11.1 reference cells, 1.23 estates of 3×3"]


def test_findings_are_listed_apart_from_problems_and_leave_the_exit_status(run_check, make_picture):
    references = [f"TestRoadTown:screenshot={make_picture(size=(400, 400))}"]
    clean = run_check([KIT_FILE, ROADS / "clean.xml"], references=references)
    assert clean.status == 0, clean.report
    assert clean.findings == []
    assert "TestRoadTown" in clean.report and "road ends by grade and class: Lane through 2, Street through 2" in clean.report

    result = run_check([KIT_FILE, ROADS / "dangling.xml"], references=references)
    assert result.status == 0, result.report
    assert result.problems == []
    wheres = [f["where"] for f in result.findings]
    assert "parts spur end at (34,4)" in wheres, result.report
    assert all(f["number"].startswith("L") for f in result.findings)
