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
outside the game against `Data/`, which sets a laid-out city beside its reference; the Empire's kit and the river-bend
town's template, written from its screenshot and render, which calibrate the method first and come with Imperium (R15);
and the tribal culture's kit and its first templates, one for each attitude of its factions, which the alpha opens.
Deferred: the industrial (outlander) and pirate cultures' kits and templates, which the alpha opens too (R16); the
other cultures' kits and templates; generation, which picks templates, may mirror, turn and stretch them, and lays out
cities from them (R2); the check in the game, which is the final one, once R2 places the tribal culture's settlements
and R15 the Empire's.
Depends on R1 and R14, Mantle as a mod of its own. As requested for this feature, the
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
This feature holds two cultures' kits and first templates [Roadmap: R13]: the tribal culture's, which the alpha of
Mantle, a mod of its own, opens [Roadmap: R14, Releases; Direction], and the Empire's, with the river-bend town's
template, which calibrate the method first and come with Imperium [Roadmap: R15]. The alpha also opens the base
game's other cultures with settlements, the industrial (outlander) culture for the civil and rough outlanders and the
pirate culture, whose kits and templates are R16's, in this feature's forms and checked by its check [Roadmap: R16,
Releases; Direction]. The other cultures' kits and templates are later work [Direction].

A settlement is built from three layers [Direction]. The first is Mantle's and the same for every culture: the forms,
the check, generation and the pieces each faction skins (FR-033). The second is the culture's: one kit, which all of
its factions share. The third is the faction's: which of its culture's templates its settlements are laid out from,
picked on two dimensions, of which each culture uses only those it needs (FR-038 to FR-040):

- **Attitude**, by the two fields with which a faction's definition says how it stands toward others, `naturalEnemy` and
  `permanentEnemy` [Data: `Core/Defs/FactionDefs/Factions_Misc.xml` lines 202, 462, 485 and 529], read from the
  definition rather than bound to a faction's name. The tribal culture picks by it, as its factions' descriptions set:
  the gentle tribe, with neither field, is open to trade and alliances and gets an open village; the fierce tribe, a
  natural enemy, values warlike dominance and gets a walled stronghold; the savage tribe, a permanent enemy, is driven
  by a blood-and-honor culture that cannot be allied with and gets a fortress [Data: same file, lines 445, 480 and 504,
  confirmed by the maintainer]. Since every faction's definition can hold the two fields, as `Data/` sets them on
  factions of every kind [Data: `Core/Defs/FactionDefs/Factions_Hidden.xml` lines 77 and 122;
  `Ideology/Defs/FactionDefs/Factions_Misc.xml` lines 74 and 98; `Anomaly/Defs/FactionDefs/Factions_Misc.xml` line 8;
  `Odyssey/Defs/FactionDefs/Factions_Misc.xml` line 198], a faction another mod adds picks the same way; that the
  medieval factions of other mods set them as the base game's factions do is an inference, not yet checked.
- **Terrain**, by the biomes a template suits (FR-001). The Empire picks by it alone, since its definition holds
  neither attitude field, only the factions it is not a permanent enemy of [Data:
  `Royalty/Defs/FactionDefs/Faction_Empire.xml` lines 57-67], by the design's two looks of imperial cities, temperate
  for temperate and cold regions and arid for hot, dry ones [Design: lines 208 and 162]: in the temperate and cold
  biomes the river-bend town [Direction; Data: `Core/Defs/BiomeDefs/Biomes_Temperate.xml` lines 5 and 210;
  `Core/Defs/BiomeDefs/Biomes_Cold.xml` lines 5, 198, 371, 586 and 710], and in the desert and arid biomes a Romanized
  Egyptian city, which is later work [Direction; Data: `Core/Defs/BiomeDefs/Biomes_WarmArid.xml` lines 5, 172 and 322;
  Roadmap: R15].

Mantle is a framework that other authors build on too [Design: line 221], so adding a culture asks only for its
skeletons and its kit [Direction]. Everything else is shared and the same for every culture: the forms of templates
and kits, the check outside the game and its pictures, generation's picking, mirroring, turning, stretching and
filling [Roadmap: R2], and the pieces, generic building elements that every kit shares and each faction skins
[Design: line 194]. An author starts a culture by copying an existing culture's skeletons and kit, and the river-bend
town is the complete worked example, from reference to skeleton to generated city (FR-033 to FR-035) [Direction].

What is fixed and what is left to generation [Design: lines 184, 209; Direction]:

- **Fixed**, defined by people and abstracted from the reference city: the template, meaning its terrain shape with
  its river, and its skeleton with the wall line, the districts and their relations, the main street, the plazas and
  the places of the public buildings; and the kits.
- **Left to generation**, and only within those bounds: picking a template, mirroring, turning and stretching it to
  fit the site, and filling its blocks with the kit's buildings.

Generation never designs a city: it fills a fixed skeleton.

A culture's kit and templates are derived in a fixed order (FR-047) [Direction; constitution, Source Register, row
Imperium's own design]. First comes Imperium-old's design, and everything it defines for them is reused [Design]. Where
it is silent, the maintainer's broad direction comes next, as this repository's merged specs and roadmap record it
[Direction; Roadmap]. Only where both are silent is the gap filled from the reference city's reading, and what is
taken from it is marked [Direction], for the maintainer to judge its broad direction. A reading never overrides the
design or his recorded direction.

Templates are drawn from reference cities in four steps [Direction]:

1. A reference city is chosen: a player-built city of Anno 117 that is publicly shared, whether Ubisoft features it
   through its channels, such as the Anno Union, or a player shares it, such as on Steam, or a city Anno 117 itself
   presets for a governor or an AI rival. A preset city's layout may also be read from Anno 117's own data and drawn
   from above, and those drawings are then among its pictures (FR-041 to FR-045).
2. It is read onto the game's cells, and the reading is set beside its pictures until it matches them, as the
   river-bend town's render was. Its layout relationships are then taken apart from the reading as a template, and what
   fills them as its culture's kit, in this feature's form, wherever the design and the maintainer's recorded direction
   leave them open (FR-047). Since the reading lies on the game's flat cells and is
   built from the culture's own kit, it carries only the reference's skeleton, the general way the city is laid out,
   and the template taken from it ships as it is once it passes (FR-010, FR-036).
3. Generation lays out a city from the template and a kit [Roadmap: R2].
4. The check measures whether each relation of the template's skeleton holds in the laid-out city and draws the city
   beside pictures of the reference city; once every relation holds, the maintainer judges them side by side (FR-025,
   FR-029).

The first case is the river-bend town, a player-built city of which the project holds a screenshot, the source, and a
render on the game's cells, an earlier reading of that single 2D screenshot whose heights, hidden areas and exact sizes
were guessed [Direction]. It calibrates the method first, before the tribal culture's kit and templates are written
(FR-031) [Roadmap: R13]. Its template and the Empire's kit are taken from these pictures. Generation lays out the town
from them [Roadmap: R2, R15]. Every relation of its skeleton must hold in the laid-out town, and the maintainer then
judges the town beside the screenshot and the render. No cell-exact match to the render is asked for, since it is a
guess too. If the method cannot express the town, the method is fixed first. Once the calibration passes, the town's
template ships with Imperium as a regular template, as it stands [Roadmap: R15].

The tribal culture's first templates, one for each attitude, and its kit are taken the same way from cities of
Anno 117's Albion built only in the Celtic way, neither Romanized nor mixed, at the scale of a tribal settlement and
shown from above, either player-built and publicly shared or preset by the game for a governor or an AI rival. The
maintainer chose among the candidates three cities that a player shared on Steam: Tir Uisce for the gentle tribe's
open village, a Celtic oppidum for the fierce tribe's walled stronghold and a small Celtic hillfort for the savage
tribe's fortress, with an agricultural island looked at beside them as supplementary material only, from which
nothing is taken (FR-037) [Direction].

