# Feature Specification: Templates and kits

**Feature Branch**: `claude/project-thread-wgq7xi`

**Created**: 2026-11-24

**Status**: Draft

**Input**: Parent roadmap: `ROADMAP.md` → entry **R13**, Templates and kits. The designed layouts of city sites, each a
terrain shape with a skeleton (templates), and each culture's fixed set of generation data (kits) are data that
Mantle's generation uses, checked outside the game against the game's own definitions before Mantle uses them, and the
cities Mantle lays out from them are compared outside the game with the reference cities the templates are drawn from
(Imperium-old glossary "template", "kit", "skeleton"; constitution, Source Register, "Testing outside the game"; the
maintainer's broad direction). Scope: the forms of templates, kits and the cities laid out from them, and their check
outside the game against `Data/`, which sets a laid-out city beside its reference. Deferred: which templates and kits
the alpha holds, and generation, which picks templates, may mirror, turn and stretch them, and lays out cities from
them (R2); the check in the game, which is the final one, once R2 places them (R2). As requested for this feature, the
check shows a template as a picture of its site, so that the developer can see it without starting the game, and sets
the city that generation lays out from a template and a kit beside a picture of the reference city, so that the two
can be compared.

## Purpose

Mantle is the framework layer that Imperium's content builds on [Design: line 221], so a template is not a drawn map
of one city. It is a terrain shape and a skeleton, the fixed parts of a city's layout recorded as relations rather
than coordinates, which generation picks by world tile and size, may mirror, turn and stretch, and fills from a kit,
one culture's fixed set of generation data [Design: lines 184, 204, 209].

Each culture has its own skeletons and templates, as each kit holds a skeleton of its own [Design: line 184;
Direction]. Within a culture, a skeleton may have slots that vary, such as walls a city may have or lack, or a
secondary core that small cities do not have [Design: line 200; Direction]. Slots that would carry one template
across cultures are not used, since they would erase each culture's character [Direction]. The kit that Imperium-old's
design calls the Roman kit (glossary line 184) is the Empire kit, and is named so in Imperium's files too, since no
other faction uses its style [Direction].

The cultures are those of every faction that has settlements, on the surface and in orbit (FR-032): the Empire,
tribal, industrial (outlander), pirate and medieval, the last for the medieval factions that other mods add, and
Odyssey's Traders Guild and Salvagers, whose settlements lie on the Orbit layer [Direction; Design: line 184; Data].
This feature holds the Empire kit and the river-bend town's template; the other cultures' kits and templates are later
work [Direction].

Mantle is a framework that other authors build on too [Design: line 221], so adding a culture asks only for its
skeletons and its kit [Direction]. Everything else is shared and the same for every culture: the forms of templates
and kits, the check outside the game and its pictures, generation's picking, mirroring, turning, stretching and
filling [Roadmap: R2], and the pieces, generic building elements that every kit shares and each faction skins
[Design: line 194]. An author starts a culture by copying an existing culture's skeletons and kit, and the river-bend
town is the complete worked example, from reference to skeleton to generated city (FR-033 to FR-035) [Direction].

What is fixed and what is left to generation [Design: lines 184, 209; Direction]:

- **Fixed**, defined by people and abstracted from the reference city: the template, meaning its terrain shape with
  its river, and its skeleton with the wall line, the districts and their relations, the main streets, the plazas and
  the places of the public buildings; and the kits.
- **Left to generation**, and only within those bounds: picking a template, mirroring, turning and stretching it to
  fit the site, and filling its blocks with the kit's buildings.

Generation never designs a city: it fills a fixed skeleton.

Templates are drawn from reference cities in four steps [Direction]:

1. A reference city is chosen from the player-built cities that Ubisoft officially features as recommended Anno 117
   cities.
2. Its layout relationships are read and written as a template in this feature's form, as Imperium's own (FR-010).
3. Generation lays out a city from the template and a kit [Roadmap: R2].
4. The check measures whether each relation of the template's skeleton holds in the laid-out city and draws the city
   beside pictures of the reference city; once every relation holds, the maintainer judges them side by side (FR-025,
   FR-029).

The first case is the river-bend town, a player-built city of which the project holds a screenshot, the source, and a
render on the game's cells, an earlier reading of that single 2D screenshot whose heights, hidden areas and exact sizes
were guessed [Direction]. It calibrates the method before anything else (FR-031). Its template is written from
these pictures. R2's generation lays out the town from it with a kit [Roadmap: R2]. Every relation of its skeleton
must hold in the laid-out town, and the maintainer then judges the town beside the screenshot and the render. No
cell-exact match to the render is asked for, since it is a guess too. If the method cannot express the town, the
method is fixed first. Once the calibration passes, the town ships as a regular template, laid out with Imperium's
own buildings, materials and names.

The comparison is why the check outside the game exists [Direction]. Generation that is not held to a fixed skeleton,
and a developer, a person or an AI, working toward a target, take shortcuts toward abstract geometric layouts, such as
squares and octagons, since nothing in them carries how real towns grow around rivers, terrain, walls and streets. The
base game offers no large town to draw from: it lays out a faction base by a single generation step [Direction; Data:
`BaseFactionMapGenerator.xml` lines 14-21]. The reference cities are placed by hand around their rivers, terrain,
walls and streets, and the recommended ones are curated and publicly shared. So a template counts only once the check
has drawn the city laid out from it and that city has passed the comparison with its reference, whoever wrote the
template (FR-030), and the check in the game, the final one, still follows [Testing].

## Clarifications

### Session 2026-11-24

- Q: How is a laid-out city judged to match its reference city? → A: The check first measures whether each relation of
  the template's skeleton holds in the laid-out city and reports each one that does not; once every relation holds,
  the maintainer looks at the side-by-side picture and decides whether it passes (the maintainer's broad direction,
  constitution, Principle IV).
- Q: Does one template serve several cultures' kits, through slots that each kit fills, replaces or leaves empty? →
  A: No. Each culture has its own skeletons and templates. Slots give variation within a culture only, such as
  optional walls, or no secondary core in small cities (Imperium-old glossary line 200); slots across cultures would
  erase each culture's character (the maintainer's broad direction, constitution, Principle IV).
