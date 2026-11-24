# Mantle

This section covers Mantle, the framework layer of Imperium's code: what it is and what it holds, its layers and kits,
how other mods extend it, its seven-stage engine and the lifeline as a general concept, the principles and order by
which it generates a map, the terrain it lays under every settlement and mission map, the general siting stage, how its
results are judged, the borrowed work it started from and retires, and where the work stands. It meets cities.md and
the cities-*.md files for the Empire's cities built on it, above all cities-siting.md (where a city stands, map size and
area, and the Roman rules for terrain and rivers) and cities-forms.md (templates, kits, spec cards and the city
grammar); cultures.md for the kits and lifelines of the other cultures and for entering settlements; water.md for
water; orders.md and ruins-and-technology.md for the mission sites and ruins it generates; and terms.md for the names.

## What Mantle is

Mantle is the framework layer of Imperium's code, which the content layer builds on; the sources call it by its old
names ICF and Overworld (`.github/deprecated-terms.json` L395-418; `docs/glossary.md` L221). ICF, the short name for
Imperium's own generation and technical base, is symmetrical with CBF (Custom Base Framework)
(`Imperium-Knowledge/09_地图生成与CBF技术.md` L484, R-1028-1355).

Mantle's range is only generation and the technical base: the terrain layer, the site requirements (选址需求单), the district
and wall components, and the loading of templates and spec cards. Gameplay (Orders, Rank, the institutions, the
mechanoids) is to be organised later, because it may be redone; for now it reaches generation only through the L4
interface (`Imperium-Knowledge/designs/ICF/ICF设计.md` L19-21; `Imperium-Knowledge/09_地图生成与CBF技术.md` L484;
`Imperium-Knowledge/裁定归档/2026-10.md` L116). Mantle is the backbone of generation, and CBF was only an early reference
(`Imperium-Knowledge/01_项目宪章与规范索引.md` L185; `Imperium-Knowledge/现行/流程/借用与第三方.md` L82).

Mantle is a general framework. Starting from the world tile, it generates ground suited to the Empire's content and then
works together with the systems of city building: the lifeline, the palace district, spec cards, imperial facilities
and the idea of each faction. Ground and content are designed together, made by an author and used by rules, and
gathered against a covering table; settlements, mission maps and ruins all reuse this method
(`Imperium-Knowledge/09_地图生成与CBF技术.md` L868, R-1111-1908; `Imperium-Knowledge/现行/城/地形与选址.md` L35;
`Imperium-Knowledge/designs/做法史/地形与选址.md` L139).

Mantle also generates the medieval settlements. Imperium is therefore meant to stay installed for every player, players
of Medieval Overhaul included, and for players who do not use the Empire's content Mantle is the main selling point
(`Imperium-Knowledge/01_项目宪章与规范索引.md` L164, R-1103-1402).

Terrain and settlement generated as one are the biggest selling point of expeditions, since the complaint about the base
game's expeditions is that their destinations hold nothing to do. Faction and terrain generation are built as a
framework at the level of a DLC, but they are not advertised in the description, the update notes or in-game text;
players find them on expeditions (`Imperium-Knowledge/09_地图生成与CBF技术.md` L444-445, R-1028-0157, R-1028-0159;
`Imperium-Knowledge/现行/城/地形与选址.md` L12-16).

## Layers and kits

Mantle has five layers whose dependencies run only downward: L0 base (random numbers, logs, export, timing, version and
save compatibility), L1 data (Defs), L2 pipeline (stages, strategy interfaces and the transaction), L3 faction kits and
L4 gameplay interface. The third-party terrain code sits in a separate assembly that only the L2 terrain stage calls
(`Imperium-Knowledge/designs/ICF/ICF设计.md` L57-68).

L1 holds Defs that are loaded at start and checked: a terrain profile, the site requirements, spec cards in one format,
wall components, object roles, material tiers, parameter tables, the settlement plan and the faction kit
(`Imperium-Knowledge/designs/ICF/ICF设计.md` L83-96). An object role leads to a chain of candidates: the mod's own
component, then the base game or a DLC, then ReBuild only when its switch is on and it is loaded, then a placeholder
(`Imperium-Knowledge/designs/ICF/ICF设计.md` L91). The framework's design is set out in its design document, a city
skeleton format, a component requirement table and the settlement plan grammar (`Imperium-Knowledge/目录/ICF.md` L7-60).

> [!NOTE]
> **Deleted**: the block library, a Def of ready-made blocks built from spec cards and drawn by seed into block slots,
> 6-8 modules to a grade (`Imperium-Knowledge/designs/ICF/ICF设计.md` L95), was removed with its slots and modules by
> R-1030-1930 (`Imperium-Knowledge/designs/ICF/ICF设计.md` L6; `Imperium-Knowledge/designs/整理/整理方案-2026-11-02.md`
> L97).

