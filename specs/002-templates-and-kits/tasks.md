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

- [X] T001 Create `pyproject.toml` declaring the package `mantle-check` in `src/mantle_check/` with the command
  `mantle-check`, Python 3.11 or later, Typer and Pillow, Hatchling, and a `test` extra with pytest (research R-9;
  contracts/check-command.md, Install and run)
- [X] T002 [P] Add Spec Kit's Python lines and Harmony's `[Bb]in/` and `[Oo]bj/` lines to `.gitignore`
  (research R-9, Ignored files)
- [X] T003 [P] Create `Mantle/Source/Directory.Build.props` with `RimWorldAssemblyDir`, and
  `Mantle/Source/Mantle/Mantle.csproj` targeting `net10.0`, referencing the game's assemblies through that property
  without copying them, and writing `Assemblies/Mantle.dll` (research R-2)
- [X] T004 [P] Create `src/mantle_check/__init__.py` and `tests/conftest.py`, which takes `Data/` from
  `RIMWORLD_DATA_DIR`, fails with a message naming the variable when it is unset, and gives tests a helper that writes a
  small reference picture into a temporary folder (research R-12)

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Reading `Data/`, the mods and the forms, and the report and command every story uses

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [X] T005 Implement reading `Data/` in `src/mantle_check/gamedata.py`: `Version.txt` must name 1.7; every XML
  file under each expansion's and each `--mod`'s `Defs/`; each `About/About.xml`'s `packageId` and `modDependencies`;
  inheritance by `Name`, `Abstract`, `ParentName` and `Inherit="False"`; each definition's origin; and the fields
  research R-10 lists under What it reads from each definition
- [X] T006 [P] Implement the common forms in `src/mantle_check/forms.py`: rect, layer, position, size,
  minMapSize, rotation and `MayRequire` (data-model.md, Common forms)
- [X] T007 Implement reading templates in `src/mantle_check/forms.py`: data-model.md `TemplateDef.defName`,
  `TemplateDef.kit`, `TemplateDef.reference`, `TemplateDef.allowedBiomes`, `TemplateDef.allowedRivers`,
  `TemplateDef.naturalEnemy`, `TemplateDef.permanentEnemy`, `TemplateDef.minMapSize`, `TemplateDef.terrainShape` and
  `TemplateDef.skeleton`; `TerrainShape.terrain`, `TerrainShape.rocks`, `TerrainShape.roofs`, `TerrainShape.features`
  and `Feature.flowsFrom`; `Skeleton.parts`, `Skeleton.relations`, `Part.kind`, `Part.optional` and
  `Relation.relation` with the field each kind needs (contracts/template-and-kit-defs.md, A template)
- [X] T008 Implement reading kits in `src/mantle_check/forms.py`: data-model.md `KitDef.defName`,
  `KitDef.nameMaker`, `KitDef.skeleton`, `KitDef.wallSettings`, `KitDef.groups`, `KitDef.fill` and
  `KitDef.blockLibrary`, with `Group.size` and `SpecCard.size` (contracts/template-and-kit-defs.md, A kit)
- [X] T009 Implement reading laid-out cities and readings in `src/mantle_check/forms.py`: data-model.md
  `LaidOutCity.template`, `LaidOutCity.kit`, `LaidOutCity.reference`, `LaidOutCity.size`, `LaidOutCity.terrain`,
  `LaidOutCity.roofs`, `LaidOutCity.things`, `LaidOutCity.parts`, `LaidOutCity.features`, `Thing.rect` and
  `Thing.stuff` (contracts/laid-out-city.md)
- [X] T010 Implement the report in `src/mantle_check/report.py`: problems numbered and sorted, each with its
  file, template, kit, city or spec card, part or field, cell and what is wrong; written to standard output and
  `report.txt`; ending with the statement that testing in the game is the final check and is still to come; no time,
  path or random value in it (data-model.md, Report and pictures; spec FR-019, FR-020, FR-022)
- [X] T011 Implement the command in `src/mantle_check/cli.py` with `--data`, `--out`, `--mod`, `--reference`
  and files; refuse an output folder inside a repository, a `--mod` folder without `About/About.xml`, `Data/` missing
  or not 1.7, and a file that is not XML, each with exit status 2; exit 0 with no problem and 1 with problems
  (contracts/check-command.md)
- [X] T012 [P] Write Mantle's definition classes in `Mantle/Source/Mantle/TemplateDef.cs` (data-model.md `TemplateDef`,
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

- [X] T013 [P] [US1] Write two test mods in `tests/fixtures/mods/`: one whose `About/About.xml` requires no
  expansion, as Mantle's does, and one that requires Royalty, as Imperium does (spec FR-015)
