---

description: "Task list for R13, templates and kits"
---

# Tasks: Templates and kits

**Input**: Design documents from `/specs/002-templates-and-kits/`

**Prerequisites**: [plan.md](plan.md), [spec.md](spec.md), [research.md](research.md), [data-model.md](data-model.md),
[contracts/](contracts/), [quickstart.md](quickstart.md)

**Tests**: Included. The spec asks for them: each user story's Independent Test, SC-001, and research R-12, which runs
pytest over test files written by hand before the check in the game.

**Organization**: Tasks are grouped by user story, so that each story can be built and tested on its own. The first
kits and templates, which are game content rather than a story, have a phase of their own after the stories they use.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (US1 to US5)
- Include exact file paths in descriptions

## Path Conventions

- Paths are relative to the repository root, which holds Imperium's mod folder `Imperium/` and Mantle's `Mantle/` side
  by side, and at the root the files that serve both mods: the check's `pyproject.toml`, `src/` and `tests/`, and
  `readings/` (R14 `specs/003-mantle-mod/contracts/repository-layout.md`; plan, Project Structure).
- `template-references/` is the project's files folder, outside every repository (spec FR-028).

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: The check's package at the repository root and Mantle's C# project in `Mantle/Source/`

- [ ] T001 Create `pyproject.toml` declaring the package `mantle-check` in `src/mantle_check/` with the command
  `mantle-check`, Python 3.11 or later, Typer and Pillow, Hatchling, and a `test` extra with pytest (research R-9;
  contracts/check-command.md, Install and run)
- [ ] T002 [P] Add Spec Kit's Python lines and Harmony's `[Bb]in/` and `[Oo]bj/` lines to `.gitignore`
  (research R-9, Ignored files)
- [ ] T003 [P] Create `Mantle/Source/Directory.Build.props` with `RimWorldAssemblyDir`, and
  `Mantle/Source/Mantle/Mantle.csproj` targeting `net10.0`, referencing the game's assemblies through that property
  without copying them, and writing `Assemblies/Mantle.dll` (research R-2)
- [ ] T004 [P] Create `src/mantle_check/__init__.py` and `tests/conftest.py`, which takes `Data/` from
  `RIMWORLD_DATA_DIR`, fails with a message naming the variable when it is unset, and gives tests a helper that writes a
  small reference picture into a temporary folder (research R-12)

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Reading `Data/`, the mods and the forms, and the report and command every story uses

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [ ] T005 Implement reading `Data/` in `src/mantle_check/gamedata.py`: `Version.txt` must name 1.7; every XML
  file under each expansion's and each `--mod`'s `Defs/`; each `About/About.xml`'s `packageId` and `modDependencies`;
  inheritance by `Name`, `Abstract`, `ParentName` and `Inherit="False"`; each definition's origin; and the fields
  research R-10 lists under What it reads from each definition
- [ ] T006 [P] Implement the common forms in `src/mantle_check/forms.py`: rect, layer, position, size,
  minMapSize, rotation and `MayRequire` (data-model.md, Common forms)
- [ ] T007 Implement reading templates in `src/mantle_check/forms.py`: data-model.md `TemplateDef.defName`,
  `TemplateDef.kit`, `TemplateDef.reference`, `TemplateDef.allowedBiomes`, `TemplateDef.allowedRivers`,
  `TemplateDef.naturalEnemy`, `TemplateDef.permanentEnemy`, `TemplateDef.minMapSize`, `TemplateDef.terrainShape` and
  `TemplateDef.skeleton`; `TerrainShape.terrain`, `TerrainShape.rocks`, `TerrainShape.roofs`, `TerrainShape.features`
  and `Feature.flowsFrom`; `Skeleton.parts`, `Skeleton.relations`, `Part.kind`, `Part.optional` and
  `Relation.relation` with the field each kind needs (contracts/template-and-kit-defs.md, A template)
- [ ] T008 Implement reading kits in `src/mantle_check/forms.py`: data-model.md `KitDef.defName`,
  `KitDef.nameMaker`, `KitDef.skeleton`, `KitDef.wallSettings`, `KitDef.groups`, `KitDef.fill` and
  `KitDef.blockLibrary`, with `Group.size` and `SpecCard.size` (contracts/template-and-kit-defs.md, A kit)