A kit (套件) is a culture's fixed set of generation data (`docs/glossary.md` L184). Rome has one kit, whose skin follows
the region, arid or temperate (干热区、温寒区); there is a medieval kit, and modern, tribal and tent-camp kits come later.
A kit provides the L1 data and a strategy for each stage (`Imperium-Knowledge/designs/ICF/ICF设计.md` L124-128;
`Imperium-Knowledge/09_地图生成与CBF技术.md` L580, R-1029-1323). Form and skin are separate for all four factions: form
comes from the terrain and the plan, skin from the biome (`Imperium-Knowledge/09_地图生成与CBF技术.md` L580).

> [!NOTE]
> **Deleted**: two Roman kits named after Justinian and Basil (`Imperium-Knowledge/designs/ICF/ICF设计.md` L128) were
> merged into the one Roman kit with its two regional skins (`Imperium-Knowledge/09_地图生成与CBF技术.md` L580, R-1029-1323),
> and the identifiers JustinianCity and BasilCity are deprecated terms, replaced by arid and temperate
> (`.github/deprecated-terms.json` L597-622).

The generic terrain pieces (地形件), namely terrace edge, ramp, low railing, steps, channel edge and retaining wall,
belong to Mantle's component library and not to the Roman kit. Their form is shared and their skin follows the faction:
limestone for Rome, rough stone for medieval, steel for modern (the base game has no concrete material, so a concrete
skin comes later with the mod's own pieces) and rammed earth for tribes
(`Imperium-Knowledge/现行/流程/借用与第三方.md` L20, R-1029-2053, R-1029-2112).

L4 has two entrances: one generates a settlement (faction bases, cities) and one generates a mission site (Orders,
claims, ruins). Gameplay obtains maps only through these two, and the medieval outpost group of cards is used only
through the second (`Imperium-Knowledge/designs/ICF/ICF设计.md` L130-134).

## Openness to other mods

Other mods may add faction kits, spec cards, object roles, material tiers and parameter tables in XML, or inherit the
stage strategy base classes in C#. L0 and L2 internals are not public; outside mods connect only through L1 data, the
strategy base classes and the two L4 entrances (`Imperium-Knowledge/designs/ICF/ICF设计.md` L157-167;
`Imperium-Knowledge/09_地图生成与CBF技术.md` L502, R-1028-1806). Public fields are only ever added: a field to be renamed
or removed is kept for one version and converted with a warning when read. A kit declares the framework version it needs
and is skipped with an error when that is not met, while the other kits carry on; an object role of an outside kit that
has no candidate falls to a placeholder with a warning, and generation goes on. The GL assembly is not an outside
interface, and templates derived from CBF are not published with the public interface
(`Imperium-Knowledge/designs/ICF/ICF设计.md` L160-167). defNames and Keyed keys take no mod prefix
(`.claude/rules/naming.md` L31).

> [!NOTE]
> **Deleted**: the Def prefix `Imperium_` that the framework kept (`Imperium-Knowledge/designs/ICF/ICF设计.md` L159;
> `Imperium-Knowledge/09_地图生成与CBF技术.md` L502) is a deprecated term, replaced by names without a mod prefix
> (`.github/deprecated-terms.json` L659-671).

## The engine and the lifeline

The settlement generator is an engine of seven stages, each with one duty: (1) landform; (2) siting, which turns the
site requirements into a site envelope, edges classed as mountain, water or opening, high ground, an approach edge and a
core position; (3) assembly, which fits the plan to the site; (4) wrapping the wall; (5) the lifeline; (6) building,
which puts cards into card slots with their material tiers and builds outside the city; and (7) checks, which are
self-checks that count to zero, an image for every change, a summary of differences and a list of the points decided
without the user. Each stage of each faction is a replaceable strategy class, the L2 pipeline with the L3 kit
(`Imperium-Knowledge/09_地图生成与CBF技术.md` L578, R-1029-1310). A kit changes the strategy of a stage, not the stages: in
assembly the medieval kit grows the town from a core (`Imperium-Knowledge/designs/ICF/ICF设计.md` L109, L120;
`Imperium-Knowledge/09_地图生成与CBF技术.md` L580); how the Roman city is assembled is in cities.md. The order of stages is not
a written-in one-way chain: in the growth strategy of assembly roads and buildings constrain each other, and stage D can
return to assembly when it finds a gate that does not meet a road (`Imperium-Knowledge/designs/ICF/ICF设计.md` L119).

> [!NOTE]
> **Deleted**: the Roman strategy of assembly, reading a hand-designed plan Def and fitting it to the terrain
> (`Imperium-Knowledge/09_地图生成与CBF技术.md` L580; `Imperium-Knowledge/designs/ICF/ICF设计.md` L109), was removed when
> the Roman plan came to be generated from its main core (`Imperium-Knowledge/designs/ICF/ICF设计.md` L6, R-1030-1802).

The lifeline (命脉线) is the fifth stage's general concept: every settlement has a line from a source through a trunk to
the places where it shows and out at an exit, and cutting the source is felt across the whole settlement. The engine
knows only these four kinds of node and the edges between them; the plan names the node types and positions, and the kit
supplies the parts and their effects (`Imperium-Knowledge/09_地图生成与CBF技术.md` L579, R-1029-1310; `docs/glossary.md` L187).
A settlement may have several sources, an exit may be a chain, nodes may be marked as ones that can be left out, and
what stops when a source is cut is written as a check that the kit's table supplies
(`Imperium-Knowledge/designs/ICF/聚落平面语法-v4.md` L100-107). A ruin's "restore power to open the door" and an Order's
"destroy communications" are operations of the same kind on the same line (`Imperium-Knowledge/09_地图生成与CBF技术.md` L579).
Each faction fills one kind of lifeline, the details supplied by its kit when that faction is made; those of the other
cultures are in cultures.md, and the medieval lifeline was earlier the road, changed to the lord on 2026-10-30 00:21
(`Imperium-Knowledge/designs/ICF/聚落平面语法-v4.md` L108, R-1030-0021).

> [!NOTE]
> **Deleted**: the Roman lifeline, water that is also the city's power grid, from the aqueduct or the water tower through
> the street channels to the fountains, baths and outflow gate and on to the fields, belonged to the hydraulics the
> maintainer deleted (`Imperium-Knowledge/09_地图生成与CBF技术.md` L579;
> `Imperium-Knowledge/designs/ICF/聚落平面语法-v4.md` L108-114).

> [!NOTE]
> **Unverified**: the "world-layer ledger" (the living city written back to the world layer, ruins taking effect on the
> world map, contribution and tendency sharing one layer) is not done now and is to be decided before Rank is completed
> (`Imperium-Knowledge/09_地图生成与CBF技术.md` L580).

## Principles of generation

Imperium uses its own generator and in the end does not depend on the CBF/MO research architecture to run. Its quality
target is at least the complete building groups, blocks, courtyards and harmony with terrain of CBF's settlements of the
same kind; this is a target, not a claim that it is met (`Imperium-Knowledge/09_地图生成与CBF技术.md` L8). The base strategies
are CompactTown and OrganicVillage, which are tendencies toward concentration or spread and not a simulation of city or
village life; generation driven by use (city, village, fortress, market, mine) is a named direction of discussion and by
itself approves no new generators, buildings or quests (`Imperium-Knowledge/09_地图生成与CBF技术.md` L10). Real relations of
production, housing, transport, defence and land use explain why space is organised as it is; CBF serves to learn
methods, community images serve only as visual reference, and the design simulates neither centuries of economic history
nor unlimited resident AI (`Imperium-Knowledge/09_地图生成与CBF技术.md` L12).

The default tendency comes from the terrain, the style rules and functional relations, and explicit configuration still
applies. Concentration is not symmetry, dispersal is not spreading rooms apart on purpose, and a settlement is not broken
up for effect where its ground has no notable obstacle (`Imperium-Knowledge/09_地图生成与CBF技术.md` L20). Building
candidates, real entrances, shared space, roads and needed local changes of terrain constrain one another and may be
coordinated over several passes in planning. Approach road, main street and gate direction are set first by the style
rules (the modern style, for one, lays its road net first); inside a block, side roads, lanes and buildings constrain one
another, so buildings are not scattered first and then refused the road links they need. Local regularity and straight
roads may arise naturally (`Imperium-Knowledge/09_地图生成与CBF技术.md` L22).

Buildings rest on complete usable pieces, real doors, interior facilities and real demand. A functional core is bound
to a concrete building, not to an abstract centre point; shared space matches the real entrances and used cells of the
final map; and a small public open space is not called a large courtyard, plaza or mature block
(`Imperium-Knowledge/09_地图生成与CBF技术.md` L28). Road, entrance forecourt, courtyard and building footprint are
separate duties of space: a passage that needs protecting is not covered by later buildings, a courtyard does not become
free building land because nothing stands in it, and names such as Ward, District, Block or Cluster prove no complete
city-building capability of the same name (`Imperium-Knowledge/09_地图生成与CBF技术.md` L30).

Adding hard constraints and a complete expression of land use is more direct than piling up soft scoring, which may
still rank legal candidates; what is learned from others is rewritten as Imperium's own data, interfaces and algorithms,
and no formal runtime dependence on third-party code is built (`Imperium-Knowledge/09_地图生成与CBF技术.md` L66-68).
Optimisation may cut repeated sorting, repeated scoring and useless payload but does not quietly loosen hard constraints
or drop demands, and performance, planning correctness and visual organisation are judged separately
(`Imperium-Knowledge/09_地图生成与CBF技术.md` L51). The formal generator, a research replay and an isolated prototype are three
different things: a replay that matches on CBF's frozen input does not mean a physical map is newly generated each time,
and a prototype that reads cold successfully does not mean its new algorithm is deployed
(`Imperium-Knowledge/09_地图生成与CBF技术.md` L72).

Sizes are odd: the width of a gate passage, the sides of gatehouses and towers, and the width and depth of building
outlines take odd cell counts, because an even count has no centre cell. This concerns sizes, not numbers; even sizes in
drawings become the neighbouring odd size when built, and component sizes (tower, gate, spec card) do not scale with the
map (`Imperium-Knowledge/09_地图生成与CBF技术.md` L333, R-1027-2219;
`Imperium-Knowledge/designs/instructions/生成具象规格-现行版.md` L31). A margin of 15 cells applies to all generation by
default, and roads may run to the map edge (`Imperium-Knowledge/09_地图生成与CBF技术.md` L162).

## Terrain first

Maps are generated in two steps, terrain first and buildings on it afterwards, so that buildings do not adapt to random
terrain. This covers every faction settlement the mod generates, in all four styles, and every map of an Empire quest
(Orders expedition maps, commission camps, ruins and claim sites), and not the player colony
(`Imperium-Knowledge/designs/instructions/生成具象规格-现行版.md` L49-51, R-1027-2350;
`Imperium-Knowledge/现行/城/地形与选址.md` L22). The terrain counts as natural landform; the building stage reads the
marks the terrain stage leaves (urban area, stretches the city leans on, holding points, corridors, bridge sites, field
zones) instead of inferring positions from random terrain, and whatever the path, it checks against the final terrain
without assuming that the terrain stage's intent was fully realised (`Imperium-Knowledge/09_地图生成与CBF技术.md` L16).
Player colonies, the contact ruins on the start map, underground layers and paths with the terrain stage off still read
the actual terrain (`Imperium-Knowledge/09_地图生成与CBF技术.md` L16). Natural landform is finished first and then read:
an ungenerated map is not treated as plain, changes made by later base-game steps are included in the final check, and
no height or slope data is invented (`Imperium-Knowledge/09_地图生成与CBF技术.md` L18).

The terrain stage acts at the base game's landform step, behind the switch `terrainTemplates`, which counts among the
switches of "all off"; with it off the terrain is cell for cell the base game's. After it, the base game's ground, stone,
plants, ore veins and animals follow as usual (`Imperium-Knowledge/designs/instructions/生成具象规格-现行版.md` L60-62,
R-1028-0020). Terrain agrees with the world tile in river presence, size and flow, coast direction, world road entries,
biome, soil, stone, plants and hilliness (`Imperium-Knowledge/designs/instructions/生成具象规格-现行版.md` L64;
`Imperium-Knowledge/现行/城/地形与选址.md` L27). It is not used for the player colony with the contact ruins on its start
map, for underground levels or for settlements that other mods generate
(`Imperium-Knowledge/designs/instructions/生成具象规格-现行版.md` L63; `Imperium-Knowledge/现行/城/地形与选址.md` L23).

River, rock, coast and the flat urban ground are set at the terrain stage only. The building stage makes only structural
terrain (moat, channel, pool, bridge, clearing belt, paving) and a few fallbacks (replacing the bearing ground, sealing
rock cracks), which are counted. Legal local changes for real buildings, roads, courtyards, entrances and defence are
allowed and carry no separate engineering cost, resource budget or player action; large unconditional cutting of
mountains or filling of rivers is not done, and on a map with a river the settlement may keep to one bank
(`Imperium-Knowledge/09_地图生成与CBF技术.md` L24; `Imperium-Knowledge/现行/城/地形与选址.md` L25-26). Every settlement
starts from natural terrain, the city adapts to it, and only the problem stretches found afterwards are fixed by the
natural terrain adapting to the city (`Imperium-Knowledge/09_地图生成与CBF技术.md` L503, L506-507;
`Imperium-Knowledge/现行/城/地形与选址.md` L31; `Imperium-Knowledge/designs/instructions/生成第2轮重做-第一段批准与第二段补充.md`
L66-137). How the Roman city and the medieval town treat terrain is in cities-siting.md and cultures.md.

A generation runs in this order: base-game map generation (when the template switch is on and the map is in range, the
landform step is set by the terrain template); the needed natural terrain; a generation id and a terrain snapshot; an
Imperium construction transaction; preliminary planning and a structure check; legal local adjustment, layout
coordination and a final legality check; committing the entities; and an automatic check of the real buildings, roads,
entrances and reserved space (`Imperium-Knowledge/09_地图生成与CBF技术.md` L36-45). When the terrain stage fails, another
landform is tried inside map generation, and when that fails too the map falls back to base-game terrain and the old
path, with a record. A failure rolls back only this construction and keeps the finished natural map; save, load and cold
start are checkpoints in the game, separate from every normal generation (`Imperium-Knowledge/09_地图生成与CBF技术.md` L47;
`Imperium-Knowledge/designs/instructions/生成具象规格-现行版.md` L95).

On settlement maps that use the mod's site requirements, the base game's and DLCs' scattered ancient structures (ruined
walls, ancient shrines and cryptosleep caskets, ancient facilities, complexes, junk) are not generated; those that Odyssey
landmarks and mutators bring stay (`Imperium-Knowledge/designs/instructions/生成具象规格-现行版.md` L93, R-1028-1909;
`Imperium-Knowledge/designs/instructions/生成第2轮重做-第一段批准与第二段补充.md` L253-259;
`Imperium-Knowledge/09_地图生成与CBF技术.md` L507). On maps that use the mod's terrain, other mods that change terrain are
always taken over and their effect is not kept; only freedom from errors is asked of them
(`Imperium-Knowledge/现行/城/地形与选址.md` L55; `Imperium-Knowledge/09_地图生成与CBF技术.md` L431).

