# Research: Templates and kits

Each decision names its source, from the constitution's Source Register, in the order the register gives: `Data/` of
RimWorld 1.7.5014, then `ModUpdating.txt`, then Harmony (`pardeike/HarmonyRimWorld`), for the released mod; `EULA.txt`
always; `Data/` for testing outside the game; `Readme.txt`, then RimBridgeServer with GABS, for testing in the game;
Spec Kit for the development workflow; GitHub Docs for repository files; Imperium-old `main` (20a052b), then the
maintainer's broad direction, for Imperium's own design. Line numbers refer to those files as copied into the project
files, to `Neiro-dev/Imperium-old` at 20a052b, to Spec Kit at v1.4.3 and to HarmonyRimWorld at `master`. `[Design]`,
`[Direction]` and the FR numbers point to [spec.md](spec.md).

## R-1: Templates and kits are Defs of Mantle's own types, in two mods

- **Decision**: a template is a `Mantle.TemplateDef` and a kit a `Mantle.KitDef`, written as XML in a mod's
  `Defs/TemplateDefs/` and `Defs/KitDefs/`. Their C# classes are Mantle's, in `Source/Mantle/` of Mantle's own mod,
  compiled into its `Assemblies/Mantle.dll`. Mantle's mod also holds the tribal culture's kit and first templates
  (`Defs/KitDefs/Kits_Tribal.xml`, `Defs/TemplateDefs/Templates_Tribal.xml`). Imperium holds the Empire's kit and the
  river-bend town's template (`Defs/KitDefs/Kits_Empire.xml`, `Defs/TemplateDefs/Templates_Empire.xml`), and from the
  same pull request its `About/About.xml` requires Mantle: an entry in `modDependencies` with Mantle's `packageId`, a
  `displayName` and a `downloadUrl`, and Mantle's `packageId` in `loadAfter`. Mantle's mod folder is `Mantle/` and
  Imperium's `Imperium/`, side by side at the repository root, and Mantle's `packageId` is `Neiro.RimWorld.Mantle`, as
  R14 sets (`specs/003-mantle-mod/research.md` R-1, R-4). Mantle has no Workshop page, so its entry gives the
  repository's page as `downloadUrl`, which `ModUpdating.txt` accepts in place of `steamWorkshopUrl` (lines 266-275).
- **Rationale**: templates and kits are data that the mod holding them carries and Mantle's generation reads (FR-009),
  and a mod's new XML definitions go in `Defs/`, laid out as the base game lays out its own (`ModUpdating.txt` lines
  98-106). A definition the game loads has a class, as `ThingDef`, `PawnKindDef` and `JobDef` do (line 98), and a mod's
  classes are a C# project in `Source/` compiled into `Assemblies/` (lines 139-151, 173-182). The classes are Mantle's
  because every culture shares the forms (FR-033) and Mantle is a mod of its own that requires no expansion, which the
  mods built on it depend on (ROADMAP R14, Releases). The tribal culture's kit and templates open Mantle's alpha, and
  the Empire's come with Imperium (FR-032; ROADMAP R13, R15). A mod whose definitions use another mod's types needs that
  mod active and loaded first, which `modDependencies` and `loadAfter` say (`ModUpdating.txt` lines 266-289, 309-316);
  so Imperium requires Mantle from the first slice whose content uses it (ROADMAP, Releases). The files are named by
  type and then by what they hold, as `Data/` names its own (`Core/Defs/RiverDefs/RiverDefs.xml`,
  `Odyssey/Defs/LayoutDefs/Layouts_Misc.xml`).
- **Alternatives considered**: `PrefabDef`, which holds a size, terrain and things (`Data/`: its fields across Core,
  Biotech and Odyssey are `size`, `things`, `terrain`, `edgeOnly`, `rotations`, `prefabs`). Rejected: it holds no roof
  and no skeleton (FR-004, FR-005). The Empire's kit and template kept out of Imperium's `Defs/` until R15. Rejected:
  neither `Data/` nor `ModUpdating.txt` gives a form for data a mod holds but the game does not load as definitions,
  and loading them is what shows that they load (R-12).

## R-2: Building Mantle's assembly

- **Decision**: in Mantle's mod, `Source/Mantle/Mantle.csproj` targets `net10.0` and references the game's own
  assemblies where the game is installed, through a `RimWorldAssemblyDir` property that a `Directory.Build.props` in
  `Mantle/Source/` sets. It is built on the maintainer's computer through Remote Control, and the built
  `Assemblies/Mantle.dll` is committed. No Harmony and no other package. Imperium holds no code for this feature.
