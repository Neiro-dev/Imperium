"""The old sample set beside a reading: its codes sorted into the reading's kinds, its findings and shares listed beside
the reading's, and the two comparisons drawn at one width (spec FR-057, SC-018; research R-27). The sample and
mapping here are made by the test itself, never the old project's."""

import json

from PIL import Image

from mantle_check import oldsample

from conftest import FIXTURES

ROADS = FIXTURES / "us2" / "roads"
KIT_FILE = ROADS / "TestRoadKit.xml"

# 40 by 40 cells, north row first: a street along row 19 from the north (z 20), a lane piece that joins nothing, a
# house on the street, and a yard that touches no house.
ROWS = []
for y in range(40):
    row = ["."] * 40
    if 17 <= y <= 21:
        row = ["S"] * 40
    ROWS.append(row)
for y in range(11, 17):
    for x in range(7, 13):
        ROWS[y][x] = "#"
for y in range(2, 4):
    for x in range(30, 36):
        ROWS[y][x] = "l"
for y in range(30, 33):
    for x in range(2, 5):
        ROWS[y][x] = "y"


def write_sample(tmp_path):
    sample = tmp_path / "old" / "sample.json"
    sample.parent.mkdir(parents=True)
    sample.write_text(json.dumps({"format": "imperium-citysample-1", "box": [0, 0, 40, 40],
                                  "rows": ["".join(r) for r in ROWS]}), encoding="utf-8")
    mapping = tmp_path / "old" / "mapping.json"
    # Ten pixels to a cell, the sample's y down the picture as its rows go.
    mapping.write_text(json.dumps({"homography": [0.1, 0, 0, 0, 0.1, 0, 0, 0], "pixelScale": 1.0}), encoding="utf-8")
    picture = tmp_path / "old" / "screenshot.png"
    Image.new("RGB", (400, 400), (90, 120, 60)).save(picture)
    return sample, mapping, picture


def test_codes_are_sorted_into_the_readings_kinds(tmp_path):
    sample_path, mapping_path, _ = write_sample(tmp_path)
    sample = oldsample.load_sample(sample_path)
    cells = oldsample.kind_cells(sample, (0, 0, 39, 39))
    assert set(cells) == {"Road", "House", "Yard"}
    assert (0, 39 - 19) in cells["Road"]
    mapping = oldsample.load_mapping(mapping_path)
    assert mapping.cell((105, 205)) == (10.5, 20.5)
    x, y = mapping.pixel((10.5, 20.5))
    assert abs(x - 105) < 1e-9 and abs(y - 205) < 1e-9


def test_the_old_samples_findings_and_shares_are_listed_beside_the_readings(run_check, tmp_path):
    sample, mapping, picture = write_sample(tmp_path)
    result = run_check([KIT_FILE, ROADS / "clean.xml"], references=[f"TestRoadTown:screenshot={picture}"],
                       crops=["TestRoadTown:screenshot=0,0,399,399"], old_sample=sample, old_mapping=mapping,
                       old_area="0,0,39,39")
    assert result.status == 0, result.report
    old = [f for f in result.findings if f["owner"] == "old sample"]
    messages = " | ".join(f["message"] for f in old)
    assert "not joined to the main network" in messages
    assert "touches no house" in messages
    assert "old sample sample.json (0, 0, 39, 39): shares of the land" in result.report
    over = Image.open(result.out / "clean.compare-over.png")
    compare = Image.open(result.out / "clean.compare.png")
    assert over.width == 2 * 1100 + 16
    assert compare.width == 3 * 900 + 2 * 16


def test_the_old_sample_needs_its_mapping(run_check, tmp_path):
    sample, _, _ = write_sample(tmp_path)
    result = run_check([ROADS / "clean.xml"], old_sample=sample)
    assert result.status == 2