- [ ] T009 Implement reading laid-out cities and readings in `src/mantle_check/forms.py`: data-model.md
  `LaidOutCity.template`, `LaidOutCity.kit`, `LaidOutCity.reference`, `LaidOutCity.size`, `LaidOutCity.terrain`,
  `LaidOutCity.roofs`, `LaidOutCity.things`, `LaidOutCity.parts`, `LaidOutCity.features`, `Thing.rect` and
  `Thing.stuff` (contracts/laid-out-city.md)
- [ ] T010 Implement the report in `src/mantle_check/report.py`: problems numbered and sorted, each with its
  file, template, kit, city or spec card, part or field, cell and what is wrong; written to standard output and
  `report.txt`; ending with the statement that testing in the game is the final check and is still to come; no time,
  path or random value in it (data-model.md, Report and pictures; spec FR-019, FR-020, FR-022)
- [ ] T011 Implement the command in `src/mantle_check/cli.py` with `--data`, `--out`, `--mod`, `--reference`
  and files; refuse an output folder inside a repository, a `--mod` folder without `About/About.xml`, `Data/` missing
  or not 1.7, and a file that is not XML, each with exit status 2; exit 0 with no problem and 1 with problems
  (contracts/check-command.md)
- [ ] T012 [P] Write Mantle's definition classes in `Mantle/Source/Mantle/TemplateDef.cs` (data-model.md `TemplateDef`,
  with `naturalEnemy` and `permanentEnemy` as `bool`, false by default), `Mantle/Source/Mantle/KitDef.cs`
  (data-model.md `KitDef`), `Mantle/Source/Mantle/Skeleton.cs` (Skeleton, Part, Relation and their kinds) and
  `Mantle/Source/Mantle/Cells.cs` (rects, layers, features, Group, SpecCard) (research R-1, R-5)

**Checkpoint**: The forms read and the command runs; user stories can begin

---

## Phase 3: User Story 1 - Check a template or kit against the game (Priority: P1) 🎯 MVP

**Goal**: The check reports every problem of a template or kit against `Data/` and the mods it is given

**Independent Test**: Test templates and kits, each holding one known kind of problem and one holding none, are
checked, and each report lists exactly the problems its file holds (spec, User Story 1)

### Tests for User Story 1

- [ ] T013 [P] [US1] Write two test mods in `tests/fixtures/mods/`: one whose `About/About.xml` requires no
  expansion, as Mantle's does, and one that requires Royalty, as Imperium does (spec FR-015)
- [ ] T014 [P] [US1] Write test templates and kits in `tests/fixtures/us1/`, each holding one problem of
  data-model.md, What the check reports: unknown definition; wrong kind (a terrain that is not natural, a `wallDef`
  that is not a wall, an unknown part or relation kind, a relation missing its field); other expansion (a Biotech
  definition unmarked, and a Royalty definition unmarked in a kit of each test mod); outside the map; no terrain;
  unknown name; duplicate name; no kit; a building on a template's cell; and one template and kit with none
- [ ] T015 [US1] Write `tests/test_templates_and_kits.py`: each fixture of T014 gives exactly its problem with
  its cell, the Royalty definition is reported only in the kit of the mod that does not require Royalty, the clean
  pair gives none and exit status 0, and every report ends with the statement of FR-020 (spec, User Story 1,
  scenarios 1-6; SC-001, SC-004)
- [ ] T016 [P] [US1] Write `tests/test_command.py`: `Data/` missing, `Version.txt` of another version, a `--mod`
  folder without `About/About.xml`, an output folder inside the repository and a file that is not XML each give exit
  status 2 and report nothing as passing (contracts/check-command.md, Exit status; spec, Edge Cases)

### Implementation for User Story 1

- [ ] T017 [US1] Implement unknown definition and wrong kind in `src/mantle_check/checks.py`: names found
  neither in `Data/` nor in the given mods' `Defs/`, and names where their kind cannot go: natural terrain, rock and
  roofs only in data-model.md `TerrainShape.terrain`, `TerrainShape.rocks` and `TerrainShape.roofs`, a wall in
  `KitDef.wallSettings` and in `KitDef.fill`'s `wallDef`, a material `doorDef` takes in `KitDef.fill`'s
  `doorStuffDef`, a `BiomeDef` in `TemplateDef.allowedBiomes`, a `RiverDef` in `TemplateDef.allowedRivers`, a
  `RulePackDef` in `KitDef.nameMaker`, and a known `Part.kind` and `Relation.relation`; and wrong form, not square and
  missing field as data-model.md, What the check reports, lists them (spec FR-013, FR-014; research R-4)