## Landforms

The terrain is based on Geological Landforms (GL). Its generation code and method (TerrainGraph noise and slope nodes,
landform XML, world-tile requirements) are carried to 1.7, renamed to isolate them, active only on the mod's settlement
maps, and replaced step by step with the mod's own (`Imperium-Knowledge/现行/城/地形与选址.md` L61;
`Imperium-Knowledge/09_地图生成与CBF技术.md` L455, R-1028-0754). What was built around the earlier terrain templates
stays in use: the hook framework, the handling of roads and scatter, the tile database, the anchor format, the site
requirements and the test tools (`Imperium-Knowledge/09_地图生成与CBF技术.md` L455;
`Imperium-Knowledge/现行/城/地形与选址.md` L72). The tile database lists every attribute of a world tile (hilliness,
river, road, coast or lake, caves, elevation, temperature, rainfall, swampiness, stone, pollution, features and
landmarks, biome), each marked as shaping form, shaping style or irrelevant
(`Imperium-Knowledge/09_地图生成与CBF技术.md` L437).

> [!NOTE]
> **Deleted**: the line of terrain templates of the mod's own drawing: 2-3 templates (inferred, 推) for each kind of
> settlement fixing only the terrain skeleton, layered base maps with river, coast and landmark layers, a real city site
> behind each template (the first blueprints inferred, 推, the user may change them) and a one-sentence setting shaped
> with means of level design, 30 terrain sketches, then a landform library of about 30 parametric landforms, about 12
> large templates holding about 20 small ones under biome style layers, and a first batch of 21 large templates with
> their geometric metrics (`Imperium-Knowledge/09_地图生成与CBF技术.md` L414, L418, L420-424, L431-443). It was removed when
> the terrain moved to Geological Landforms, which discarded the geometric templates, sketch targets and metrics, and
> all the sketch settings were dropped (`Imperium-Knowledge/09_地图生成与CBF技术.md` L455-456, R-1028-0754, R-1028-0813).

