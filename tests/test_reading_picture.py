"""The drawing of a reading from a picture: households in their colours with plot, house and yard lines, findings in
orange, a legend with counts, a pixel ruler on the reference picture, all panels at one width (spec FR-053;
contracts/check-command.md; research R-24)."""

from PIL import Image

from mantle_check.pictures import (
    FINDING, INK, KIND_COLOURS, KindPainter, Piece, household_colour, legend_counts, same_width, with_ruler,
)

from conftest import FIXTURES

ROADS = FIXTURES / "us2" / "roads"
KIT_FILE = ROADS / "TestRoadKit.xml"


def test_a_household_is_drawn_in_its_colour_with_its_plot_outlined_thick():
    plot = Piece({(x, z) for x in range(2, 8) for z in range(2, 8)}, "Plot", "p", "west")
    house = Piece({(x, z) for x in range(3, 6) for z in range(3, 6)}, "House", "h", "west")
    painter = KindPainter((10, 10), 10)
    image = painter.draw([plot, house], "test", True, [("L1", (0, 0, 0, 0), FINDING)])
    colour = household_colour("west")
    left, top = painter.corner(2, 8)
    assert image.getpixel((int(left) + 1, int(top) + 20)) == colour
    house_fill = tuple((c + 2 * b) // 3 for c, b in zip(KIND_COLOURS["House"], colour))
    hx, hy = painter.corner(4.5, 4.5)
    assert image.getpixel((int(hx), int(hy))) == house_fill
    fx, fy = painter.corner(0, 1)
    assert image.getpixel((int(fx), int(fy))) == FINDING


def test_the_legend_counts_pieces_by_kind():
    pieces = [Piece({(0, 0)}, "House"), Piece({(1, 1)}, "House"), Piece({(2, 2)}, "Yard")]
    legend = legend_counts(pieces, [])
    assert legend.height == 22 + 16 * 2 + 8


def test_the_reference_picture_carries_a_ruler_of_its_pixels():
    picture = Image.new("RGB", (200, 100), (90, 120, 60))
    ruled = with_ruler(picture, (0, 0, 199, 99), "screenshot")
    zoom = ruled.width - 34
    assert ruled.getpixel((34 + 50 * zoom // 200, 30)) == INK


def test_panels_are_set_side_by_side_at_one_width():
    out = same_width([Image.new("RGB", (100, 50)), Image.new("RGB", (300, 300))], 200)
    assert out.size == (2 * 200 + 16, 200)


def test_a_reading_is_drawn_beside_its_picture(run_check, tmp_path):
    picture = tmp_path / "screenshot.png"
    Image.new("RGB", (400, 400), (90, 120, 60)).save(picture)
    result = run_check([KIT_FILE, ROADS / "clean.xml"], references=[f"TestRoadTown:screenshot={picture}"])
    assert result.status == 0, result.report
    assert (result.out / "clean.png").is_file()
    side = Image.open(result.out / "clean.side-by-side.png")
    assert side.width == 3 * 900 + 2 * 16