- [X] T014 [P] [US1] Write test templates, kits and readings in `tests/fixtures/us1/`, each holding one problem of
  data-model.md, What the check reports: unknown definition; wrong kind (a terrain that is not natural, a `wallDef` that
  is not a wall, a name that is not a `BiomeDef` in `allowedBiomes`, one that is not a `RiverDef` in `allowedRivers`,
  one that is not a `RulePackDef` in `nameMaker`, an unknown part or relation kind, a relation missing its field); wrong
  form (an attitude field that is neither `true` nor `false`, a `minMapSize` not in its form, a rotation that is not one
  of the four directions); not square (a `minMapSize` whose `x` and `z` differ); missing field (a template without
  `kit`, a template without `minMapSize`, a reading without `reference`); other expansion (a Biotech definition
  unmarked, a Royalty definition unmarked in a kit of each test mod, and a Biotech definition unmarked in a reading that
  no template names); outside the map; no terrain; unknown name; duplicate name; no kit; a building on a template's
  cell; and one template and kit with none
- [X] T015 [US1] Write `tests/test_templates_and_kits.py`: each fixture of T014 gives exactly its problem, with its cell
  where it has one, the Royalty definition is reported only in the kit of the mod that does not require Royalty, the
  Biotech definition in the reading that no template names is reported (spec FR-015), the clean pair gives none and exit
  status 0, and every report ends with the statement of FR-020 (spec, User Story 1, scenarios 1-6; SC-001, SC-004)
- [X] T016 [P] [US1] Write `tests/test_command.py`: `Data/` missing, `Version.txt` of another version, a `--mod`
  folder without `About/About.xml`, an output folder inside the repository and a file that is not XML each give exit
  status 2 and report nothing as passing (contracts/check-command.md, Exit status; spec, Edge Cases)

### Implementation for User Story 1

- [X] T017 [US1] Implement unknown definition and wrong kind in `src/mantle_check/checks.py`: names found
  neither in `Data/` nor in the given mods' `Defs/`, and names where their kind cannot go: natural terrain, rock and
  roofs only in data-model.md `TerrainShape.terrain`, `TerrainShape.rocks` and `TerrainShape.roofs`, a wall in
  `KitDef.wallSettings` and in `KitDef.fill`'s `wallDef`, a material `doorDef` takes in `KitDef.fill`'s
  `doorStuffDef`, a `BiomeDef` in `TemplateDef.allowedBiomes`, a `RiverDef` in `TemplateDef.allowedRivers`, a
  `RulePackDef` in `KitDef.nameMaker`, and a known `Part.kind` and `Relation.relation`; and wrong form, not square and
  missing field as data-model.md, What the check reports, lists them (spec FR-013, FR-014; research R-4)
- [X] T018 [US1] Implement other expansion in `src/mantle_check/checks.py`: a definition of an expansion that
  the mod holding the file does not require, without that expansion's `MayRequire`, a laid-out city or reading held
  as spec FR-015 sets (spec FR-015; research R-3)
- [X] T019 [US1] Implement outside the map, no terrain, unknown name and no kit for templates and kits in
  `src/mantle_check/checks.py`, against data-model.md `TemplateDef.kit`, `TemplateDef.minMapSize`,
  `TerrainShape.features`, `Skeleton.parts`, `Skeleton.relations` and `Group.size` (spec FR-016, FR-017)
- [X] T020 [US1] Run the checks of T017 to T019 from `src/mantle_check/cli.py` on each template and kit file
  given, and pass T015 and T016

**Checkpoint**: User Story 1 works on its own: the MVP

---

## Phase 4: User Story 2 - Compare a laid-out city with its reference (Priority: P2)

**Goal**: The check checks a laid-out city, measures each skeleton relation in it, and draws it beside its reference
pictures

**Independent Test**: Laid-out cities written by hand from a test template and kit, one with a known problem, one that
breaks a relation and one with neither, each given with a test reference picture (spec, User Story 2)

### Tests for User Story 2

- [X] T021 [P] [US2] Write a test template and kit and laid-out cities from them in `tests/fixtures/us2/`: a
  granite block wall on marshy soil; a thing whose `rect` does not match its definition's size; a material the
  definition does not take; a part that is not optional left without cells; each relation kind broken once; an
  optional part left out; and one city with no problem (data-model.md, What the check reports)
- [X] T022 [US2] Write `tests/test_laid_out_city.py`: each fixture of T021 gives exactly its problem; each
  relation is `holds`, `broken` or `not measured` as its fixture sets; a city given with a reference picture gives
  `<out>/<city file name>.png` and `<out>/<city file name>.side-by-side.png`; a missing or unreadable picture gives a
  no comparison problem without stopping the run (spec, User Story 2, scenarios 1-4; Edge Cases)

### Implementation for User Story 2