- Q: How does the river-bend town fit a city's 350×350 map, whatever size its render was drawn at? → A: Its template is
  written with its terrain shape inside 350×350 cells and the same skeleton relations, and the render's cell sizes are
  not carried over. A skeleton is relations, not coordinates (Imperium-old glossary line 204); the render's sizes are
  guesses and no cell-exact match to it is required (the maintainer's broad direction, FR-031); and generation may
  stretch a template to fit its site (glossary line 209). Whether the fitted town still reads as the river-bend town is
  part of the maintainer's judgment in the calibration (FR-031).

## Sources

Each requirement below names its source in brackets. The sources are those the constitution's Source Register gives:

- **[Roadmap]**: `ROADMAP.md`, entries R13 (intent and scope boundary) and R2.
- **[Design]**: Imperium's own design, Imperium-old `main` (20a052b), `docs/glossary.md`, section City building and
  generation: block library (line 167), city building (line 173), kit (line 184), piece (line 194), skeleton
  (line 204), spec card (line 206), template (line 209) and Mantle (line 221); `docs/imperium.md`, section Expansions
  (lines 108-110); and `docs/setting.md`, section Rome (lines 56 and 59-60).
- **[Testing]**: the constitution's Source Register, row Testing outside the game: the base game and official
  expansions in `Data/`; testing outside the game comes before testing in the game and does not replace it, and
  testing in the game is the final check.
- **[Data]**: the base game and official expansions in `Data/` of RimWorld 1.7.5014: terrain
  (`Core/Defs/TerrainDefs/`), and the affordances a terrain gives (`Terrain_Natural.xml` lines 5-7, 51-55 and
  126-131); natural rock (`Core/Defs/ThingDefs_Buildings/Buildings_Natural.xml` line 47); roofs
  (`Core/Defs/Misc/RoofDefs/Roofs.xml` lines 5, 14 and 24); the affordance a thing needs
  (`Core/Defs/ThingDefs_Buildings/Buildings_Base.xml` line 11), or its material needs when the thing says so
  (`Buildings_Structure.xml` lines 277-278; `Core/Defs/ThingDefs_Misc/Various_Stone.xml` line 88); the materials a
  thing takes (`Buildings_Structure.xml` lines 286-290); a faction base's generation
  (`Core/Defs/MapGeneration/BaseFactionMapGenerator.xml` lines 14-21); the smallest map a site needs
  (`Ideology/Defs/Sites/AncientComplex.xml` line 15); square maps (`Core/Languages/English/Keyed/Dialogs_Various.xml`
  line 153); a site's map taking its own size (`Core/Defs/WorldObjectDefs/WorldObjects.xml` line 205); a thing placed
  by its position as `(x, 0, z)`, its rotation and its material (`Odyssey/Defs/PrefabDefs/AncientPrefabs.xml` lines
  12, 13 and 23); the factions that have settlements (`Royalty/Defs/FactionDefs/Faction_Empire.xml` line 5;
  `Core/Defs/FactionDefs/Factions_Misc.xml` lines 185, 443, 511 and 517; `Odyssey/Defs/FactionDefs/Factions_Misc.xml`
  lines 5, 17, 40-42, 168, 188 and 202-204); and each expansion's `About/About.xml`.
- **[EULA]**: `EULA.txt`, which is always followed (constitution, Source Register).
- **[Direction]**: the maintainer's broad direction on where template layouts come from and how they are accepted,
  which Imperium-old's design leaves open (constitution, Source Register, row Imperium's own design; Principle IV):
  - Templates are drawn from player-built cities that Ubisoft officially features as recommended Anno 117 cities, as
    reference only. The layout relationships read from such a city, its river, walls, districts, streets, plazas and
    public buildings, are expressed as Imperium's own templates in the design's form, and kits fill them. Nothing of
    Anno's art, names, models or code is used, and no reference picture is traced cell by cell, apart from the
    river-bend town below.
  - Imperium's city maps are 350×350 cells.
  - Each culture has its own skeletons and templates; slots vary only within a culture. The old design's Roman kit is
    the Empire kit, also in Imperium's files.
  - Every faction that has settlements gets its own, on the surface and in orbit: the Empire, tribal, industrial
    (outlander), pirate, medieval (for medieval mods), and Odyssey's Traders Guild and Salvagers. Only the Empire kit
    and the river-bend town belong to this feature; the rest is later work.
  - Lowering the barrier for other authors is necessary: a new culture needs only its skeletons and kit, everything
    else is shared and identical across cultures, an author can copy an existing culture as a starting point, and the
    river-bend town is the complete worked example.
  - The template's skeleton holds the wall line, districts, main streets, plazas and public buildings read from the
    reference, beside the parts the design names; generation only picks, mirrors, turns and stretches a template and
    fills it from a kit.
  - The city laid out from a template is compared with its reference, and a template counts only once that comparison
    passes, whoever wrote it, since generation and developers alike tend toward geometric layouts. The check measures
    whether the skeleton's relations hold in the laid-out city, and once they all hold, the maintainer judges the
    side-by-side picture (Clarifications).
  - The river-bend town is the first case, and it calibrates the method before anything else. Its reference pictures
    are kept in `template-references/` in the project's files: the screenshot of the player-built city, which is the
    source, and the newest render of it on the game's cells (2026-11-12), an earlier reading of that single 2D
    screenshot whose heights, hidden areas and exact sizes were guessed. The calibration checks that the method can
    express the town. Every relation of the skeleton must hold in the town that generation lays out, and the
    maintainer then judges it by eye beside the screenshot and the render, with no cell-exact match to the render. A
    method that cannot express the town is fixed first. Once the calibration passes, the town's content is Imperium's
    own buildings, materials and names, and it ships as a regular template, with no credit line.