A city that Anno 117 presets, on an AI rival's or a third party's island, can be read from the game's own data
[Direction]. Only the game's own files are read: its file index, `file_h.db`, and its `.rda` packages, which hold each
preset island as an `.a7m` file; never the index, cfg or cut files the old project left. The packages stay on the
maintainer's computer, and what is read from them goes into `template-references/` in the project's files, never into
the repository. Each object takes its category from the game data itself, in two layers: its asset Template, and the
graphics folder its ConfigFilename names. The island is then drawn from above: each object at its `(x, z)` position on
the cells, over the island's heightmap, turned to match the game's own top-down image of the island, `mapimage.png`,
with linear pieces drawn as lines, houses as markers and fields as squares. Each island gives a skeleton picture, the
same laid over the game's image, a list of every object, `objects.json`, and a summary. The drawing is built in steps,
and the maintainer sees each step's picture before the next: first the objects as dots by category, then the skeleton,
then, if wanted, each building's real footprint from the game's `.ifo` files. The old project's output and images, and
FileDBReader, only cross-check what is read (constitution, Principle II). The pictures drawn this way are the
reference's pictures, and its reading on RimWorld's cells is set beside them as beside any other (FR-036).

The cultures that come later take their references as follows [Direction]: the industrial (outlander) culture's from
Anno 1800, Bright Sands for the civil outlanders and Wormways for the rough, and the pirate culture's from Anno 1800's
two pirate islands, Anne Harlow's and Jean La Fortune's [Roadmap: R16]; Odyssey's Traders Guild's from Odyssey's own
form of an orbital settlement, rooms laid off a spine of corridors on one enclosed platform [Data:
`Odyssey/Defs/LayoutDefs/Layouts_OrbitalPlatform.xml` lines 5, 7, 23 and 158-194;
`Odyssey/Defs/MapGeneration/SpaceMapGenerator.xml` lines 82-87], and the Salvagers' the same way only if they really get
settlements: their definition does not settle it, since the faction is hidden [Data:
`Odyssey/Defs/FactionDefs/Factions_Misc.xml` line 172], so it is checked in the game when their kit comes.

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
- Q: What do a kit's groups and fill hold? → A: What its culture's reference city shows. The reference is read onto the
  game's cells and the reading is set beside its pictures until it matches them, as the river-bend town's render was;
  the template's skeleton and the kit's contents, its groups and fill among them, are then taken apart from that
  reading (the maintainer's broad direction, constitution, Principle IV; Imperium-old glossary line 184 names groups and
  fill without saying what they hold, and `Data/` has no kit).