- [X] T023 [US2] Implement the checks of a laid-out city in `src/mantle_check/checks.py`: cells outside its
  map and cells without terrain (data-model.md `LaidOutCity.size`, `LaidOutCity.terrain`), a template or kit that
  does not exist or a kit that is not the template's (`LaidOutCity.template`, `LaidOutCity.kit`), affordance, with the
  material's affordance where the definition says so, size against `Thing.rect`, material against `Thing.stuff`, and
  missing part (`LaidOutCity.things`, `LaidOutCity.parts`; spec FR-016, FR-017, FR-018, FR-029)
- [X] T024 [US2] Implement measuring relations in `src/mantle_check/relations.py`: `Inside`, `Adjoins`,
  `Across`, `SameSide`, `Upstream` and `Farther` as research R-6 reads them on cells, and not measured where an
  optional part is left out (data-model.md, Skeleton; spec FR-029)
- [X] T025 [US2] Implement the grid drawing in `src/mantle_check/pictures.py`: square cells, a thin line between
  cells and a stronger one every 10 numbered on all four edges as `x` and `z` with north at the top, fills from each
  definition's `color` or a colour drawn from its name, a legend by `label` naming each expansion other than the base
  game, and each problem marked at its cell with its number (research R-11; spec FR-023, FR-026, FR-027)
- [X] T026 [US2] Draw laid-out cities in `src/mantle_check/pictures.py` with each thing in place and each part
  and feature outlined and named, and the side-by-side picture with each whole reference picture, read as JPEG, PNG or
  WebP, at the same height (research R-11; spec FR-025, FR-028)
- [X] T027 [US2] Report each relation's result and the reference pictures set beside each city in
  `src/mantle_check/report.py`, run all of it from `src/mantle_check/cli.py` for laid-out city files,
  and pass T022 (contracts/check-command.md, Output)

**Checkpoint**: User Stories 1 and 2 work on their own

---

## Phase 5: User Story 3 - See a template as a picture of its site (Priority: P3)

**Goal**: Each checked template is drawn as its site, with its skeleton, beside its reference pictures

**Independent Test**: A small test template with a known terrain shape and skeleton is checked, and each cell, part
and relation in its picture is compared with the template (spec, User Story 3)

### Tests for User Story 3

- [X] T028 [P] [US3] Write a test template in `tests/fixtures/us3/` with a known terrain shape, a river feature,
  a skeleton that relates a palace quarter to the river, and one problem at one cell
- [X] T029 [US3] Write `tests/test_template_picture.py`: each cell's colour in `<out>/<defName>.png` is its
  terrain's, the coordinates run along the edges, the problem's cell is marked with its number, the parts and the
  relation are named, and a template given reference pictures gets a side-by-side picture (spec, User Story 3,
  scenarios 1-3)

### Implementation for User Story 3

- [X] T030 [US3] Draw templates in `src/mantle_check/pictures.py`: the terrain shape on the grid of T025 with
  each feature named, and the skeleton's parts and relations as a named diagram beside it, since a template's parts
  have no cells (research R-11; spec FR-023)
- [X] T031 [US3] Set a template's picture beside its reference pictures, named by `TemplateDef.reference` in
  data-model.md, in `src/mantle_check/pictures.py`, and pass T029 (spec FR-025)

**Checkpoint**: User Stories 1 to 3 work on their own

---

## Phase 6: User Story 4 - Check a kit's buildings (Priority: P4)

**Goal**: Each spec card of a kit's block library is checked

**Independent Test**: A test kit with a block library of three spec cards, one naming a definition `Data/` does not
hold, one with a room or thing past its plot and one with neither, is checked, and the report is compared with the cards
(spec, User Story 4)

### Tests for User Story 4

- [X] T032 [P] [US4] Write a test kit with a block library of three spec cards in `tests/fixtures/us4/`: one naming a
  definition `Data/` does not hold, one with a room or thing past its plot, and one with neither
- [X] T033 [US4] Write `tests/test_spec_cards.py`: the unknown name is reported with its cell, the room or thing past
  its plot is reported with its cell, and the third card gives none (spec, User Story 4, scenarios 1-2)

### Implementation for User Story 4

- [X] T034 [US4] Check spec cards in `src/mantle_check/checks.py`, with every cell inside its plot
  (data-model.md `KitDef.blockLibrary` and SpecCard; spec FR-007); pass T033

**Checkpoint**: User Stories 1 to 4 work on their own

---

## Phase 7: The first kits and templates

**Purpose**: The game content this feature holds, taken from readings and checked with the stories above (spec FR-031,
FR-032, FR-036, FR-037, FR-039, FR-040; research R-13, R-14), and the drawing of any preset reference read from its
game's data (spec FR-041 to FR-045; research R-15). Every kit and template here is derived in the order of spec
FR-047, Imperium-old's design first, then the maintainer's recorded direction, and a reading only where both are
silent, each part naming its source (research R-13). The industrial (outlander) and pirate cultures' kits and
templates are R16's, not this feature's (spec FR-032)

### The Empire and the river-bend town, which calibrate the method first

