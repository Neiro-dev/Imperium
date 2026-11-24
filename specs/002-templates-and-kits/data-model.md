# Data Model: Templates and kits

Templates and kits are definitions the game loads, from Mantle's mod for the tribal culture and from Imperium for the
Empire (research R-1); a laid-out city is a file generation writes and the check reads, and a reading is a file in the
same form that a culture's template and kit are taken from (R-7); the report and pictures are the check's output
(R-11). Their XML forms are in
[contracts/](contracts/), and the sources of each form in [research.md](research.md). The forms hold the parts the
design and the maintainer's direction name, and take further parts when either names them (spec, Assumptions).

Common forms, all from `Data/` (R-3):

- **rect**: `(minX,minZ,maxX,maxZ)`, inclusive, in cells.
- **pixel rect** (only in a reading from a picture): the same form, `(minX,minY,maxX,maxY)`, inclusive, in the
  reference picture's pixels counted from its upper-left pixel as Pillow counts them (R-9; R-17).
- **layer**: a list whose elements are each named by a definition and hold that definition's `rects`; an element
  written later covers the cells of one written earlier, so an author can lay a whole site and then the river on it
  [Direction: lowering the barrier for other authors].
- **position**: `(x, 0, z)`. **size**: `(x, z)`. **minMapSize**: `(x, 1, z)`. **rotation**: `North`, `East`, `South`
  or `West`.
- **MayRequire**: on the element that names a definition of an expansion that the mod holding the file does not
  require, that expansion's package identifier (FR-015).

## TemplateDef (`Mantle.TemplateDef`, in a mod's `Defs/TemplateDefs/`)

| Field | Form | Rule | Source |
|-------|------|------|--------|
| `defName`, `label` | text | as every definition | `Data/` |
| `kit` | a `KitDef` | required; the culture whose kit fills it; the check reports a template whose kit does not exist | FR-001, FR-002, FR-017 |
| `reference` | `name` and `pictures` | the mod's own name for the reference city and a label for each of its reference pictures, such as `screenshot` and `render`; no name of another game | FR-001, FR-010, FR-028 |
| `allowedBiomes`, `allowedRivers` | lists of `BiomeDef`, `RiverDef` | the world tiles it suits; empty means any; the Empire's templates state the biomes, the tribal culture's leave them empty | FR-001, FR-040; R-3, R-14 |
| `naturalEnemy`, `permanentEnemy` | `true` or `false`, `false` when left out | the attitude of the factions it serves: those whose `FactionDef` holds the same two values; no faction is named | FR-039; R-14 |
| `minMapSize` | `(x, 1, z)` | required; square; no larger than `(350, 1, 350)` | FR-003 |
| `terrainShape` | TerrainShape | where `terrain` holds any cell, every cell inside `minMapSize` has a terrain, and nothing lies outside it; a template taken from a preset island leaves `terrain`, `rocks` and `roofs` empty, since the land is generated first from the world tile and the city follows it, and its `features` hold only what its skeleton relations name | FR-004, FR-016, FR-036; R-18 |
| `skeleton` | Skeleton | read together with its kit's skeleton | FR-005; R-5 |

## TerrainShape

| Field | Form | Rule | Source |
|-------|------|------|--------|
| `terrain` | layer of `TerrainDef` | natural terrain only | FR-004; R-4 |
| `rocks` | layer of `ThingDef` | natural rock only | FR-004; R-4 |
| `roofs` | layer of `RoofDef` | natural roofs only | FR-004; R-4 |
| `features` | list of Feature | names unique within the template | FR-005, FR-017; R-5 |

**Feature**: `name`; `rects`; `flowsFrom`, a rotation naming the map edge a river enters by, for a river only.

## Skeleton (in a TemplateDef and in a KitDef)

| Field | Form | Rule | Source |
|-------|------|------|--------|
| `parts` | list of Part | names unique across the template's and its kit's skeletons, except that a template may name a kit's part again with the same kind | R-5 |
| `relations` | list of Relation | each names parts, or features of the template's terrain shape; a kit's relations name parts only | FR-005, FR-017; R-5 |

**Part**: `name`; `kind`, one of `Core`, `SecondaryCore`, `PalaceQuarter`, `Gate`, `RiverGate`, `WaterGate`,
`TowerChain`, `Lifeline`, `MainStreet`, `SecondaryAxis`, `District`, `Acropolis`, `Landmark`, `Bridge`, `WallLine`,
`Plaza`, `PublicBuilding`; `optional`, true for a slot that a city may leave out (default false).

**Relation**: `relation`, one of the kinds below; `a` and `b`, each a part or feature; and the field the kind needs.