- Q: Where do the tribal culture's first templates come from? → A: From cities of Anno 117's Albion built only in the
  Celtic way, neither Romanized nor mixed, at the scale of a tribal settlement, and shown from above so that their
  layout can be read: player-built cities shared publicly from any source, or cities the game itself presets for a
  governor or an AI rival. The maintainer chose one for each attitude among the candidates, all shared by one player
  as Steam screenshots: Tir Uisce (3639186959) for the gentle tribe, a Celtic oppidum (3625652909) for the fierce
  tribe and a small Celtic hillfort (3621994739) for the savage tribe, with an agricultural island (3639163413) beside
  them as supplementary material only (the maintainer's broad direction).
- Q: Is a calibrated template's content changed before it ships? → A: No. Its reading lies on RimWorld's flat cells
  and is built from Imperium's own kit, so all it reproduces of the reference is the skeleton, the general way the
  city is laid out, and none of Anno's own expression; once its skeleton relations pass the check and the maintainer
  accepts it by eye, the template ships as it is (the maintainer's broad direction).
- Q: How does a faction's settlement pick among its culture's templates? → A: On two dimensions, of which each culture
  uses only those it needs: attitude, by the `naturalEnemy` and `permanentEnemy` fields of the faction's definition,
  never by its name, and terrain, by the biomes a template suits. The tribal culture picks by attitude, as its factions'
  descriptions set: an open village for the gentle tribe, a walled stronghold for the fierce tribe and a fortress for
  the savage tribe (`Data/`, `Factions_Misc.xml` lines 445, 480 and 504, confirmed by the maintainer). The Empire, which
  holds neither field (`Faction_Empire.xml` lines 57-67), picks by terrain: the river-bend town in temperate biomes, and
  a Romanized Egyptian city in desert and arid ones later (the maintainer's broad direction). These are the design's two
  looks of imperial cities, temperate for temperate and cold regions and arid for hot, dry ones (Imperium-old
  `docs/glossary.md` lines 208 and 162), so the river-bend town suits the cold biomes too, Odyssey's glacial plain among
  them (FR-040).
- Q: Can a reference city's layout be read from its game's own data, and how? → A: Yes, for a city Anno 117 presets on
  an AI rival's or a third party's island. Only the game's own `file_h.db` and `.rda` packages are read, which hold the
  island as an `.a7m` file, never the old project's index, cfg or cut files. The packages stay on the maintainer's
  computer, and what is read goes into `template-references/` in the project's files, never into the repository. Each
  object takes its category from the game data in two layers, its asset Template and the graphics folder its
  ConfigFilename names. The island is drawn from above, each object at its `(x, z)` on the cells over the heightmap,
  turned to match the game's own `mapimage.png`, with lines for linear pieces, markers for houses and squares for
  fields, and gives a skeleton picture, the same laid over the game's image, `objects.json` and a summary. It is built
  in steps, each picture seen by the maintainer before the next: dots by category, then the skeleton, then, optionally,
  real footprints from `.ifo` files. The old project's output and images, and FileDBReader, only cross-check (the
  maintainer's broad direction, constitution, Principle IV; Imperium-old's design says nothing on reading a game's data,
  checked at 20a052b; constitution, Principle II).
- Q: In what order are a culture's kit and templates derived? → A: First Imperium-old's default-branch design
  meaning, reusing everything it defines; then, where it is silent, the maintainer's broad direction as the merged
  specs and roadmap record it; and only where both are silent, the reference city's reading, marked [Direction] for
  his judgment of its broad direction. A reading never overrides the design or his recorded direction (the
  maintainer's broad direction; constitution, Source Register, row Imperium's own design).
- Q: Does this feature hold the kits and templates of every culture the alpha opens? → A: No. The alpha opens every
  culture of the base game whose factions have settlements, but this feature holds the tribal culture's; the industrial
  (outlander) and pirate cultures' kits and templates are R16's, written in this feature's forms and checked by its
  check (`ROADMAP.md`, R13, R16 and Releases).
- Q: Where do the later cultures take their references from? → A: The industrial (outlander) culture from Anno 1800,
  Bright Sands for the civil outlanders and Wormways for the rough; the pirate culture from Anno 1800's pirate islands,
  Anne Harlow's and Jean La Fortune's; Odyssey's Traders Guild from Odyssey's own form of an orbital settlement, rooms
  off a spine of corridors; and the Salvagers the same way only if they really get settlements (the maintainer's broad
  direction).
- Q: How is a reference city that exists only as a picture read onto the game's cells? → A: As the design traces a
  reference: the cell is sized first, by things the size of a person; the picture is traced into cells only as far as
  blocks, house groups, yards and roads; the tracing is set over the picture at the same scale and each traced piece is
  compared with the picture, the check marking each piece that does not match for the maintainer and never deciding
  anything itself; and each area is shown to the maintainer once after it is traced and once after it is laid out. The
  effect of the old project's preview tool is kept; its code, settings and numbers are not taken. A picture these steps
  cannot read, such as one not shown from above, is not read by a method of its own, and which picture to use instead is
  the maintainer's broad direction (the maintainer's broad direction, 2026-11-24; design archive `cities.md`, The size
  of a cell, and `cities-forms.md` lines 123, 199 and 475; constitution, Principles IV and V). A first reading of the
  open village, made with a camera guessed from a screenshot, was removed because no source supports that method.

## Sources

Each requirement below names its source in brackets. The sources are those the constitution's Source Register gives:

- **[Roadmap]**: `ROADMAP.md`, entries R13 (intent and scope boundary), R2, R14, R15 and R16, and its section Releases.
- **[R14]**: Mantle as a mod of its own, `specs/003-mantle-mod/`: `contracts/repository-layout.md`, which places each
  mod's files in its folder, `Mantle/` or `Imperium/`, and the files that serve both at the repository root, and
  `contracts/about-xml.md`, which gives Mantle's package identifier.
- **[Design]**: Imperium's own design, Imperium-old `main` (20a052b), `docs/glossary.md`, section City building and
  generation: block library (line 167), city building (line 173), kit (line 184), piece (line 194), skeleton (line 204),
  spec card (line 206), template (line 209), Mantle (line 221), and the looks of imperial cities, arid (line 162) and
  temperate (line 208); `docs/imperium.md`, section Expansions (lines 108-110); and `docs/setting.md`, section Rome
  (lines 57 and 60-61).
- **[Design archive]**: `docs/design-archive/` in this repository, its record of Imperium-old's design meaning as of
  Imperium-old b218bdc (`specs/005-imperium-design-archive/`): `cities.md`, sections The size of a cell and the Anno
  sample, which the settlement grafted onto RimWorld's logic is kept as "for side-by-side comparison"; and
  `cities-forms.md`, lines 123 (a template candidate comes only from tracing an accepted reference), 199 (each area shown
  once after tracing and once after layout) and 475 (traced only as far as blocks, house groups, yards and roads).
- **[Testing]**: the constitution's Source Register, row Testing outside the game: the base game and official
  expansions in `Data/`; testing outside the game comes before testing in the game and does not replace it, and
  testing in the game is the final check.
- **[Data]**: the base game and official expansions in `Data/` of RimWorld 1.7.5014: terrain (`Core/Defs/TerrainDefs/`),
  and the affordances a terrain gives (`Terrain_Natural.xml` lines 5-7, 51-55 and 126-131); natural rock
  (`Core/Defs/ThingDefs_Buildings/Buildings_Natural.xml` line 47); roofs (`Core/Defs/Misc/RoofDefs/Roofs.xml` lines 5,
  14 and 24); the affordance a thing needs (`Core/Defs/ThingDefs_Buildings/Buildings_Base.xml` line 11), or its material
  needs when the thing says so (`Buildings_Structure.xml` lines 277-278; `Core/Defs/ThingDefs_Misc/Various_Stone.xml`
  line 88); the materials a thing takes (`Buildings_Structure.xml` lines 286-290); a faction base's generation
  (`Core/Defs/MapGeneration/BaseFactionMapGenerator.xml` lines 14-21); the smallest map a site needs
  (`Ideology/Defs/Sites/AncientComplex.xml` line 15); square maps (`Core/Languages/English/Keyed/Dialogs_Various.xml`
  line 153); a site's map taking its own size (`Core/Defs/WorldObjectDefs/WorldObjects.xml` line 205); a thing placed by
  its position as `(x, 0, z)`, its rotation and its material (`Odyssey/Defs/PrefabDefs/AncientPrefabs.xml` lines 12, 13
  and 23); the factions that have settlements (`Royalty/Defs/FactionDefs/Faction_Empire.xml` lines 5 and 11;
  `Core/Defs/FactionDefs/Factions_Misc.xml` lines 9, 185, 224, 443, 511 and 517;
  `Odyssey/Defs/FactionDefs/Factions_Misc.xml` lines 5, 17, 40-42, 168, 188 and 202-204), the Salvagers being hidden
  (the same Odyssey file, line 172); Odyssey's form of an orbital settlement, one enclosed platform of rooms laid off
  corridors (`Odyssey/Defs/LayoutDefs/Layouts_OrbitalPlatform.xml` lines 5, 7, 23 and 158-194;
  `Odyssey/Defs/MapGeneration/SpaceMapGenerator.xml` lines 82-87), on a map of its own size
  (`Odyssey/Defs/WorldObjectDefs/WorldObjects.xml` lines 44 and 50-51); a faction's attitude
  (`Core/Defs/FactionDefs/Factions_Misc.xml` lines 202, 462, 485 and 529), set on factions of every kind
  (`Core/Defs/FactionDefs/Factions_Hidden.xml` lines 77 and 122; `Ideology/Defs/FactionDefs/Factions_Misc.xml` lines 74
  and 98; `Anomaly/Defs/FactionDefs/Factions_Misc.xml` line 8; `Odyssey/Defs/FactionDefs/Factions_Misc.xml` line 198),
  and the descriptions of the gentle, fierce and savage tribes (`Core/Defs/FactionDefs/Factions_Misc.xml` lines 445, 480
  and 504); the factions the Empire is not a permanent enemy of (`Royalty/Defs/FactionDefs/Faction_Empire.xml` lines
  57-67); the temperate biomes (`Core/Defs/BiomeDefs/Biomes_Temperate.xml` lines 5 and 210), the cold ones
  (`Biomes_Cold.xml` lines 5, 198, 371, 586 and 710), the desert and arid ones (`Biomes_WarmArid.xml` lines 5, 172 and
  322), the tropical ones (`Biomes_Warm.xml` lines 5 and 203), the water ones (`Biomes_Water.xml` lines 7 and 22) and
  the underground (`Biomes_Misc.xml` line 7); the expansions' biomes (`Odyssey/Defs/BiomeDefs/GlacialPlain.xml`,
  `Glowforest.xml`, `Grasslands.xml`, `LavaField.xml` and `Scarlands.xml`, each line 7, and `Space.xml` lines 7 and 45;
  `Anomaly/Defs/MapGeneration/LabyrinthMapGenerator.xml` line 32, `MetalHellMapGenerator.xml` line 31 and
  `UndercaveMapGenerator.xml` line 105, whose parent is the underground) and the form that marks one in a list
  (`Core/Defs/Misc/FeatureDefs/Features.xml` line 268); and each expansion's `About/About.xml`.