- [X] T035 Add Mantle to `Imperium/About/About.xml`: a `modDependencies` entry with `Neiro.RimWorld.Mantle`, the
  `displayName` `Mantle` and the repository's page as `downloadUrl`, and `Neiro.RimWorld.Mantle` in `loadAfter`
  (research R-1); and change the place sentence of `Imperium/README.md` so that Imperium is enabled directly below
  Mantle (R14 research R-7)
- [X] T036 [P] Write the Empire's word list as a `RulePackDef` in
  `Imperium/Defs/RulePackDefs/RulePacks_Namers_Empire.xml`, named by type and then by what it holds, as `Data/` names
  its own (`Royalty/Defs/RulePackDefs/RulePacks_Namers_Factions.xml`), with its words in
  `Imperium/Languages/English/Strings/`, from sources on Rome leaning toward New Rome (spec FR-011; research R-3)
- [X] T037 Write the Empire kit in `Imperium/Defs/KitDefs/Kits_Empire.xml`, taken from the river-bend town's
  screenshot and render in `template-references/河湾城-原图与描线/` and `template-references/河湾城-最新版-1112/`:
  data-model.md `KitDef.nameMaker` (T036), `KitDef.skeleton`, `KitDef.wallSettings`, `KitDef.groups` and `KitDef.fill`
  (spec FR-006, FR-036; research R-8)
- [X] T038 Write the river-bend town's template in `Imperium/Defs/TemplateDefs/Templates_Empire.xml`: its terrain shape
  inside 350×350 cells, its skeleton as research R-13 lists it, data-model.md `TemplateDef.allowedBiomes` set to
  `TemperateForest`, `TemperateSwamp`, `BorealForest`, `Tundra`, `ColdBog`, `IceSheet`, `SeaIce` and `GlacialPlain`, the
  last marked `MayRequire="Ludeon.RimWorld.Odyssey"` (research R-14), `TemplateDef.allowedRivers`,
  `TemplateDef.naturalEnemy` and `TemplateDef.permanentEnemy` left out, and `TemplateDef.reference` with the labels
  `screenshot` and `render` (spec FR-015, FR-031, FR-040)
- [X] T039 Check T037 and T038 with `--mod` for `Mantle/` and `Imperium/` and `--reference` for both pictures until no
  problem is reported, and put the side-by-side picture in the project's files for the maintainer, not in the pull
  request (quickstart.md step 5; spec SC-007, SC-008)

### The tribal culture, after the river-bend town passes the check

- [ ] T040 [P] Write the gentle tribe's reading in `readings/`, under the mod's own name for an open village, from the
  reference the maintainer chooses for it, shown from above (spec FR-037, FR-052), in the steps of spec FR-048 to
  FR-050, with T059 to T061 done, set beside it until the maintainer accepts it, and add its items to
  `specs/002-templates-and-kits/checklists/acceptance.md`, one after each area is traced and one after it is laid out
  (data-model.md `LaidOutCity.reference`, `scale`, `from`, A reading's acceptance; spec FR-029, FR-036, FR-050;
  research R-17)
- [ ] T041 [P] Write the fierce tribe's reading in `readings/`, under the mod's own name for a walled
  stronghold, from the reference the maintainer chooses for it, shown from above, the same way (spec FR-036, FR-037,
  FR-052)
- [ ] T042 [P] Write the savage tribe's reading in `readings/`, under the mod's own name for a fortress, from the
  reference the maintainer chooses for it, shown from above, the same way; the agricultural island is only looked at
  beside the three, and nothing is taken from it (spec FR-036, FR-037, FR-052)
- [ ] T043 Write the tribal kit in `Mantle/Defs/KitDefs/Kits_Tribal.xml`, derived in the order of spec FR-047, with the
  three accepted readings filling what the design and the recorded direction leave open, each part naming its source
  (research R-13): data-model.md `KitDef.nameMaker` as the base game's `NamerSettlementTribal`, `KitDef.skeleton`,
  `KitDef.wallSettings`, `KitDef.groups` and `KitDef.fill`, with base-game definitions only, or expansion content marked
  (spec FR-006, FR-011, FR-015)
- [ ] T044 Write the three tribal templates in `Mantle/Defs/TemplateDefs/Templates_Tribal.xml`, one from each reading,
  derived in the order of spec FR-047 as T043 is, each with its reading's extent as data-model.md
  `TemplateDef.minMapSize` (spec FR-037), `TemplateDef.allowedBiomes` left empty and its tribe's attitude in
  `TemplateDef.naturalEnemy` and `TemplateDef.permanentEnemy`: neither for the open village, `naturalEnemy` for the
  walled stronghold, `permanentEnemy` for the fortress (spec FR-038, FR-039; research R-14)
- [ ] T045 Check the three readings with their pictures, then T043 and T044, until no problem is reported, and put the
  side-by-side pictures in the project's files for the maintainer (quickstart.md step 6; spec SC-010)

