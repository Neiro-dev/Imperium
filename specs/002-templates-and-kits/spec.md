# Feature Specification: Templates and kits

**Feature Branch**: `claude/project-thread-wgq7xi`

**Created**: 2026-11-24

**Status**: Draft

**Input**: Parent roadmap: `ROADMAP.md` → entry **R13**, Templates and kits. The designed layouts of city sites, each a
terrain shape with a skeleton (templates), and each culture's fixed set of generation data (kits) are data that
Mantle's generation uses, checked outside the game against the game's own definitions before Mantle uses them
(Imperium-old glossary "template", "kit", "skeleton"; constitution, Source Register, "Testing outside the
game"). Scope: the forms of templates and kits, and their check outside the game against `Data/`. Deferred: which
templates and kits the alpha holds, and generation, which picks templates and may mirror, turn and stretch them (R2);
the check in the game, which is the final one, once R2 places them (R2). As requested for this feature, the check
shows a template as a picture of its site, so that the developer can see it without starting the game.

## Sources

Each requirement below names its source in brackets. The sources are those the constitution's Source Register gives:

- **[Roadmap]**: `ROADMAP.md`, entries R13 (intent and scope boundary) and R2.
- **[Design]**: Imperium's own design, Imperium-old `main` (20a052b), `docs/glossary.md`, section City building and
  generation: block library (line 167), kit (line 184), piece (line 194), skeleton (line 204), spec card (line 206)
  and template (line 209); `docs/imperium.md`, section Expansions (lines 108-110); and `docs/setting.md`, section
  Rome (lines 56 and 59-60).
- **[Testing]**: the constitution's Source Register, row Testing outside the game: the base game and official
  expansions in `Data/`; testing outside the game comes before testing in the game and does not replace it, and
  testing in the game is the final check.
- **[Data]**: the base game and official expansions in `Data/` of RimWorld 1.7.5014: terrain
  (`Core/Defs/TerrainDefs/`), natural rock (`Core/Defs/ThingDefs_Buildings/Buildings_Natural.xml` line 47), roofs
  (`Core/Defs/Misc/RoofDefs/Roofs.xml` lines 5, 14 and 24), the smallest map a site needs
  (`Ideology/Defs/Sites/AncientComplex.xml` line 15), square maps (`Core/Languages/English/Keyed/Dialogs_Various.xml`
  line 153), positions on a map as `(x, 0, z)` (`Odyssey/Defs/PrefabDefs/AncientPrefabs.xml` line 12), and each
  expansion's `About/About.xml`.
- **[EULA]**: `EULA.txt`, which is always followed (constitution, Source Register).
- **[Direction]**: the maintainer's broad direction on where template layouts come from, which Imperium-old's design
  leaves open (constitution, Source Register, row Imperium's own design; Principle IV). Templates are drawn from
  player-built cities that Ubisoft officially features as recommended Anno 117 cities, as reference only: the layout
  relationships read from such a city, its river, walls, districts, streets and public buildings, are expressed as
  Imperium's own templates in the design's form. Nothing of Anno's art, names, models or code is used, and no
  reference image is traced cell by cell. Two pictures of one such city, a town at a river bend, are in the project's
  files (`uploads/hearth/`), kept only for comparison.
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
4. **Given** a template and a kit with no problem, **When** the check runs, **Then** it reports none, and says that
   the check in the game, which is the final one, is still to come.

---

### User Story 2 - See a template as a picture of its site (Priority: P2)

The developer gets each checked template as a picture of its site: its terrain shape on the game's cells, with a grid
and coordinates, the parts of its skeleton and their relations to each other and to the terrain, a legend, and each
problem the check found marked where it is. The developer changes the template and checks it again until it is right.

**Why this priority**: A template is a designed layout [Design: line 209], and the request for this feature is to see
it without starting the game [Spec Kit]. The report of User Story 1 says what is wrong; the picture shows the layout
as a whole.

**Independent Test**: Write a small test template with a known terrain shape and skeleton, check it, and compare each
cell, part and relation in the picture with the template.

**Acceptance Scenarios**:

1. **Given** a checked template, **When** the developer opens its picture, **Then** every cell of its terrain shape is
   in its place on a grid, with the coordinates along the edges.
2. **Given** a template whose skeleton relates its palace quarter to the river, **When** the developer opens its
   picture, **Then** both parts and the relation are shown and named.
3. **Given** a template with a problem at one cell, **When** the developer opens its picture, **Then** that cell is
   marked and the mark names the problem.

---

### User Story 3 - Check and see a kit's buildings (Priority: P3)

Where a kit has a block library, the ready-made blocks built from spec cards, the developer checks each spec card,
the design card that fixes one building's plot, rooms and contents, and gets it as a picture of the building on the
game's cells.

**Why this priority**: A block library belongs to a kit, though the Roman city does not use one [Design: lines 167,
206], so it comes after the checks every kit needs.

**Independent Test**: Write a test kit with a block library of two spec cards, one with a known problem; check it and
compare the report and the two pictures with the cards.

**Acceptance Scenarios**:

1. **Given** a spec card whose contents name a definition `Data/` does not hold, **When** the check runs, **Then** it
   reports that name and the cell where it is.
2. **Given** a checked spec card, **When** the developer opens its picture, **Then** its plot, rooms and contents are
   shown on the grid, with a legend.

---

### Edge Cases

- A template or kit names one of Imperium's own definitions, such as a piece, a generic building element the base game
  lacks [Design: line 194]: the check looks for it among Imperium's own definitions, and reports it when it is not
  there.
- A terrain shape reaches past the map size the template states, or leaves a cell with no terrain: the check reports
  each such cell.
- A skeleton relation names a part the skeleton does not hold, or a terrain the terrain shape does not hold: the check
  reports the relation.
- A definition from an expansion other than Royalty, marked as that expansion's content: the check accepts it, and the
  picture's legend names the expansion [Design: imperium.md line 110].
- `Data/` cannot be found or is of another game version: the check stops and says so, and reports no template as
  passing.

## Requirements *(mandatory)*

### Functional Requirements

**The forms**

- **FR-001**: A template MUST hold its terrain shape and its skeleton together, and what generation picks it by, the
  world tile and size it suits [Design: line 209].
- **FR-002**: A template MUST state the smallest map it needs, as an official site states the smallest map it needs
  [Data: `AncientComplex.xml` line 15]; maps are square [Data: `Dialogs_Various.xml` line 153].
- **FR-003**: A terrain shape MUST hold, for each cell of the site, the terrain there, any natural rock, and the roof
  over it, each as a definition the game holds [Data: terrain, natural rock, roofs], so that it can be checked against
  `Data/` [Testing].
- **FR-004**: A skeleton MUST hold the fixed parts of a city's layout, such as its core, palace quarter, gates and
  main street, and record them as their relations to each other and to the terrain, not as coordinates
  [Design: line 204].
- **FR-005**: A kit MUST hold its culture and its fixed generation data: its word list, skeleton, groups, fill and wall
  settings [Design: line 184], and, where it uses one, a block library of ready-made blocks built from spec cards
  [Design: line 167].
- **FR-006**: A spec card MUST fix one building: its plot, its rooms and their contents [Design: line 206].
- **FR-007**: Templates and kits MUST be data that Imperium holds and Mantle's generation reads, and MUST NOT hold
  generation itself: picking, mirroring, turning and stretching belong to R2 [Roadmap: R13, R2; Design: line 209].
- **FR-008**: A template's layout MUST be Imperium's own: the relations of its terrain shape and skeleton may be drawn
  from a reference city's layout relationships, but a template MUST NOT hold another game's art, names, models or
  code, and MUST NOT be a cell-by-cell tracing of a reference image [Direction; EULA: line 76].
- **FR-009**: The Empire's elements in a template or kit, such as the names in a word list and its public buildings,
  MUST come from Rome as reliable sources describe it, leaning toward New Rome, and not from popular images of Rome
  or from a reference city [Design: setting.md lines 56, 59-60; Direction].

**The check**

- **FR-010**: The check MUST run outside the game, reading templates, kits and the game's definitions in `Data/`,
  without starting the game [Testing].
- **FR-011**: The check MUST report each name of a definition that it finds neither in `Data/` nor among Imperium's own
  definitions [Testing; Data].
- **FR-012**: The check MUST report each name that stands where its kind of definition cannot go, such as a
  definition that is not a terrain in a terrain shape, or one that is not a wall in wall settings [Data].
- **FR-013**: The check MUST accept definitions of the base game and Royalty, and MUST report a definition of any other
  expansion unless the template or kit marks it as that expansion's content, since Imperium requires Royalty alone and
  other expansions add content [Design: imperium.md lines 108-110; Data: each expansion's `About/About.xml`].
- **FR-014**: The check MUST report each cell of a terrain shape that lies outside the smallest map the template states,
  or that has no terrain [Data].
- **FR-015**: The check MUST report each skeleton relation that names a part the skeleton does not hold, or a terrain
  the terrain shape does not hold [Design: line 204].
- **FR-016**: Each problem MUST be reported with its template or kit, the part it is in and, where it has one, its cell
  [Spec Kit].
- **FR-017**: Every result MUST state that testing in the game is the final check and that it is still to come; a
  template or kit with no problem found MUST NOT be reported as final [Testing; Roadmap: R13].
- **FR-018**: The check MUST read the game's files where they are installed, and MUST NOT copy them into Imperium or
  its results, beyond the names and labels it reports [EULA: line 86].
- **FR-019**: The same template or kit, checked against the same `Data/`, MUST always give the same report and the
  same pictures [Testing].

**The pictures**

- **FR-020**: The check MUST draw each template as a picture of its site: every cell of the terrain shape in its place
  on a grid, the coordinates along the edges as the game gives positions, `x` and `z`
  [Data: `AncientPrefabs.xml` line 12], and the skeleton's parts and relations shown and named on it [Spec Kit].
- **FR-021**: The check MUST draw each spec card as a picture of its building: its plot, rooms and contents on the
  same kind of grid [Design: line 206; Spec Kit].
- **FR-022**: Each picture MUST hold a legend that names each terrain, rock, roof and thing it shows under the label
  its definition gives, and names the expansion of any definition from an expansion other than Royalty [Data;
  Design: imperium.md line 110].
- **FR-023**: Each problem that has a cell MUST be marked at that cell in the picture, with what it is [Spec Kit].

### Key Entities *(include if feature involves data)*

- **Template**: the designed layout of a whole city site: its terrain shape, its skeleton, what it is picked by and
  the smallest map it needs.
- **Terrain shape**: the site's cells, each with its terrain, any natural rock and its roof, as the game defines them.
- **Skeleton**: the fixed parts of a city's layout and their relations to each other and to the terrain. A kit holds
  one too [Design: line 184].
- **Kit**: one culture's fixed set of generation data: word list, skeleton, groups, fill and wall settings, and
  possibly a block library.
- **Block library**: a kit's ready-made blocks, built from spec cards.
- **Spec card**: one building's plot, rooms and contents.
- **Report**: what one run of the check found, each problem with its place, and the statement that the check in the
  game is still to come.
- **Picture**: the drawing of one template or spec card, with grid, coordinates, legend and marked problems.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: For a set of test templates and kits holding one problem of each kind that FR-011 to FR-015 name, the
  check reports 100% of the problems, and reports none for the test template and kit that hold no problem.
- **SC-002**: For every reported problem that has a cell, a developer finds that cell in the picture from the report
  alone, without reading the template.
- **SC-003**: Checking and drawing one template finishes before the game, started on the same computer, reaches its
  main menu.
- **SC-004**: 100% of reports state that testing in the game is the final check and is still to come.

## Assumptions

- The supported game version is 1.7, as for R1 (`specs/001-mod-foundation/spec.md`, Clarifications), and the
  definitions read are those of RimWorld 1.7.5014.
- The check runs where `Data/` is available: on the maintainer's computer, in the game's install folder, and in cloud
  threads, from the project's copy of RimWorld 1.7.5014's `Data/`.
- Which templates and kits the alpha holds, the map size each template needs, and generation are R2's
  [Roadmap: R13, R2]. Test templates and kits written for this feature are not game content.
- The check in the game, the final one, comes when R2 places templates on a map [Roadmap: R13; Testing].
- The forms hold the parts the design names, and take further parts when the design names them [Design].
- How the forms are written, and the pictures' look and file format, are chosen in `/speckit-plan`.
