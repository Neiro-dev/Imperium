# Contract: the check command

Developers run the check outside the game (spec FR-012); every culture uses the same command (FR-033). Sources are in
[../research.md](../research.md) R-9 to R-11.

## Install and run

```text
pip install -e ".[test]"          # from the repository root
mantle-check --data <Data folder> --out <output folder> [--reference <name>:<label>=<picture>]... <file>...
```

- `--data`: the game's `Data/` folder; `Version.txt` beside it must name version 1.7.
- `--out`: the folder for the report and pictures; it must not lie inside the repository (FR-028).
- `--reference`: a reference picture, by the template's `reference` name and the picture's label, such as
  `RiverBendTown:screenshot=<path>`; repeatable. JPEG, PNG and WebP are read.
- `<file>`: definition files from `Defs/` and laid-out city files. Imperium's own `Defs/` is always read for names
  (FR-013); the files given are the ones checked and drawn.

## Output

- The report, on standard output and in `<out>/report.txt`: each problem numbered, with its file, its template, kit,
  city or spec card, its part or field, its cell where it has one, and what is wrong; for each laid-out city, every
  relation with `holds`, `broken` or `not measured`; for each template and city, the reference pictures it was set
  beside or which were missing; and, last, that testing in the game is the final check and is still to come (FR-019,
  FR-020, FR-029).
- `<out>/<defName>.png` for each template and spec card, and `<out>/<city file name>.png` for each laid-out city
  (FR-023 to FR-027).
- `<out>/<defName or city file name>.side-by-side.png` when reference pictures are given (FR-025).
- The same inputs give the same files, byte for byte (FR-022).

## Exit status

- `0`: no problem found. The report still says the check in the game is to come; nothing is final (FR-020).
- `1`: problems found.
- `2`: the check could not run: `Data/` missing or not 1.7, an output folder inside the repository, or a file that is
  not XML. Nothing is reported as passing.
