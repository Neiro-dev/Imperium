# Contract: Mantle's metadata

The game and other mods refer to Mantle through `Mantle/About/About.xml` (`ModUpdating.txt` lines 81 and 230). This
is what they can rely on from R14 on. Field values are in [../data-model.md](../data-model.md).

## Stable

- **Identity**: the package identifier `Neiro.RimWorld.Mantle` names Mantle in every release. The mods built on it,
  Imperium first, use it in their own `modDependencies` and `loadAfter` (`ModUpdating.txt` lines 266-314; R13
  research R-1). It does not change once released (spec FR-010).
- **Requirement**: Mantle requires no expansion and no other mod (spec FR-003). The first entry whose code uses
  Harmony adds the Harmony mod (research R-6).
- **Placement**: Mantle loads after Core and every official expansion (spec FR-004), and its load order names no other
  package, so it can sit directly after them, ahead of the mods that depend on it and every ordinary mod placed after
  them (spec FR-011). A mod built on Mantle places itself after it with its own `loadAfter` (`ModUpdating.txt` lines
  308-309).

## May change in later entries

- The supported versions, when the game's version changes (spec FR-002 follows the official expansions).
- The requirement on the Harmony mod, from the first entry whose code uses it (research R-6).
- The description and preview image, added with the content they describe (research R-8).
