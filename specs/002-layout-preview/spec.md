# Feature Specification: Layout preview

**Feature Branch**: `claude/project-thread-wgq7xi`

**Created**: 2026-11-24

**Status**: Draft

**Input**: Parent roadmap: `ROADMAP.md` → entry **R13**. Layout preview: a settlement's layout on the game's cells is
drawn as a gridded map with coordinates and a legend, outside the game, so that a layout can be checked and changed
without starting the game (Imperium-old glossary "city building", "template"). Scope: drawing a layout description
that holds only what the game can place. Deferred: generating layouts (R2), placing them in the game (R4). A
development tool that goes into no release.

## Sources

Each requirement below names its source in brackets. The sources are those the constitution's Source Register gives:

- **[Roadmap]**: `ROADMAP.md`, entry R13, the paragraph after the table, and the section Releases.
- **[Spec Kit]**: Spec Kit 1.4.3, `docs/how-to/spec-of-specs.md`, The roadmap pass, step 2; and
  `.specify/templates/spec-template.md` lines 15-23. Development workflow.
- **[Design]**: Imperium's own design, Imperium-old `main` (20a052b): `docs/glossary.md`, section City building and
  generation (lines 157-215): "block" (line 166), "city building" (line 173), "district" (line 178), "landmark"
  (line 185), "skeleton" (line 204), "template" (line 209); `docs/imperium.md`, section Expansions (lines 106-112).
  Only the meaning of the design is used, not Imperium-old's code or tools.
- **[Data]**: the base game and official expansions in `Data/` of RimWorld 1.7.5014 (`Version.txt`): their terrain,
  roof and thing definitions (for example `Data/Core/Defs/TerrainDefs/`, `Data/Core/Defs/Misc/RoofDefs/Roofs.xml`,
  `Data/Core/Defs/ThingDefs_Buildings/`), each with its name (`defName`) and label; the terrain's affordances (for
  example `Data/Core/Defs/TerrainDefs/Terrain_Water.xml`); and the map size dialog, which gives every map as square,
  "{0}x{0}" cells (`Data/Core/Languages/English/Keyed/Dialogs_Various.xml` lines 152-157).
- **[Readme]**: `Readme.txt` of the same install, line 58: `-quicktest` starts the game into a tiny, fast-loading map.
  The first testing source.
- **[RimBridgeServer]**: RimBridgeServer (`pardeike/RimBridgeServer`), which addresses a map cell by its `x` and `z`
  coordinates (`docs/tool-reference.md` line 313) and inspects and screenshots cells on a map (`README.md`, Architect
  And Map State; Camera And Screenshots). The testing source after `Readme.txt`.
- **[EULA]**: `EULA.txt` of RimWorld, line 86: the game's resources may be used as a reference for a mod, but not
  ripped out and passed around on their own. Always followed.

A layout exists before the game places it on a map, as a designed template or as generated output [Design: "template",
"city building"], while the tests in the game look only at what is on a map [Readme; RimBridgeServer]. This feature is
the way to check a layout on its own before it is placed [Roadmap; Spec Kit]. It decides no game content: it draws
whatever a layout description holds. What a layout holds is decided by the slices that make layouts (R2, R4).

## User Scenarios & Testing *(mandatory)*

### User Story 1 - See a layout as a map (Priority: P1)

A developer working on Mantle, or the maintainer judging a layout's broad direction (constitution, Principle IV),
gives the preview a layout description and gets back one picture of the whole map: every cell in its place on a grid,
the coordinates along the edges, a legend that names each kind of terrain, roof and thing the layout uses, and the
layout's named areas outlined and labeled.

**Why this priority**: drawing a layout is the whole purpose of R13 [Roadmap]; the other stories change or check what
this one draws.

**Independent Test**: write a small description by hand (for example a 20 by 20 cell map with two kinds of terrain, a
walled room with a door and a roof, a tree and one named area), draw it, and compare each cell of the picture with the
description.

**Acceptance Scenarios**:

1. **Given** a layout description, **When** it is drawn, **Then** each cell shows the terrain the description gives
   it, and its roof and the things on it where the description gives them.
