# Research: Mantle as a mod of its own

Each decision names its source, from the constitution's Source Register, in the order the register gives: GitHub Docs
for the repository's files, Spec Kit for the development workflow, Imperium-old `main` (20a052b) for Imperium's own
design; `Data/` of RimWorld 1.7.5014, then `ModUpdating.txt`, then Harmony (`pardeike/HarmonyRimWorld`, `master`),
for the released mod; `EULA.txt` always; `Data/` for testing outside the game; `Readme.txt`, then RimBridgeServer with
GABS, for testing in the game. Line numbers refer to those files as copied into the project files, to GitHub Docs'
source (`github/docs`, `main` on 2026-11-24), to Spec Kit at v1.4.3, to HarmonyRimWorld and RimBridgeServer on their
default branches on 2026-11-24, and to Imperium-old at 20a052b. FR numbers point to [spec.md](spec.md); R1's
decisions are in [../001-mod-foundation/research.md](../001-mod-foundation/research.md).

## R-1: One repository, two mod folders side by side

- **Decision**: Mantle stays in this repository. The repository root holds two mod folders, `Imperium/` and
  `Mantle/`, each with `About/About.xml` at its root, and the repository's own files: `.specify/`, `.claude/`,
  `specs/`, `ROADMAP.md`, `CLAUDE.md`, `README.md`, `LICENSE` and `.gitignore`. Imperium's mod files, `About/` and its
  `README.md`, move from the root into `Imperium/`.
- **Rationale**: a repository usually groups together the items that belong to the same project (GitHub Docs, Hello
  World line 34). Mantle is the framework layer of Imperium's code (Imperium-old `docs/glossary.md` line 221), and
  Imperium is complete with Royalty alone, Mantle included (`docs/imperium.md` line 109), so Mantle belongs to the
  Imperium project and its repository. A Spec Kit project is the directory that holds `.specify/` (Spec Kit
  `docs/how-to/monorepo.md` line 3); this repository's root holds the one roadmap whose entries cover both mods, so
  both mods' code sits under it. Spec Kit's plan template lays a project with several parts out as one folder per part
  at the repository root (Project Structure, its options for a web application and for mobile with an API). In the
  game, each mod is its own folder with `About/About.xml` at its root (`ModUpdating.txt` lines 68-81), and `Data/`
  holds Core and each official expansion as folders side by side, none inside another (`Data/Core`, `Data/Royalty`,
  ...). With two mods, the root can no longer be one mod's folder, as R1 had it (R1 research R-1).
- **Alternatives considered**:
  - A repository of its own for Mantle, whose root is its mod folder, as the Harmony mod's repository is. Rejected:
    GitHub Docs groups one project's items in one repository, and Mantle is part of the Imperium project. A second
    repository would also be a second Spec Kit project with a constitution of its own, which Spec Kit can only
    duplicate or sync, having no inheritance between constitutions (`monorepo.md` lines 129-135).
  - Mantle's folder inside Imperium's, with the root staying Imperium's folder. Rejected: no package in `Data/` lies
    inside another, and Imperium's released folder would then carry Mantle's files (spec FR-013, FR-014).
- **Effect on R1**: R1 research R-1 ("the repository root is the mod's folder") and R-10 (`Mods\Imperium` as a clone
  of the repository) are superseded for the repository's layout; R1's requirements are unchanged (spec FR-016). The
  maintainer's clone leaves `Mods`, and each mod folder is put into `Mods` as described in R-9.

## R-2: Folder names

- **Decision**: `Imperium/` and `Mantle/`.
- **Rationale**: `Data/` names each package's folder after the package (`Data/Royalty/` holds
  `Ludeon.RimWorld.Royalty`, `Data/Odyssey/` holds `Ludeon.RimWorld.Odyssey`), and the mod names are Imperium and
  Mantle (R1 data-model; spec, Assumptions). The folder in `Mods` takes the same name (`ModUpdating.txt` lines 68-72,
  `-YourMod/`).

## R-3: What each folder holds

