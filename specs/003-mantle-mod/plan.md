# Implementation Plan: Mantle as a mod of its own

**Branch**: `claude/project-thread-048ozg` | **Date**: 2026-11-24 | **Spec**: [spec.md](spec.md)

**Input**: Feature specification from `/specs/003-mantle-mod/spec.md`

**Note**: This template is filled in by the `/speckit-plan` command; its definition describes the execution workflow.

## Summary

Mantle becomes a mod RimWorld 1.7 lists and loads apart from Imperium: it requires no expansion, loads after Core and
every official expansion, and is presented as community-created content (spec FR-001 to FR-011). It stays in this
repository, since a repository groups one project's items and Mantle is part of Imperium (research R-1). The repository
root becomes the parent of two mod folders side by side, `Imperium/` and `Mantle/`, as `Data/` holds Core and the
official expansions, and keeps the repository's own files (R-1 to R-3). Imperium's `About/` and `README.md` move into
`Imperium/` unchanged; `Mantle/` gets `About/About.xml` with the package identifier `Neiro.RimWorld.Mantle`, shaped
as R1 shaped Imperium's (R-4 to R-7), a `README.md` with its place and the EULA's disclaimer, and each mod folder a
copy of the license (R-3, R-8). No code, content or Harmony. It is validated outside the game first, then in the game
on the maintainer's computer, with the clone moved out of `Mods` and each mod folder copied into it
([quickstart.md](quickstart.md); R-9).

## Technical Context

**Language/Version**: XML 1.0, UTF-8, with the byte order mark and declaration the official `About.xml` files use
(research R-5); Markdown for the READMEs

**Primary Dependencies**: RimWorld 1.7.5014 (`Version.txt`); no expansion and no other mod (spec FR-003); no Harmony
(research R-6)

**Storage**: N/A

**Testing**: outside the game first, in the cloud, against the official files in `Data/` (constitution, Source
Register); then in the game: `-quicktest` (`Readme.txt` lines 58-60) with `-savedatafolder=SaveData` (lines 27-38),
then RimBridgeServer with GABS, comparing each launch's `Player.log` with its baseline (research R-9)

**Target Platform**: RimWorld 1.7 only (research R-5), tested on the maintainer's Windows install at
`D:\Steam\steamapps\common\RimWorld`

**Project Type**: two RimWorld mod folders in one repository (`ModUpdating.txt` lines 68-81; research R-1)

**Performance Goals**: none; R14 adds no content (spec FR-007)

**Constraints**: the package identifier's format (`ModUpdating.txt` lines 231-237); never presented as official
(`EULA.txt` lines 57 and 78); Imperium keeps everything R1 gave it (spec FR-016)

**Scale/Scope**: one new `About.xml`, two moved files, three READMEs and two license copies

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

| Principle | Check | Result |
|-----------|-------|--------|
| I. One Source per Topic | Where Mantle lives from GitHub Docs (the repository) and Spec Kit (the workflow), with Imperium's design from Imperium-old `main` (Mantle is part of Imperium); the mod folders' and metadata's form from `Data/`, `ModUpdating.txt`, Harmony; the license from the repository's `LICENSE` (chosen from choosealicense.com) and GitHub Docs; testing outside the game from `Data/`; testing in the game from `Readme.txt`, RimBridgeServer, GABS | Pass |
| II. Other Sources Only Cross-Check | The Harmony mod's own repository, whose root is its mod folder, is not taken as the form of a repository: GitHub Docs and Spec Kit are the sources for that (R-1). Harmony's released files only cross-check what a mod folder holds (R-3) | Pass |
| III. Sources in Order | Each field takes `Data/`'s form first; the folders take `Data/`'s side-by-side form (R-1, R-2); `name` comes from `ModUpdating.txt` only because `Data/` gives no form (R-5); Harmony's `README.md` is reached only for telling players Mantle's place (R-7); testing uses RimBridgeServer only where `Readme.txt` gives no form (R-9) | Pass |
| IV. Asking the Maintainer | No question goes to the maintainer: where Mantle lives is a repository and workflow question, and nothing here is game content left unsettled | Pass |
| V. When a Source Gives No Form | No icon, description or preview (R-8); no `modDependencies` (R-6); no `LoadFolders.xml`, version folders, empty content folders or code, because nothing in R14 needs them; no second repository or constitution (R-1) | Pass |
| VI. Every Conclusion Names Its Source | Every decision in research.md and every row in data-model.md names its source | Pass |
| Source Register, `EULA.txt` always followed | Community-created presentation, no `ExpansionDef`, the disclaimer in each mod folder's `README.md` and the root's (R-3, R-8) | Pass |
| Source Register, testing outside the game | The checks in the cloud come before the checks in the game, hold both `About.xml` files and the layout against `Data/` and data-model.md, and do not replace the checks in the game (quickstart.md; R-9) | Pass |

Post-design re-check (after Phase 1): unchanged, all pass.

## Project Structure

### Documentation (this feature)

```text
specs/003-mantle-mod/
├── plan.md              # This file (/speckit-plan command output)
├── research.md          # Phase 0 output (/speckit-plan command)
├── data-model.md        # Phase 1 output (/speckit-plan command)
├── quickstart.md        # Phase 1 output (/speckit-plan command)
├── contracts/           # Phase 1 output (/speckit-plan command)
│   ├── about-xml.md
│   └── repository-layout.md
└── tasks.md             # Phase 2 output (/speckit-tasks command - NOT created by /speckit-plan)
```

### Source Code (repository root)

```text
Imperium/                # Imperium's mod folder (R-1, R-2)
├── About/
│   └── About.xml        # moved from the root, unchanged
├── README.md            # moved from the root, unchanged
└── LICENSE              # copy of the root's (R-3)
Mantle/                  # Mantle's mod folder (R-1, R-2)
├── About/
│   └── About.xml        # new (R-4 to R-7)
├── README.md            # Mantle's place and the EULA's disclaimer (R-7, R-8)
└── LICENSE              # copy of the root's (R-3)
README.md                # rewritten: the repository's README (R-3)
LICENSE                  # unchanged
```

**Structure Decision**: the repository root is the parent of the two mod folders, `Imperium/` and `Mantle/`, each a
complete mod when it alone is put into the game's `Mods` folder, and holds the repository's own files (research R-1
to R-3; [contracts/repository-layout.md](contracts/repository-layout.md)). Later entries add each mod's content
folders inside its own folder, in `ModUpdating.txt`'s layout, and files that serve the repository or both mods at the
root. On the maintainer's computer the clone moves out of `Mods`, and each mod folder is copied into `Mods` for the
checks in the game (R-9).

## Complexity Tracking

No Constitution Check violations.