GL's generation code is compiled as an independent assembly and shipped with its 44 landform files under the same
licence. It is replaced in steps: first GL's method and landform data as they are, then the mod's own landforms in
TerrainGraph format one by one, and the mod's own code wherever behaviour has to differ
(`Imperium-Knowledge/现行/流程/借用与第三方.md` L65-67). GL is licensed CC BY-NC-SA 4.0, so its part has its own directory
and assembly, carries attribution, is not commercial and is shared under the same licence; the mod is free
(`Imperium-Knowledge/09_地图生成与CBF技术.md` L455; `Imperium-Knowledge/09_地图生成与CBF技术.md` L478, R-1028-1228;
`Imperium-Knowledge/designs/instructions/生成第2轮重做-第一段批准与第二段补充.md` L8-18). LunarFramework has no licence,
so the few small tools needed from it are written anew (`Imperium-Knowledge/09_地图生成与CBF技术.md` L478).

The landforms apply on the mod's Roman and medieval settlement maps, touch no world data and do not depend on Map
Preview: with or without it the result is the same cell for cell
(`Imperium-Knowledge/designs/instructions/生成具象规格-现行版.md` L55-56; `Imperium-Knowledge/09_地图生成与CBF技术.md`
L456). A map has at most one main landform plus river layers (`Imperium-Knowledge/现行/城/地形与选址.md` L66;
`Imperium-Knowledge/09_地图生成与CBF技术.md` L465); how a Roman city's river is laid is in cities-siting.md and water.md.
GL landforms follow GL's own tile requirements, so a flat tile may hold a lone mountain or a caldera; tiles that are flat,
without a river and inland take the mod's own plain landforms, which stay flat, add no ridge and make no streams
(`Imperium-Knowledge/designs/instructions/生成具象规格-现行版.md` L57; `Imperium-Knowledge/09_地图生成与CBF技术.md` L465;
`Imperium-Knowledge/现行/城/地形与选址.md` L67). GL's "no settlement" flag is not copied; a fit table of landform against
site requirements decides by style (`Imperium-Knowledge/designs/instructions/生成具象规格-现行版.md` L58). Each landform is
judged by its form for the tier of settlement it suits (City, medium, small), and one that does not suit is not chosen
(`Imperium-Knowledge/09_地图生成与CBF技术.md` L457; `Imperium-Knowledge/现行/城/地形与选址.md` L98). The size of the map
follows the settlement's tier and not the world setting: 350 × 350 for a large city, 300 for a medium city, 250 for a
small one and 200 for a post (哨所) (`Imperium-Knowledge/现行/城/地形与选址.md` L98, R-1111-1933).