- **[Spec Kit]**: the feature description given to `/speckit-specify` (Input, above), the development workflow's
  source for what a feature is for.

Imperium-old's earlier layout tool and the reverted spec of the earlier R13 are not sources, and nothing is taken from
them.

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Check a template or kit against the game (Priority: P1)

A developer writes a template, the designed layout of a city site, or a kit, a culture's fixed set of generation
data, in the form this feature sets. Without starting the game, the developer runs the check, which reads the
template or kit next to the game's own definitions in `Data/` and lists every place where it names something the game
does not define, names it where it cannot go, or holds something only another expansion defines.

**Why this priority**: Mantle's generation picks and uses templates and kits [Design: line 209; Roadmap: R2], so
they have to be right before Mantle uses them. Testing outside the game comes first [Testing], and without the forms
and the check there is nothing to test.

**Independent Test**: Write a set of test templates and kits, each holding one known kind of problem, and one holding
none; run the check on each, and compare what it reports with what each holds.

**Acceptance Scenarios**:

1. **Given** a template whose terrain shape names a terrain that `Data/` does not define, **When** the check runs,
   **Then** it reports that name and the cell where it is.
2. **Given** a kit whose wall settings name a definition that is not a wall, **When** the check runs, **Then** it
   reports that the name cannot go there.
