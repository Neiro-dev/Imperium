# Quickstart: validating the mod foundation

Validation runs in the game on the maintainer's computer; the cloud can only check the file. Sources for each step
are in [research.md](research.md) R-10.

## Prerequisites

- RimWorld 1.7.5014 with Royalty, Ideology, Biotech, Anomaly and Odyssey at `D:\Steam\steamapps\common\RimWorld`.
- `Mods\Imperium` is the repository's clone, pulled to the commit under test.
- RimBridgeServer 2.4.0 or later in `Mods`, and GABS configured for this install (RimBridgeServer `README.md`,
  Installation).
- The log is `output_log.txt` in the install's `_Data` folder (`Readme.txt` line 21).

## Checks in the cloud

1. `About/About.xml` is well-formed XML with the declaration the official files use.
2. The package identifier meets the format in [data-model.md](data-model.md).

## Checks in the game

Each launch below runs once without Imperium as the baseline and once with it; a launch passes when Imperium's adds
no error or warning line to the baseline's log (spec, Clarifications).

1. **Mod list** (spec US1.1): Imperium is listed by its name. Expect no warning on it with Core and Royalty on
   (`rimworld/list_mods`, `rimworld/get_mod_configuration_status`).
2. **New game** (US1.2, SC-001): Core, Royalty and Imperium on; launch with `-quicktest` (`Readme.txt` lines 58-60).
3. **Saved game** (US1.3, SC-001): save that game and load it again (`rimworld/load_game_ready`).
4. **Royalty off** (US2, SC-002): turn Royalty off (`rimworld/set_mod_enabled`); Imperium shows a missing requirement
   for Royalty and for nothing else.
5. **Load order first** (FR-004, research R-6): with all expansions on, Imperium is after Odyssey, and no log line
   concerns `forceLoadAfter`. If either fails, switch to `loadAfter` (R-6) and repeat from step 1.
6. **Combinations** (US3, SC-003): each of the 16 combinations of Ideology, Biotech, Anomaly and Odyssey added to
   Core and Royalty, none included; each launch passes against its baseline, with Imperium after every active
   expansion and no load-order warning.
7. **Out of order** (edge case): move Imperium above an expansion (`rimworld/reorder_mod`); the game refuses the
   move or warns that Imperium must load after it.
8. **Mod set changed** (edge case): load the save from step 3 with Imperium off; the game shows its mods-mismatch
   warning and the save loads.
9. **Community content** (FR-008, FR-009, SC-004): nothing shown for Imperium names Ludeon as its maker or places it
   among the official expansions; `README.md` in the mod's folder holds the EULA's disclaimer.