> [!NOTE]
> **Deleted**: the earlier rules on map size, first enlarging the map to the edge a suitable landform needs (City up to
> 325, medium up to 275, small not enlarged), then keeping the player's map size and letting the city follow it, then
> 325, 275 and 225 by tier (`Imperium-Knowledge/09_地图生成与CBF技术.md` L457, L785, L871;
> `Imperium-Knowledge/designs/instructions/生成具象规格-现行版.md` L69), were replaced in turn and last by the sizes by
> tier above (`Imperium-Knowledge/09_地图生成与CBF技术.md` L873, R-1111-1933).

The chosen landform suppresses the base game's mutators of the same category, while Odyssey landmarks and other mods'
mutators count as conflicts; candidate landforms are evaluated on a temporary grid and written to the map only on
success (`Imperium-Knowledge/09_地图生成与CBF技术.md` L462). Odyssey landmarks and modifiers take up a category, and the
base game's terrain also uses GL's river layers (`Imperium-Knowledge/09_地图生成与CBF技术.md` L478). All seventeen biomes
of the base game and Odyssey are supported; glowing forest, scorched ground and lava field need only be usable and free
of errors (`Imperium-Knowledge/现行/城/地形与选址.md` L73; `Imperium-Knowledge/09_地图生成与CBF技术.md` L434-435).