- **Rationale**: `Data/` and `ModUpdating.txt` give no form for building a mod's code, so it comes from Harmony
  (Principle III). RimWorld 1.7 runs on .NET 10 (`README.md` line 6), Harmony's 1.7 build selects the `net10.0` asset
  (`BUILDING.md` line 12; `Source/packages.lock.json`) and compiles against the installed game's assemblies, found
  through `RIMWORLD_ASSEMBLY_DIR` (`BUILDING.md` lines 18-19) and `RimWorldAssemblyDir` in `Directory.Build.props` (line
  17), which sits at the root of Harmony's mod folder; in this repository a mod's files for its code go in its `Source/`
  (R14 `contracts/repository-layout.md`). Harmony commits its built assemblies, and its release packages that committed
  payload rather than rebuilding against the game's files (`BUILDING.md` lines 14 and 38-39); the maintainer's clone
  holds the built `Mantle.dll`, and the game loads it once `Mantle/` is copied into `Mods` (R14 research R-9). The
  game's assemblies exist only in the maintainer's install, and are neither copied into the repository nor into the
  cloud (`EULA.txt` line 86). Def classes patch nothing, so Harmony is still not a requirement (R1 research R-9).
  `Assemblies/` sits at the root of `Mantle/`, since Mantle supports 1.7 only and has no load folders, as R1 set for
  Imperium (R1 research R-1, R-5; R14 research R-5).
- **Alternatives considered**: a `1.7/Assemblies/` folder, as Harmony has. Rejected: Harmony supports several game
  versions; Mantle supports one, and `ModUpdating.txt` lines 173-180 put `Assemblies/` at the root.
- **Open for implement**: whether the maintainer's computer has the .NET 10 SDK, and where the 1.7 install keeps its
  assemblies. If the SDK is missing, the implement step says so and stops there.

## R-3: Field forms taken from `Data/`

- **Decision**: wherever a template, kit or laid-out city holds something `Data/` already writes, it is written in
  `Data/`'s form:
  - a layer of cells (terrain, roofs, terrain features, the places of parts) as `PrefabDef`'s terrain form: the
    definition, then `rects` of `(minX,minZ,maxX,maxZ)` (`Odyssey/Defs/PrefabDefs/SitePrefabs.xml` lines 64-74);
  - a thing as `PrefabDef`'s thing form: the definition, its `position` as `(x, 0, z)`, its `stuff`
    (`AncientPrefabs.xml` lines 10-13), and its rotation by `Rot4` name (`North`, line 8);
  - a map size as `(x, z)` (`AncientPrefabs.xml` line 9), and the smallest map a site needs as `minMapSize`
    `(x, 1, z)` (`Ideology/Defs/Sites/AncientComplex.xml` line 15);
  - content of an expansion that the mod holding the file does not require marked with `MayRequire="<packageId>"` on
    the element that names it (`Odyssey/Defs/PrefabDefs/CommonRoomPrefabs.xml` line 225;
    `Core/Defs/CultureDefs/Cultures.xml` line 43), each package identifier from that expansion's `About/About.xml`;
    what a mod requires is its `About/About.xml`'s `modDependencies` (`ModUpdating.txt` lines 266-289), which is none
    for Mantle's mod and Royalty for Imperium (FR-015);
  - the world tiles a template suits as `allowedBiomes` (`Core/Defs/Storyteller/Incidents_Map_Misc.xml` line 56) and,
    in the same form, `allowedRivers`, from the river definitions (`Core/Defs/RiverDefs/RiverDefs.xml` lines 4, 33,
    52, 71);
  - a kit's word list as a `RulePackDef`, as a faction names its settlements
    (`Royalty/Defs/FactionDefs/Faction_Empire.xml` line 21), with the words in `Languages/English/Strings/`
    (`ModUpdating.txt` lines 129-135);
  - a kit's wall settings with `StructureLayoutDef`'s `wallDef` (`Odyssey/Defs/LayoutDefs/Layouts_Misc.xml` line 22).
- **Rationale**: Principle III; the released mod follows `Data/` first, and a laid-out city, written by R2's
  generation, is checked against the same definitions.
- **Alternatives considered**: a grid of characters or an image for a terrain shape. Rejected: `Data/` gives a form.

## R-4: What a template's cells may hold

