# Contract: Imperium's metadata

The game and other mods refer to Imperium through `About/About.xml` (`ModUpdating.txt` lines 81 and 230). This is
what they can rely on from R1 on. Field values are in [../data-model.md](../data-model.md).

## Stable

- **Identity**: the package identifier `Neiro.RimWorld.Imperium` names Imperium in every release. Other mods use it
  in their own `modDependencies`, `loadAfter`, `loadBefore` or `incompatibleWith` (`ModUpdating.txt` lines 266-314).
  It does not change once released (spec FR-010).
- **Requirement**: Imperium requires Royalty (`Ludeon.RimWorld.Royalty`) and no other package (spec FR-002, FR-003).
- **Placement**: Imperium loads after Core and every official expansion (spec FR-004).

## May change in later entries

- The supported versions, when the game's version changes (spec FR-001 follows the official expansions).
- The description and preview image, added with the content they describe (research R-8).
