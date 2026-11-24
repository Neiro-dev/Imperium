# Implementation Plan: Mod foundation

**Branch**: `claude/project-thread-b1vpqw` | **Date**: 2026-11-24 | **Spec**: [spec.md](spec.md)

**Input**: Feature specification from `/specs/001-mod-foundation/spec.md`

**Note**: This template is filled in by the `/speckit-plan` command; its definition describes the execution workflow.

## Summary

Imperium becomes a mod RimWorld 1.7 lists and loads: it requires Royalty and no other expansion, loads after Core
and every official expansion, and is presented as community-created content (spec FR-001 to FR-010). The whole
feature is one file, `About/About.xml` at the repository root, shaped like an official expansion's `About.xml`
where a community mod can be, and like `ModUpdating.txt`'s form where it cannot ([research.md](research.md) R-1
to R-8). No code, content or Harmony (R-9). It is validated in the game on the maintainer's computer
([quickstart.md](quickstart.md)).

## Technical Context

**Language/Version**: XML 1.0, UTF-8, with the declaration the official `About.xml` files use (research R-2)

**Primary Dependencies**: RimWorld 1.7.5014 (`Version.txt`) and Royalty (spec FR-002); no Harmony (research R-9)

**Storage**: N/A

**Testing**: in the game: `-quicktest` (`Readme.txt` lines 58-60), the log in `_Data/output_log.txt` (`Readme.txt`
line 21), then RimBridgeServer 2.4.0 or later with GABS for what `Readme.txt` gives no form for (research R-10)

**Target Platform**: RimWorld 1.7 only (research R-5), tested on the maintainer's Windows install at
`D:\Steam\steamapps\common\RimWorld`, the only install of the game the project has

**Project Type**: RimWorld mod folder (`ModUpdating.txt` lines 68-81)

**Performance Goals**: none; R1 adds no content (spec FR-007)

**Constraints**: the package identifier's format (`ModUpdating.txt` lines 231-237); never presented as official
(`EULA.txt` lines 57 and 78)

**Scale/Scope**: one file

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

| Principle | Check | Result |
|-----------|-------|--------|
| I. One Source per Topic | Imperium's design from Imperium-old `main` (spec, Sources); the mod's form from `Data/`, `ModUpdating.txt`, Harmony; testing from `Readme.txt`, RimBridgeServer, GABS; workflow from Spec Kit; repository files from GitHub Docs | Pass |
| II. Other Sources Only Cross-Check | No decision rests on a source outside its topic's register entry | Pass |
| III. Sources in Order | Each field takes `Data/`'s form first; `name` and `modDependencies` come from `ModUpdating.txt` only because `Data/` gives no form (R-2); `loadAfter` is held back unless `forceLoadAfter` proves Ludeon-only (R-6); Harmony is not reached (R-9); testing uses RimBridgeServer only where `Readme.txt` gives no form (R-10) | Pass |
| IV. Asking the Maintainer | No question goes to the maintainer: nothing here is game content left unsettled | Pass |
| V. When a Source Gives No Form | No icon, because no source gives a community mod one (R-8); no `LoadFolders.xml`, version folders, empty content folders or code, because nothing in R1 needs them (R-1, R-9) | Pass |
| VI. Every Conclusion Names Its Source | Every decision in research.md and every row in data-model.md names its source | Pass |
| Source Register, `EULA.txt` always followed | Community-created presentation, no `ExpansionDef`, disclaimer in `README.md` (R-8) | Pass |

Post-design re-check (after Phase 1): unchanged, all pass.

## Project Structure

### Documentation (this feature)

```text
specs/001-mod-foundation/
├── plan.md              # This file (/speckit-plan command output)
├── research.md          # Phase 0 output (/speckit-plan command)
├── data-model.md        # Phase 1 output (/speckit-plan command)
├── quickstart.md        # Phase 1 output (/speckit-plan command)
├── contracts/           # Phase 1 output (/speckit-plan command)
│   └── about-xml.md
└── tasks.md             # Phase 2 output (/speckit-tasks command - NOT created by /speckit-plan)
```

### Source Code (repository root)

```text
About/
└── About.xml            # new in R1
README.md                # holds the EULA's disclaimer (already on main)
LICENSE                  # names the maker (already on main)
```

**Structure Decision**: the repository root is the mod's folder, as `Mods\Imperium` on the maintainer's computer is a
clone of it (research R-1). Content folders come with later entries in the layout of an official expansion's folder
(`Data/Royalty/`: `Defs`, `Languages`, `Patches`); code comes with Mantle (R2), the framework layer of Imperium's code
(Imperium-old `docs/glossary.md` line 221), in `ModUpdating.txt`'s `Source/` and `Assemblies/` (lines 139-151),
since the official expansions' folders hold no assemblies (`Data/*/`).

## Complexity Tracking

No Constitution Check violations.
