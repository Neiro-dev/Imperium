"""A reading from a picture: its scale, regions and uses checked, and its cells laid over the reference picture
(spec FR-019, FR-022, FR-028, FR-048, FR-049, FR-051; SC-013; contracts/laid-out-city.md, A reading)."""

import pytest
from PIL import Image

from conftest import FIXTURES

READINGS = FIXTURES / "us2" / "readings"
PICTURE_SIZE = (400, 300)
BACKGROUND = (90, 120, 60)
KIND = "wrong scale, region or use"
NOT_MARKED = "mismatches are not marked and no picture is reported as a match"

# Each reading holds one problem: the part of the reading it is reported at, and a word of its message.
ONE_PROBLEM = {
    "ppc-zero.xml": ("scale pixelsPerCell", "positive number"),
    "ppc-word.xml": ("scale pixelsPerCell", "positive number"),
    "reference-cell-negative.xml": ("scale referenceCell", "positive number"),
    "no-measured.xml": ("scale measured", "no thing"),
    "measured-no-name.xml": ("scale measured #1", "name"),
    "measured-no-rect.xml": ("scale measured door", "rect"),
    "measured-outside.xml": ("scale measured door", "outside the picture"),
    "from-outside.xml": ("parts block from", "outside the picture"),
    "use-outside.xml": ("parts block use", "Castle"),
    "use-no-basis.xml": ("parts block use", "basis"),
}


def references(make_picture, name="reference.png"):
    return [f"TestPicture:screenshot={make_picture(name, size=PICTURE_SIZE, colour=BACKGROUND)}"]


@pytest.mark.parametrize("name", sorted(ONE_PROBLEM))
def test_each_malformed_reading_is_reported_with_its_part_and_what_is_wrong(run_check, make_picture, name):
    where, words = ONE_PROBLEM[name]
    result = run_check([READINGS / name], references=references(make_picture))
    assert result.status == 1, result.report
    assert result.kinds() == [KIND], result.report
    problem = result.problems[0]
    assert problem["file"] == name
    assert problem["where"] == where
    assert words in problem["message"], problem["message"]


def test_a_clean_reading_with_a_scale_gives_no_problem(run_check, make_picture):
    result = run_check([READINGS / "clean.xml"], references=references(make_picture))
    assert result.status == 0, result.report
    assert result.problems == []
    assert NOT_MARKED in result.report


def test_a_region_outside_the_picture_is_reported_only_where_the_picture_is_given(run_check):
    result = run_check([READINGS / "measured-outside.xml"])
    assert result.problems == [], result.report


def test_a_reading_without_a_scale_is_drawn_and_reported_as_before(run_check, make_picture):
    result = run_check([READINGS / "no-scale.xml"], references=references(make_picture))
    assert result.status == 0, result.report
    assert result.problems == []
    assert NOT_MARKED not in result.report
    side = Image.open(result.out / "no-scale.side-by-side.png").convert("RGB")
    drawing = Image.open(result.out / "no-scale.png")
    # The reference picture is set beside the drawing as it is, with nothing laid over it.
    assert side.getpixel(placed(drawing, side, 75, 225)) == BACKGROUND


def placed(drawing, side, x, y):
    """Where a pixel of the reference picture lands in the side-by-side picture, which sets it at the drawing's height."""
    factor = drawing.height / PICTURE_SIZE[1]
    return (drawing.width + 16 + round(x * factor), round(y * factor))


def test_a_known_scale_puts_a_known_cell_at_a_known_pixel_of_the_reference_picture(run_check, make_picture):
    result = run_check([READINGS / "clean.xml"], references=references(make_picture))
    drawing = Image.open(result.out / "clean.png")
    side = Image.open(result.out / "clean.side-by-side.png").convert("RGB")
    # 20 pixels a cell of the reference game and 4 RimWorld cells to it give 5 pixels a RimWorld cell, the reading's
    # cell (0, 0) at the picture's lower left corner: the part's cells (10, 10) to (19, 19) fill the pixels
    # x 50 to 99 and y 200 to 249 of the 400×300 picture.
    inside_part = side.getpixel(placed(drawing, side, 75, 225))
    inside_soil = side.getpixel(placed(drawing, side, 155, 272))
    outside = side.getpixel(placed(drawing, side, 350, 50))
    just_right = side.getpixel(placed(drawing, side, 110, 225))
    assert outside == BACKGROUND
    assert inside_soil != BACKGROUND
    assert inside_part != inside_soil
    assert inside_part[2] > inside_part[1]  # the parts are blue
    assert just_right == side.getpixel(placed(drawing, side, 120, 225))  # soil beside the part, not part


def test_the_same_inputs_give_identical_pictures_and_reports(run_check, make_picture, tmp_path):
    first = run_check([READINGS / "clean.xml"], references=references(make_picture), out=tmp_path / "one")
    second = run_check([READINGS / "clean.xml"], references=references(make_picture), out=tmp_path / "two")
    assert first.report == second.report
    for name in ("clean.png", "clean.side-by-side.png", "report.txt"):
        assert (first.out / name).read_bytes() == (second.out / name).read_bytes(), name