### A preset reference read from its game's data, before its reading

Only for a reference city that Anno 117 presets, once the maintainer chooses it; none of the tribal references chosen
so far is one (spec, Assumptions). On the maintainer's computer, outside every repository (research R-15).

- [ ] T054 Read the island from the game's own `file_h.db` and `.rda` packages, never the old project's index, cfg or
  cut files, and give each object its asset Template and the graphics folder its ConfigFilename names (spec FR-041,
  FR-042)
- [ ] T055 Draw step 1 into `template-references/`: each object as a dot coloured by category at its `(x, z)` on the
  cells, over the island's heightmap, turned to match the game's `mapimage.png`; the maintainer sees it before step 2
  (spec FR-043, FR-044)
- [ ] T056 Draw step 2 into `template-references/`: the skeleton, with linear pieces as lines, houses as markers and
  fields as squares, as a skeleton PNG and an overlay on `mapimage.png`, with `objects.json` and a summary; the
  maintainer sees it before step 3 (spec FR-043, FR-044; SC-011)
- [ ] T057 Optionally, once the packages holding the buildings' `.ifo` files are on the maintainer's computer, draw step
  3, each building's real footprint (spec FR-044; Edge Cases)
- [ ] T058 Cross-check what T054 to T056 read against the old project's output and images and, where it is at hand,
  FileDBReader, taking nothing from them, and confirm that neither the packages nor anything read or drawn is in the
  repository (spec FR-041, FR-045; quickstart.md step 10; SC-011)

### A template that leaves the land to generation, before the tribal templates

For T044, since a tribal reference that is a preset island is read for its skeleton only (spec FR-036; research R-18).

- [x] T062 Write, in `tests/fixtures/us1/` and `tests/test_templates_and_kits.py`, a template whose `terrain` holds no
  cell and one whose `terrain` holds some cells but not all, and report "no terrain" only for the second; then change
  the check in `src/mantle_check/checks.py` to that rule, keeping the report for every laid-out city; the picture of
  the first shows its features without terrain (data-model.md `TemplateDef.terrainShape`, What the check reports; spec
  FR-004, FR-016, FR-023, FR-036; research R-18)

### A reference that exists only as a picture, before its reading

For T040 to T042, in the steps of spec FR-048 to FR-052 (research R-17). They come before those three tasks, and the
tests come first and fail before the code, as in each story.

- [x] T059 Write a test reading, with a small reference picture the test makes itself and never a reference picture, and
  readings each holding one problem, in `tests/fixtures/us2/`; then write `tests/test_picture_reading.py`: a known
  `scale` puts a known cell at a known pixel of the reference picture in the side-by-side picture; a `pixelsPerCell`
  or `referenceCell` that is not a positive number, a `scale` with no `measured` thing, a `measured` thing without a
  `name` or a `rect`, a pixel `rect` of a `measured` thing or a `from` that lies outside the picture, a `use` outside
  the design's eight and a `use` without its `basis` are each reported, with the file, part and what is wrong; a
  reading without a `scale` is drawn as before and reported as before; and the same inputs give identical pictures
  and reports (spec FR-019, FR-022, FR-028, FR-048, FR-049, FR-051; SC-013; contracts/laid-out-city.md, A reading)
- [x] T060 Implement reading `scale`, with its `measured` things, `from` of a part or feature, and `use` and `basis` of
  a part in `src/mantle_check/forms.py`, and report each malformed one in `src/mantle_check/checks.py` as the problem
  "wrong scale, region or use", as T059 sets (data-model.md `LaidOutCity`, Common forms, What the check reports; spec
  FR-019, FR-048, FR-049; research R-17)
- [x] T061 In `src/mantle_check/pictures.py`, lay the cells of a reading that holds a `scale` over its reference
  picture in the side-by-side picture, at the pixels the `scale` gives from its `origin`, with each piece's name and number, the numbers of the problems at its cells and a legend, adding no picture or file name; in
  `src/mantle_check/report.py`, say for such a reading that mismatches are not marked and that no picture is reported
  as a match (contracts/check-command.md, Output); and pass T059 (research R-11, R-17; spec FR-020, FR-025, FR-029,
  FR-051; SC-014)

Not tasks: what is done with an area of which more than three tenths is unclear, and the marks of a piece that does
not match its picture in colour and shape. No source gives either form (spec FR-049, FR-051, marked NEEDS
CLARIFICATION; constitution, Principles IV and V). They are built only after a source or the maintainer's recorded
direction gives them, through the spec, plan and tasks again. No value is taken from the design's 3.7 "trace cells"
either, since no source says whether they are RimWorld cells (spec FR-048); `referenceCell` is written for each picture
by FR-048's steps.

**Checkpoint**: Both cultures' kits and first templates pass the check outside the game

---

### The river-bend town read again from its screenshot, better than the old preview (spec FR-052 to FR-057; research R-19 to R-28)

