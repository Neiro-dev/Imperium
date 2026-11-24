# Research: Mod foundation

Each decision names its source, from the constitution's Source Register, in the order the register gives:
`Data/` of RimWorld 1.7.5014, then `ModUpdating.txt`, then Harmony, for the released mod; `EULA.txt` always;
`Readme.txt`, then RimBridgeServer with GABS, for testing. Line numbers refer to those files as copied into the
project files.

## R-1: Where the mod lives

- **Decision**: the repository root is the mod's folder. R1 adds one file there, `About/About.xml`.
- **Rationale**: a mod is a folder in `Mods/` with an `About/About.xml` (`ModUpdating.txt` lines 68-81). Each official
  expansion is one folder whose root holds `About/` and its content folders (`Data/Royalty/`: `About`, `Defs`,
  `Languages`, `Patches`).
- **Alternatives considered**: a `1.7/` load folder or `LoadFolders.xml` (`ModUpdating.txt` lines 154-170,
  206-211). Rejected: no official expansion uses either, and Imperium supports 1.7 only (spec FR-001).

## R-2: Metadata fields and their form

- **Decision**: `About/About.xml` takes the fields of an official expansion's `About.xml` (`Data/Royalty/About/About.xml`:
  `packageId`, `author`, `supportedVersions`, `forceLoadAfter`), plus `name` and `modDependencies` from
  `ModUpdating.txt`. It has the same XML declaration as the official files (`<?xml version="1.0" encoding="utf-8"?>`).
- **Rationale**: Principle III. `Data/` gives the form for identity, author, versions and load order. It gives no form
  for a name (an official expansion's label comes from the base game's `ExpansionDefs.xml`, whose entries link only
  Ludeon's packages) and none for a requirement (no official expansion requires another), so those two come from
  `ModUpdating.txt` (lines 223-224 and 266-289). `name` is required there (line 223).
- **Alternatives considered**: `steamAppId`, which each official expansion has. Rejected: it names the expansion's
  own Steam store product, which a community mod does not have.

## R-3: Package identifier

- **Decision**: `Neiro.RimWorld.Imperium`.
- **Rationale**: the official form is `<maker>.RimWorld.<expansion>`, with the maker's name shortened to one word
  (`Ludeon Studios` gives `Ludeon.RimWorld.Royalty`, `Data/Royalty/About/About.xml`). Imperium's maker is `Neiro-dev`,
  the copyright holder in `LICENSE`. The game's format allows letters, digits and dots only (`ModUpdating.txt`
  lines 231-237), so the maker's one-word name is `Neiro`. The result has three parts, as `ModUpdating.txt`'s second
  example does (line 241), is 23 characters (limit 60) and has no "Ludeon".
- **Alternatives considered**: `Neiro.Imperium`, the shorter `AuthorName.ModName` example (`ModUpdating.txt`
  line 240). Rejected: `Data/` gives a form, so it comes first.
- **Note**: the identifier must not change once released (spec FR-010). This is the one value in R1 that becomes
  permanent at the first release.

## R-4: Author

- **Decision**: `Neiro-dev`.
- **Rationale**: an official expansion's `author` is its maker (`Ludeon Studios`, each `Data/*/About/About.xml`), and
  the field is the maker's name or nickname (`ModUpdating.txt` line 227). The repository's `LICENSE` names
  `Neiro-dev` as the copyright holder.

## R-5: Supported versions

- **Decision**: `1.7` only.
- **Rationale**: each official expansion lists only `1.7` (`Data/*/About/About.xml`), the install is 1.7.5014
  (`Version.txt`), and the format is `X.Y` (`ModUpdating.txt` line 254).

## R-6: Load order

- **Decision**: `forceLoadAfter` lists `Ludeon.RimWorld`, `Ludeon.RimWorld.Royalty`, `Ludeon.RimWorld.Ideology`,
  `Ludeon.RimWorld.Biotech`, `Ludeon.RimWorld.Anomaly` and `Ludeon.RimWorld.Odyssey`. No `forceLoadBefore`.
- **Rationale**: each official expansion loads after every one before it, through `forceLoadAfter`
  (`Data/Odyssey/About/About.xml` lines 9-15 lists the other five). Imperium comes after all of them (spec FR-004).
  Nothing official comes after it, so it has no `forceLoadBefore`.
- **Alternatives considered**: `loadAfter` (`ModUpdating.txt` lines 308-314). Kept as the fallback: `ModUpdating.txt`
  documents `loadAfter` and not `forceLoadAfter`, so if the game ignores or rejects `forceLoadAfter` from a package
  that is not Ludeon's (a log line about the field, or Imperium placed before an official expansion), the form is
  open only to Ludeon's packages and the next source applies (spec, Sources; Principle III). The quickstart checks
  this first.