3. **Given** a template that names a definition only Biotech holds, without marking it as Biotech's content, **When**
   the check runs, **Then** it reports it, since Imperium is complete with Royalty alone [Design: imperium.md lines
   108-110].
4. **Given** a template that places a building on a cell, **When** the check runs, **Then** it reports it, since a
   template holds no building (FR-002).
5. **Given** a template and a kit with no problem, **When** the check runs, **Then** it reports none, and says that
   the check in the game, which is the final one, is still to come.

---

### User Story 2 - Compare a laid-out city with its reference (Priority: P2)

Generation lays out a city on a map from a template and a kit [Roadmap: R2]. The developer gives the check that
laid-out city and a picture of the reference city the template is drawn from. The check checks the laid-out city
against the game's definitions, draws it on the game's cells, and sets the drawing beside the reference picture, so
that the developer can see whether the city keeps its reference's river, walls, districts, streets, plazas and public
buildings in their relations, or has fallen back to geometric shapes.

**Why this priority**: The comparison is why templates are drawn from reference cities and why the check outside the
game exists, and a template counts only once it passes [Direction]. It uses the check of User Story 1, so it comes
after it.

**Independent Test**: Until R2 generates cities, write small laid-out cities by hand from a test template and a test
kit: one with a known problem, one that breaks a relation of the template's skeleton, and one with neither; give each
with a test reference picture, and compare the report and the side-by-side picture with what each holds.

**Acceptance Scenarios**:

1. **Given** a laid-out city and a picture of its reference city, **When** the check runs, **Then** the drawing of the
   whole city, with its grid, coordinates and legend, and the whole reference picture are shown side by side.
2. **Given** a laid-out city, **When** the developer opens its drawing, **Then** each part of the template's skeleton
   is named where it lies, so that the same part can be found in the reference picture.
3. **Given** a laid-out city with a granite block wall on marshy soil, **When** the check runs, **Then** it reports
   the wall, the terrain and the cell, since stone blocks need heavy ground and marshy soil gives only light
   [Data: `Buildings_Structure.xml` lines 277-278; `Various_Stone.xml` line 88; `Terrain_Natural.xml` lines 126-131].
4. **Given** a laid-out city with no problem, **When** the check runs, **Then** it reports none, and says that the
   check in the game, which is the final one, is still to come.

---

### User Story 3 - See a template as a picture of its site (Priority: P3)

The developer gets each checked template as a picture of its site: its terrain shape on the game's cells, with a grid
and coordinates, the parts of its skeleton and their relations to each other and to the terrain, a legend, and each
problem the check found marked where it is, beside a picture of its reference city where one is given. The developer
changes the template and checks it again until it is right.

**Why this priority**: A template is a designed layout [Design: line 209], and the request for this feature is to see
it without starting the game [Spec Kit]. The report of User Story 1 says what is wrong; the picture shows the layout
as a whole, before generation fills it.

**Independent Test**: Write a small test template with a known terrain shape and skeleton, check it, and compare each
cell, part and relation in the picture with the template.

**Acceptance Scenarios**:

1. **Given** a checked template, **When** the developer opens its picture, **Then** every cell of its terrain shape is
   in its place on a grid, with the coordinates along the edges.
2. **Given** a template whose skeleton relates its palace quarter to the river, **When** the developer opens its
   picture, **Then** both parts and the relation are shown and named.
3. **Given** a template with a problem at one cell, **When** the developer opens its picture, **Then** that cell is
   marked and the mark names the problem.
4. **Given** the river-bend town's template and its reference pictures, the screenshot and the render, **When**
   the developer opens its picture, **Then** the picture and each reference picture are side by side, and each part
   of the skeleton can be found in each.

---

### User Story 4 - Check and see a kit's buildings (Priority: P4)

Where a kit has a block library, the ready-made blocks built from spec cards, the developer checks each spec card,
the design card that fixes one building's plot, rooms and contents, and gets it as a picture of the building on the
game's cells.

**Why this priority**: A block library belongs to a kit, though the Empire's cities do not use one [Design: lines 167,
206], so it comes after the checks every kit needs.

**Independent Test**: Write a test kit with a block library of two spec cards, one with a known problem; check it and
compare the report and the two pictures with the cards.

