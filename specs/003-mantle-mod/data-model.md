# Data Model: Mantle as a mod of its own

R14 has two pieces of data: the repository's layout, which says where each mod's folder lives, and Mantle's metadata
in `Mantle/About/About.xml`, which the game reads to list, order and load Mantle. Their sources are in
[research.md](research.md); what later entries rely on is in [contracts/](contracts/).

## Repository layout

| Path | What it is | Rule | Source |
|------|------------|------|--------|
| `Imperium/` | Imperium's mod folder | holds only Imperium's own files; `About/About.xml` at its root | R-1, R-2, R-3; spec FR-013, FR-014 |
| `Imperium/About/About.xml` | Imperium's metadata | moved from the root unchanged (R1 data-model) | R-1; spec FR-016 |
| `Imperium/README.md` | Imperium's place in the mod list and the EULA's disclaimer | moved from the root unchanged | R-3; R1 research R-6, R-8 |
| `Imperium/LICENSE` | the repository's license | a copy of `LICENSE` | R-3; spec FR-015 |
| `Mantle/` | Mantle's mod folder | holds only Mantle's own files; `About/About.xml` at its root | R-1, R-2, R-3; spec FR-013, FR-014 |
| `Mantle/About/About.xml` | Mantle's metadata | below | R-4 to R-7 |
| `Mantle/README.md` | Mantle's place in the mod list and the EULA's disclaimer | the place sentence of R-7, then the disclaimer | R-3, R-7, R-8 |
| `Mantle/LICENSE` | the repository's license | a copy of `LICENSE` | R-3; spec FR-015 |
| `README.md` | the repository's README | what the repository holds, where each mod's folder is, the EULA's disclaimer | R-3 |
| `LICENSE` | the repository's license | unchanged | R-3 |
| `.specify/`, `.claude/`, `specs/`, `ROADMAP.md`, `CLAUDE.md`, `.gitignore` | the repository's own files | unchanged, at the root | R-1; spec FR-014 |

A mod folder's own files are, besides those above, the folders `ModUpdating.txt` names for a mod: `Defs/`,
`Textures/`, `Sounds/`, `Patches/`, `Languages/`, and for code `Source/` and `Assemblies/` (lines 96-151), which later
entries add. Files that serve the repository or both mods go at the root (spec FR-014, Clarifications). No `About/`
at the root.

## Mantle's metadata (`Mantle/About/About.xml`, one `ModMetaData` element)

| Field | Value | Rule | Source |
|-------|-------|------|--------|
| `name` | `Mantle` | required | R-5; `ModUpdating.txt` line 223 |
| `packageId` | `Neiro.RimWorld.Mantle` | letters, digits and dots; at least one dot; no repeated, leading or trailing dot; 60 characters or fewer; no "Ludeon"; differs from Imperium's; never changes once released | R-4; `ModUpdating.txt` lines 231-237; spec FR-010 |
| `author` | `Neiro-dev` | the maker | R-5 |
| `supportedVersions` | `1.7` | `X.Y` entries | R-5; `ModUpdating.txt` line 254 |
| `forceLoadAfter` | `Ludeon.RimWorld`, `Ludeon.RimWorld.Royalty`, `Ludeon.RimWorld.Ideology`, `Ludeon.RimWorld.Biotech`, `Ludeon.RimWorld.Anomaly`, `Ludeon.RimWorld.Odyssey` | package identifiers | R-7 |

Fields left out in R14: `modDependencies` (R-6), `description`, `url`, `steamAppId`, `forceLoadBefore`, `loadBefore`,
`loadAfter`, `incompatibleWith` and the versioned fields (R-5, R-7, R-8). No load-order field names a package that is
not Ludeon's (spec FR-011). The fields come in the order of Imperium's file: `name`, `packageId`, `author`,
`supportedVersions`, `forceLoadAfter`.

## States

The game shows Mantle in one of these states in the mod list (`Menus_Main.xml`):

- Any set of official expansions active or inactive: no missing requirement (spec FR-003).
- Placed before an official expansion: move refused (line 95) or load-order warning (lines 139 and 143).
- Game version other than 1.7: not made for this version (line 147).
- Another active mod with the same identifier: same-ID warning (line 144).
- Directly after the last official expansion and ahead of the mods that depend on it and of an ordinary mod: no
  warning (spec FR-011).
- Before or after Imperium: no warning, until R13 places Imperium after it (research R-7).
