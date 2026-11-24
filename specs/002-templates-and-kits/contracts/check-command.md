# Contract: the check command

Developers run the check outside the game (spec FR-012); every culture uses the same command (FR-033). Sources are in
[../research.md](../research.md) R-9 to R-11.

## Install and run

```text
pip install -e ".[test]"          # from the repository root
mantle-check --data <Data folder> --out <output folder> --mod <mod folder>... [--reference <name>:<label>=<picture>]...
             <file>...
```

- `--data`: the game's `Data/` folder; `Version.txt` beside it must name version 1.7.
- `--out`: the folder for the report and pictures; it must not lie inside the repository (FR-028).
- `--mod`: the folder of a mod whose definitions are read, repeatable: `Mantle/`, and `Imperium/` for the Empire's.
  Each mod's `About/About.xml` gives its package identifier and what it requires (FR-015).
- `--reference`: a reference picture, by the template's `reference` name and the picture's label, such as
  `RiverBendTown:screenshot=<path>`; repeatable. JPEG, PNG and WebP are read.
- `<file>`: definition files from a mod's `Defs/`, laid-out city files and readings. Every given mod's `Defs/` is read
  for names (FR-013), and a definition file belongs to the mod whose folder holds it; a laid-out city belongs to the
  mod that holds its template, and a reading to the mod that holds the template whose reference names it, or to none,
  requiring no expansion, while no template names it (FR-015). The files given are the ones checked and drawn.

## Output

- The report, on standard output and in `<out>/report.txt`: each culture the files name, by its kit's `defName`, with
  the file that holds its kit, its word list, its walls and its templates (FR-033, FR-034); each problem numbered, with
  its file, its template, kit, city or spec card, its part or field, its cell where it has one, and what is wrong; for
  each laid-out city, every relation with `holds`, `broken` or `not measured`; for each template and city, the reference
  pictures it was set beside or which were missing; and, last, that testing in the game is the final check and is still
  to come (FR-019, FR-020, FR-029).
- `<out>/<defName>.png` for each template, and `<out>/<city file name>.png` for each laid-out city and reading
  (FR-023, FR-025 to FR-027).
- `<out>/<defName or city file name>.side-by-side.png` when reference pictures are given (FR-025).
- The same inputs give the same files, byte for byte (FR-022).

## Exit status

- `0`: no problem found. The report still says the check in the game is to come; nothing is final (FR-020).
- `1`: problems found.
- `2`: the check could not run: `Data/` missing or not 1.7, a `--mod` folder with no `About/About.xml`, an output
  folder inside the repository, or a file that is not XML. Nothing is reported as passing.