**Acceptance Scenarios**:

1. **Given** a spec card whose contents name a definition `Data/` does not hold, **When** the check runs, **Then** it
   reports that name and the cell where it is.
2. **Given** a checked spec card, **When** the developer opens its picture, **Then** its plot, rooms and contents are
   shown on the grid, with a legend.

---

### User Story 5 - Add a culture by copying one (Priority: P5)

Another author adds a culture to Mantle. The author copies an existing culture's skeletons and kit, such as the
Empire's with the river-bend town's template, changes them for the new culture, and runs the same check, which reports
problems and draws the pictures as it does for the Empire. The author changes nothing that is shared.

**Why this priority**: Lowering the barrier for other authors is necessary, and a culture adds only its skeletons and
kit [Direction]. It needs the forms, the check and the pictures of the stories before it.

**Independent Test**: Copy the Empire kit and the river-bend town's template into a test culture, change its word
list, wall settings and one skeleton relation, and run the check; compare the report and pictures with the changes,
and confirm that no shared file was changed.

**Acceptance Scenarios**:

1. **Given** a copy of the Empire kit and the river-bend town's template under a new culture's name, **When** the
   check runs, **Then** it checks and draws them as it does the originals, with the new culture named.
2. **Given** a new culture whose kit names a piece, **When** the check runs, **Then** it finds the piece among the
   shared pieces, which the new culture does not have to define again [Design: line 194].

---

### Edge Cases

- A template, kit or laid-out city names one of Imperium's own definitions, such as a piece, a generic building
  element the base game lacks [Design: line 194]: the check looks for it among Imperium's own definitions, and reports
  it when it is not there.
- A terrain shape reaches past the map size the template states or past a city's 350×350 map, a laid-out city reaches
  past its map, or either leaves a cell with no terrain: the check reports each such cell.
- A skeleton relation names a part the skeleton does not hold, or a terrain the terrain shape does not hold: the check
  reports the relation.
- A definition from an expansion other than Royalty, marked as that expansion's content: the check accepts it, and the
  picture's legend names the expansion [Design: imperium.md line 110].
- A laid-out city is given without a reference picture, or with one the check cannot read: the check checks and draws
  the city, says that no comparison was made, and does not count its template as passing the comparison.
- One of the river-bend town's reference pictures is not yet in `template-references/`: the check draws the template
  beside those that are there and says which is missing, and the maintainer's judgment of the calibration waits for
  both [Direction].
- `Data/` cannot be found or is of another game version: the check stops and says so, and reports nothing as
  passing.

## Requirements *(mandatory)*

### Functional Requirements

**The forms**

- **FR-001**: A template MUST hold its terrain shape and its skeleton together, what generation picks it by, the world
  tile and size it suits [Design: line 209], its culture, and the reference city it is drawn from [Direction].
- **FR-002**: A template MUST NOT be a drawn map of a city: it MUST NOT place on its cells the things a city is built
  of, such as buildings, walls and paving, which a kit gives when generation lays out a city [Design: lines 184, 204,
  209, 221]. A template MUST belong to one culture, whose kit fills it, and each culture MUST have its own skeletons and
  templates [Design: line 184; Direction]. A skeleton MAY hold slots that vary within its culture, such as walls a city
  may have or lack, or a secondary core that small cities do not have [Design: line 200; Direction], and MUST NOT hold
  slots meant to carry it to another culture [Direction].
- **FR-003**: A template MUST state the smallest map it needs, as an official site states the smallest map it needs
  [Data: `AncientComplex.xml` line 15], and MUST fit a city's map, which is 350×350 cells [Direction]; maps are square
  [Data: `Dialogs_Various.xml` line 153], and a site's map takes its own size [Data: `WorldObjects.xml` line 205].
- **FR-004**: A terrain shape MUST hold, for each cell of the site, the terrain there, any natural rock, and the roof
  over it, each as a definition the game holds [Data: terrain, natural rock, roofs], so that it can be checked against
  `Data/` [Testing].
- **FR-005**: A skeleton MUST hold the fixed parts of a city's layout, such as its core, palace quarter, gates and
  main street [Design: line 204], and the wall line, districts, plazas and public buildings read from the reference
  city [Direction], and MUST record them as their relations to each other and to the terrain, not as coordinates
  [Design: line 204].