- **Decision**: `Mantle/` holds `About/About.xml`, `README.md` and `LICENSE`. `Imperium/` holds `About/About.xml` and
  `README.md`, moved unchanged from the root, and `LICENSE`. The root keeps `LICENSE` and gets a `README.md` of its
  own that says what the repository holds and carries the EULA's disclaimer.
- **Rationale**:
  - A mod's own files are its folders for the game and for its code (`ModUpdating.txt` lines 75-151), its README and
    its license (spec FR-014, Clarifications). Nothing else goes into a mod folder, so that it alone is a complete mod
    in `Mods` (spec FR-014), as the Harmony mod's released files are its mod folder's files and no others (Harmony
    `Release-payload.json`; `README.md` line 10).
  - The license sits in the root of the repository (GitHub Docs, Licensing a repository line 27), and its notice must
    be included in all copies or substantial portions of the software (`LICENSE` lines 12-13), so each mod folder,
    which is released on its own, holds a copy (GitHub Docs, Licensing a repository line 31, "include the license file
    with your project"; Harmony `Release-payload.json` lists `LICENSE`).
  - The disclaimer is displayed on or reasonably in connection with each mod (`EULA.txt` lines 32-34): in each mod
    folder's `README.md`, as R1 has it for Imperium (R1 research R-8), and in the root `README.md`, which GitHub shows
    to the repository's visitors (GitHub Docs, About READMEs lines 24-31).
  - The root `README.md` says what the project does and how to get started (About READMEs lines 24-30): the two mods,
    where each one's folder is, and that each goes into the game's `Mods` folder by its own folder.
- **Alternatives considered**: one `LICENSE` at the root only. Rejected: a mod folder released alone would then not
  include the license's notice.

## R-4: Mantle's package identifier

- **Decision**: `Neiro.RimWorld.Mantle`.
- **Rationale**: the official form is `<maker>.RimWorld.<name>` (`Data/Royalty/About/About.xml`), which R1 gave
  Imperium with the maker's one-word name `Neiro` (R1 research R-3). The result is 21 characters (limit 60), has three
  parts as `ModUpdating.txt`'s second example does (line 241), has no "Ludeon", and differs from Imperium's
  `Neiro.RimWorld.Imperium` (spec FR-010).
- **Alternatives considered**: `Neiro.Imperium.Mantle`, `ModUpdating.txt`'s `AuthorName.ModSeriesName.ModName`
  example (line 241) with Imperium as the series. Rejected: `Data/` gives a form, so it comes first (Principle III).
- **Note**: the identifier does not change once released (spec FR-010). R13 names it in Imperium's
  `modDependencies` and `loadAfter` (R13 research R-1).

## R-5: Name, author, supported versions, declaration

- **Decision**: `name` `Mantle`; `author` `Neiro-dev`; `supportedVersions` `1.7`; the declaration
  `<?xml version="1.0" encoding="utf-8"?>` preceded by the byte order mark, as the official files and Imperium's file
  have.
- **Rationale**: the same sources as R1 research R-2, R-4 and R-5: `name` is required (`ModUpdating.txt` line 223)
  and is the design's name for the framework layer (Imperium-old `docs/glossary.md` line 221); `author` is the maker
  (`Data/*/About/About.xml`; `LICENSE`); each official expansion lists only `1.7` (`Data/*/About/About.xml`;
  `Version.txt`). The official `About.xml` files begin with the byte order mark and that declaration
  (`Data/Royalty/About/About.xml` line 1).

## R-6: No requirements

- **Decision**: no `modDependencies`.
- **Rationale**: Mantle requires no expansion and no other mod (spec FR-003; ROADMAP R14, Releases), and
  `modDependencies` lists the mods that must be active for a mod to function (`ModUpdating.txt` lines 266-267). It
  is optional (line 266), so it is left out rather than written empty, as each official expansion leaves it out
  (`Data/*/About/About.xml`).
- **Harmony**: not a requirement in R14, which has no code (spec FR-007). The first entry whose code uses Harmony adds
  `brrainz.harmony` to Mantle's `modDependencies` and no load-order entry, as R1 research R-9 sets for Imperium. R2's
  removal of the base game's Empire where Royalty is active is such code (ROADMAP R2).

## R-7: Load order

- **Decision**: `forceLoadAfter` lists `Ludeon.RimWorld`, `Ludeon.RimWorld.Royalty`, `Ludeon.RimWorld.Ideology`,
  `Ludeon.RimWorld.Biotech`, `Ludeon.RimWorld.Anomaly` and `Ludeon.RimWorld.Odyssey`. No `forceLoadBefore`,
  `loadBefore` or `loadAfter`. `Mantle/README.md` says: "Enable Mantle directly below the official expansions and
  above the mods that depend on it."
- **Rationale**: each official expansion loads after every one before it through `forceLoadAfter`
  (`Data/Odyssey/About/About.xml` lines 9-15), and Mantle comes after all of them (spec FR-004). The game honors
  `forceLoadAfter` from a package that is not Ludeon's: R1's checks in the game found Imperium after Odyssey with no
  log line about the field (R1 quickstart, check 5; R1 research R-6). No load-order field names a package that is not
  Ludeon's (spec FR-011), and each names single packages (`ModUpdating.txt` lines 300-314), so players are told
  Mantle's place as the Harmony mod tells its own: "Enable it above Core and mods that depend on Harmony" (Harmony
  `README.md` lines 3-4).
