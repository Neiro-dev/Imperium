"""Writes the test readings of tests/test_roads.py: one clean reading and variants, each holding one road or household
finding (spec FR-054, FR-055; research R-21, R-24). Run it from this folder to write them again; they are kept
written so that the tests read plain files."""

from pathlib import Path

HERE = Path(__file__).parent

STREET = ("street", "Road", "<grade>Street</grade><line><li>(0,20)</li><li>(39,20)</li></line><leadsTo>westHouse</leadsTo>"
          "<wayInFrom><li>(100,150,110,160)</li></wayInFrom>")
LANE = ("lane", "Road", "<grade>Lane</grade><line><li>(20,22)</li><li>(20,39)</li></line><leadsTo>eastHouse</leadsTo>"
        "<wayInFrom><li>(200,100,210,110)</li></wayInFrom>")
CLEAN = [
    STREET,
    LANE,
    ("westPlot", "Plot", "<household>west</household><rects><li>(5,23,14,32)</li></rects>"),
    ("westHouse", "House", "<household>west</household><rects><li>(7,23,12,28)</li></rects>"
     "<use>Housing</use><basis>A red roof facing the street.</basis>"),
    ("westYard", "Yard", "<household>west</household><rects><li>(7,29,12,31)</li></rects>"),
    ("eastPlot", "Plot", "<household>east</household><rects><li>(22,23,31,32)</li></rects>"),
    ("eastHouse", "House", "<household>east</household><rects><li>(22,23,27,28)</li></rects>"
     "<use>Housing</use><basis>A red roof facing the lane.</basis>"),
    ("eastYard", "Yard", "<household>east</household><rects><li>(28,23,31,28)</li></rects>"),
]


def replace(pieces, name, new):
    return [new if p[0] == name else p for p in pieces]


def without(pieces, name):
    return [p for p in pieces if p[0] != name]


VARIANTS = {
    "clean": CLEAN,
    "network-in-pieces": CLEAN + [("plaza", "Plaza", "<rects><li>(35,32,37,35)</li></rects>")],
    "road-on-house": replace(CLEAN, "lane", ("lane", "Road", LANE[2].replace("(20,22)", "(23,22)").replace("(20,39)", "(23,39)"))),
    "dangling": CLEAN + [("spur", "Road", "<grade>Lane</grade><line><li>(34,4)</li><li>(38,4)</li></line>"
                          "<leadsTo>eastHouse</leadsTo><uncertain>true</uncertain><because>Faint in the picture.</because>")],
    "no-way-in": replace(CLEAN, "street", ("street", "Road", STREET[2].replace("<wayInFrom><li>(100,150,110,160)</li></wayInFrom>", ""))),
    "no-leads-to": replace(CLEAN, "street", ("street", "Road", STREET[2].replace("<leadsTo>westHouse</leadsTo>", ""))),
    "yard-outside-plot": replace(CLEAN, "westYard", ("westYard", "Yard", "<household>west</household><rects><li>(7,29,12,34)</li></rects>")),
    "plot-too-large": replace(CLEAN, "westPlot", ("westPlot", "Plot", "<household>west</household><rects><li>(4,23,18,37)</li></rects>")),
    "no-plot": without(CLEAN, "eastPlot"),
    "off-eight-directions": replace(CLEAN, "lane", ("lane", "Road", LANE[2].replace("(20,39)", "(23,39)"))),
    "wrong-grade": replace(CLEAN, "street", ("street", "Road", STREET[2].replace("<grade>Street</grade>", "<grade>Avenue</grade>"))),
    "yard-cut-off": CLEAN + [("looseYard", "Yard", "<household>west</household><rects><li>(8,35,10,36)</li></rects>")],
    "route-line-is-no-road": CLEAN + [("plaza", "Plaza", "<rects><li>(35,32,37,35)</li></rects>"),
                                      ("path", "RouteLine", "<line><li>(36,23)</li><li>(36,31)</li></line>")],
}


def write(name, pieces):
    rows = "\n".join(f"    <li><name>{n}</name><kind>{k}</kind>{body}<from><li>(10,10,20,20)</li></from></li>"
                     for n, k, body in pieces)
    text = f"""<?xml version="1.0" encoding="utf-8"?>
<LaidOutCity>
  <reference>TestRoadTown</reference>
  <size>(40,40)</size>
  <scale>
    <pixelsPerCell>9</pixelsPerCell>
    <referenceCell>3</referenceCell>
    <measured><li><name>figure</name><rect>(5,5,7,7)</rect></li></measured>
  </scale>
  <terrain>
    <Soil><rects><li>(0,0,39,39)</li></rects></Soil>
  </terrain>
  <roofs />
  <parts>
{rows}
  </parts>
</LaidOutCity>
"""
    (HERE / f"{name}.xml").write_text(text, encoding="utf-8", newline="\n")


if __name__ == "__main__":
    for name, pieces in VARIANTS.items():
        write(name, pieces)