2. **Given** a drawn map, **When** the reader picks any cell, **Then** they can read its `x` and `z` coordinates from
   the grid and the edge labels, and these are the coordinates by which the game's testing tools address that cell
   [RimBridgeServer].
3. **Given** a description that uses several kinds of terrain, roof and thing, **When** it is drawn, **Then** the
   legend lists each kind used, under the label its definition gives [Data], and no kind that is not used.
4. **Given** a description with named areas, **When** it is drawn, **Then** each area is outlined and carries its
   name as the description writes it.

---

### User Story 2 - Change a layout and see it again quickly (Priority: P2)

After looking at a map, the developer changes the layout description as text and draws it again. Nothing in the game
is started, and no file of the game or of Imperium's released mod is touched.

**Why this priority**: R13 exists so that a layout can be changed and checked again without starting the game
[Roadmap]; it builds on the drawing of User Story 1.

**Independent Test**: draw a description, change the terrain of one cell in it, draw it again, and compare the two
pictures; then time the second drawing against starting the game with `-quicktest` on the same computer [Readme].

**Acceptance Scenarios**:

1. **Given** a drawn description, **When** one entry in it changes and it is drawn again, **Then** the new picture
   shows the change, and nothing else in it differs from the first.
2. **Given** the game is not running, **When** a description is drawn, **Then** the drawing succeeds, and no file of
   the game's install or of Imperium's released mod changes.

---

### User Story 3 - Show only what the game can place (Priority: P3)

A description that holds something the game cannot place is never shown as if the game could place it. Each problem is
marked at its cell on the map and listed with its reason.

**Why this priority**: R13 draws descriptions that hold only what the game can place [Roadmap]; this story keeps the
pictures honest about that, once User Stories 1 and 2 work.

**Independent Test**: draw a description that holds a kind the game does not define, a thing whose footprint runs past
the map's edge, and a wall on deep water; each is marked and listed with its cell and reason, and the picture says the
layout cannot be placed as it stands.

**Acceptance Scenarios**:

1. **Given** a description that names a terrain, roof, thing or material the game does not define, **When** it is
   drawn, **Then** that name and its cell are listed as a problem.