The render stops being the town's reading and becomes the comparison; T037 and T038 stand as drafts until the reading's
areas are accepted (spec FR-031). An area is accepted only by the maintainer's judgment of SC-018's pictures, the new
reading against the old sample and the screenshot (SC-017); the road and household checks are findings, places to look
again, and no number is a condition (SC-019; R-24). Each test is written first and fails before its implementation.

- [ ] T074 [P] Write, in `tests/fixtures/us1/` and `tests/fixtures/us2/readings/`, a template, a kit and a reading
  each holding one misspelled element, one holding an unknown attribute, and one holding an unknown element marked
  `IgnoreIfNoMatchingField="True"`, and `tests/test_unknown_fields.py`: the first two are reported as wrong form with
  the file and the element's name, the third is not; then make every reader in `src/mantle_check/forms.py` report the
  elements and attributes its form does not hold, and make `DefLayer` and `Feature` in `Mantle/Source/Mantle/Cells.cs`
  log each child they do not read with `Log.Error` (spec FR-014; research R-25)
- [ ] T064 Read a part's `kind`, `uncertain`, `because`, a road's `grade`, `width`, `widthFrom`, `line`, `leadsTo` and
  `wayInFrom`, `household`, and the reading's `ground` pairs in `src/mantle_check/forms.py`, reporting each value not in
  its form (data-model.md, LaidOutCity; spec FR-014, FR-052 to FR-055; research R-20, R-21)
- [ ] T063 [P] Write test readings in `tests/fixtures/us2/roads/`, each holding one road or household finding of
  data-model.md (road, household), among them a dangling road, a `leadsTo` with no `wayInFrom`, a yard outside its plot
  and a residence plot over one and a half estates, and one holding none, and `tests/test_roads.py`: each finding is
  listed with its cells among the findings and none among the problems, the exit status counts no finding, the clean
  reading lists none, a `RouteLine` counts as no road, and the road ends are counted by class and grade (spec FR-054,
  FR-055, SC-019; research R-21, R-24)
- [ ] T065 Read `KitDef.roads`, `KitDef.households` and `KitDef.cultures` (data-model.md) into Mantle's `KitDef` and
  the check, reporting a `cultures` entry that is not a `CultureDef`, a kit with none, and a `nameMaker` as deprecated;
  set the Empire's in `Imperium/Defs/KitDefs/Kits_Empire.xml` (`Sophian`, the grades and widths, eight directions, no
  dead ends, a plot for every household) without `nameMaker`, update the tests and fixtures that wrote a
  `nameMaker` or read the word list from the report (T046, T047), and add `Imperium/Patches/Faction_Empire_Names.xml`
  setting the Empire faction's `settlementNameMaker` to the Empire's word list (spec FR-006, FR-011, FR-032, FR-054,
  FR-055; research R-21, R-26)
- [ ] T066 Build `src/mantle_check/roads.py`: lay each road's cells from its line and width; find, as findings, every
  road and household case of data-model.md (road, household); sort every road end into its class; list every residence
  plot's size in reference cells; and count the shares of FR-053; and show them in `src/mantle_check/report.py` in a
  section of their own, numbered `L1` on, outside the exit status, until T063 passes (spec FR-053 to FR-055, SC-019;
  research R-21, R-24)
- [ ] T069 Write `tests/test_ground.py` (a test picture the test draws in a known perspective, four or more pairs,
  each pair's error reported, the tracing laid over the picture where the mapping puts it) and build
  `src/mantle_check/ground.py`, used by `src/mantle_check/pictures.py` (spec FR-052; research R-20)
- [ ] T067 [P] Write `tests/test_reading_picture.py` for FR-053's drawing and shares: each household's colour and
  plot, house and yard lines, one outline per building with an inner court open, grade labels, route lines and unsure
  pieces dashed, findings in orange with their `L` numbers, a legend with counts, a pixel ruler on the reference
  picture, and shares that add up to one; then build them in `src/mantle_check/pictures.py` and
  `src/mantle_check/report.py`, with `--crop` in `src/mantle_check/cli.py` (contracts/check-command.md; research R-24)
- [ ] T075 Write `tests/test_old_sample.py` with a small sample and mapping the test makes itself, never the old
  project's: its codes sorted into kinds, its findings and shares listed beside the reading's, the sample's area laid
  over the picture where the mapping puts it, and `compare-over.png` and `compare.png` drawn with each panel at the same
  width; then build `src/mantle_check/oldsample.py` and `--old-sample`, `--old-mapping` and `--old-area` in
  `src/mantle_check/cli.py` (spec FR-057, SC-018; research R-27)
- [ ] T068 Withdrawn: the wall circle's share and distance (spec FR-056) are built with R2's fitting of a town to its
  map; nothing of it is built here
- [ ] T070 Read the East Square area into `readings/RiverBendTown.xml` from
  `template-references/河湾城-原图与描线/原图-1596x1017.png` alone: size cells by person-sized things at several places
  (FR-048) and place the ground pairs (FR-052); trace each piece as a ground-level polygon of the screenshot in a working
  file kept with the area's pictures outside the repository, roads first as centre lines with grades and destinations,
  then households with plots, each piece with its region and each building or group with its use, and lay them onto
  cells through the reading's ground fit (research R-28); open the render's same area and the old tracing only after
  the tracing is drawn; check and draw it with `--reference`, `--crop` and the old sample; answer each finding by a
  change that names its region or by the piece left as read, never to make a finding go away (SC-019); record the
  minutes spent (spec FR-049, FR-050, FR-052, FR-053, FR-057, SC-015, SC-016). Waits for T063 to T069, T074, T075
- [ ] T071 Put the East Square pictures of SC-018 in the project's files, and add one item to
  `checklists/acceptance.md` naming the reading, the commit, the pictures, the minutes and, with its pixel region, each
  place where the old sample's same area shows a shortfall of FR-057, listed after the tracing was drawn, for the
  maintainer to judge whether the new reading reproduces the screenshot better than the old sample (spec FR-029,
  FR-050, FR-057, SC-016 to SC-018)
- [ ] T072 Read the town's other areas the same way, one at a time, each after the one before is accepted (spec
  FR-050)