- **Effect on the spec's edge case**: with `forceLoadAfter` the game may refuse the move
  (`Menus_Main.xml` line 95, `ModReorderConflict_MustLoadAfter`); with `loadAfter` it warns and offers auto-sort
  (lines 139 and 143). Either shows that Imperium must load after the expansion; the spec's edge case names both.

## R-7: Requirement on Royalty

- **Decision**: one `modDependencies` entry: `packageId` `Ludeon.RimWorld.Royalty`, `displayName` `Royalty`,
  `steamWorkshopUrl` `steam://url/StoreAppPage/1149640`, `downloadUrl` `https://rimworldgame.com/`.
- **Rationale**: `modDependencies` makes the game show the requirement on the mod info page (`ModUpdating.txt`
  lines 266-268). The package identifier is Royalty's own (`Data/Royalty/About/About.xml`). The display name and the
  two links are the ones the base game gives Royalty (`ExpansionDefs.xml` lines 15, 32 and 33). One of the two links is
  required, and the Steam one is preferred in the Steam version (`ModUpdating.txt` lines 272-275).

## R-8: Presentation and the EULA

- **Decision**: no `ExpansionDef`, no `description`, no preview image and no icon in R1. When later entries write
  the description and images, they go in `About.xml`'s `description` and `About/Preview.png`
  (`ModUpdating.txt` lines 84-90 and 246-248). The EULA's disclaimer stays in `README.md` at the mod's root.
- **Rationale**: the base game's `ExpansionDefs.xml` defines Ludeon's own expansions; adding Imperium there would
  present it as one of them, which the EULA forbids (`EULA.txt` lines 57 and 78; spec FR-008). That form is open only
  to Ludeon's packages, so the next source, `ModUpdating.txt`, gives the description and preview image. No source
  gives a community mod an icon, so none is made (Principle V). The disclaimer must be on or reasonably in
  connection with the mod (`EULA.txt` lines 32-34); `README.md` in the mod's folder already holds it (spec FR-009).
  Description and images are deferred with the content they describe (spec, Assumptions).

## R-9: Code and Harmony

- **Decision**: no code, no `Assemblies/`, no Harmony in R1.
- **Rationale**: R1 adds no content (spec FR-007), and the official expansions' folders hold no assemblies
  (`Data/*/`). Harmony is the third source and is used only where `Data/` and `ModUpdating.txt` give no form
  (Principle III); R1 needs nothing from it.

## R-10: Testing

- **Decision**: in the game on the maintainer's computer (`D:\Steam\steamapps\common\RimWorld`, with `Mods\Imperium`
  as a clone of the repository). New games start with `-quicktest` (`Readme.txt` lines 58-60). Every launch adds
  `-savedatafolder=SaveData`, the example of `Readme.txt` lines 27-38, so the checks' mod lists and saves stay in
  `SaveData` in the install's folder and the maintainer's own are not touched. What `Readme.txt` gives no form for
  (turning expansions on and off, reading the mod list's warnings, reordering mods, saving and loading) uses
  RimBridgeServer with GABS: `rimworld/set_mod_enabled`, `rimworld/reorder_mod`,
  `rimworld/get_mod_configuration_status`, `rimworld/list_mods`, `rimworld/load_game_ready` and
  `rimbridge/list_logs` (RimBridgeServer `README.md`, sections Installation and Tool Surface). RimBridgeServer 2.4.0
  and later support 1.7 (same `README.md`, section RimWorld 1.7 build and frozen 1.6 payload).
- **The log**: `Readme.txt` line 21 places `output_log.txt` in the install's `_Data` folder, but 1.7.5014 on the
  maintainer's install writes no such file; it keeps `Player.log` in the `Logs` folder of the save data folder
  (inventory of the install, 2026-11-24). Since `Readme.txt`'s form does not hold, the log is read with
  `rimbridge/list_logs`, the next testing source (constitution, Principle III).
- **Rationale**: the constitution's testing order (Source Register, Testing in the game).
- **Note**: RimBridgeServer is a mod and writes its own log lines, so each baseline launch also runs it, and a
  launch passes when it adds no error or warning line to that baseline (spec, Clarifications).
- **Where checks run**: the game does not run in the cloud container, so the in-game checks wait for the
  maintainer's computer. The cloud can check that the XML is well-formed and that the identifier meets the game's
  format.