## Siting

Each kind of settlement has its site requirements, one Def holding its size, preferred landforms, hard requirements and
rules for finding a site (`Imperium-Knowledge/09_地图生成与CBF技术.md` L431; `docs/glossary.md` L202). There are eight: J and B
(the Roman City with the arid and the temperate skin), C (Castellum), Fortlet, Burgus, MV, MM and ML, in three tiers:
City (J, B, ML), medium (C, MM) and small (Fortlet, Burgus, MV) (`Imperium-Knowledge/designs/instructions/生成具象规格-现行版.md`
L65-68). The urban area is the net buildable area inside the wall, and the wall band, clearing belt and moat are added
outside it (`Imperium-Knowledge/designs/instructions/生成具象规格-现行版.md` L67); how large it is comes in cities-siting.md.

When a settlement does not fit, its tier is not lowered: generation tries the next candidate landform, then a site on
base-game terrain, then the current generation as with the switch off, recorded as ATTENTION
(`Imperium-Knowledge/09_地图生成与CBF技术.md` L464, R-1028-0900;
`Imperium-Knowledge/designs/instructions/生成具象规格-现行版.md` L70) (replaces `Imperium-Knowledge/09_地图生成与CBF技术.md`
L463, the drop to the next tier). For the Roman city this chain is replaced by its own retries, which cities-siting.md
gives (`Imperium-Knowledge/09_地图生成与CBF技术.md` L746; `Imperium-Knowledge/现行/城/地形与选址.md` L103-106).

The siting stage puts out the site envelope, the edges classed in three kinds, the high ground, the approach edge, the
entry segment of the approach world road and the core position
(`Imperium-Knowledge/designs/instructions/生成具象规格-现行版.md` L92; `Imperium-Knowledge/designs/ICF/ICF设计.md` L108).

> [!NOTE]
> **Deleted**: the water source among the outputs of siting, the point and corridor from which the aqueduct feeds the
> city's water system, belonged to the hydraulics the maintainer deleted
> (`Imperium-Knowledge/designs/instructions/生成具象规格-现行版.md` L92; `Imperium-Knowledge/09_地图生成与CBF技术.md` L479,
> L578).

An
edge is mountain where rock lies at least 5 cells thick outward from it, water where deep water cannot be waded, and an
opening otherwise; only openings are walled and gated, and edges within 12 cells of a mountain foot or a shoreline reach
over to hug it (`Imperium-Knowledge/designs/instructions/生成具象规格-现行版.md` L72-74;
`Imperium-Knowledge/现行/城/地形与选址.md` L45). Whether a barrier holds is judged by pathfinding: with the openings
closed, nobody outside reaches the city without mining or breaking a wall
(`Imperium-Knowledge/现行/城/地形与选址.md` L48; `Imperium-Knowledge/09_地图生成与CBF技术.md` L460).

Problem stretches are of three kinds: a hook (an open stretch that reaches out at least 3 cells to touch mountain or
water and turns back), a string of short openings (each at most 5 cells, separated on the same side by mountain, at
least two in a row) and a gate against a mountain (a gate within 3 cells of where the edge meets a mountain, where the
gate moves and the mountain is not pulled); long straight stretches do not count (`Imperium-Knowledge/现行/城/地形与选址.md`
L47, R-1110-1931). Only on problem stretches, and only in the belt of 8 cells outside the edge, is the mountain pulled:
a decaying bump with noise of GL's kind raises the height so that rock grows where height passes 0.7, rock is filled to
at least 5 cells thick, and an opening of at most 12 cells with mountain at both ends is closed by mountain; outline and
problem stretches are recomputed at most twice (`Imperium-Knowledge/designs/instructions/生成具象规格-现行版.md` L85-88,
R-1028-1818; `Imperium-Knowledge/09_地图生成与CBF技术.md` L503). This is done on the temporary grid before rock is placed
(`Imperium-Knowledge/designs/ICF/ICF设计.md` L113, L118). Prevention comes first: a site with fewer problem stretches
scores higher, protruding parts of the urban area narrower than 8 cells are cut out to the outside, and when the net
area then falls short of the site requirements the next candidate is used
(`Imperium-Knowledge/designs/instructions/生成第2轮重做-第一段批准与第二段补充.md` L139-146).

## Judging the results