- [ ] T073 Once every area is accepted, take the Empire kit, with the design's area spectra, and the river-bend
  template again from the reading in FR-047's order, replacing the drafts of T037 and T038, and check them as T039
  (spec FR-031, FR-053)

## Phase 8: User Story 5 - Add a culture by copying one (Priority: P5)

**Goal**: An author copies a culture and checks it with nothing shared changed

**Independent Test**: The Empire kit and the river-bend town's template are copied into a test culture, changed, and
checked, and no shared file changes (spec, User Story 5)

### Tests for User Story 5

- [X] T046 [P] [US5] Write a test piece, a definition of a test mod in `tests/fixtures/mods/`, and a test kit
  that names it in `tests/fixtures/us5/` (spec, User Story 5, scenario 2)
- [X] T047 [US5] Write `tests/test_copied_culture.py`: copy `Kits_Empire.xml` and `Templates_Empire.xml` into a
  temporary folder under a test culture's name, change its word list, wall settings and one relation, and check that
  the report and pictures follow the changes and name the new culture, that the piece of T046 is found, and that no
  shared file changed (spec, User Story 5, scenario 1; SC-009)

### Implementation for User Story 5

- [X] T048 [US5] Name each template's and kit's culture by data-model.md `KitDef.defName` in
  `src/mantle_check/report.py` and `src/mantle_check/pictures.py`, so that a copy is reported and drawn
  under its new culture, with nothing a culture must define added to the shared check, and pass T047 (spec FR-033,
  FR-034)

**Checkpoint**: All user stories work on their own

---

## Phase 9: Polish & Cross-Cutting Concerns

**Purpose**: What spans the stories, and the load in the game

- [X] T049 [P] Write `tests/test_same_files.py`: two runs on the same inputs give byte-identical reports and
  pictures (spec FR-022; quickstart.md step 2)
- [ ] T050 [P] On the maintainer's computer, time checking and drawing the river-bend town against the game,
  launched without `-quicktest` with Royalty, Mantle and Imperium, reaching its main menu (spec SC-003; quickstart.md
  step 9)
- [X] T051 Build `Mantle/Assemblies/Mantle.dll` from `Mantle/Source/Mantle/` in the maintainer's clone through
  Remote Control, stopping and saying so if the .NET 10 SDK is missing, and commit it (research R-2)
- [X] T052 Copy `Mantle/` and `Imperium/` from the clone into the game's `Mods` (R14 quickstart.md, Prerequisites), and
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
  comes before the tribal culture (T040 to T045) (spec FR-031, SC-008); T054 to T058 depend on nothing in the
  repository, and come before the reading of the preset reference they draw (spec FR-043); T059 to T061 come before
  T040 to T042 (spec FR-048 to FR-051; research R-17), and T062 before T044 (spec FR-036; research R-18); T063 to T068 depend on T059 to T061, T069 on T061, T070 on T063 to T069, T071 on
  T070, T072 on each area's acceptance, T073 on T072, and User Story 5 (T046 to T048) is rerun on T073's kit and
  template
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
- Reference pictures, side-by-side pictures and the game's files never go into a repository (spec FR-021, FR-028),
  nor does another game's package or anything read or drawn from it (spec FR-041)
- Spec FR-046 and FR-032's industrial (outlander) and pirate cultures record work for R16 and later slices, so no task
  here writes them (ROADMAP R16)
- Placing templates on a map in the game, the final check, comes with R2 for the tribal culture and R15 for the
  Empire (spec, Assumptions)