- **[EULA]**: `EULA.txt`, which is always followed (constitution, Source Register).
- **[Direction]**: the maintainer's broad direction on where template layouts come from and how they are accepted,
  which Imperium-old's design leaves open (constitution, Source Register, row Imperium's own design; Principle IV):
  - Templates are drawn, as reference only, from player-built cities of Anno 117 that are publicly shared, whether
    Ubisoft features them through its channels or players share them, or from cities Anno 117 itself presets for
    governors and AI rivals. The layout relationships read from such a city, its river, walls, districts, streets,
    plazas and public buildings, are expressed as templates in the design's form, and kits fill them. Nothing of
    Anno's art, names, models or code is used. A reading lies on RimWorld's flat cells, without heights, and is built
    from Imperium's own kits, so it reproduces only the reference's skeleton, the general way the city is laid out,
    and none of Anno's own expression; the template taken from it ships as it is once it passes.
  - A preset reference may be read from the game's own data, which Imperium-old's design does not address (checked at
    20a052b). Sources and inputs: only Anno 117's own `file_h.db` and `.rda` packages, and in them the preset AI and
    third-party islands, `.a7m` files; never the old project's index, cfg or cut files. The raw packages stay on the
    maintainer's computer, and what is read from them goes into `template-references/` in the project's files, never
    into the public repository.
  - Object categories come from the game data itself, in two layers: the asset Template, and the graphics folder its
    ConfigFilename names.
  - The top-down skeleton view places each object at its `(x, z)` position on the cells, over a heightmap base, turned
    to match the game's own `mapimage.png`, and draws linear pieces as lines, houses as markers and fields as squares.
    Its output for each island is a skeleton PNG, an overlay on the game's image, `objects.json` and a summary.
  - The view is built in steps, with a picture seen at each step before the next: the objects as dots by category,
    then the skeleton, then, optionally, real footprints from `.ifo` files.
  - Old-project output and old images, and FileDBReader, only cross-check what is read (constitution, Principle II).
  - Imperium's city maps are 350×350 cells.
  - Each culture has its own skeletons and templates; slots vary only within a culture. The old design's Roman kit is
    the Empire kit, also in Imperium's files.
  - Every faction that has settlements gets its own, on the surface and in orbit: the Empire, tribal, industrial
    (outlander), pirate, medieval (for medieval mods), and Odyssey's Traders Guild and Salvagers. This feature holds
    the tribal culture's kit and its first templates, one for each attitude, which the alpha opens, and the Empire's
    kit with the river-bend town's template. The alpha covers every culture of the base game with settlements, so the
    industrial (outlander) and pirate cultures' kits and templates come for it too, in R16 [Roadmap: R16, Releases];
    the rest is later work.
  - Further references by culture: Anno 1800 for the outlanders, Bright Sands for the civil and Wormways for the
    rough, and for the pirates, Harlow's and La Fortune's islands; Odyssey's own orbital platform form, a spine of
    corridors with rooms, for the Traders Guild, and for the Salvagers if they really get settlements.
  - A culture's kit and templates are derived in this order: Imperium-old's design meaning first, reusing everything
    it defines; then, where it is silent, the maintainer's direction as the merged specs and roadmap record it; and
    only where both are silent, the reference city's reading, marked [Direction] for his broad-direction judgment. A
    reading never overrides the design or his recorded direction.
  - Within that order, a culture's kit and templates are taken from its reference city: the reference is read onto
    the game's cells and the reading set beside its pictures until it matches, as the river-bend town's render was,
    and then its skeleton and its kit, groups and fill among them, are taken apart from that reading.
  - The tribal culture's references are cities of Anno 117's Albion, built only in the Celtic way, neither Romanized
    nor mixed, at the scale of a tribal settlement, and shown from above so that their layout can be read:
    player-built cities shared publicly from any source, or cities the game presets for a governor or an AI rival.
    Candidates go to the maintainer, who chose one for each attitude: Tir Uisce for the gentle tribe, a Celtic oppidum
    for the fierce tribe and a small Celtic hillfort for the savage tribe, each a player's Steam screenshot, with an
    agricultural island as supplementary material only.
  - A settlement is built from three layers: Mantle's, shared by every culture; the culture's kit, shared by all its
    factions; and the faction's templates, picked by attitude and terrain, of which each culture uses only what it
    needs. The tribal culture picks by attitude, as its factions' descriptions in `Data/` set, which the maintainer
    confirmed; the Empire picks by terrain, the river-bend town in temperate biomes and a Romanized Egyptian city in
    desert and arid ones, later.
  - Lowering the barrier for other authors is necessary: a new culture needs only its skeletons and kit, everything
    else is shared and identical across cultures, an author can copy an existing culture as a starting point, and the
    river-bend town is the complete worked example.
  - The template's skeleton holds the wall line, districts, main street, plazas and public buildings read from the
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
    method that cannot express the town is fixed first. Once the calibration passes, the town's template ships as a
    regular template, as it stands, with no credit line.
- **[Spec Kit]**: the feature description given to `/speckit-specify` (Input, above), the development workflow's
  source for what a feature is for; and Spec Kit v1.4.3's own forms where the Input gives none: a report's findings
  each with its location (`templates/commands/analyze.md` line 181), a rerun without changes giving the same results
  (line 263), and a reviewer's judgment recorded as a checked item of a reviewer-owned checklist
  (`templates/commands/checklist.md` lines 32-36).

Imperium-old's earlier layout tool and the reverted spec of the earlier R13 are not sources: their code, settings and
numbers are not taken. What the design says of reading a picture is taken from the design archive (FR-048 to FR-050),
and the effect of the old preview tool is kept as the maintainer directed (FR-051) [Direction]. The old project's output
and old images, and FileDBReader, only cross-check what a reading of a game's data gives (constitution, Principle II)
[Direction].

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
   the check runs, **Then** it reports it, since neither Mantle's own mod nor Imperium requires Biotech [Design:
   imperium.md lines 108-110; Roadmap: R14].
4. **Given** the tribal culture's kit naming a definition only Royalty holds, without marking it as Royalty's content,
   **When** the check runs, **Then** it reports it, since Mantle's own mod requires no expansion; the same definition
   in the Empire's kit is accepted, since Imperium requires Royalty [Roadmap: R14, Releases].
5. **Given** a template that places a building on a cell, **When** the check runs, **Then** it reports it, since a
   template holds no building (FR-002).
6. **Given** a template and a kit with no problem, **When** the check runs, **Then** it reports none, and says that
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

### User Story 4 - Check a kit's buildings (Priority: P4)

Where a kit has a block library, the ready-made blocks built from spec cards, the developer checks each spec card,
the design card that fixes one building's plot, rooms and contents.

**Why this priority**: A block library belongs to a kit, though the Empire's cities do not use one [Design: lines 167,
206], so it comes after the checks every kit needs.

**Independent Test**: Write a test kit with a block library of three spec cards, one naming a definition `Data/` does
not hold, one with a room or thing past its plot and one with neither; check it and compare the report with the cards.

**Acceptance Scenarios**:

1. **Given** a spec card whose contents name a definition `Data/` does not hold, **When** the check runs, **Then** it
   reports that name and the cell where it is.
2. **Given** a spec card with a room or thing past its plot, **When** the check runs, **Then** it reports the cell
   (FR-007).

---

### User Story 5 - Add a culture by copying one (Priority: P5)

Another author adds a culture to Mantle. The author copies an existing culture's skeletons and kit, such as the
tribal culture's, or the Empire's with the river-bend town's template, changes them for the new culture, and runs the
same check, which reports problems and draws the pictures as it does for the original. The author changes nothing that
is shared.

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

- A template, kit or laid-out city names a definition of Mantle's or Imperium's own, such as a piece, a generic
  building element the base game lacks [Design: line 194]: the check looks for it among the definitions of the mods it
  is given, and reports it when it is not there.
- A terrain shape reaches past the map size the template states or past a city's 350×350 map, a laid-out city reaches
  past its map, or either leaves a cell with no terrain: the check reports each such cell.
- A skeleton relation names a part the skeleton does not hold, or a terrain the terrain shape does not hold: the check
  reports the relation.
- A definition from an expansion that the mod holding the template, kit or laid-out city does not require, marked as
  that expansion's content: the check accepts it, and the picture's legend names the expansion [Design: imperium.md
  line 110; Roadmap: R14].
- The pictures of the tribal culture's references are not yet in `template-references/`: its readings, kit and
  templates wait for them; the forms, the check, the Empire's kit and the river-bend town's template do not
  [Direction].
- A faction holds an attitude that no template of its culture serves, or settles in a biome that none suits, such as the
  Empire in a tropical rainforest, which is hot and wet and so neither of the design's looks (FR-040), before its other
  templates come: this feature gives it no template, and what generation does then is R2's [Roadmap: R2, R15].
- A faction another mod adds, such as a medieval mod's, holds the two attitude fields as every faction's definition
  can, and picks its culture's templates by them; that those mods set the fields as the base game's factions do is an
  inference, to be checked when the medieval culture's kit comes [Direction].
- A preset reference's island is in a package not yet on the maintainer's computer: its top-down view waits for that
  package, and the old project's index, cfg or cut files are not used in its place (FR-041).
- The packages holding the `.ifo` files of a preset island's buildings are not on the maintainer's computer: its view
  draws houses as markers, and real footprints, the optional third step, wait for those packages (FR-044).