- **Decision**: a terrain shape holds only terrain whose definition is `natural`
  (`Core/Defs/TerrainDefs/Terrain_Natural.xml` line 11; `Terrain_Water.xml` line 7), things whose definition is natural
  rock (`isNaturalRock`, `Core/Defs/ThingDefs_Buildings/Buildings_Natural.xml` line 47), and roofs whose definition is
  natural (`isNatural`, `Core/Defs/Misc/RoofDefs/Roofs.xml` lines 17 and 27). Anything else on a template's cells is a
  thing a city is built of, and the check reports it (FR-002, FR-014).
- **Rationale**: a template is a terrain shape and a skeleton, never a drawn map [Design: lines 204, 209]; `Data/`
  marks what is natural.

## R-5: The skeleton's form

- **Decision**: a skeleton is a list of `parts` and a list of `relations`, and a terrain shape names its terrain
  `features`. Both a template and a kit hold a skeleton of this form:
  - A **part** has a `name`, a `kind` and, for a slot, `optional`. The kinds are those the design and the maintainer
    name as fixed parts of a layout: `Core` [line 174], `SecondaryCore` [200], `PalaceQuarter` [193], `Gate` [204],
    `RiverGate` [197], `MainStreet` [188], `SecondaryAxis` [199], `District` [178], `Acropolis` [161], `Landmark`
    [185], `Bridge` [197, the bridge of a bridge gate], and `WallLine`, `Plaza` and `PublicBuilding` [Direction].
  - A **feature** of the terrain shape has a `name` and `rects`, and a river feature names the map edge it flows from,
    `flowsFrom`, by `Rot4` name.
  - A **relation** has its kind and the parts or features it relates. The kinds are the relations the design's
    definitions use: `Inside` (a district within the walls [178]; a secondary core inside a gate [200]; a civic core
    around its first square [174]), `Adjoins` (beside [165]; runs from the gates through the squares [188]; ends at
    [199]; by the river [197]; which districts adjoin [Direction]), `Upstream` (upstream on the river [193]),
    `Farther` (far from the main gate [193]), and `Across` and `SameSide` (the river bend and which side of it each
    part lies on [Direction; 204, relations to the terrain]).
  - A **kit's skeleton** holds what every city of its culture has, such as where the palace quarter lies [193], and
    names parts only; a **template's skeleton** holds what its site has, and may name its features. A template is
    read with its kit's skeleton: a part of the same name is the same part, and both skeletons' relations hold.
  - A part marked `optional` is a slot within the culture [Design: line 200; Direction]; there is no field that would
    carry a skeleton to another culture (FR-002).
- **Rationale**: a skeleton records the fixed parts as relations to each other and to the terrain, not coordinates
  [Design: line 204]; a kit holds a skeleton [184] and so does a template [209]; the parts and relations named are those
  the design's own definitions use, and the river-bend calibration is the test of whether they are enough (FR-031).
  Further kinds are added when the design or the maintainer names them (spec, Assumptions).
- **Alternatives considered**: free-text kinds. Rejected: the check could not tell a misspelt kind from a new one
  (FR-014).

## R-6: How the check measures a relation

- **Decision**: on the laid-out city, each part and feature is the set of cells its `rects` cover, and each relation is
  read plainly on those cells, with neighbours sharing an edge and distance between cell centres:
  - `Inside(a, b)`: every cell of `a` is a cell of `b` or is enclosed by `b`, meaning no path of neighbouring cells
    leads from it to the map's edge without crossing `b`.
  - `Adjoins(a, b)`: a cell of `a` is a cell of `b` or a neighbour of one.
  - `Across(a, b, feature)`: no path of neighbouring cells outside the feature leads from `a` to `b`; `SameSide` is
    the opposite.
  - `Upstream(a, b, feature)`: along the river feature, counted in steps from its cells on the edge it flows from, the
    river cell nearest `a` comes before the river cell nearest `b`.
  - `Farther(a, b, than)`: `a` is farther from `b` than `than` is, each distance being the shortest between their cells.
  A relation whose optional part the city leaves out is reported as not measured rather than broken.
- **Rationale**: FR-029 asks the check to measure each relation and report each one that does not hold; the readings add
  no threshold that no source gives. Once every relation holds, the maintainer judges by eye (FR-029, Clarifications).

## R-7: The laid-out city's form

- **Decision**: one XML file per city, root element `LaidOutCity`, holding: the `template` and `kit` it comes from;
  its map `size`; `terrain` and `roofs` as layers of cells; `things`, each with its definition, `position`,
  `rotation`, `stuff` where its definition takes one, and `rect`, the cells it covers, where it covers more than one;
  and `parts` and `features`, where each part and terrain feature of the template lies after generation picked,
  mirrored, turned and stretched it, with each river's `flowsFrom`. The game does not load it and the mod does not
  ship it.
