# Contract: the check command

Developers run the check outside the game (spec FR-012); every culture uses the same command (FR-033). Sources are in
[../research.md](../research.md) R-9 to R-11.

## Install and run

```text
pip install -e ".[test]"          # from the repository root
mantle-check --data <Data folder> --out <output folder> --mod <mod folder>... [--reference <name>:<label>=<picture>]...
             [--crop <name>:<label>=x0,y0,x1,y1]... [--old-sample <file> --old-mapping <file> [--old-area x0,y0,x1,y1]]
             <file>...
```

- `--data`: the game's `Data/` folder; `Version.txt` beside it must name version 1.7.
- `--out`: the folder for the report and pictures; it must not lie inside the repository (FR-028).
- `--mod`: the folder of a mod whose definitions are read, repeatable: `Mantle/`, and `Imperium/` for the Empire's.
  Each mod's `About/About.xml` gives its package identifier and what it requires (FR-015).
- `--reference`: a reference picture, by the template's `reference` name and the picture's label, such as
  `RiverBendTown:screenshot=<path>`; repeatable. JPEG, PNG and WebP are read.
- `--crop`: the part of a reference picture an area of a reading is set beside, by the same name and label and a pixel
  box, such as `RiverBendTown:render=x0,y0,x1,y1`; repeatable. Where it is left out for a picture the reading lays its
  cells over (FR-051), the box is the reading's map as the reading's `scale`, or its `ground` fit, places it on the
  picture (spec FR-053; research R-19, R-20).
- `--old-sample`, `--old-mapping`, `--old-area`: the old project's sample of the town, its mapping of the screenshot
  and the box of the sample's cells an area takes (data-model.md, The old sample; research R-27); kept outside the
  repository. Given with a reading of the river-bend town, they add the old sample's same area to its pictures and its
  findings to the report (spec FR-057, SC-018).
- `<file>`: definition files from a mod's `Defs/`, laid-out city files and readings. Every given mod's `Defs/` is read
  for names (FR-013), and a definition file belongs to the mod whose folder holds it; a laid-out city belongs to the
  mod that holds its template, and a reading to the mod that holds the template whose reference names it, or to none,
  requiring no expansion, while no template names it (FR-015). The files given are the ones checked and drawn.

## Output

- The report, on standard output and in `<out>/report.txt`: each culture the files name, by its kit's `defName`, with
  the file that holds its kit, the culture definitions it serves, its walls and its templates (FR-033, FR-034); each problem numbered, with
  its file, its template, kit, city or spec card, its part or field, its cell where it has one, and what is wrong; for
  each laid-out city, every relation with `holds`, `broken` or `not measured`; for each template and city, the reference
  pictures it was set beside or which were missing; and, last, that testing in the game is the final check and is still
  to come (FR-019, FR-020, FR-029).
- `<out>/<defName>.png` for each template, and `<out>/<city file name>.png` for each laid-out city and reading
  (FR-023, FR-025 to FR-027).
- `<out>/<defName or city file name>.side-by-side.png` when reference pictures are given (FR-025); where a reading
  holds a `scale`, the reference picture in it carries the reading's cells laid over it at the scale (a small picture enlarged by a whole number first, so that the names, numbers and legend are readable), and the report
  says that mismatches are not marked and that no picture is reported as a match (FR-020, FR-029, FR-051).
- For a reading from a picture, beside the side-by-side picture, each kind of piece's share of the reading's land,
  adding up to one, with no threshold; each piece drawn as spec FR-053 sets; and, for a reading with `ground`, each
  pair's error in cells after the fit (FR-053; research R-20, R-21).
- For a reading from a picture, its findings, places to look again, in a section of their own numbered `L1`, `L2`
  and so on, marked in orange on its pictures, with the count of road ends by class and grade, each residence plot's
  size in reference cells, and the shares; and, with the old sample, the same findings and shares for its same area
  beside them. Findings are no problems: they do not change the exit status (spec SC-019; research R-24).
- With the old sample, `<out>/<reading file name>.compare-over.png`, the new tracing laid over the screenshot's area
  beside the old sample laid over the same pixels, and `<out>/<reading file name>.compare.png`, the area's drawing
  beside the old sample's same area and the screenshot's area, each panel at the same width (spec SC-018; research
  R-27). Neither says which is better: that is the maintainer's judgment (SC-017).
- The wall circle's share and distance (FR-056) come with R2's fitting of a town to its map.
- The same inputs give the same files, byte for byte (FR-022).

## Exit status

- `0`: no problem found; a reading's findings do not count. The report still says the check in the game is to come; nothing is final (FR-020).
- `1`: problems found.
- `2`: the check could not run: `Data/` missing or not 1.7, a `--mod` folder with no `About/About.xml`, an output
  folder inside the repository, or a file that is not XML. Nothing is reported as passing.