- Odyssey's orbital settlements take a map of their own size, 200×200 cells, not a city's 350×350 [Data:
  `Odyssey/Defs/WorldObjectDefs/WorldObjects.xml` lines 44 and 50]: how their templates fit it is settled when their
  kit comes, as later work [Direction].
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
  tile and size it suits [Design: line 209] and the attitude of the factions it serves (FR-039), its culture, and the
  reference city it is drawn from [Direction].
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
  [Design: line 167]. What its groups, fill and wall settings hold MUST be taken in the order of FR-047, and so from
  its culture's reference city, as its skeleton is (FR-036), wherever the design and the maintainer's recorded
  direction leave them open [Direction].
- **FR-007**: A spec card MUST fix one building: its plot, its rooms and their contents [Design: line 206].
- **FR-008**: A laid-out city, the city that generation lays out on a map from a template and a kit, MUST be written in
  one form that holds the template and kit it comes from, its map size, each cell's terrain, natural rock and roof,
  each thing that stands on the map with its definition, cell, rotation and, where its definition takes one, its
  material, and where each part of the template's skeleton lies, so that the check reads what generation writes
  [Roadmap: R2; Design: lines 173, 204; Data: `AncientPrefabs.xml` lines 12, 13 and 23].
- **FR-009**: Templates and kits MUST be data that Mantle's mod or Imperium holds and Mantle's generation reads, and
  MUST NOT hold generation itself. Picking a template, mirroring, turning and stretching it to fit the site, and filling
  its blocks with the kit's buildings belong to R2, and generation does nothing else to a template [Roadmap: R13, R2;
  Design: lines 184, 209; Direction].
- **FR-010**: A template MUST NOT hold another game's art, names, models or code. Its terrain shape and skeleton MAY
  follow its reading cell by cell, since a reading lies on the game's flat cells and is built from the culture's own
  kit, and so carries only the reference city's skeleton, the general way it is laid out (FR-036) [Direction;
  EULA: line 76].
- **FR-011**: The Empire's elements in a template or kit, such as the names in a word list and its public buildings,
  MUST come from Rome as reliable sources describe it, leaning toward New Rome, and not from popular images of Rome
  or from a reference city [Design: setting.md lines 57, 60-61; Direction]. The tribal culture's word list MUST be
  the one the base game names its tribes' settlements with [Data: `Core/Defs/FactionDefs/Factions_Misc.xml` line
  230].

**The check**

- **FR-012**: The check MUST run outside the game, reading templates, kits, laid-out cities and the game's definitions
  in `Data/`, without starting the game [Testing].
- **FR-013**: The check MUST report each name of a definition that it finds neither in `Data/` nor among the
  definitions of Mantle's and Imperium's mods [Testing; Data; Roadmap: R14].
- **FR-014**: The check MUST report each name that stands where its kind of definition cannot go, such as a
  definition that is not a terrain in a terrain shape, one that is not a wall in wall settings, one that is not a
  biome, river or word list where a template's biomes, rivers or a kit's word list stand, or any thing a city is built
  of placed on a template's cells (FR-002) [Data; Design: line 209]. It MUST also report each value not in its field's
  form, such as an attitude field that is neither true nor false, a cell range, position, size or rotation not in the
  form `Data/` writes it in, and a map size that is not square, and each required field left out, such as a template's
  kit or smallest map (FR-001, FR-003) [Data: `AncientPrefabs.xml` lines 12 and 13; `Dialogs_Various.xml` line
  153].
- **FR-015**: The check MUST accept definitions of the base game and of each expansion that the mod holding the
  template, kit or laid-out city requires, none for Mantle's own mod and Royalty for Imperium, and MUST report a
  definition of any other expansion unless it is marked as that expansion's content, since a mod's requirements are
  the mods it needs to function and other expansions add content [Roadmap: R14, Releases; Design: imperium.md lines
  108-110; Data: each expansion's `About/About.xml`]. A laid-out city, which comes from a template (FR-008), is held by
  the mod that holds its template, and a reading, its template's source (FR-036), by the mod that holds the template
  whose reference it reads; a reading that no template names yet is held by no mod, so it requires no expansion, and
  every expansion's definition in it MUST be marked.
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
  has one, its cell, as Spec Kit's own report gives each finding with its location [Spec Kit:
  `templates/commands/analyze.md` line 181].
- **FR-020**: Every result MUST state that testing in the game is the final check and that it is still to come; a
  template, kit or laid-out city with no problem found MUST NOT be reported as final [Testing; Roadmap: R13].
- **FR-021**: The check MUST read the game's files where they are installed, and MUST NOT copy them into the repository
  or its results, beyond the names and labels it reports [EULA: line 86].
- **FR-022**: The same template, kit or laid-out city, checked against the same `Data/` with the same reference
  picture, MUST always give the same report and the same pictures, as a rerun of Spec Kit's own report without changes
  does [Spec Kit: `templates/commands/analyze.md` line 263].

**The pictures**

- **FR-023**: The check MUST draw each template as a picture of its site: every cell of the terrain shape in its place
  on a grid, the coordinates along the edges as the game gives positions, `x` and `z`
  [Data: `AncientPrefabs.xml` line 12], and the skeleton's parts and relations shown and named on it [Spec Kit].
- **FR-024**: Withdrawn: neither the Input nor another source asks for a picture of a spec card, so none is drawn;
  spec cards are checked (FR-007, FR-013, FR-014) (constitution, Principle V).
- **FR-025**: The check MUST draw each laid-out city on the same kind of grid, with each thing where it stands and each
  part of the template's skeleton named where it lies, and MUST set the whole drawing beside the whole of each
  reference picture given, so that all are seen at once; a template's picture MUST be set beside its reference
  pictures in the same way when they are given [Direction; Spec Kit].
- **FR-026**: Each picture MUST hold a legend that names each terrain, rock, roof and thing it shows under the label
  its definition gives, and names the expansion of each definition that is not the base game's [Data; Design:
  imperium.md line 110].
- **FR-027**: Each problem that has a cell MUST be marked at that cell in the picture, with what it is, so that
  FR-019's location is shown on FR-023's grid [FR-019; FR-023].
- **FR-028**: The check MUST read a reference picture where the developer keeps it, and MUST NOT put it into
  the repository or either mod's released files [Direction; EULA: line 76].

**The comparison**

- **FR-029**: The check MUST measure whether each relation of the template's skeleton holds in the laid-out city, and
  MUST report each one that does not, with the parts it relates and where they lie [Design: line 204; Direction]. A
  laid-out city in which every relation holds MUST then be judged by the maintainer, who looks at the side-by-side
  picture and accepts or rejects it; the check MUST NOT report a match by itself [Direction]. His judgment MUST be
  recorded as an item of a reviewer-owned checklist in the feature where he judges it, one item for each picture,
  naming the template or reading, the commit it was drawn from and where the picture is in the project's files, and
  checked only when he accepts it [Spec Kit: `templates/commands/checklist.md` lines 32-36].
- **FR-030**: A template MUST count as passing only once the check has drawn a city laid out from it, every relation
  of its skeleton holds there, and the maintainer has accepted the comparison with its reference as FR-029 sets,
  whoever wrote the template; the check in the game still follows [Direction; Testing].
- **FR-031**: The first template MUST be the river-bend town's, with the Empire's kit, and they MUST calibrate the
  method first [Direction; Roadmap: R13]:
  - In this feature, before the tribal culture's kit and templates are written, its template and the Empire's kit MUST
    be derived in the order of FR-047, and where that order leaves them to a reading, taken from its reference pictures:
    the screenshot of the player-built city, which is the source, and the newest render on the game's cells, the town's
    reading, with its heights, hidden areas and exact sizes guessed, both in `template-references/` in the project's
    files (FR-036). The template MUST fit a city's 350×350 map, whatever size the render was drawn at, keeping the same
    skeleton relations (Clarifications). The check MUST pass the template and kit and draw the template beside both
    pictures; if the forms cannot express the town, they MUST be fixed first [Direction; FR-003; FR-025].
  - Once generation lays the town out from them [Roadmap: R2, R15], the town MUST keep every relation of its skeleton,
    as FR-029 measures: the river bend, the wall line, which districts adjoin, how the main street connects, and where
    the plazas and public buildings lie. The town MUST come from generation, not be written by hand, since only
    generation tests the method [Direction].
  - The maintainer MUST then judge the laid-out town by eye beside the screenshot and the render. A cell-exact match
    to the render MUST NOT be required, since it is a guess too [Direction].
  - If the method cannot express the town, the method MUST be fixed before anything else [Direction].
  - Once the calibration passes, the town's template MUST ship with Imperium as a regular template, as it stands, with
    no step that changes its content [Direction; Roadmap: R15].
