# Quickstart: validating templates and kits

Testing outside the game comes first and does not replace testing in the game, which is the final check (constitution,
Source Register). Sources for each step are in [research.md](research.md) R-10 to R-13.

## Prerequisites

- Python 3.11 or later, and from the repository root `pip install -e ".[test]"`.
- The mod folders `Mantle/` and `Imperium/`, each passed to the check with `--mod`.
- RimWorld 1.7.5014's `Data/` with `Version.txt` beside it: on the maintainer's computer
  `D:\Steam\steamapps\common\RimWorld\Data`; in a cloud thread, `rimworld-1.7.5014-data.zip` from the project's files,
  unpacked outside the repository.
- `RIMWORLD_DATA_DIR` set to that `Data/` folder for the tests.
- For the river-bend town: its two reference pictures in `template-references/` in the project's files; for the
  tribal culture, the reference pictures of the three cities the maintainer chooses among candidates shown from
  above (spec FR-037), in `template-references/` in the project's files.
- For a reference city that Anno 117 presets, if it is read from the game's own data: its skeleton picture and its
  overlay on the game's `mapimage.png`, in `template-references/` in the project's files (research R-15).
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
6. **The tribal culture** (SC-010, FR-036, FR-037, FR-039): run the check on each of the three tribal readings in
   `readings/` with its reference pictures; expect no problem and a side-by-side picture the maintainer accepts,
   recorded as a checked item of `checklists/acceptance.md` (FR-029). Then
   run it on Mantle's tribal templates and kit; expect no problem, no definition of any expansion that is not marked
   (FR-015), and each template stating its tribe's attitude: neither field for the open village, `naturalEnemy` for
   the walled stronghold, `permanentEnemy` for the fortress, as `Factions_Misc.xml` lines 445, 480 and 504 set.
7. **Expansion content by mod** (FR-015): a test kit in Mantle's mod that names a Royalty definition without
   `MayRequire` is reported; the same kit in Imperium is not.
8. **A copied culture** (SC-009): copy the kit and the river-bend template under a test culture's name in a scratch
   folder, change its wall settings and one relation, and check them; the report and pictures follow the changes, and
   `git status` shows no shared file changed.
9. **Speed** (SC-003): on the maintainer's computer, checking and drawing the river-bend town against `Data/` with
   every expansion and `--mod` for `Mantle/` and `Imperium/` finishes before the game, launched there without
   `-quicktest` with Royalty, Mantle and Imperium, reaches its main menu.
10. **A preset reference read from its game's data** (SC-011, FR-041 to FR-045): its folder in
    `template-references/` holds the skeleton picture, the overlay, `objects.json` with every object's two categories
    and position, and a summary; the maintainer saw each step's picture before the next; `git status` and the
    repository's tree hold none of the game's packages or of what was read or drawn; and the check, given the two
    pictures with `--reference <name>:skeleton=<path>` and `--reference <name>:overlay=<path>`, sets them beside the
    reading as it does a screenshot.

## In the game

On the maintainer's computer, through Remote Control, in the clone at `RimWorld\Imperium` checked out at the commit
under test, which R14 moves out of `Mods` (R14 quickstart.md, Prerequisites):

1. Build `Mantle/Assemblies/Mantle.dll` from `Mantle/Source/Mantle/` against the installed game's assemblies (research
   R-2), and copy `Mantle\` and `Imperium\` from the clone into `RimWorld\Mods`.
2. Launch with `-quicktest` (`Readme.txt` lines 58-60) and `-savedatafolder=SaveData` (lines 27-38): with no mod as the
   baseline, with Mantle's mod alone and no expansion, and with Royalty, Mantle and Imperium.
3. Copy `Player.log` after each launch and compare with the baseline: neither mod adds an error or warning line about
   its definitions or assembly.

Placing templates on a map and laying out cities in the game, the final check of templates and kits, comes with R2
for the tribal culture and R15 for the Empire (spec, Assumptions).
