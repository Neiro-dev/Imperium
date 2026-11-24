# Contract: where each mod's files go

Later entries, R13 first, place their files by this layout (research R-1 to R-3; spec FR-012 to FR-015). Paths are
relative to the repository root.

## Stable

- `Mantle/` is Mantle's mod folder and `Imperium/` is Imperium's. Each is a complete mod when it alone is put into the
  game's `Mods` folder, under its own name.
- A file a mod holds for the game or for its code goes in that mod's folder, in the folder `ModUpdating.txt` names for
  it: `About/`, `Defs/`, `Textures/`, `Sounds/`, `Patches/`, `Languages/`, `Source/`, `Assemblies/` (lines 75-151),
  with `Defs/` laid out as the base game lays out its own (lines 98-106).
- Each mod folder holds its `README.md`, with its place in the mod list and the EULA's disclaimer, and a copy of the
  repository's `LICENSE`.
- A file that serves the repository or both mods, such as Spec Kit's files, the specifications, the roadmap or a
  development tool that checks both mods, goes at the repository root, never in a mod folder (spec FR-014).
- Neither mod folder lies inside the other, and the root holds no `About/`.

## May change in later entries

- New content folders inside a mod folder, as each entry adds them.
- New files at the root for the repository or for both mods.