| `relation` | Needs | Holds when (R-6) | Source |
|------------|-------|------------------|--------|
| `Inside` | `a`, `b` | every cell of `a` is a cell of `b` or enclosed by it | glossary lines 174, 178, 200 |
| `Adjoins` | `a`, `b` | a cell of `a` is a cell of `b` or shares an edge with one | lines 165, 188, 197, 199; [Direction] |
| `Across` | `a`, `b`, `feature` | no path of neighbouring cells outside `feature` joins `a` and `b` | line 204; [Direction] |
| `SameSide` | `a`, `b`, `feature` | such a path exists | line 204; [Direction] |
| `Upstream` | `a`, `b`, `feature` (a river) | the river cell nearest `a` lies fewer steps from where the river enters than the one nearest `b` | line 193 |
| `Farther` | `a`, `b`, `than` | the distance from `a` to `b` is greater than from `than` to `b` | line 193 |

## KitDef (`Mantle.KitDef`, in a mod's `Defs/KitDefs/`)

| Field | Form | Rule | Source |
|-------|------|------|--------|
| `defName`, `label` | text | the `defName` names the culture, such as `Tribal` or `Empire` | FR-006; [Direction] |
| `nameMaker` | a `RulePackDef` | the word list | FR-006, FR-011; R-3 |
| `skeleton` | Skeleton | what every city of the culture has; parts only | FR-006; R-5 |
| `wallSettings` | `wallDef`, a `ThingDef` | a wall (`building/isWall`) | FR-006, FR-014; R-3 |
| `groups` | list of Group | derived in FR-047's order; where the design and the recorded direction are silent, the sets of things placed together that the culture's reading shows (R-8) | FR-006, FR-036, FR-047 |
| `fill` | `wallDef`, `doorDef`, `doorStuffDef`, `plots` (list of Group) | derived in FR-047's order; where the design and the recorded direction are silent, what the reading's blocks are built with (R-8); `wallDef` a wall, `doorStuffDef` a material `doorDef` takes | FR-006, FR-014, FR-018, FR-036, FR-047 |
| `blockLibrary` | list of SpecCard | optional; the Empire has none | FR-006; glossary line 167 |

**Group**: `name`; `size`; `terrain`, a layer; `things`, each in the thing form below, placed from the group's own
corner, as `PrefabDef` places them (R-8). Every cell lies inside its `size`.

**SpecCard**: `name`; `size`, its plot; `terrain`, a layer; `rooms`, each a `name` and `rects`; `things`, each in the
thing form below. Every cell of its terrain, rooms and things lies inside its plot (FR-007).

## LaidOutCity (a file, root `LaidOutCity`)

| Field | Form | Rule | Source |
|-------|------|------|--------|
| `template`, `kit` | defNames | both exist, and the kit is the template's; a reading holds `reference` instead | FR-008, FR-017 |
| `reference` | a template's `reference` name | in a reading only: the reference city it reads | FR-036; R-7 |
| `size` | `(x, z)` | square | FR-003, FR-008 |
| `terrain`, `roofs` | layers | every cell has a terrain; nothing outside the map | FR-008, FR-016 |
| `things` | list of Thing | below | FR-008, FR-018 |
| `parts`, `features` | lists, each a `name` and `rects`, a river feature also `flowsFrom`; in a reading each may also hold `from` | every part of both skeletons that is not optional, and every feature a relation names, has cells; a reading holds the parts and features it reads | FR-008, FR-029; R-7 |
| `scale` | `pixelsPerCell` and `referenceCell`, positive numbers: the pixels one cell is and the RimWorld cells one cell of the reference game is; `origin`, optional, the pixel `(x,y)` of the picture where cell (0, 0)'s lower left corner lies, the picture's own lower left corner where it is left out; and `measured`, a list of at least one thing it was got from, each a `name` and a pixel `rect` | in a reading from a picture only, which only a `scale` shows: one cell is sized first, by the figure where the sizes differ | FR-048; R-17 |
| `from` (of a part or feature) | pixel `rect`s in the reference picture | in a reading from a picture only: the region of the picture the piece was read from | FR-049; R-17 |
| `use`, `basis` (of a part) | `use` is one of `Housing`, `ShopFront`, `Workshop`, `Tavern`, `Market`, `Public`, `AnnexOrAttic` or `Unclear`; `basis` is one sentence | in a reading from a picture only: a building or group holds both; a `use` outside the list, or a `use` without its `basis`, is reported; the form records no kind of piece, so whether each building or group holds one is judged by eye (spec FR-029, FR-049, SC-013) | FR-049, SC-013; R-17 |

**Thing**: an element named by its `ThingDef`, holding `position`, `rotation`, `stuff` where the definition takes one,
and `rect` where the definition's `size` is larger than one cell.

A laid-out city is held, for FR-015, by the mod that holds its `template`; a reading by the mod that holds the template
whose `reference` names it, or by no mod, requiring no expansion, while no template names it (FR-015).

**A reading's acceptance**: a reading counts once the check reports no problem in it and the maintainer has accepted
it beside its reference pictures (FR-036), recorded as an item of `checklists/acceptance.md` that names the reading,
the commit and where the picture is in the project's files, checked when he accepts it (FR-029).

## Top-down view (in the project's files, not the repository)

The drawing of a preset reference read from its game's own data (spec FR-041 to FR-044; research R-15). The check
does not read it as data: its two pictures are given to the check as reference pictures (`--reference`).