- [ ] T018 [US1] Implement other expansion in `src/mantle_check/checks.py`: a definition of an expansion that
  the mod holding the file does not require, without that expansion's `MayRequire`, a laid-out city or reading held
  as spec FR-015 sets (spec FR-015; research R-3)
- [ ] T019 [US1] Implement outside the map, no terrain, unknown name and no kit for templates and kits in
  `src/mantle_check/checks.py`, against data-model.md `TemplateDef.kit`, `TemplateDef.minMapSize`,
  `TerrainShape.features`, `Skeleton.parts`, `Skeleton.relations` and `Group.size` (spec FR-016, FR-017)
- [ ] T020 [US1] Run the checks of T017 to T019 from `src/mantle_check/cli.py` on each template and kit file
  given, and pass T015 and T016

**Checkpoint**: User Story 1 works on its own: the MVP

---

## Phase 4: User Story 2 - Compare a laid-out city with its reference (Priority: P2)

**Goal**: The check checks a laid-out city, measures each skeleton relation in it, and draws it beside its reference
pictures

**Independent Test**: Laid-out cities written by hand from a test template and kit, one with a known problem, one that
breaks a relation and one with neither, each given with a test reference picture (spec, User Story 2)

### Tests for User Story 2

- [ ] T021 [P] [US2] Write a test template and kit and laid-out cities from them in `tests/fixtures/us2/`: a
  granite block wall on marshy soil; a thing whose `rect` does not match its definition's size; a material the
  definition does not take; a part that is not optional left without cells; each relation kind broken once; an
  optional part left out; and one city with no problem (data-model.md, What the check reports)
- [ ] T022 [US2] Write `tests/test_laid_out_city.py`: each fixture of T021 gives exactly its problem; each
  relation is `holds`, `broken` or `not measured` as its fixture sets; a city given with a reference picture gives
  `<out>/<city file name>.png` and `<out>/<city file name>.side-by-side.png`; a missing or unreadable picture gives a
  no comparison problem without stopping the run (spec, User Story 2, scenarios 1-4; Edge Cases)

### Implementation for User Story 2

- [ ] T023 [US2] Implement the checks of a laid-out city in `src/mantle_check/checks.py`: cells outside its
  map and cells without terrain (data-model.md `LaidOutCity.size`, `LaidOutCity.terrain`), a template or kit that
  does not exist or a kit that is not the template's (`LaidOutCity.template`, `LaidOutCity.kit`), affordance, with the
  material's affordance where the definition says so, size against `Thing.rect`, material against `Thing.stuff`, and
  missing part (`LaidOutCity.things`, `LaidOutCity.parts`; spec FR-016, FR-017, FR-018, FR-029)
- [ ] T024 [US2] Implement measuring relations in `src/mantle_check/relations.py`: `Inside`, `Adjoins`,
  `Across`, `SameSide`, `Upstream` and `Farther` as research R-6 reads them on cells, and not measured where an
  optional part is left out (data-model.md, Skeleton; spec FR-029)
- [ ] T025 [US2] Implement the grid drawing in `src/mantle_check/pictures.py`: square cells, a thin line between
  cells and a stronger one every 10 numbered on all four edges as `x` and `z` with north at the top, fills from each
  definition's `color` or a colour drawn from its name, a legend by `label` naming each expansion other than the base
  game, and each problem marked at its cell with its number (research R-11; spec FR-023, FR-026, FR-027)
- [ ] T026 [US2] Draw laid-out cities in `src/mantle_check/pictures.py` with each thing in place and each part
  and feature outlined and named, and the side-by-side picture with each whole reference picture, read as JPEG, PNG or
  WebP, at the same height (research R-11; spec FR-025, FR-028)