- **FR-006**: A kit MUST hold its culture and its fixed generation data: its word list, skeleton, groups, fill and wall
  settings [Design: line 184], and, where it uses one, a block library of ready-made blocks built from spec cards
  [Design: line 167].
- **FR-007**: A spec card MUST fix one building: its plot, its rooms and their contents [Design: line 206].
- **FR-008**: A laid-out city, the city that generation lays out on a map from a template and a kit, MUST be written in
  one form that holds the template and kit it comes from, its map size, each cell's terrain, natural rock and roof,
  each thing that stands on the map with its definition, cell, rotation and, where its definition takes one, its
  material, and where each part of the template's skeleton lies, so that the check reads what generation writes
  [Roadmap: R2; Design: lines 173, 204; Data: `AncientPrefabs.xml` lines 12, 13 and 23].
- **FR-009**: Templates and kits MUST be data that Imperium holds and Mantle's generation reads, and MUST NOT hold
  generation itself. Picking a template, mirroring, turning and stretching it to fit the site, and filling its blocks
  with the kit's buildings belong to R2, and generation does nothing else to a template [Roadmap: R13, R2;
  Design: lines 184, 209; Direction].
- **FR-010**: A template's layout MUST be Imperium's own: the relations of its terrain shape and skeleton may be drawn
  from a reference city's layout relationships, but a template MUST NOT hold another game's art, names, models or
  code, and MUST NOT be a cell-by-cell tracing of a reference picture, apart from the river-bend town's, which may
  follow its reference pictures closely (FR-031) [Direction; EULA: line 76].
- **FR-011**: The Empire's elements in a template or kit, such as the names in a word list and its public buildings,
  MUST come from Rome as reliable sources describe it, leaning toward New Rome, and not from popular images of Rome
  or from a reference city [Design: setting.md lines 56, 59-60; Direction].

**The check**

- **FR-012**: The check MUST run outside the game, reading templates, kits, laid-out cities and the game's definitions
  in `Data/`, without starting the game [Testing].
- **FR-013**: The check MUST report each name of a definition that it finds neither in `Data/` nor among Imperium's own
  definitions [Testing; Data].
- **FR-014**: The check MUST report each name that stands where its kind of definition cannot go, such as a
  definition that is not a terrain in a terrain shape, one that is not a wall in wall settings, or any thing a city is
  built of placed on a template's cells (FR-002) [Data; Design: line 209].
- **FR-015**: The check MUST accept definitions of the base game and Royalty, and MUST report a definition of any other
  expansion unless the template, kit or laid-out city marks it as that expansion's content, since Imperium requires
  Royalty alone and other expansions add content [Design: imperium.md lines 108-110; Data: each expansion's
  `About/About.xml`].
- **FR-016**: The check MUST report each cell of a terrain shape that lies outside the smallest map its template
  states or outside a city's 350×350 map, each cell of a laid-out city that lies outside its map, and each cell of
  either that has no terrain [Data; Direction].
- **FR-017**: The check MUST report each skeleton relation that names a part the skeleton does not hold, or a terrain
  the terrain shape does not hold [Design: line 204], and each template whose culture has no kit [Direction].
- **FR-018**: The check MUST report each thing in a laid-out city that stands on a terrain lacking the affordance the
  thing needs, which is its material's when its definition says so [Data: `Buildings_Base.xml` line 11;
  `Buildings_Structure.xml` lines 277-278; `Various_Stone.xml` line 88; `Terrain_Natural.xml`]; each thing whose
  cells, by its definition's size, reach past the map; and each material its definition does not take
  [Data: `Buildings_Structure.xml` lines 286-290].
- **FR-019**: Each problem MUST be reported with its template, kit or laid-out city, the part it is in and, where it
  has one, its cell [Spec Kit].
- **FR-020**: Every result MUST state that testing in the game is the final check and that it is still to come; a
  template, kit or laid-out city with no problem found MUST NOT be reported as final [Testing; Roadmap: R13].
- **FR-021**: The check MUST read the game's files where they are installed, and MUST NOT copy them into Imperium or
  its results, beyond the names and labels it reports [EULA: line 86].
- **FR-022**: The same template, kit or laid-out city, checked against the same `Data/` with the same reference
  picture, MUST always give the same report and the same pictures [Testing].

**The pictures**

- **FR-023**: The check MUST draw each template as a picture of its site: every cell of the terrain shape in its place
  on a grid, the coordinates along the edges as the game gives positions, `x` and `z`
  [Data: `AncientPrefabs.xml` line 12], and the skeleton's parts and relations shown and named on it [Spec Kit].