- **FR-032**: Kits and templates MUST come, in time, for the culture of every faction that has settlements: the Empire
  [Data: `Royalty/Defs/FactionDefs/Faction_Empire.xml` lines 5 and 11], tribal and industrial (outlander) [Data:
  `Core/Defs/FactionDefs/Factions_Misc.xml` lines 9, 185, 224 and 443], pirate [Data: same file, lines 511 and 517],
  medieval, for the medieval factions other mods add [Direction], and Odyssey's Traders Guild and Salvagers, whose
  settlements lie on the Orbit layer [Data: `Odyssey/Defs/FactionDefs/Factions_Misc.xml` lines 5, 17, 40-42, 168, 188
  and 202-204] [Design: line 184; Direction], the Salvagers only if they really get settlements, which their
  definition leaves open, since the faction is hidden [Data: same file, line 172], and which a check in the game is to
  show [Direction]. This feature MUST hold the tribal culture's kit and its first templates, one for each attitude
  (FR-039), which Mantle's alpha opens as a mod of its own [Roadmap: R13, R14, Releases; Direction], and the Empire's
  kit with the river-bend town's template, which come with Imperium [Roadmap: R15]. The industrial (outlander) and
  pirate cultures' kits and templates, which the alpha opens too, are R16's, and MUST be written in this feature's
  forms and checked by its check [Roadmap: R16, Releases]. The other cultures' kits and templates are later work
  [Direction; Roadmap: R13].
- **FR-033**: Adding a culture MUST need only its skeletons, in its templates, and its kit [Direction]. Everything else
  MUST be shared and the same for every culture: the forms of templates and kits, the check outside the game and its
  pictures, generation's picking, mirroring, turning, stretching and filling [Roadmap: R2], and the pieces, which every
  kit shares and each faction skins [Design: line 194; Direction].
- **FR-034**: An author MUST be able to start a culture by copying an existing culture's skeletons and kit, and the
  check MUST treat the copy as it treats the original [Direction].
- **FR-035**: The river-bend town MUST serve as the complete worked example, from its reference pictures through its
  skeleton and the Empire kit to the city generation lays out from them [Direction; FR-031].
- **FR-036**: Wherever the design and the maintainer's recorded direction leave them open (FR-047), a culture's
  templates and kit MUST be taken from its reference city's reading: the reference is read onto the game's cells, and
  the reading is set beside its pictures until the maintainer, judging it by eye beside them, accepts it, recorded as
  FR-029 sets, as the river-bend town's render was judged; then the template's terrain shape and skeleton, and what the
  kit's groups, fill and wall settings hold, are taken apart from the reading [Direction]. A new reading MUST be written
  in the laid-out city's form (FR-008), naming the reference city it reads in place of a template and kit, so that the
  check checks it and draws it beside the reference pictures as it does a laid-out city (FR-025) [Direction; Spec Kit];
  the river-bend town's reading is its render, which already exists (FR-031). A reading written in that form MUST be
  kept in the repository, outside both mod folders and so outside their released files, as the template's source; its
  reference pictures MUST NOT be (FR-028) [Direction; R14; EULA: line 76].
- **FR-037**: Where FR-047 leaves them to a reading, the tribal culture's first templates and its kit MUST be taken from
  cities of Anno 117's Albion built only in the Celtic way, neither Romanized nor mixed, at the scale of a tribal
  settlement, and shown from above so that their layout can be read: player-built cities shared publicly from any
  source, or cities the game presets for a governor or an AI rival, which the maintainer chooses among candidates before
  their readings are written [Direction]. There MUST be one for each attitude (FR-039), from the references the
  maintainer chose: Tir Uisce for the gentle tribe's open village, a Celtic oppidum for the fierce tribe's walled
  stronghold and a small Celtic hillfort for the savage tribe's fortress, Steam screenshots 3639186959, 3625652909 and
  3621994739, whose pictures are kept in `template-references/部落城-凯尔特/` in the project's files and never in the
  repository (FR-028). These pictures are oblique, not shown from above, so they are read only where FR-052 allows;
  the references shown from above that the maintainer chooses instead, among the candidates found, are open
  [Direction, 2026-11-24]. An agricultural island, 3639163413, MAY be looked at beside them as supplementary material only,
  to help read them: no reading is written of it, and it is the source of no template and of nothing in the kit
  [Direction]. A tribal template's extent MUST be its reading's, laid on the game's cells with things of the sizes their
  definitions give (FR-036) [Data], and is stated as its smallest map, no larger than a city's 350×350 map (FR-003); a
  tribal settlement's map is a city's map, since the design's city building is the generation of every settlement
  [Design: line 173; Direction].
- **FR-038**: Settlements MUST be built from three layers [Direction]: Mantle's, the same for every culture (FR-033);
  the culture's, one kit that all of the culture's factions share (FR-006); and the faction's, the templates of its
  culture that its settlements are laid out from, picked by attitude (FR-039) and terrain (FR-040). A template MUST
  serve a faction's settlement only where both hold: its two attitude fields match the faction's, and its biomes,
  where it names any, include the settlement's [Direction; FR-039; FR-040]; which of several such templates
  generation takes is R2's [Roadmap: R2]. A culture MUST
  pick only by the dimensions it needs [Direction]: the tribal culture's templates MUST leave their biomes open, and
  the Empire's MUST leave both attitude fields out, which serves the Empire, since it holds neither (FR-040).
- **FR-039**: A template MUST state the attitude of the factions it serves in the two fields with which a faction's
  definition states it, `naturalEnemy` and `permanentEnemy`, each false unless set [Data: `Factions_Misc.xml` lines
  202, 462, 485 and 529], and serves the factions whose definitions hold the same two values; it MUST NOT name a
  faction, so that factions other mods add pick the same way [Direction]. The tribal culture's templates MUST follow
  its factions' descriptions: an open village for the gentle tribe, which holds neither field and is open to trade
  and alliances; a walled stronghold for the fierce tribe, a natural enemy that values warlike dominance; and a
  fortress for the savage tribe, a permanent enemy driven by a blood-and-honor culture that cannot be allied with
  [Data: same file, lines 445, 480 and 504, confirmed by the maintainer].