- [ ] T027 [US2] Report each relation's result and the reference pictures set beside each city in
  `src/mantle_check/report.py`, run all of it from `src/mantle_check/cli.py` for laid-out city files,
  and pass T022 (contracts/check-command.md, Output)

**Checkpoint**: User Stories 1 and 2 work on their own

---

## Phase 5: User Story 3 - See a template as a picture of its site (Priority: P3)

**Goal**: Each checked template is drawn as its site, with its skeleton, beside its reference pictures

**Independent Test**: A small test template with a known terrain shape and skeleton is checked, and each cell, part
and relation in its picture is compared with the template (spec, User Story 3)

### Tests for User Story 3

- [ ] T028 [P] [US3] Write a test template in `tests/fixtures/us3/` with a known terrain shape, a river feature,
  a skeleton that relates a palace quarter to the river, and one problem at one cell
- [ ] T029 [US3] Write `tests/test_template_picture.py`: each cell's colour in `<out>/<defName>.png` is its
  terrain's, the coordinates run along the edges, the problem's cell is marked with its number, the parts and the
  relation are named, and a template given reference pictures gets a side-by-side picture (spec, User Story 3,
  scenarios 1-3)

### Implementation for User Story 3

- [ ] T030 [US3] Draw templates in `src/mantle_check/pictures.py`: the terrain shape on the grid of T025 with
  each feature named, and the skeleton's parts and relations as a named diagram beside it, since a template's parts
  have no cells (research R-11; spec FR-023)
- [ ] T031 [US3] Set a template's picture beside its reference pictures, named by `TemplateDef.reference` in
  data-model.md, in `src/mantle_check/pictures.py`, and pass T029 (spec FR-025)

**Checkpoint**: User Stories 1 to 3 work on their own

---

## Phase 6: User Story 4 - Check and see a kit's buildings (Priority: P4)

**Goal**: Each spec card of a kit's block library is checked and drawn as its building

**Independent Test**: A test kit with a block library of two spec cards, one with a known problem, is checked, and the
report and the two pictures are compared with the cards (spec, User Story 4)

### Tests for User Story 4

- [ ] T032 [P] [US4] Write a test kit with a block library of two spec cards in `tests/fixtures/us4/`, one
  naming a definition `Data/` does not hold
- [ ] T033 [US4] Write `tests/test_spec_cards.py`: the unknown name is reported with its cell, and a room or thing
  past its plot is reported with its cell (spec, User Story 4, scenarios 1-2)

### Implementation for User Story 4

- [ ] T034 [US4] Check spec cards in `src/mantle_check/checks.py`, with every cell inside its plot
  (data-model.md `KitDef.blockLibrary` and SpecCard; spec FR-007); pass T033

**Checkpoint**: User Stories 1 to 4 work on their own

---

## Phase 7: The first kits and templates

**Purpose**: The game content this feature holds, taken from readings and checked with the stories above (spec FR-031,
FR-032, FR-036, FR-037, FR-039, FR-040; research R-13, R-14)

### The Empire and the river-bend town, which calibrate the method first

- [ ] T035 Add Mantle to `Imperium/About/About.xml`: a `modDependencies` entry with `Neiro.RimWorld.Mantle`, the
  `displayName` `Mantle` and the repository's page as `downloadUrl`, and `Neiro.RimWorld.Mantle` in `loadAfter`
  (research R-1); and change the place sentence of `Imperium/README.md` so that Imperium is enabled directly below
  Mantle (R14 research R-7)
- [ ] T036 [P] Write the Empire's word list as a `RulePackDef` in
  `Imperium/Defs/RulePackDefs/RulePacks_Namers_Empire.xml`, named by type and then by what it holds, as `Data/` names
  its own (`Royalty/Defs/RulePackDefs/RulePacks_Namers_Factions.xml`), with its words in
  `Imperium/Languages/English/Strings/`, from sources on Rome leaning toward New Rome (spec FR-011; research R-3)
- [ ] T037 Write the Empire kit in `Imperium/Defs/KitDefs/Kits_Empire.xml`, taken from the river-bend town's
  screenshot and render in `template-references/河湾城-原图与描线/` and `template-references/河湾城-最新版-1112/`:
  data-model.md `KitDef.nameMaker` (T036), `KitDef.skeleton`, `KitDef.wallSettings`, `KitDef.groups` and `KitDef.fill`
  (spec FR-006, FR-036; research R-8)