- **FR-024**: The check MUST draw each spec card as a picture of its building: its plot, rooms and contents on the
  same kind of grid [Design: line 206; Spec Kit].
- **FR-025**: The check MUST draw each laid-out city on the same kind of grid, with each thing where it stands and each
  part of the template's skeleton named where it lies, and MUST set the whole drawing beside the whole of each
  reference picture given, so that all are seen at once; a template's picture MUST be set beside its reference
  pictures in the same way when they are given [Direction; Spec Kit].
- **FR-026**: Each picture MUST hold a legend that names each terrain, rock, roof and thing it shows under the label
  its definition gives, and names the expansion of any definition from an expansion other than Royalty [Data;
  Design: imperium.md line 110].
- **FR-027**: Each problem that has a cell MUST be marked at that cell in the picture, with what it is [Spec Kit].
- **FR-028**: The check MUST read a reference picture where the developer keeps it, and MUST NOT put it into
  Imperium's repository or its released files [Direction; EULA: line 76].

**The comparison**

- **FR-029**: The check MUST measure whether each relation of the template's skeleton holds in the laid-out city, and
  MUST report each one that does not, with the parts it relates and where they lie [Design: line 204; Direction]. A
  laid-out city in which every relation holds MUST then be judged by the maintainer, who looks at the side-by-side
  picture and accepts or rejects it; the check MUST NOT report a match by itself [Direction].
- **FR-030**: A template MUST count as passing only once the check has drawn a city laid out from it, every relation
  of its skeleton holds there, and the maintainer has accepted the comparison with its reference as FR-029 sets,
  whoever wrote the template; the check in the game still follows [Direction; Testing].
- **FR-031**: The first template MUST be the river-bend town's, and it MUST calibrate the method before any other
  template of game content is written [Direction]:
  - Its template MUST be written from its reference pictures: the screenshot of the player-built city, which is the
    source, and the newest render on the game's cells, an earlier reading of that screenshot with its heights, hidden
    areas and exact sizes guessed, both in `template-references/` in the project's files. The template MUST fit a
    city's 350×350 map, whatever size the render was drawn at, keeping the same skeleton relations (Clarifications).
    The check MUST pass the template and draw it beside them [Direction; FR-003; FR-025].
  - The town that R2's generation lays out from it with a kit MUST keep every relation of its skeleton, as FR-029
    measures: the river bend, the wall line, which districts adjoin, how the main streets connect, and where the
    plazas and public buildings lie. The town MUST come from generation, not be written by hand, since only generation
    tests the method [Direction; Roadmap: R2].
  - The maintainer MUST then judge the laid-out town by eye beside the screenshot and the render. A cell-exact match
    to the render MUST NOT be required, since it is a guess too [Direction].
  - If the method cannot express the town, the method MUST be fixed before anything else [Direction].
  - Once the calibration passes, the town MUST be laid out with Imperium's own buildings, materials and names, and its
    template MUST then ship as a regular template [Direction; FR-011].
- **FR-032**: Kits and templates MUST come, in time, for the culture of every faction that has settlements: the Empire
  [Data: `Royalty/Defs/FactionDefs/Faction_Empire.xml` line 5], tribal and industrial (outlander) [Data:
  `Core/Defs/FactionDefs/Factions_Misc.xml` lines 185 and 443], pirate [Data: same file, lines 511 and 517], medieval,
  for the medieval factions other mods add [Direction], and Odyssey's Traders Guild and Salvagers, whose settlements lie
  on the Orbit layer [Data: `Odyssey/Defs/FactionDefs/Factions_Misc.xml` lines 5, 17, 40-42, 168, 188 and 202-204]
  [Design: line 184; Direction]. This feature MUST hold the Empire kit and the river-bend town's template; the other
  cultures' kits and templates are later work [Direction; Roadmap: R13].
- **FR-033**: Adding a culture MUST need only its skeletons, in its templates, and its kit [Direction]. Everything else
  MUST be shared and the same for every culture: the forms of templates and kits, the check outside the game and its
  pictures, generation's picking, mirroring, turning, stretching and filling [Roadmap: R2], and the pieces, which every
  kit shares and each faction skins [Design: line 194; Direction].
- **FR-034**: An author MUST be able to start a culture by copying an existing culture's skeletons and kit, and the
  check MUST treat the copy as it treats the original [Direction].