| Output | Holds | Source |
|--------|-------|--------|
| skeleton picture, PNG | each object at its `(x, z)` on the cells, over the island's heightmap, turned to match the game's `mapimage.png`; linear pieces as lines, houses as markers, fields as squares | FR-043 |
| overlay, PNG | the same laid over the game's `mapimage.png` | FR-043 |
| `objects.json` | every object read, each with its asset Template, the graphics folder its ConfigFilename names, and its position | FR-042, FR-043 |
| summary | what was read and drawn | FR-043 |

It is drawn in steps, each seen by the maintainer before the next: dots by category, then the skeleton, then,
optionally, real footprints from the game's `.ifo` files (FR-044). All of it, and the packages it is read from, stay
out of the repository (FR-041).

## Report and pictures

A **problem** has a number, the file, the template, kit, city or spec card, the part or field, the cell where it has
one, and what is wrong. A **relation result** is `holds`, `broken` (with the cells of its parts) or `not measured`
(an optional part left out). The report ends by saying that testing in the game is the final check and is still to
come (FR-020). The picture files are listed in [contracts/check-command.md](contracts/check-command.md).

## What the check reports

| Problem | When | Source |
|---------|------|--------|
| unknown definition | a name found neither in `Data/` nor in the `Defs/` of the mods given | FR-013 |
| wrong kind | a name where its kind cannot go: not a terrain in `terrain`, not natural in a terrain shape, not a wall in a `wallDef`, not a `BiomeDef` in `allowedBiomes`, not a `RiverDef` in `allowedRivers`, not a `RulePackDef` in `nameMaker`, an unknown part or relation kind, a relation missing the field its kind needs | FR-014; R-4, R-5 |
| wrong form | a value not in its field's form: an attitude field that is not `true` or `false`; a rect, position, size or `minMapSize` not in its form; a rotation or `flowsFrom` that is not `North`, `East`, `South` or `West` | FR-014; R-3 |
| wrong scale, region or use | in a reading: a `pixelsPerCell` or `referenceCell` that is not a positive number, or an `origin` not in the form `(x,y)` of whole pixels (reported as wrong form); a `scale` with no `measured` thing, or a `measured` thing without its `name` or pixel `rect`; a pixel `rect` of a `measured` thing or a `from` that lies outside the reference picture where the picture is given; a `use` outside the list; a `use` without its `basis` | FR-019, FR-048, FR-049 |
| not square | a `minMapSize` or a city's `size` whose `x` and `z` differ | FR-003, FR-014 |
| missing field | a required field left out: a template's `kit` or `minMapSize`; a laid-out city's `template`, `kit` or `size`; a reading's `reference` or `size` | FR-001, FR-003, FR-008, FR-014 |
| other expansion | a definition of an expansion that the mod holding the file, as FR-015 sets for laid-out cities and readings, does not require, without that expansion's `MayRequire` | FR-015 |
| outside the map | a cell past `minMapSize`, past 350×350 or past a city's `size`; a cell of a group or spec card past its `size`; a thing whose cells reach past the map | FR-007, FR-016, FR-018 |
| no terrain | a cell inside the map with no terrain, in a laid-out city and in a template whose `terrain` holds any cell; a template whose `terrain` holds none leaves the land to generation and has none to report | FR-016, FR-036; R-18 |
| unknown name | a relation naming a part or feature neither skeleton nor the terrain shape holds; a duplicate name | FR-017 |
| no kit | a template whose `kit` does not exist; a laid-out city whose `kit` is not its template's | FR-017 |
| affordance | a thing on a cell whose terrain lacks the affordance it needs, or its material's when its definition uses the material's | FR-018 |
| size | a thing's `rect` that does not match its definition's `size` | FR-018; R-7 |
| material | a material the definition does not take, or none where it takes one | FR-018 |
| missing part | a part that is not optional and has no cells in a laid-out city | FR-029 |
| broken relation | a relation that does not hold in a laid-out city | FR-029 |
| no comparison | a template or laid-out city with a reference picture label given no picture, or one that cannot be read; it does not stop the run | spec, Edge Cases |

The check does not report a reading that lacks a `scale`, a `from` or a `use`: it cannot tell a reading from a picture
except by its `scale`, and whether each traced piece holds them is judged by the maintainer's eye (spec SC-013;
FR-029).

The check stops, and reports nothing as passing, when `Data/` is missing or not of version 1.7 (spec, Edge Cases).

## States of a template

1. **Written**: in its mod's `Defs/TemplateDefs/`, derived in FR-047's order, its culture's reading filling what the
   design and the recorded direction leave open, each part naming its source (FR-036, FR-047).
2. **Checked**: the check reports no problem in it or its kit.
3. **Laid out**: a city generation laid out from it is checked, every relation holds (R2).
4. **Accepted**: the maintainer has accepted the side-by-side picture, recorded as a checked item of a reviewer-owned
   checklist naming the template, the commit and where the picture is in the project's files (FR-029, FR-030). Only
   now does it count.
5. **Confirmed in the game**: the final check, once R2 places it, or R15 for the Empire's (spec, Assumptions).