## Handoff after T059 to T062 (left unbuilt, none of it is committed)

T059 to T062 are done and tested, with the scale's `origin` and the names, numbers, grid-less legend, enlarged-picture overlay of
T061. Left, each to be written first as a test and each needing its source named (constitution, Principle VI):

- The design's nine classes of a piece (`class`), found in the old design's legend (Imperium-old,
  `designs/研究/城/纪元117-图例-2026-11-12.md`, section 二) and drawn in one colour each with a count of pieces.
- A household (`household`, `yardOf`) of pieces whose roofs are one building, outlined and named once, from Imperium-old
  `做法史/城建·生成流程.md` R-1112-2214 and `研究/城/纪元资料/民居与变体.md`; and the building kind and variant
  (`kind`, `variant`) of the legend's table of kinds, section 二·7.
- An `uncertain` mark (dashed outline, with `because`) from the legend's section 三, "拿不准".
- `anchors` (at least four pixel and cell-corner pairs) fitting a homography to straighten a slanted picture, from the
  research page `研究/城/纪元资料/河湾聚落尺度查证.md`, which names the homography ("单应"); how many points to take is
  not given there.
- A pixel ruler and grid on the picture, counts in the legend, and a `--font` option for Chinese names; none needs a source.
- Not buildable now: what counts as a piece not matching its picture (FR-051), which is only in the old tool's own
  documentation (`tools/city/说明/sample.md`), not in design meaning.

## Handoff: the East Square correction (2026-11-25)

Taken up in spec FR-052 to FR-056, research R-19 to R-23 and T063 to T073; what follows is the handoff as it was
written.

**Target** (the maintainer's broad direction, to be recorded in spec 002 first): the East Square reading delivers a
top-down picture on the game's cells of the same kind as the river-bend town's newest cell-level render: roads laid
first as one connected network, houses along the roads, and plots, yards, walls, trees and plazas as separate pieces,
in the render's proportions. The original screenshot stays the source of the reading and is set beside that render. No
cell-exact match to the render is asked for (FR-031). Any brief, spec text or acceptance item for this reading names
the render as a comparison.

**To resolve first**: FR-031 takes the screenshot as the source, while FR-052 forbids reading a picture the spec gives
no form for, such as one not shown from above, and the screenshot is oblique. The old project read this screenshot
through a straightened base image (Imperium-old `designs/tools/city/说明/sample.md` lines 6, 13 and 241, a tool
document). Whether any source gives that form is research for the plan.

**Design sources to read whole** (Imperium-old default branch, commit `b218bdc`, under `Imperium-Knowledge/`):
`现行/城/城建-生成流程.md` (lines 10-12 and 36); `现行/城/罗马城-做法与顺序.md` (lines 90, 144, 153-156 and
172-173); `现行/城/罗马城-城内.md` (lines 78, 97-98 and 134); `designs/研究/城/片区谱-广场住片.md`;
`designs/研究/城/布置思路.md`; `现行/城/地形与选址.md` (lines 33-34 and 83-90). The newest render is
`designs/回报/纪元样张/整张样张.png` with its cells in `样张格.json`; it is pixel-identical to
`template-references/河湾城-最新版-1112/` in the project's files. Rulings R-1114-0852 and R-1113-1543
(`09_地图生成与CBF技术.md` lines 977 and 975) are about plot cards, not about reading a town picture.

**Next, in Spec Kit's order**: update spec 002 (FR-031, FR-052, the clarifications and Edge Cases), then
`/speckit-plan` with the Constitution Check and `research.md`, with the recurring cost of each reading in the
Performance Goals or success criteria, then `/speckit-tasks` and `/speckit-analyze`, and only then
`/speckit-implement`.

**Draft code of the earlier trial**, local to the maintainer's clone and never pushed: `claude/east-square-demo`
(`f8bd238`) and `claude/east-square-lookup` (`46ba3cd`).

- `46ba3cd` builds with no warnings, and its `check` command runs. Its other commands were not rerun.
- Usable as a starting point if the plan chooses C#: `Tools/MantleCheck/Game.cs` (boots the installed game outside
  the game and reads `Data/` with the game's loader) and `Canvas.cs` (the game's PNG and font libraries), both first
  written in `f8bd238`. The check on this branch is Python (research R-9), and the draft is not wired to it.
- Not to be reused: its reading (kept outside the repository), where 4 of 7 declared road junctions are open, 8 of 23
  plots are partly covered by a road and 10 touch neither a road nor a plaza; the roof-colour score (`Sheets.cs`, `Propose.cs`),
  which proposed plot positions and ordered candidates of which only the first page of five was looked at; and the
  camera fitted by eye that lays game meshes over the oblique picture (`Camera.cs`, `Raster.cs`; FR-052).

A longer write-up in Chinese, with its sources, is in the project's files as
`东广场纠正-老库整城逻辑与昨晚复盘.md`.