- **FR-035**: The river-bend town MUST serve as the complete worked example, from its reference pictures through its
  skeleton and the Empire kit to the city generation lays out from them [Direction; FR-031].

### Key Entities *(include if feature involves data)*

- **Template**: the designed layout of a whole city site: its terrain shape, its skeleton, what it is picked by, the
  smallest map it needs, its culture and the reference city it is drawn from. It places no thing a city is built of.
- **Terrain shape**: the site's cells, each with its terrain, any natural rock and its roof, as the game defines them.
- **Skeleton**: the fixed parts of a city's layout and their relations to each other and to the terrain. A kit holds
  one too [Design: line 184].
- **Kit**: one culture's fixed set of generation data: word list, skeleton, groups, fill and wall settings, and
  possibly a block library.
- **Block library**: a kit's ready-made blocks, built from spec cards.
- **Spec card**: one building's plot, rooms and contents.
- **Piece**: a generic building element of generated settlements that the base game lacks, shared by every kit and
  skinned by faction [Design: line 194].
- **Culture**: one kind of settlement with its own kit and its own skeletons and templates, such as the Empire's.
- **Laid-out city**: the city generation lays out on a map from a template and a kit: each cell's terrain, rock and
  roof, each thing that stands there, and where each part of the skeleton lies.
- **Reference city**: the player-built city a template is drawn from, and its **reference pictures**, such as a
  screenshot of it or, for the river-bend town, the render of an earlier reading, which the developer keeps outside
  Imperium's files.
- **Report**: what one run of the check found, each problem with its place, and the statement that the check in the
  game is still to come.
- **Picture**: the drawing of one template, laid-out city or spec card, with grid, coordinates, legend and marked
  problems, and for a template or laid-out city, the reference picture beside it.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: For a set of test templates, kits and laid-out cities holding one problem of each kind that FR-013 to
  FR-018 and FR-029 name, the check reports 100% of the problems, and reports none for those that hold no problem.
- **SC-002**: For every reported problem that has a cell, a developer finds that cell in the picture from the report
  alone, without reading the template or laid-out city.
- **SC-003**: Checking and drawing one template, or one laid-out city beside its reference, finishes before the game,
  started on the same computer, reaches its main menu.
- **SC-004**: 100% of reports state that testing in the game is the final check and is still to come.
- **SC-005**: For every laid-out city given with a reference picture, the developer sees the whole city and the whole
  reference at once, side by side, and can name in both where each part of the skeleton lies.
- **SC-006**: No template counts as passing without a laid-out city from it in which every skeleton relation holds
  and whose comparison with its reference the maintainer has accepted (FR-030).
- **SC-007**: The river-bend town's template passes the check, and in its picture beside each reference picture,
  every part of its skeleton is found in the same relations to the river and to the other parts.
- **SC-008**: Before any other template of game content is written, a town that generation lays out from the
  river-bend town's template keeps 100% of its skeleton relations, and the maintainer has accepted it beside the
  screenshot and the render (FR-031).
- **SC-009**: A test culture copied from the Empire kit and the river-bend town's template is checked and drawn with no
  change to any shared form, check, picture or piece (FR-033, FR-034).

## Assumptions

- The supported game version is 1.7, as for R1 (`specs/001-mod-foundation/spec.md`, Clarifications), and the
  definitions read are those of RimWorld 1.7.5014.
- The check runs where `Data/` is available: on the maintainer's computer, in the game's install folder, and in cloud
  threads, from the project's copy of RimWorld 1.7.5014's `Data/`.
- Which templates and kits the alpha holds, and generation, are R2's [Roadmap: R13, R2]. The form of a laid-out city
  is set here so that R2's generation writes it and the check reads it.
- Until R2 generates cities, the laid-out cities the check is tested with are written by hand from test templates and
  kits. Test templates, kits and laid-out cities written for this feature are not game content. The river-bend town's
  template is the first template of game content, and it ships once its calibration passes (FR-031), in a release
  that R2 sets [Roadmap: R2]. The Empire kit is the first kit of game content (FR-032).
- The check in the game, the final one, comes when R2 places templates on a map [Roadmap: R13; Testing].
- The forms hold the parts the design and the maintainer's direction name, and take further parts when either names
  them [Design; Direction].
- How the forms are written, and the pictures' look and file format, are chosen in `/speckit-plan`.