- [ ] T038 Write the river-bend town's template in `Imperium/Defs/TemplateDefs/Templates_Empire.xml`: its terrain shape
  inside 350×350 cells, its skeleton as research R-13 lists it, data-model.md `TemplateDef.allowedBiomes` set to
  `TemperateForest`, `TemperateSwamp`, `BorealForest`, `Tundra`, `ColdBog`, `IceSheet` and `SeaIce`,
  `TemplateDef.allowedRivers`, `TemplateDef.naturalEnemy` and
  `TemplateDef.permanentEnemy` left out, and `TemplateDef.reference` with the labels `screenshot` and `render`
  (spec FR-031, FR-040)
- [ ] T039 Check T037 and T038 with `--mod` for `Mantle/` and `Imperium/` and `--reference` for both pictures until no
  problem is reported, and put the side-by-side picture in the project's files for the maintainer, not in the pull
  request (quickstart.md step 5; spec SC-007, SC-008)

### The tribal culture, after the river-bend town passes the check

- [ ] T040 [P] Write the gentle tribe's reading in `readings/`, under the mod's own name for an open village,
  from `template-references/部落城-凯尔特/温和部落-TirUisce-3639186959.jpg`, set beside it until the maintainer accepts it,
  and add its item to `specs/002-templates-and-kits/checklists/acceptance.md` (data-model.md `LaidOutCity.reference`,
  A reading's acceptance; spec FR-029, FR-036, FR-037)
- [ ] T041 [P] Write the fierce tribe's reading in `readings/`, under the mod's own name for a walled
  stronghold, from `template-references/部落城-凯尔特/凶猛部落-Oppidum-3625652909.jpg`, the same way (spec FR-036, FR-037)
- [ ] T042 [P] Write the savage tribe's reading in `readings/`, under the mod's own name for a fortress, from
  `template-references/部落城-凯尔特/野蛮部落-小山堡-3621994739.jpg`, the same way; the agricultural island is only looked
  at beside the three, and nothing is taken from it (spec FR-036, FR-037)
- [ ] T043 Write the tribal kit in `Mantle/Defs/KitDefs/Kits_Tribal.xml`, taken from the three accepted readings:
  data-model.md `KitDef.nameMaker` as the base game's `NamerSettlementTribal`, `KitDef.skeleton`,
  `KitDef.wallSettings`, `KitDef.groups` and `KitDef.fill`, with base-game definitions only, or expansion content
  marked (spec FR-006, FR-011, FR-015)
- [ ] T044 Write the three tribal templates in `Mantle/Defs/TemplateDefs/Templates_Tribal.xml`, one from each reading,
  each with its reading's extent as data-model.md `TemplateDef.minMapSize` (spec FR-037), `TemplateDef.allowedBiomes`
  left empty and its tribe's attitude in
  `TemplateDef.naturalEnemy` and `TemplateDef.permanentEnemy`: neither for the open village, `naturalEnemy` for the
  walled stronghold, `permanentEnemy` for the fortress (spec FR-038, FR-039; research R-14)
- [ ] T045 Check the three readings with their pictures, then T043 and T044, until no problem is reported, and put the
  side-by-side pictures in the project's files for the maintainer (quickstart.md step 6; spec SC-010)

**Checkpoint**: Both cultures' kits and first templates pass the check outside the game

---

## Phase 8: User Story 5 - Add a culture by copying one (Priority: P5)

**Goal**: An author copies a culture and checks it with nothing shared changed

**Independent Test**: The Empire kit and the river-bend town's template are copied into a test culture, changed, and
checked, and no shared file changes (spec, User Story 5)

### Tests for User Story 5

- [ ] T046 [P] [US5] Write a test piece, a definition of a test mod in `tests/fixtures/mods/`, and a test kit
  that names it in `tests/fixtures/us5/` (spec, User Story 5, scenario 2)
- [ ] T047 [US5] Write `tests/test_copied_culture.py`: copy `Kits_Empire.xml` and `Templates_Empire.xml` into a
  temporary folder under a test culture's name, change its word list, wall settings and one relation, and check that
  the report and pictures follow the changes and name the new culture, that the piece of T046 is found, and that no
  shared file changed (spec, User Story 5, scenario 1; SC-009)

### Implementation for User Story 5

- [ ] T048 [US5] Name each template's and kit's culture by data-model.md `KitDef.defName` in
  `src/mantle_check/report.py` and `src/mantle_check/pictures.py`, so that a copy is reported and drawn
  under its new culture, with nothing a culture must define added to the shared check, and pass T047 (spec FR-033,
  FR-034)

**Checkpoint**: All user stories work on their own

---

## Phase 9: Polish & Cross-Cutting Concerns

**Purpose**: What spans the stories, and the load in the game

- [ ] T049 [P] Write `tests/test_same_files.py`: two runs on the same inputs give byte-identical reports and
  pictures (spec FR-022; quickstart.md step 2)
- [ ] T050 [P] On the maintainer's computer, time checking and drawing the river-bend town against the game,
  launched without `-quicktest` with Royalty, Mantle and Imperium, reaching its main menu (spec SC-003; quickstart.md
  step 9)
- [ ] T051 Build `Mantle/Assemblies/Mantle.dll` from `Mantle/Source/Mantle/` in the maintainer's clone through
  Remote Control, stopping and saying so if the .NET 10 SDK is missing, and commit it (research R-2)
- [ ] T052 Copy `Mantle/` and `Imperium/` from the clone into the game's `Mods` (R14 quickstart.md, Prerequisites), and
  launch the game with `-quicktest` and `-savedatafolder=SaveData` with no mod, with Mantle alone, and with Royalty,
  Mantle and Imperium, and compare each `Player.log` with the first: neither mod adds an error or warning
  about its definitions or assembly (quickstart.md, In the game; research R-12)
- [ ] T053 Run every step of quickstart.md and record the results in the pull request, and check the code in
  `Mantle/Source/` against R14's `checklists/layout.md` CHK020 and CHK021 before the pull request merges

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: needs R14's mod folders and Mantle's `packageId`, merged in #27 (research R-1)
- **Foundational (Phase 2)**: depends on Setup; blocks every story
- **User Stories 1 to 4 (Phases 3 to 6)**: depend on Foundational; User Story 2 uses the check of User Story 1, and
  User Stories 3 and 4 use the grid drawing of User Story 2 (T025)
- **The first kits and templates (Phase 7)**: depends on User Stories 1 to 3; the river-bend town (T035 to T039)
  comes before the tribal culture (T040 to T045) (spec FR-031, SC-008)
- **User Story 5 (Phase 8)**: depends on the Empire kit and the river-bend town's template (T037, T038)
- **Polish (Phase 9)**: depends on all before it; T051 and T052 need the maintainer's computer, with the clone moved
  out of `Mods` as R14's T007 sets up

### Within Each User Story

- Fixtures and tests are written first and fail before the implementation
- Reading before checking, checking before drawing, drawing before the command runs it

### Parallel Opportunities

- T002, T003 and T004 in Setup
- T006 and T012 in Foundational, beside the reading tasks
- In each story, its fixtures beside its other test files
- T040, T041 and T042, the three tribal readings
- T049 and T050 in Polish

---

## Parallel Example: User Story 1

```text
Task: "Write two test mods in tests/fixtures/mods/"
Task: "Write test templates and kits in tests/fixtures/us1/"
Task: "Write tests/test_command.py"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational
3. Complete Phase 3: User Story 1
4. **Stop and validate**: run its tests and quickstart.md steps 1, 3 and 4

### Incremental Delivery

1. Setup and Foundational, then User Story 1: the check reports problems (MVP)
2. User Story 2: laid-out cities and the comparison
3. User Story 3: templates as pictures beside their references
4. User Story 4: spec cards
5. The river-bend town and the Empire kit, then the three tribal templates and the tribal kit
6. User Story 5: a copied culture
7. Polish, and the load in the game

---

## Notes

- [P] tasks touch different files and depend on no unfinished task
- [Story] labels map tasks to the spec's user stories
- Reference pictures, side-by-side pictures and the game's files never go into a repository (spec FR-021, FR-028)
- Placing templates on a map in the game, the final check, comes with R2 for the tribal culture and R15 for the
  Empire (spec, Assumptions)