Settlement generation is a high-priority, heavyweight system. Each of the four styles is to reach at least 90% of the
features of the design atlas on the landforms that suit it, scored by the feature checklist. Roman work has three
stages: the first (components and loopholes) goes to 0.9; the second (wall lines and outer layering) and the third
(buildings and facilities) each need only 0.8 to move on; at layout tuning the fixed examples reach 0.9 as a whole. A
fallback for lack of a suitable landform, terrain changed by other mods and a map smaller than the minimum are only
recorded (`Imperium-Knowledge/designs/instructions/生成具象规格-现行版.md` L37-41, R-1029-0849;
`Imperium-Knowledge/09_地图生成与CBF技术.md` L325-329, R-1027-1703). Cases on difficult terrain are scored and recorded too but
do not hold back progress (`Imperium-Knowledge/09_地图生成与CBF技术.md` L329).

Correctness items are not scored and pass in every fixed example: the wall ring is closed, rivers included; towers and
gates are reachable; with all switches off the result equals the baseline; the fixed examples' own items hold (agreement
with the world tile, a road from every gate edge to the map edge, no closed dead zone outside, a fallback to base-game
terrain when the landform fails); there are no errors; and a fault rolls back completely
(`Imperium-Knowledge/designs/instructions/生成具象规格-现行版.md` L97-107). Each example measures only three items where they
apply: wall closure, tower reachability and empty ground (the Roman built-up area at most 0.15 empty, the medieval area
inside the wall at most 0.20). Defenders on the wall are measured once, at tuning, with one Roman and one medieval
example: after one game hour of siege, at least 0.5 of the garrison stands in the shooting gallery or the towers
(inferred, 推), and shooting through the loopholes is seen (`Imperium-Knowledge/designs/instructions/生成具象规格-现行版.md`
L108-109; `Imperium-Knowledge/09_地图生成与CBF技术.md` L331-332). Every other feature is scored by looking: 1 when present, 0.5
when partial and 0 when absent, averaged over the examples, and the user's view of a picture overrides the score
(`Imperium-Knowledge/designs/instructions/生成具象规格-现行版.md` L110-115).

Testing outside the game turns the planning input into a pure data grid, outputs the layout as JSON and compares
snapshots of the same input, as regression only and not replacing the in-game acceptance; whether the game assemblies
can be referenced without starting Unity is for Code to verify first, and if not, the existing planonly comparison is
kept; inside the game, the stages are shown as overlays (`Imperium-Knowledge/designs/ICF/ICF设计.md` L136-141).

## Borrowed work and its retirement

The route decided on 25 October is to implement the mechanisms CBF confirmed independently, in Imperium's own data
structures and algorithms; decompiled code serves only to compare behaviour and is not copied into the source, and the
shipped mod depends on neither the CBF assembly nor MO (`Imperium-Knowledge/09_地图生成与CBF技术.md` L80;
`Imperium-Knowledge/现行/流程/借用与第三方.md` L81).

> [!NOTE]
> **Deleted**: the line on which the generator was built on Imperium's transcription of CBF's pipeline (grouping, shared
> walls, Annex, Ward expansion, the interface of wall-line templates) (`Imperium-Knowledge/09_地图生成与CBF技术.md` L141).
> It was replaced by Mantle as the
> backbone of generation, with CBF only an early reference whose transcriptions and derived templates retire
> (`Imperium-Knowledge/01_项目宪章与规范索引.md` L185, R-1029-2020; `Imperium-Knowledge/09_地图生成与CBF技术.md` L868;
> `RimWorld-Imperium/docs/claude/ref-生成批次规则.md` L12).

From a summary of CBF that was submitted for research, CBF forms settlements through complete templates, legal shared
walls, entrances really connected to roads, expansion region by region, Annex and local rollback, rather than a global
optimum. What follows for Imperium: scoring cannot invent the content a complete template lacks; a shared wall is a
question of legality (structure, wall segment, normal, forbidden sharing, final ownership of the entity), not only of
distance; a candidate is accepted only with a workable entrance; new buildings join an existing spatial structure; an
Annex needs an explicit relation of connection or occupation; and a rejected expansion undoes its own reservations and
content without destroying the layout (`Imperium-Knowledge/09_地图生成与CBF技术.md` L53-64).

Four defaults hold. A physical shared wall is one wall entity that the buildings on both sides reference; structure,
normal, forbidden sharing, door and window conflicts and entity compatibility are checked before scoring, a local
rollback removes only wall segments no valid member still references, and no double wall overlaps. A required Anchor or
Annex follows the template author's own marks, unmarked ones are optional, and necessity is never raised or lowered on
its own. Optional interface fields such as `<spatialInterfaces>` and `<composition>` may be added to building templates,
and leaving them out equals the current behaviour. VEF and ReBuild are only test dependencies of the isolated 4985
environment, not in the release list and not asked of players, and making them player dependencies needs a separate
approval (`Imperium-Knowledge/09_地图生成与CBF技术.md` L82-89; `RimWorld-Imperium/docs/claude/ref-生成批次规则.md` L12-16). ReBuild's
switches stay off in the official release, and once the mod's own components are made, they replace its pieces as a
whole, one for one, by a mapping table (`Imperium-Knowledge/裁定归档/2026-10.md` L113;
`RimWorld-Imperium/docs/claude/ref-基线与回归.md` L51).