- **Between Mantle and Imperium**: neither names the other in R14 (spec, Clarifications), so either order loads with
  no warning. R13 adds Mantle to Imperium's `modDependencies` and `loadAfter` (R13 research R-1), and with it the place
  Imperium's `README.md` gives players, directly below Mantle.

## R-8: Presentation and the EULA

- **Decision**: no `ExpansionDef`, no `description`, no preview image and no icon in R14; the disclaimer in
  `Mantle/README.md` (R-3).
- **Rationale**: as R1 research R-8: the base game's `ExpansionDefs.xml` holds only Ludeon's expansions, and a
  community mod must not be presented as one of them (`EULA.txt` lines 57 and 78). Mantle's description says what the
  alpha is and is written with that content in R2 (ROADMAP R2), in `About.xml`'s `description` and
  `About/Preview.png` (`ModUpdating.txt` lines 84-90 and 246-248).

## R-9: Testing

- **Decision**:
  - **Outside the game, first** (constitution, Source Register: `Data/`): in the cloud, check that both `About.xml`
    files are well-formed, begin as the official files do, and hold the fields and values of
    [data-model.md](data-model.md) against `Data/*/About/About.xml`; that the package identifiers meet the format and
    differ; that no load-order field names a package that is not Ludeon's; that `Imperium/` and `Mantle/` each hold
    only the files listed in data-model.md and the root holds no `About/`.
  - **In the game, the final check**, on the maintainer's computer (`D:\Steam\steamapps\common\RimWorld`), as R1
    research R-10 sets: `-quicktest` (`Readme.txt` lines 58-60) with `-savedatafolder=SaveData` (lines 27-38), and
    RimBridgeServer with GABS for what `Readme.txt` gives no form for, comparing each launch's `Player.log` with its
    baseline. The repository's clone moves out of `Mods`, to `D:\Steam\steamapps\common\RimWorld\Imperium`, and each
    mod folder is copied into `Mods` under its own name before the checks, as RimBridgeServer's local development
    copies a mod into `$RIMWORLD_MOD_DIR/<mod>`; the checks then confirm with
    `rimworld/get_mod_configuration_status` that the game loads those folders (RimBridgeServer `README.md` lines
    118-129). The install's `CLAUDE.md` imports the constitution from the clone's new place.
- **Rationale**: a copy of the whole repository in `Mods` is not a mod, since its root holds no `About/` (spec, Edge
  Cases; `ModUpdating.txt` lines 68-81). The clone stays in the install's folder, where the work on the maintainer's
  computer takes place (project instructions).
- **Note**: the game does not run in the cloud, so the checks in the game wait for the maintainer's computer.