2. **Given** a thing whose footprint, at its rotation, runs past the map's edge, **When** it is drawn, **Then** it is
   listed as a problem [Data: the thing's size].
3. **Given** a thing on terrain whose affordances do not allow it, **When** it is drawn, **Then** it is listed as a
   problem [Data: the terrain's affordances and the affordance the thing needs].
4. **Given** two things in one cell that the game cannot place together, **When** it is drawn, **Then** they are listed
   as a problem.
5. **Given** a description with at least one problem, **When** it is drawn, **Then** the picture states that the layout
   cannot be placed in the game as it stands, and a description with none does not.

---

### Edge Cases

- A kind that comes from an official expansion other than Royalty: it is drawn, and the legend names the expansion it
  comes from, because Imperium requires only Royalty and must be complete with Royalty alone, while each other active
  expansion adds content [Design: `docs/imperium.md` lines 108-110].
- A cell whose terrain the description does not give: listed as a problem, since every cell of a game map has a
  terrain [Data: every map is its full square of cells].
- A named area that runs past the map's edge: listed as a problem.
- Named areas that overlap, such as a block inside a district: both are drawn, since the design nests them [Design:
  "block", "district"].
- A thing the game makes from a material, given without one or with one it does not accept: listed as a problem [Data:
  the thing's material categories].
- A description with no roofs, things or named areas: the map shows the terrain alone and the legend lists only the
  terrain kinds.
- The largest map size the game offers: the whole map is drawn, and every cell can still be told apart.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: The preview MUST draw a layout description as one picture of the whole map, a square of cells as wide as
  the description's map size [Roadmap; Data: Dialogs_Various.xml line 153].
- **FR-002**: A layout description MUST give the terrain of every cell, and MAY give each cell a roof, things placed
  with their position, rotation and material, and named areas with the cells they cover [Data: terrain, roof and thing
  definitions; Design: "block", "district", "landmark"].
- **FR-003**: A layout description MUST name each terrain, roof, thing and material by the name the game's definition
  gives it (`defName`), so that it holds only what the game can place [Roadmap; Data].
- **FR-004**: The names a description may use MUST be those defined in the base game and official expansions in
  `Data/` of the supported game version, and in Imperium's own definitions once it has any [Data; Roadmap].
- **FR-005**: The picture MUST separate every two neighboring cells by a grid line and carry the coordinates along its
  edges, so that the coordinates of any cell can be read from it; the coordinates MUST be the game's `x` and `z` cell
  coordinates [Roadmap; RimBridgeServer: tool-reference.md line 313].
- **FR-006**: Each kind of terrain, roof and thing in a picture MUST be drawn so that it can be told apart from every
  other kind in the same picture, and listed in a legend under the label its definition gives; the legend MUST list
  exactly the kinds the layout uses [Roadmap; Data].
- **FR-007**: For a kind from an official expansion other than Royalty, the legend MUST name that expansion [Design:
  `docs/imperium.md` lines 108-110].
- **FR-008**: Each named area MUST be outlined and labeled with its name exactly as the description writes it
  [Roadmap; Design: "landmark"].
- **FR-009**: A thing MUST cover the cells that its size and rotation give it in the game [Data: the thing's size].
- **FR-010**: A layout description MUST be plain text that a person can read and change by hand [Roadmap: a layout
  can be changed].
- **FR-011**: The same description MUST always give the same picture, so that a change shows only its own difference
  [Roadmap: a layout can be changed and checked again].
- **FR-012**: Drawing MUST NOT need the game to run, and MUST NOT change any file of the game's install or of
  Imperium's released mod [Roadmap: without starting the game; Releases: R13 goes into no release].
- **FR-013**: The preview MUST read the game's definitions from a copy of the game the user has, and MUST NOT carry
  copies of the game's files in the repository [EULA: line 86].
- **FR-014**: Each problem of User Story 3 MUST be listed with its cell and reason and marked at its cell on the
  picture, and a picture with any problem MUST state that the layout cannot be placed in the game as it stands
  [Roadmap: only what the game can place].
- **FR-015**: The preview MUST NOT be part of any release of Imperium [Roadmap: Releases].

### Key Entities *(include if feature involves data)*

- **Layout description**: the text that describes one layout: its map size, the terrain of every cell, the roofs, the
  placed things and the named areas. Written by hand until a later slice generates it (R2) [Roadmap].
- **Kind**: a terrain, roof, thing or material as the game defines it, with its name, its label and the expansion it
  comes from [Data].
- **Placed thing**: one thing in the layout, with its kind, its cell, its rotation and, where the game needs one, its
  material [Data].
- **Named area**: a set of cells with a name, such as a district, a block or a landmark [Design].
- **Map picture**: the drawing of one description: the grid, the coordinates, every cell, the named areas, the legend
  and the list of problems [Roadmap].
- **Problem**: something in a description that the game cannot place, with its cell and reason (User Story 3).

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: For a test description, every cell of the picture (100%) shows the terrain, roof and things the
  description gives, at the coordinates it gives, checked cell by cell.
- **SC-002**: After a change to one cell, the new picture is ready sooner than the game, started with `-quicktest` on
  the same computer, shows its map [Readme: line 58].
- **SC-003**: For a test description that holds each kind of problem of User Story 3, every problem (100%) is listed
  with its cell and reason; for a description with no problem, none is listed.
- **SC-004**: Across any number of drawings, no file of the game's install or of Imperium's released mod changes,
  checked by comparing those files before and after.

## Assumptions

- The maintainer and the developers look at the picture as an image file, which a session attaches to its thread or
  pull request; this needs no game and no special viewer.
- Until R2 generates layouts, descriptions are written by hand; R2 writes the same kind of description, and R4 places
  one in the game. Both are deferred [Roadmap].
- The supported game version is 1.7, as for R1 (`specs/001-mod-foundation/spec.md`, Clarifications), and the
  definitions read are those of RimWorld 1.7.5014.
- How each kind looks in the picture, and the picture's file format, are chosen in `/speckit-plan`; they are not game
  content.
- The images of an earlier tool of Imperium-old show what existed then, not design, and are not a source.