- **A reading**: written in the same form, with `reference`, the reference city's name as the template's `reference`
  gives it, in place of `template` and `kit`, and the parts and features it reads. It is kept in `readings/` at the
  repository root, as its template's source: a mod folder holds only its folders for the game and its code, its README
  and its license, and the check that reads the readings sits at the root (R14 `contracts/repository-layout.md`), so a
  reading is in neither mod's released files; its reference pictures are not kept there (FR-036, FR-028). The folder
  sits beside the check's `src/` and `tests/` and is named in lower case, as Spec Kit's own repository names every
  top-level folder (`docs/`, `scripts/`, `src/`, `templates/`, `tests/` at v1.4.3).
- **Rationale**: FR-008 lists what it holds, in the forms of R-3; generation writes it in R2 and the check reads it now.
  The covered cells are written by generation, which has them from the game, so the check does not have to rebuild the
  game's rule for where a large thing's cells lie; it checks that they match the definition's `size`, crosswise when
  the thing is turned east or west.
- **Alternatives considered**: a saved game. Rejected: it is not in `Data/` and holds far more than the check reads.

## R-8: A kit's groups and fill

- **Decision**: what a kit's groups and fill hold is taken apart from its culture's reading, as its skeleton is (spec,
  Clarifications; FR-006, FR-036), and written in `Data/`'s forms for what they are: `groups` is a list of named sets
  of things placed together, each in `PrefabDef`'s form (`size`, `things` with `position`, `rotation` and `stuff`,
  `terrain`; `AncientPrefabs.xml` lines 8-13), so a set read off a reading's things is written with no conversion;
  `fill`, what a block's plots are built with, holds `StructureLayoutDef`'s `wallDef`, `doorDef` and `doorStuffDef`
  (`Layouts_Misc.xml` lines 19-22) and a list of plot sets in the same `PrefabDef` form.
- **Rationale**: the design names a kit's groups and fill [Design: line 184], a building or group [185] and a block
  divided into plots for its households [166], without saying what they hold; the maintainer's direction is that they
  come from the reference city, as the skeleton does, and are never asked. The base game ships `PrefabDef` and
  `StructureLayoutDef` in its own assembly and uses them in Core (`Core/Defs/PrefabDefs/CommonRoomPrefabs.xml`), so
  Mantle's mod needs no expansion for them (FR-015).
- **What R13 writes**: the forms of all five fields (FR-006); the tribal kit's and the Empire kit's skeletons, wall
  settings, groups and fill, each from its culture's readings, the tribal culture's three (R-13) and the river-bend
  town's render (FR-031); and each culture's word list (FR-011): the Empire's from its sources on Rome, and the tribal
  culture's the base game's own `NamerSettlementTribal` (`Core/Defs/FactionDefs/Factions_Misc.xml` line 230).

## R-9: The check is a Python package in Spec Kit's form

- **Decision**: `pyproject.toml` at the repository root declares the package `mantle-check` (`src/mantle_check/`) with
  a `mantle-check` command, Python 3.11 or later, Typer for the command line and Pillow for pictures, built with
  Hatchling; tests in `tests/` run with pytest.
- **Rationale**: the check is a development tool, so its form comes from the development workflow's source, Spec Kit,
  which offers no tool form of its own; Principle V then takes the option Spec Kit uses in its own repository: a Python
  package declared in `pyproject.toml`, with `requires-python = ">=3.11"`, Typer for its command line, a
  `[project.scripts]` entry, Hatchling, and pytest over `tests/` (`pyproject.toml` lines 1-26, 39-55; `.gitignore`
  lines 1-27). Pillow is needed to read the reference pictures, which are JPEG, PNG and WebP files
  (`template-references/`), and to write PNG (R-11). XML is read with Python's own library. The package sits at
  the repository root, outside both mod folders, as a development tool that checks both mods (R14
  `contracts/repository-layout.md`), and every culture shares it (FR-033).
- **Ignored files**: `.gitignore` adds Spec Kit's Python lines (`.gitignore` lines 1-27) and Harmony's lines for the
  C# build's output, `[Bb]in/` and `[Oo]bj/` (Harmony `.gitignore` lines 13-23), since `Data/` and `ModUpdating.txt`
  give no form for ignored files.