- **FR-040**: A template MUST state the biomes it suits, or none for any biome (FR-001). The Empire's templates MUST be
  picked by terrain alone [Direction: the maintainer confirmed that the Empire picks by biome and the tribes by
  attitude], as the base game's Empire definition, which Imperium's Empire replaces [Design: setting.md line 83], holds
  neither attitude field, only the factions it is not a permanent enemy of [Data:
  `Royalty/Defs/FactionDefs/Faction_Empire.xml` lines 57-67]. They MUST follow the design's
  two looks of imperial cities: temperate, the look in temperate and cold regions, and arid, the look in hot, dry ones
  [Design: lines 208 and 162], which the direction's temperate and desert and arid biomes name. The river-bend town's
  MUST suit the temperate look's biomes: temperate forest and temperate swamp [Data:
  `Core/Defs/BiomeDefs/Biomes_Temperate.xml` lines 5 and 210] and boreal forest, tundra, cold bog, ice sheet and sea ice
  [Data: `Core/Defs/BiomeDefs/Biomes_Cold.xml` lines 5, 198, 371, 586 and 710], and Odyssey's glacial plain, a region
  scraped clean by glaciers and so cold, marked as Odyssey's content (FR-015) [Data:
  `Odyssey/Defs/BiomeDefs/GlacialPlain.xml` line 7] [Direction]. A Romanized Egyptian city's, which is later work, MUST
  suit the arid look's: arid shrubland, desert and extreme desert [Data: `Biomes_WarmArid.xml` lines 5, 172 and 322;
  Direction; Roadmap: R15]. "Temperate" here is the design's look, which is wider than the biomes `Data/` calls
  temperate. The other biomes are in neither list: the tropical ones, hot and wet [Data: `Biomes_Warm.xml` lines 5 and
  203]; Odyssey's grasslands, glowforest and scarlands, whose descriptions name no region, and its lava field, whose
  description names volcanic heat but no region's climate, since no source places them (Principle V) [Data:
  `Odyssey/Defs/BiomeDefs/Grasslands.xml`, `Glowforest.xml`, `Scarlands.xml` and `LavaField.xml`, each line 7]; the
  ocean and the lake, which are water [Data: `Core/Defs/BiomeDefs/Biomes_Water.xml` lines 7 and 22]; Odyssey's space and
  orbit, which are empty space [Data: `Space.xml` lines 7 and 45]; and the underground and Anomaly's labyrinth, metal
  hell and undercave, which never generate on the world [Data: `Core/Defs/BiomeDefs/Biomes_Misc.xml` line 7;
  `Anomaly/Defs/MapGeneration/LabyrinthMapGenerator.xml` line 32, `MetalHellMapGenerator.xml` line 31 and
  `UndercaveMapGenerator.xml` line 105].

**The order of derivation**

- **FR-047**: A culture's kit and templates MUST be derived in this order [Direction; constitution, Source Register,
  row Imperium's own design]:
  1. Imperium-old's default-branch design meaning, reusing everything it defines for them, such as the parts and
     relations of a skeleton and what a kit holds [Design: lines 184, 193, 204, 209];
  2. where that design is silent, the maintainer's broad direction, as this repository's merged specs and roadmap
     record it [Direction; Roadmap];
  3. only where both are silent, the reference city's reading (FR-036), with what is taken from it marked [Direction]
     for the maintainer's judgment of its broad direction.
  What a reading gives MUST NOT override 1 or 2 [Direction]. Each part of a kit or template MUST name the source it was
  derived from, and each part filled from a reading MUST be marked [Direction] [constitution, Principle VI;
  Direction].

**Reading a reference from its game's data**

- **FR-041**: A reference city that Anno 117 presets, on an AI rival's or a third party's island, MAY be read from the
  game's own data, and MUST then be read only from the game's own files: its `file_h.db` and its `.rda` packages, and
  in them the island's `.a7m` file [Direction]. It MUST NOT be read from the old project's index, cfg or cut files
  [Direction]. The packages MUST stay on the maintainer's computer, and everything read or drawn from them MUST go into
  `template-references/` in the project's files and MUST NOT go into the repository or either mod's released files
  [Direction; EULA: line 76; FR-028].
- **FR-042**: Each object read MUST take its category from the game data itself, in two layers: its asset Template,
  and the graphics folder its ConfigFilename names [Direction].
- **FR-043**: A preset reference read from the game's data MUST be drawn from above: each object at its `(x, z)`
  position on the cells, over the island's heightmap, turned to match the game's own top-down image of the island,
  `mapimage.png`, with linear pieces drawn as lines, houses as markers and fields as squares. For each island the
  drawing MUST give a skeleton picture as PNG, the same laid over the game's image, `objects.json` listing every object
  with its two categories and its position, and a summary [Direction]. The two pictures are the reference's pictures,
  set beside its reading as any reference picture is (FR-025, FR-036) [Direction].
- **FR-044**: The drawing MUST be built in steps, and the maintainer MUST have seen each step's picture before the next
  is built: first the objects as dots coloured by category, then the skeleton, then, optionally, each building's real
  footprint from the game's `.ifo` files [Direction].
- **FR-045**: The old project's output and old images, and FileDBReader, MUST be used only to cross-check what a
  reading of the game's data gives, and MUST NOT be what a reference's drawing is taken from [Direction; constitution,
  Principle II].
- **FR-046**: The later cultures' references MUST come from: Anno 1800 for the industrial (outlander) culture, Bright
  Sands for the civil outlanders and Wormways for the rough, and for the pirate culture, Anne Harlow's and Jean La
  Fortune's islands [Direction; Roadmap: R16]; and Odyssey's own form of an orbital settlement, rooms laid off a spine
  of corridors on one enclosed platform, for the Traders Guild, and for the Salvagers if they really get settlements
  (FR-032) [Direction; Data: `Odyssey/Defs/LayoutDefs/Layouts_OrbitalPlatform.xml` lines 5, 7, 23 and 158-194;
  `Odyssey/Defs/MapGeneration/SpaceMapGenerator.xml` lines 82-87].

**Reading a reference from its picture**

- **FR-048**: A reference city that exists only as a picture MUST be read onto the game's cells by first sizing a cell:
  in the picture a door, a figure or a tree is one RimWorld cell, which gives how many pixels one cell is; then how many
  RimWorld cells the reference game's own cell is; and only then are sizes compared and things laid out. The other
  game's cell MUST NOT be mapped one to one, and the size of one of Imperium's households MUST NOT size a reference's
  houses [Design archive: `cities.md`, The size of a cell]. The scale MUST name the things it was got from, each with
  its region of the picture [constitution, Principle VI].
- **FR-049**: A reference MUST be traced into cells only as far as blocks, house groups, yards and roads, not building
  by building, and, where FR-047 leaves a template to a reading, a template candidate MUST come only from tracing an
  accepted reference [Design archive: `cities-forms.md` lines 123 and 475]. Each traced piece MUST name the region of
  the picture it was read from [constitution, Principle VI]. Each building or group MUST be given a use first, one of
  housing, shop front, workshop, tavern, market, public, annex or attic, or unclear, with a one-sentence basis [Design
  archive: `cities-forms.md` lines 475-477]. What is done with an area of which more than three tenths is unclear is
  [NEEDS CLARIFICATION: the design archive sends the area's image to the maintainer to mark (`cities-forms.md` lines
  478-479), but he judges only broad direction (constitution, Principle IV), and no other source gives a form; none is
  written (Principle V)]. The old project's legend of the river-bend screenshot is classed `research` in the archive
  (`specs/005-imperium-design-archive/research/C19.md` line 11) and describes that one picture, so it is not design
  meaning and is not taken.
- **FR-050**: A reading MUST be made one area at a time, and the maintainer MUST see each area's picture once after it
  is traced and once after it is laid out, before the next area is begun [Design archive: `cities-forms.md` line 199;
  FR-044]. An area is 2800 to 9200 cells, floating with the attraction field's weight so that areas near the core and
  the main street are small and outlying ones large, the strength of the weighting being a trial value [Design archive:
  `cities-forms.md` line 487].
- **FR-051**: The check MUST draw a tracing over its reference picture at the same scale, compare each traced piece with
  the colour and shape of the picture where it lies, and mark each piece that does not match as a candidate for the
  maintainer's attention, with what differs. It MUST NOT decide that a piece is wrong or that the reading matches
  (FR-029) [Direction: the effect of the old project's preview tool is kept, 2026-11-24; Design archive: `cities.md`,
  the Anno sample "kept for side-by-side comparison"]. What counts as a piece not matching the picture in colour and
  shape is [NEEDS CLARIFICATION: no source gives it. The design and the maintainer's direction state the effect only;
  the old tool's criteria are implementation, which the Source Register excludes; none is written (constitution,
  Principle V)].
- **FR-052**: Where FR-048 to FR-051 give no form for a picture, such as one not shown from above (FR-037), it MUST NOT
  be read by a method of its own; which picture to use instead is the maintainer's broad direction [constitution,
  Principles IV and V; FR-037].

