# Quickstart: validating templates and kits

Testing outside the game comes first and does not replace testing in the game, which is the final check (constitution,
Source Register). Sources for each step are in [research.md](research.md) R-10 to R-13.

## Prerequisites

- Python 3.11 or later, and from the root of Mantle's repository `pip install -e ".[test]"`.
- The folders of Mantle's mod and of Imperium, each passed to the check with `--mod`.
- RimWorld 1.7.5014's `Data/` with `Version.txt` beside it: on the maintainer's computer
  `D:\Steam\steamapps\common\RimWorld\Data`; in a cloud thread, `rimworld-1.7.5014-data.zip` from the project's files,
  unpacked outside the repository.
- `RIMWORLD_DATA_DIR` set to that `Data/` folder for the tests.
- For the river-bend town: its two reference pictures in `template-references/` in the project's files; for the
  tribal culture, the reference pictures of the city the maintainer chose, kept there too.
- An output folder outside the repository.

## Outside the game

1. **Tests** (spec SC-001, SC-002, SC-004, SC-009): `pytest`. The test templates, kits and laid-out cities in
   `tests/fixtures/` each hold one kind of problem from [data-model.md](data-model.md), What the check reports, or
   none; each report lists exactly the problems its file holds, and every report ends with the statement that the
   check in the game is still to come.
2. **Same inputs, same files** (FR-022): run the check twice on the same files into two folders and compare them byte
   for byte.
3. **Data missing or wrong** (spec, Edge Cases): run with `--data` pointing at an empty folder, then at a copy whose
   `Version.txt` names another version; both exit with status 2 and report nothing as passing.
4. **Output inside the repository** (FR-028): run with `--out` inside the repository; it exits with status 2.
5. **The river-bend town** (SC-007, SC-008, FR-031): run the check on Imperium's template and kit files with
   `--reference RiverBendTown:screenshot=<screenshot>` and `--reference RiverBendTown:render=<render>`. Expect no
   problem, and `<out>/RiverBendTown.side-by-side.png` with the template's picture beside both references. Each part
   of the skeleton is named in the picture and can be found in each reference. Give the picture to the maintainer in
   the project's files, not in the pull request, since it holds the screenshot.
6. **The tribal culture** (SC-010, FR-036, FR-037): run the check on the tribal reading in `readings/` with its
   reference pictures; expect no problem and a side-by-side picture the maintainer accepts. Then run it on Mantle's
   tribal template and kit; expect no problem, and no definition of any expansion that is not marked (FR-015).
7. **Expansion content by mod** (FR-015): a test kit in Mantle's mod that names a Royalty definition without
   `MayRequire` is reported; the same kit in Imperium is not.
8. **A copied culture** (SC-009): copy the kit and the river-bend template under a test culture's name in a scratch
   folder, change its wall settings and one relation, and check them; the report and pictures follow the changes, and
   `git status` shows no shared file changed.
9. **Speed** (SC-003): checking and drawing the river-bend town finishes before the game, started on the same
   computer, reaches its main menu.

## In the game

On the maintainer's computer, through Remote Control, with Mantle's mod and `Mods\Imperium` pulled to the commits
under test:

1. Build `Assemblies/Mantle.dll` from Mantle's `Source/Mantle/` against the installed game's assemblies (research R-2).
2. Launch with `-quicktest` (`Readme.txt` lines 58-60) and `-savedatafolder=SaveData` (lines 27-38): with no mod as the
   baseline, with Mantle's mod alone and no expansion, and with Royalty, Mantle and Imperium.
3. Copy `Player.log` after each launch and compare with the baseline: neither mod adds an error or warning line about
   its definitions or assembly.

Placing templates on a map and laying out cities in the game, the final check of templates and kits, comes with R2
for the tribal culture and R15 for the Empire (spec, Assumptions).
