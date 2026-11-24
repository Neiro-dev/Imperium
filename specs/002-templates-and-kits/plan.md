# Implementation Plan: Templates and kits

**Branch**: `claude/project-thread-wgq7xi` | **Date**: 2026-11-24 | **Spec**: [spec.md](spec.md)

**Input**: Feature specification from `/specs/002-templates-and-kits/spec.md`

**Note**: This template is filled in by the `/speckit-plan` command; its definition describes the execution workflow.

## Summary

Templates and kits become definitions of Mantle's own types, `Mantle.TemplateDef` and `Mantle.KitDef`, in `Defs/`,
with their classes in `Source/Mantle/` built into `Assemblies/Mantle.dll` against the installed game (research R-1,
R-2). Their fields take `Data/`'s own forms wherever `Data/` writes the same thing (R-3): a template is a terrain
shape of natural terrain, rock and roofs (R-4) and a skeleton of named parts and relations taken from the design's
definitions (R-5); a kit holds its word list, skeleton, wall settings, groups and fill (R-8). A laid-out city is one
XML file that R2's generation writes (R-7). The check is a Python package in Spec Kit's form, `mantle-check`, that
reads `Data/` 1.7.5014 and Imperium's `Defs/`, reports every problem of the spec's kinds, measures each skeleton
relation in a laid-out city, and draws PNG pictures with a grid, coordinates and a legend beside the reference
pictures, outside the repository (R-6, R-9 to R-11). The river-bend town's template and the Empire kit are written
with it (R-13). It is validated by tests outside the game, then by a load in the game ([quickstart.md](quickstart.md)).

## Technical Context

**Language/Version**: C# for Mantle's definition classes, targeting `net10.0` (research R-2); XML 1.0, UTF-8, for
definitions and laid-out cities (R-1, R-7); Python 3.11 or later for the check (R-9)

**Primary Dependencies**: RimWorld 1.7.5014's assemblies, referenced where the game is installed and never copied
(R-2); Royalty (R1 spec FR-002); for the check, Typer and Pillow (R-9); no Harmony (R-2)

**Storage**: files: definitions in `Defs/`; laid-out cities as XML files; reports and pictures in a folder outside the
repository (R-11)

**Testing**: outside the game first, with pytest against `Data/` 1.7.5014 (`RIMWORLD_DATA_DIR`), on test templates,
kits and laid-out cities written by hand (R-12); then in the game, `-quicktest` with `-savedatafolder=SaveData`
(`Readme.txt` lines 27-38, 58-60) to confirm the definitions load; the final check, templates placed on a map, with R2

**Target Platform**: RimWorld 1.7 on the maintainer's Windows install at `D:\Steam\steamapps\common\RimWorld`; the
check wherever Python and `Data/` are, on the maintainer's computer and in cloud threads (spec, Assumptions)

**Project Type**: RimWorld mod folder with a C# project (`ModUpdating.txt` lines 139-151), and a development tool that
the mod does not load

**Performance Goals**: checking and drawing one template, or one laid-out city beside its reference, finishes before
the game reaches its main menu on the same computer (SC-003)

**Constraints**: reference pictures and the game's files stay out of the repository and the released files (FR-021,
FR-028; `EULA.txt` lines 76, 86); the same inputs give the same files (FR-022); city maps are 350×350 (FR-003)

**Scale/Scope**: two definition types, one laid-out city form, one command; the Empire kit and the river-bend town's
template; test fixtures for every kind of problem

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

