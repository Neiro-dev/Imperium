"""User Story 4: each spec card of a kit's block library checked (spec, User Story 4, scenarios 1-2; FR-007)."""

from conftest import FIXTURES

KIT = FIXTURES / "us4" / "TestBlockKit.xml"


def test_spec_cards(run_check):
    result = run_check([KIT])
    assert result.status == 1, result.report
    found = sorted((p["where"], p["kind"], p["cell"]) for p in result.problems)
    assert found == [
        ("spec card pastItsPlot room porch", "outside the map", "(0, 6)-(7, 7)"),
        ("spec card pastItsPlot things Wall #1", "outside the map", "(9, 2)"),
        ("spec card unknownFloor terrain", "unknown definition", "(2, 2)-(3, 3)"),
    ]
    assert all("past its plot" in p["message"] for p in result.problems if p["kind"] == "outside the map")
    assert not [p for p in result.problems if "sound" in p["where"]]