The templates converted from CBF are temporary placeholders, replaced step by step with Imperium's own
(`Imperium-Knowledge/09_地图生成与CBF技术.md` L336). The ones left are the medieval method for fields, the gatehouse
model, the camp master for commissions and the tribal camp
(`Imperium-Knowledge/01_项目宪章与规范索引.md` L185; `Imperium-Knowledge/designs/instructions/生成具象规格-现行版.md`
L43-46). Roman cities use only spec cards (`Imperium-Knowledge/designs/instructions/生成具象规格-现行版.md` L47, R-1028-0715).
All of CBF's house templates are replaced with the mod's own; the medieval, modern and tribal styles do this when each is
made, and CBF's house templates then retire in that style
(`Imperium-Knowledge/designs/instructions/生成具象规格-现行版.md` L48; `Imperium-Knowledge/09_地图生成与CBF技术.md` L429).
House templates follow the building template atlas and keep the originals' irregular outlines and notched corners,
adjusted on the originals, with Roman houses as spec cards; only the list in use, the automatic check scripts and the
list of placeholder objects are kept (`Imperium-Knowledge/09_地图生成与CBF技术.md` L448, R-1028-0707).

> [!NOTE]
> **Deleted**: the line of houses assembled from room modules: hand-designed rooms (bedroom, kitchen, workshop, shop,
> courtyard, colonnade, small church and so on) put together into whole buildings by each style's rules, then a set of
> 37 Roman, 45 medieval and 58 modern types assembled by the generator (`Imperium-Knowledge/09_地图生成与CBF技术.md` L429,
> L446; `Imperium-Knowledge/designs/instructions/生成具象规格-现行版.md` L48). It was voided because the rectangular houses
> the generator assembled were unusable, and house templates were set to follow the atlas
> (`Imperium-Knowledge/09_地图生成与CBF技术.md` L448, R-1028-0707).

When Mantle is finished, the names CBF and GL no longer appear in the current cards, the code or the mod's content
(Defs, assembly names, interface text), and the closing acceptance counts them at zero; until then GL-derived code and
landforms are replaced one by one, and the attribution and LICENSE that the licence asks for stay where replacement is
not complete. Ledgers and histories are records and are not changed (`Imperium-Knowledge/09_地图生成与CBF技术.md` L868;
`Imperium-Knowledge/现行/流程/借用与第三方.md` L68). After the move into Mantle, nothing unrelated to the project stays in the
knowledge base, the source or the evidence: transcriptions of CBF and MO, decompiled comparisons, derived templates and
their directory and ledger names retire and are archived, and the title of the generation document and names such as
`research/cbf/` change too (`Imperium-Knowledge/01_项目宪章与规范索引.md` L185; `Imperium-Knowledge/现行/流程/借用与第三方.md` L86;
`Imperium-Knowledge/designs/整理/整理记录-2026-11-02.md` L71-72; `Imperium-Knowledge/designs/做法史/生成引擎与 ICF.md` L12-17).

## Where the work stands

Mantle is built after Rank II is done, in parallel with the Empire's face
(`Imperium-Knowledge/designs/ICF/ICF设计.md` L21; `Imperium-Knowledge/裁定归档/2026-10.md` L116). City building goes on
until its framework is complete, then turns to filling in content, and Mantle is built after that and patched later; the
framework counts as complete when the flow from tracing a reference through district spectra, arrangement and scaling to
the map runs end to end with tools, when two different reference cities have gone through it without new tools for the
second, and when one district spectrum laid on two different pieces of ground gives results that differ yet both read
as Roman (`Imperium-Knowledge/09_地图生成与CBF技术.md` L922, R-1112-1312). The existing generation moves into the layers
after Rank II in six segments: the move itself, L0 and L1, L2, random sub-streams, the kits, and tools with the
clean-up; each segment except those allowed to differ gives the same result as the one before for the same input and
seed, loads old saves and starts without errors when ReBuild is not loaded
(`Imperium-Knowledge/designs/ICF/ICF设计.md` L143-155).

From the third round of generation only Rome is made (City, Castellum, Fortlet, Burgus), and the fixed examples are
Roman only; the medieval, modern and tribal styles are designed and implemented each on its own, in an order not yet
set; the medieval second-section rewrite and the medieval wall are postponed; and milestone 1 is "a Roman city can enter
the game" (`Imperium-Knowledge/09_地图生成与CBF技术.md` L577, R-1029-1307;
`Imperium-Knowledge/designs/instructions/生成具象规格-现行版.md` L42). The third round implements only the Roman kit, with the
interfaces written for all (`Imperium-Knowledge/09_地图生成与CBF技术.md` L579). Rank II's mechanoid content, the promotion from
rank I to II included, waits until all four styles reach 90% (`Imperium-Knowledge/09_地图生成与CBF技术.md` L335, R-1027-1923).

> [!NOTE]
> **Unverified**: the sources do not say whether Rank II still waits for all four styles after the work turned to Rome
> alone and the medieval, modern and tribal lines were paused, or whether this was only not restated
> (`Imperium-Knowledge/09_地图生成与CBF技术.md` L577; `Imperium-Knowledge/14_来源同步与权威.md` L141).
