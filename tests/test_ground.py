"""The ground of a picture in perspective: a projective fit from four or more ground pairs, each pair's error, and the
tracing laid over the picture where the fit puts it (spec FR-052; research R-20)."""

import math

import pytest
from PIL import Image, ImageDraw

from mantle_check.ground import apply, fit, ground

# A known perspective: cell (x, z) to pixel, the far rows narrower and higher up, as in an oblique screenshot.
KNOWN = [[6.0, 1.5, 40.0], [0.0, -4.0, 260.0], [0.0, 0.004, 1.0]]


def to_pixel(cell):
    return apply(KNOWN, cell)


def test_four_pairs_fix_the_mapping_both_ways():
    cells = [(0, 0), (40, 0), (40, 40), (0, 40)]
    fitted = ground([(to_pixel(c), c) for c in cells])
    for cell in [(10, 10), (33, 5), (20, 38)]:
        back = fitted.cell(to_pixel(cell))
        assert math.dist(back, cell) < 1e-6
        assert math.dist(fitted.pixel(cell), to_pixel(cell)) < 1e-6
    assert max(fitted.errors) < 1e-6


def test_each_pair_error_is_reported_in_cells_with_no_threshold():
    cells = [(0, 0), (40, 0), (40, 40), (0, 40), (20, 20)]
    pairs = [(to_pixel(c), c) for c in cells]
    (px, py), cell = pairs[4]
    pairs[4] = ((px + 9, py), cell)
    fitted = ground(pairs)
    assert len(fitted.errors) == 5
    assert max(fitted.errors) > 0.1


def test_three_pairs_on_one_line_are_refused():
    with pytest.raises(ValueError):
        fit([(0, 0), (1, 1), (2, 2), (3, 3)], [(0, 0), (1, 1), (2, 2), (3, 3)])


READING = """<?xml version="1.0" encoding="utf-8"?>
<LaidOutCity>
  <reference>TestPerspective</reference>
  <size>(40,40)</size>
  <scale>
    <pixelsPerCell>4</pixelsPerCell>
    <referenceCell>3</referenceCell>
    <measured><li><name>figure</name><rect>(100,100,103,103)</rect></li></measured>
  </scale>
  <ground>
    <pairs>
{pairs}
    </pairs>
  </ground>
  <terrain>
    <Soil><rects><li>(0,0,39,39)</li></rects></Soil>
  </terrain>
  <roofs />
  <parts>
    <li><name>house</name><kind>House</kind><rects><li>(10,10,19,19)</li></rects><from><li>(100,100,150,150)</li></from>
      <use>Housing</use><basis>A roof.</basis></li>
    <li><name>road</name><kind>Road</kind><grade>Lane</grade><width>3</width><line><li>(0,9)</li><li>(39,9)</li></line>
      <leadsTo>house</leadsTo><wayInFrom><li>(100,150,110,160)</li></wayInFrom><from><li>(40,150,300,180)</li></from></li>
  </parts>
</LaidOutCity>
"""


def test_the_tracing_is_laid_over_the_picture_where_the_fit_puts_it(run_check, tmp_path):
    picture = Image.new("RGB", (320, 300), (20, 20, 20))
    draw = ImageDraw.Draw(picture)
    corners = [to_pixel(c) for c in [(10, 10), (20, 10), (20, 20), (10, 20)]]
    draw.polygon(corners, fill=(200, 60, 40))
    path = tmp_path / "pictures" / "perspective.png"
    path.parent.mkdir(parents=True)
    picture.save(path)
    pairs = "\n".join(
        f"      <li><pixel>({to_pixel(c)[0]:.3f},{to_pixel(c)[1]:.3f})</pixel><cell>({c[0]},{c[1]})</cell></li>"
        for c in [(0, 0), (40, 0), (40, 40), (0, 40)]
    )
    reading = tmp_path / "Perspective.xml"
    reading.write_text(READING.format(pairs=pairs), encoding="utf-8")
    result = run_check([reading], references=[f"TestPerspective:screenshot={path}"])
    assert result.status == 0, result.report
    assert "ground pair #1 lies 0.00 cells from its cell corner" in result.report
    side = Image.open(result.out / "Perspective.side-by-side.png")
    assert side.width == 3 * 900 + 2 * 16