| Principle | Check | Result |
|-----------|-------|--------|
| I. One Source per Topic | Design from Imperium-old `main` and the maintainer's direction (spec, Sources); the released mod's forms from `Data/`, `ModUpdating.txt`, Harmony; testing outside the game from `Data/`; testing in the game from `Readme.txt`; the check's form and its ignored files from Spec Kit, the build's from Harmony | Pass |
| II. Other Sources Only Cross-Check | No decision rests on a source outside its topic's register entry; the reference pictures are the maintainer's direction's material, not a source of form | Pass |
| III. Sources in Order | Every field takes `Data/`'s form first (R-3); `Defs/`, `Source/` and `Assemblies/` come from `ModUpdating.txt` because `Data/` holds no mod layout (R-1); the build comes from Harmony because neither earlier source gives one (R-2) | Pass |
| IV. Asking the Maintainer | One game-content question asked: what a kit's groups and fill hold (R-8); the plan is not merged before the answer | Pending |
| V. When a Source Gives No Form | The check takes Spec Kit's own options (R-9); no CI, no version folders, no `LoadFolders.xml`, no Harmony, since nothing here needs them; the word list, groups and fill hold no content until generation uses them (R-8) | Pass |
| VI. Every Conclusion Names Its Source | Every decision in research.md and every row in data-model.md names its source | Pass |
| Source Register, `EULA.txt` always followed | No reference picture, Anno name or game file in the repository or released files (R-9, R-11, R-13); the game's assemblies only referenced (R-2) | Pass |
| Source Register, testing outside the game | The check and its tests run outside the game against `Data/` first, and the load in the game follows; placing templates in the game stays the final check (quickstart.md; R-12) | Pass |

Post-design re-check (after Phase 1): unchanged.

## Project Structure

### Documentation (this feature)

```text
specs/002-templates-and-kits/
├── plan.md              # This file (/speckit-plan command output)
├── research.md          # Phase 0 output (/speckit-plan command)
├── data-model.md        # Phase 1 output (/speckit-plan command)
├── quickstart.md        # Phase 1 output (/speckit-plan command)
├── contracts/           # Phase 1 output (/speckit-plan command)
│   ├── template-and-kit-defs.md
│   ├── laid-out-city.md
│   └── check-command.md
└── tasks.md             # Phase 2 output (/speckit-tasks command - NOT created by /speckit-plan)
```

### Source Code (repository root)

```text
Assemblies/
└── Mantle.dll                     # built from Source/Mantle, committed (R-2)
Defs/
├── KitDefs/
│   └── Kits_Empire.xml            # the Empire kit (R-8)
└── TemplateDefs/
    └── Templates_Empire.xml       # the river-bend town's template (R-13)
Source/
└── Mantle/
    ├── Mantle.csproj              # net10.0, the game's assemblies by RimWorldAssemblyDir
    ├── TemplateDef.cs
    ├── KitDef.cs
    ├── Skeleton.cs                # parts, relations, their kinds
    └── Cells.cs                   # rects, layers, features
Directory.Build.props              # RimWorldAssemblyDir (R-2)
pyproject.toml                     # the check's package (R-9)
src/
└── mantle_check/
    ├── __init__.py
    ├── cli.py                     # the command (contracts/check-command.md)
    ├── gamedata.py                # reading Data/ and Defs/, inheritance (R-10)
    ├── forms.py                   # reading templates, kits, laid-out cities
    ├── checks.py                  # the problems (data-model.md)
    ├── relations.py               # measuring relations (R-6)
    ├── pictures.py                # PNG pictures (R-11)
    └── report.py
tests/
├── fixtures/                      # test templates, kits, laid-out cities (not game content)
└── test_*.py
.gitignore                         # adds Spec Kit's Python lines and Harmony's bin/ and obj/ (R-9)
```

**Structure Decision**: the repository root stays the mod's folder (R1 research R-1). Mantle's code is the first code
in it, in `ModUpdating.txt`'s `Source/` and `Assemblies/`; its definitions in `Defs/` with folders named as `Data/`
names its own. The check lives beside them as a Python package in Spec Kit's layout; the game loads none of
`pyproject.toml`, `src/` or `tests/`.

## Complexity Tracking

No Constitution Check violations. Principle IV is pending one answer (R-8), not violated.
