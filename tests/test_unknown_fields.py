"""Every field a form does not hold is reported, never dropped (spec FR-014; research R-25)."""

from conftest import FIXTURES, NO_EXPANSION

US1 = FIXTURES / "us1"
READINGS = FIXTURES / "us2" / "readings"


def test_a_misspelled_field_of_a_template_is_reported_with_its_name(run_check):
    result = run_check([US1 / "field-misspelled.xml"], mods=[NO_EXPANSION])
    assert result.status == 1, result.report
    assert result.kinds() == ["wrong form"], result.report
    problem = result.problems[0]
    assert problem["file"] == "field-misspelled.xml"
    assert "<alowedBiomes>" in problem["message"]


def test_an_unknown_attribute_is_reported_with_its_name(run_check):
    result = run_check([US1 / "field-unknown-attribute.xml"], mods=[NO_EXPANSION])
    assert result.kinds() == ["wrong form"], result.report
    assert "Colour" in result.problems[0]["message"]
    assert result.problems[0]["where"] == "terrainShape features"


def test_an_element_marked_to_be_ignored_is_not_reported(run_check):
    result = run_check([US1 / "field-ignored.xml"], mods=[NO_EXPANSION])
    assert result.status == 0, result.report
    assert result.problems == []


def test_a_misspelled_field_of_a_reading_is_reported(run_check):
    result = run_check([READINGS / "field-misspelled.xml"])
    assert result.kinds() == ["wrong form"], result.report
    assert result.problems[0]["where"] == "parts block"
    assert "<houshold>" in result.problems[0]["message"]
