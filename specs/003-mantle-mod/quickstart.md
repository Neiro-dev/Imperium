# Quickstart: validating Mantle as a mod of its own

Validation runs outside the game first, in the cloud, and then in the game on the maintainer's computer, which is the
final check (constitution, Source Register). Sources for each step are in [research.md](research.md) R-9.

## Prerequisites

- RimWorld 1.7.5014 with Royalty, Ideology, Biotech, Anomaly and Odyssey at `D:\Steam\steamapps\common\RimWorld`.
- The repository's clone at `D:\Steam\steamapps\common\RimWorld\Imperium`, outside `Mods`, on the commit under test.
  The install's `CLAUDE.md` imports `@Imperium/.specify/memory/constitution.md`.
- `Mods\Imperium` and `Mods\Mantle` are copies of the clone's `Imperium\` and `Mantle\` folders, made again whenever
  the commit under test changes (research R-9).
- RimBridgeServer 2.4.0 or later in `Mods`, and GABS configured for this install, as for R1 (R1 quickstart).
- Every launch adds `-savedatafolder=SaveData` (`Readme.txt` lines 27-38). The log is `Player.log` in the `Logs`
  folder of the default save data folder; copy it after each launch and compare the copies (R1 research R-10).

## Checks outside the game

These come first (constitution, Source Register) and do not replace the checks in the game.

1. `Imperium/About/About.xml` and `Mantle/About/About.xml` are well-formed XML and begin with the byte order mark and
   the declaration the official files in `Data/` use.
2. `Mantle/About/About.xml` holds exactly the fields and values of [data-model.md](data-model.md), and every package
   in its `forceLoadAfter` is one whose `About/About.xml` is in `Data/`.
3. Both package identifiers meet the format in data-model.md and differ.
4. No load-order field in either file names a package that is not Ludeon's, and each mod folder's `README.md` states
   its place and holds the EULA's disclaimer.
5. `Imperium/` and `Mantle/` hold only the files data-model.md lists for them, each `LICENSE` copy is identical to the
   root's, neither folder is inside the other, and the root holds no `About/`.

## Checks in the game

Each launch below runs once without Mantle as the baseline and once with it; a launch passes when Mantle's adds no
error or warning line to the baseline's log, other than the game's report that Mantle loaded no content (spec FR-005).

1. **Mod roots** (US3): Mantle and Imperium are listed by their names, as two mods; `rimworld/get_mod_configuration_status`
   shows that the game loads them from `Mods\Mantle` and `Mods\Imperium` (RimBridgeServer `README.md` line 129).
2. **Base game alone** (US1.2, US1.3, SC-001, SC-002): Core and Mantle on, no expansion; launch with `-quicktest`
   (`Readme.txt` lines 58-60). Mantle shows no missing requirement.
3. **Saved game** (US1.4, SC-001): save that game and load it again (`rimworld/load_game_ready`).
4. **Combinations** (US2.1, SC-002, SC-003): each of the 32 combinations of Royalty, Ideology, Biotech, Anomaly and
   Odyssey added to Core, none included; each launch passes against its baseline, with Mantle after every active
   expansion, no missing requirement and no load-order warning.
5. **Out of order** (edge case): move Mantle above an expansion (`rimworld/reorder_mod`); the game refuses the move or
   warns that Mantle must load after it.
6. **Mod set changed** (edge case): load the save from check 3 with Mantle off; the game shows its mods-mismatch
   warning and the save loads.
7. **Community content** (FR-008, FR-009, SC-004): nothing shown for Mantle names Ludeon as its maker or places it
   among the official expansions; `README.md` in Mantle's folder holds the EULA's disclaimer.
8. **Ahead of ordinary mods** (US2.2, SC-005): with all expansions on, place Mantle directly after Odyssey and ahead of
   RimBridgeServer, an ordinary mod; the mod list shows no load-order warning and the launch passes against its
   baseline. Record where the game puts Mantle when it is turned on (`rimworld/set_mod_enabled`).
9. **Imperium from its own folder** (US3.2, SC-006, FR-016): R1's checks 2 and 4 again: Core, Royalty and Imperium on
   start a new game that passes against Core and Royalty alone; with Royalty off, Imperium shows a missing requirement
   for Royalty and for nothing else.
10. **Both mods** (US3.3, SC-006): Core, Royalty, Imperium and Mantle on, with Mantle before Imperium and then after
    it; each launch passes against Core and Royalty alone, other than the two reports that Imperium and Mantle loaded
    no content, with no load-order warning for either.