- **Alternatives considered**: a C# tool beside Mantle. Rejected: it would need the game's assemblies, which exist only
  on the maintainer's computer (R-2), and the check must also run in cloud threads (spec, Assumptions).

## R-10: Reading `Data/`

- **Decision**: the check takes the path of `Data/` (on the maintainer's computer,
  `D:\Steam\steamapps\common\RimWorld\Data`; in a cloud thread, the project's copy unpacked) and the folder of each
  mod whose definitions it reads, Mantle's and, for the Empire's, Imperium's. It reads `Version.txt` beside `Data/` and
  stops unless the version is 1.7. It reads every XML file under each expansion's `Defs/` and each mod's `Defs/`, and
  each mod's `About/About.xml` for its `packageId` and `modDependencies` (FR-015), and resolves inheritance: an
  abstract parent (`Name`, `Abstract`) gives its fields to each child that names it (`ParentName`), a child's field
  replaces the parent's, and a child's list adds to the parent's unless it is marked `Inherit="False"`
  (`Core/Defs/ThingDefs_Buildings/Buildings_Base.xml` line 4 and `Buildings_Structure.xml` lines 218 and 277-278, where
  `Wall` replaces `BuildingBase`'s affordance; `Apparel_Headgear.xml` line 552). Each
  definition's expansion or mod is the folder it is read from, with that folder's `About/About.xml` package identifier;
  a file given to the check belongs to the mod whose folder holds it.
- **Rationale**: testing outside the game reads `Data/` [Testing]; R1 supports 1.7 only (R1 research R-5); the files
  are read where they are and nothing of them is copied (FR-021; `EULA.txt` line 86).
- **What it reads from each definition**: `label`; a terrain's `natural` and `affordances`; a thing's `size`,
  `terrainAffordanceNeeded`, `useStuffTerrainAffordance`, `stuffCategories`, `building/isWall`,
  `building/isNaturalRock`; a material's `stuffProps/categories` and its own `terrainAffordanceNeeded`
  (`Various_Stone.xml` line 88); a roof's `isNatural`; and the `color` a definition gives, for the pictures.

## R-11: The pictures

- **Decision**: one PNG per template and laid-out city, and one side-by-side PNG per template or laid-out
  city with each reference picture given. Each cell is drawn as a square; a thin grid line runs between cells and a
  stronger one every 10 cells, numbered along all four edges as `x` and `z`, with `z` growing toward north at the top.
  Terrain, roofs and things are filled with the `color` their definition gives, or with a colour drawn from their
  definition's name where it gives none. Parts and features are outlined and named where they lie; a template, whose
  parts have no cells, shows its parts and relations as a named diagram beside its terrain shape, with each feature
  named on the grid. Each problem with a cell is marked there with its number in the report. A legend lists every
  definition shown by its `label`, with its expansion where it is not the base game's (FR-026). The side-by-side
  picture sets the whole drawing and each whole reference picture at the same height. Pictures are written to a folder
  the developer names, and the check refuses a folder inside the repository.
- **Rationale**: PNG is the image form `ModUpdating.txt` gives mods (lines 84-90); FR-023 to FR-028; positions are
  `x` and `z` (`AncientPrefabs.xml` line 10) and `North` is a rotation `Data/` names (line 8). The side-by-side pictures
  hold reference pictures, which stay out of the repository (FR-028; `EULA.txt` line 76).
- **Determinism**: no time, path or random value goes into a report or picture, and every list is sorted, so the same
  inputs give the same files (FR-022).

## R-12: Tests

- **Decision**: outside the game first: pytest runs the check over test templates, kits and laid-out cities written by
  hand in `tests/fixtures/`, each holding one known kind of problem or none, against `Data/` 1.7.5014, whose path the
  tests take from `RIMWORLD_DATA_DIR`. A test makes its own small reference picture, so none is committed. In the game:
  `Mantle.dll` is built and the game is launched with `-quicktest` (`Readme.txt` lines 58-60) and
  `-savedatafolder=SaveData` (lines 27-38), first with Mantle's mod alone and no expansion, then with Royalty, Mantle
  and Imperium, and `Player.log` shows that each mod's definitions load with no error. Placing templates on a map, the
  final check, comes with R2 for the tribal culture and R15 for the Empire (spec, Assumptions).
- **Rationale**: testing outside the game comes first and testing in the game is the final check [Testing]; the
  variable is named as Harmony names its own (`RIMWORLD_ASSEMBLY_DIR`, `BUILDING.md` line 18); test templates and kits
  are not game content (spec, Assumptions).

## R-13: The first templates

- **Decision**: in implement, the river-bend town first: its template and the Empire kit are taken from the screenshot
  (`template-references/河湾城-原图与描线/原图-1596x1017.png`) and the newest render, its reading
  (`template-references/河湾城-最新版-1112/1比1整城样张.png`). Its terrain shape is drawn inside 350×350 cells, and its skeleton
  holds the river bend, the wall line, the districts on each bank and inside the bend, the main streets with their
  bridges and gates, the plazas, and the public buildings, by the relations of R-5. The check's picture of it beside
  both references is given to the maintainer in the project's files, not in the pull request, since it holds the
  screenshot (FR-028). Once it passes the check, the tribal culture's three readings are written from the references the
  maintainer chose, whose pictures are in `template-references/部落城-凯尔特/`, in `readings/`: the gentle tribe's open
  village from Tir Uisce, the fierce tribe's walled stronghold from a Celtic oppidum and the savage tribe's fortress
  from a small Celtic hillfort, with the agricultural island only looked at beside them, as supplementary material, and
  nothing taken from it. Each reading counts once the maintainer accepts it beside its pictures, recorded in
  `checklists/acceptance.md` (spec FR-029, FR-036). A template is taken from each, stating its tribe's attitude (R-14),
  and the one tribal kit from all three. Each template ships as it stands once it passes (FR-010, FR-031).
- **Rationale**: FR-031, FR-036, FR-037, FR-039, Clarifications; [Direction].

## R-14: Picking a template by attitude and terrain

- **Decision**: a `TemplateDef` states the attitude of the factions it serves with two fields that take `FactionDef`'s
  own names and form, `naturalEnemy` and `permanentEnemy`, each `true` or, when left out, `false`
  (`Core/Defs/FactionDefs/Factions_Misc.xml` lines 202, 462, 485 and 529), and serves the factions whose definitions
  hold the same two values. It names no faction. The biomes it suits are its `allowedBiomes` (R-3), empty for any. The
  tribal culture's three templates leave `allowedBiomes` empty and set the attitude: neither field for the gentle
  tribe's open village, `naturalEnemy` for the fierce tribe's walled stronghold, `permanentEnemy` for the savage tribe's
  fortress. The Empire's templates leave both fields out and set `allowedBiomes` by the design's two looks of imperial
  cities, temperate for temperate and cold regions and arid for hot, dry ones (Imperium-old glossary lines 208 and 162):
  the river-bend town's `TemperateForest` and `TemperateSwamp` (`Core/Defs/BiomeDefs/Biomes_Temperate.xml` lines 5 and
  210) and `BorealForest`, `Tundra`, `ColdBog`, `IceSheet` and `SeaIce` (`Biomes_Cold.xml` lines 5, 198, 371, 586 and
  710). Which culture a faction takes, and picking among the templates that serve it, are generation's (ROADMAP R2).
- **Rationale**: Principle III: `Data/` already writes a faction's attitude in these two fields, so a template that
  states the attitude it serves writes it the same way. The tribes' descriptions set which layout each attitude gets:
  the gentle tribe is open to trade and alliances, the fierce tribe values warlike dominance, the savage tribe has a
  blood-and-honor culture that cannot be allied with (same file, lines 445, 480 and 504), which the maintainer
  confirmed (spec FR-039). The Empire holds neither field, only `permanentEnemyToEveryoneExcept`
  (`Royalty/Defs/FactionDefs/Faction_Empire.xml` lines 57-67), so its templates differ by terrain alone (spec FR-040).
  Naming no faction lets factions that other mods add, such as medieval ones, pick by the same fields; that those
  mods set them is an inference, checked when their culture's kit comes (spec, Edge Cases).
- **Alternatives considered**: a list of the `FactionDef`s a template serves. Rejected: it binds a template to faction
  names (spec FR-039). The faction category tags that `Data/` filters by (`allowedFactionCategoryTags`,
  `Ideology/Defs/PreceptDefs/Precepts_Role.xml` line 120). Rejected: a tag names a kind of faction, not its attitude,
  and the three tribes share `Tribal` (`Factions_Misc.xml` line 222). The quest filter `mustBePermanentEnemy`
  (`Royalty/Defs/QuestScriptDefs/RewardThreat/Scripts_JoinerThreat.xml` line 458). Rejected: `Data/` has no such
  filter for `naturalEnemy`, and it cannot state a template that serves only factions holding neither field.