### Key Entities *(include if feature involves data)*

- **Template**: the designed layout of a whole city site: its terrain shape, its skeleton, what it is picked by, among
  it the attitude of the factions it serves and the biomes it suits, the smallest map it needs, its culture and the
  reference city it is drawn from. It places no thing a city is built of.
- **Terrain shape**: the site's cells, each with its terrain, any natural rock and its roof, as the game defines them.
- **Skeleton**: the fixed parts of a city's layout and their relations to each other and to the terrain. A kit holds
  one too [Design: line 184].
- **Kit**: one culture's fixed set of generation data: word list, skeleton, groups, fill and wall settings, and
  possibly a block library.
- **Block library**: a kit's ready-made blocks, built from spec cards.
- **Spec card**: one building's plot, rooms and contents.
- **Piece**: a generic building element of generated settlements that the base game lacks, shared by every kit and
  skinned by faction [Design: line 194].
- **Culture**: one kind of settlement with its own kit, which all its factions share, and its own skeletons and
  templates, such as the tribal culture's or the Empire's.
- **Attitude**: how a faction stands toward others, by its definition's two fields, natural enemy and permanent enemy;
  a template serves the factions whose attitude it states.
- **Laid-out city**: the city generation lays out on a map from a template and a kit: each cell's terrain, rock and
  roof, each thing that stands there, and where each part of the skeleton lies.
- **Reference city**: the city a template is drawn from, player-built and publicly shared or preset by the game,
  and its **reference pictures**, such as a screenshot of it, which the developer keeps outside the repository and
  both mods' released files (FR-028).
- **Reading**: a reference city drawn on the game's cells and set beside its pictures until it matches them, in the
  laid-out city's form, from which a culture's templates and kit are taken; for the river-bend town, its render. It is
  kept in the repository as its template's source; its reference pictures are not.
- **Top-down view**: a preset reference city read from its game's own data and drawn from above: its objects, each
  with its two categories and its position, as a skeleton picture, the same laid over the game's image, `objects.json`
  and a summary, kept in the project's files and used as the reference's pictures (FR-041 to FR-044).
- **Report**: what one run of the check found, each problem with its place, and the statement that the check in the
  game is still to come.
- **Picture**: the drawing of one template or laid-out city, with grid, coordinates, legend and marked problems, and
  the reference picture beside it.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: For a set of test templates, kits and laid-out cities holding one problem of each kind that FR-013 to
  FR-018 and FR-029 name, the check reports 100% of the problems, and reports none for those that hold no problem.
- **SC-002**: For every reported problem that has a cell, a developer finds that cell in the picture from the report
  alone, without reading the template or laid-out city (FR-019, FR-027).
- **SC-003**: Checking and drawing one template, or one laid-out city beside its reference, finishes before the game
  reaches its main menu, both on the maintainer's computer: the check run on that one file against `Data/` with every
  expansion and with `--mod` for Mantle and Imperium, and the game launched without `-quicktest`, which starts straight
  into a map (`Readme.txt` lines 58-60), with Royalty, Mantle and Imperium active, timed from launch to the main menu.
  It measures the Input's "so that the developer can see it without starting the game" [Spec Kit].
- **SC-004**: 100% of reports state that testing in the game is the final check and is still to come (FR-020).
- **SC-005**: For every laid-out city given with a reference picture, the developer sees the whole city and the whole
  reference at once, side by side, and can name in both where each part of the skeleton lies (FR-025).
- **SC-006**: No template counts as passing without a laid-out city from it in which every skeleton relation holds
  and whose comparison with its reference the maintainer has accepted (FR-030).
- **SC-007**: The river-bend town's template passes the check, and in its picture beside each reference picture,
  every part of its skeleton is found in the same relations to the river and to the other parts (FR-031).
- **SC-008**: Before the tribal culture's kit and templates are written, the river-bend town's template and the
  Empire's kit pass the check and the template is drawn beside the screenshot and the render; before the town ships,
  a town that generation lays out from them keeps 100% of its skeleton relations and the maintainer has accepted it
  beside both (FR-031).
- **SC-009**: A test culture copied from the Empire kit and the river-bend town's template is checked and drawn with no
  change to any shared form, check, picture or piece (FR-033, FR-034).
- **SC-010**: The tribal culture's kit and its three first templates are taken from the readings of the references
  the maintainer chose, each of which he has accepted beside its pictures, each template states the attitude of the
  tribe it serves, and all pass the check (FR-036, FR-037, FR-039).
- **SC-011**: For every preset reference read from its game's data, 100% of its objects are in its `objects.json` with
  both categories and a position, its skeleton picture and its overlay on the game's image are in
  `template-references/`, the maintainer saw each step's picture before the next step was built, and none of the
  packages or of what was read or drawn from them is in the repository (FR-041 to FR-044).
- **SC-012**: In the Empire's kit and the river-bend town's template, and in the tribal culture's kit and first
  templates, 100% of the parts name their source, every part Imperium-old's design defines is taken from it, and no
  part filled from a reading contradicts the design or the maintainer's recorded direction (FR-047).
- **SC-013**: For every reference read from its picture, its reading holds a `scale` that names the things it was got
  from, 100% of its traced pieces name their regions of the picture and every building or group has a use from the
  design's list with a basis, and the maintainer saw each area's picture after it was traced and after it was laid out
  before the next area was begun (FR-048 to FR-050).

## Assumptions

- The supported game version is 1.7, as for R1 (`specs/001-mod-foundation/spec.md`, Clarifications), and the
  definitions read are those of RimWorld 1.7.5014.
- The check runs where `Data/` is available: on the maintainer's computer, in the game's install folder, and in cloud
  threads, from the project's copy of RimWorld 1.7.5014's `Data/`.
- The alpha opens the tribal culture's kit and templates; generation is R2's [Roadmap: R13, R2, Releases]. The form of
  a laid-out city is set here so that R2's generation writes it and the check reads it.
- Mantle's own mod holds what every culture shares and the tribal culture's kit and templates; Imperium holds the
  Empire's kit and templates [Roadmap: R14, R15, Releases]. Both mod folders lie side by side in this repository, with
  the check and the readings at its root, and Mantle's package identifier is `Neiro.RimWorld.Mantle` [R14].
- Every faction's definition can hold `naturalEnemy` and `permanentEnemy`, since `Data/` sets them on factions of
  every kind, in Core and in the expansions (Sources, [Data], a faction's attitude).
- Which culture a faction's settlements take, and the picking itself, are generation's; this feature gives templates
  the attitude and biomes that picking reads [Roadmap: R2].
- Until R2 generates cities, the laid-out cities the check is tested with are written by hand from test templates and
  kits. Test templates, kits and laid-out cities written for this feature are not game content. The river-bend town's
  template is the first template of game content, and it ships with Imperium once its calibration passes (FR-031)
  [Roadmap: R15]. The Empire's kit and the tribal culture's kit are the first kits of game content (FR-032).
- The check in the game, the final one, comes when R2 places the tribal culture's settlements and R15 the Empire's
  [Roadmap: R13; Testing].
- The forms hold the parts the design and the maintainer's direction name, and take further parts when either names
  them [Design; Direction].
- Reading a preset reference from its game's data runs on the maintainer's computer, where the packages are. No
  source asks for a tool in the repository that reads another game's data, so this feature adds none; the check takes
  the pictures such a reading gives as reference pictures, as it takes any other (FR-028, FR-043) [constitution,
  Principle V].
- None of the tribal culture's chosen references is a preset city, so its readings are drawn from the Steam
  screenshots (FR-037); a preset city read from the game's data serves as a reference once the maintainer chooses it
  among candidates, as FR-037 sets for the tribal references [Direction].
- How the forms are written, and the pictures' look and file format, are chosen in `/speckit-plan`.
