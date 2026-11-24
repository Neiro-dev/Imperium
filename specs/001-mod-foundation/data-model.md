# Data Model: Mod foundation

R1 has one piece of data: the mod's metadata in `About/About.xml`, which the game reads to list, order and load
Imperium. Its values and their sources are in [research.md](research.md); the contract other mods and the game rely
on is in [contracts/about-xml.md](contracts/about-xml.md).

## Mod metadata (`About/About.xml`, one `ModMetaData` element)

| Field | Value | Rule | Source |
|-------|-------|------|--------|
| `name` | `Imperium` | required | spec, Assumptions; `ModUpdating.txt` line 223 |
| `author` | `Neiro-dev` | the maker | R-4 |
| `packageId` | `Neiro.RimWorld.Imperium` | letters, digits and dots; at least one dot; no repeated, leading or trailing dot; 60 characters or fewer; no "Ludeon"; never changes once released | R-3; `ModUpdating.txt` lines 231-237; spec FR-010 |
| `supportedVersions` | `1.7` | `X.Y` entries | R-5; `ModUpdating.txt` line 254 |
| `modDependencies` | one Royalty dependency (below) | each entry has `packageId`, `displayName`, and `downloadUrl` or `steamWorkshopUrl` | R-7; `ModUpdating.txt` lines 266-275 |
| `forceLoadAfter` | `Ludeon.RimWorld`, `Ludeon.RimWorld.Royalty`, `Ludeon.RimWorld.Ideology`, `Ludeon.RimWorld.Biotech`, `Ludeon.RimWorld.Anomaly`, `Ludeon.RimWorld.Odyssey` | package identifiers | R-6 |

Fields left out in R1: `description`, `url`, `steamAppId`, `forceLoadBefore`, `loadBefore`, `incompatibleWith`,
the versioned fields (R-2, R-6, R-8), and `loadAfter` unless research R-6's fallback replaces `forceLoadAfter` with it.

## Royalty dependency (one entry of `modDependencies`)

| Field | Value | Source |
|-------|-------|--------|
| `packageId` | `Ludeon.RimWorld.Royalty` | `Data/Royalty/About/About.xml` |
| `displayName` | `Royalty` | `ExpansionDefs.xml` line 15 |
| `steamWorkshopUrl` | `steam://url/StoreAppPage/1149640` | `ExpansionDefs.xml` line 32 |
| `downloadUrl` | `https://rimworldgame.com/` | `ExpansionDefs.xml` line 33 |

## States

The game shows Imperium in one of these states in the mod list (`Menus_Main.xml`):

- Royalty inactive: missing requirement (line 146, `ModUnsatisfiedDependency`).
- Placed before an official expansion: move refused (line 95) or load-order warning (lines 139 and 143).
- Game version other than 1.7: not made for this version (line 147).
- Another active mod with the same identifier: same-ID warning (line 144).
- Otherwise: no warning.
