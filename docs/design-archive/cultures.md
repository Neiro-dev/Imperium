# Settlements of other cultures

This section covers the settlements Imperium generates for factions other than the Empire: which style serves which
faction, what these styles share with the Empire's city building and where they part from it, the lifeline of each, the
medieval town with its walls, buildings and spec cards, the tribal camps and villages, the modern towns, entering a
settlement to trade, and where the work stands. The Empire's own cities are in cities.md and the cities-*.md files
(cities-siting.md, cities-walls.md, cities-inside.md, cities-outside.md, cities-forms.md); the framework that generates
all settlements, its terrain, its siting stage and how results are scored are in mantle.md; the names are in terms.md.

## Which style serves which faction

The Roman style is for the Empire alone. The medieval style (中世纪) is compatibility content for factions of the medieval
tech level, mod factions included. Factions of the industrial tech level default to the modern style (现代; the kit
Modern), and the modern style also serves for now as the common style of every faction not designed on its own. Templates
for each faction come later, and the pirates are to be studied as a group of their own
(`Imperium-Knowledge/designs/待用/建筑模板图册-2026-10-27.md` L10-14; `Imperium-Knowledge/09_地图生成与CBF技术.md` L293,
R-1027-10; `Imperium-Knowledge/11_开发进度与未决事项.md` L54; `docs/glossary.md` L191). For those later plans the source
names references: an outlander civilisation as a medieval town or modern, rough outlanders as a frontier stockade, pirates
as scrap fencing and tribes as stockade and moat (`Imperium-Knowledge/11_开发进度与未决事项.md` L54).

> [!NOTE]
> **Base game**: in 1.7 with all DLCs, the factions with bases are seven neolithic ones (gentle, fierce and savage
> tribes, a cannibal tribe, a nudist tribe, a Neanderthal fierce tribe, an impid savage tribe), three industrial ones
> (the civil and the rough outlander unions, the pig rough union), four pirate factions of the spacer tech level (pirate
> gang, cannibal pirates, wasteland pirates, Yttakin pirates) and the Empire; Odyssey's traders' guild and scavengers
> appear only in orbit; to be checked against `Data/` (`Imperium-Knowledge/11_开发进度与未决事项.md` L54).

Tribal (neolithic) settlements are converted from Medieval Overhaul's tribal camp, `CBF_Plan_TribalCamp`, the only
neolithic base in CBF; its 25 templates were turned into base-game pieces in the atlas file `tribal_cbf.json`. They are
compatibility content and kept as they are for now (`Imperium-Knowledge/09_地图生成与CBF技术.md` L294, R-1027-11;
`Imperium-Knowledge/11_开发进度与未决事项.md` L54; `Imperium-Knowledge/designs/待用/建筑模板图册-2026-10-27.md` L15,
L147-149).

For Medieval Overhaul the medieval round makes only an adaptation hook: when Medieval Overhaul is loaded, its medieval
factions are recognised and their settlements are generated with Imperium's own medieval kit, the lifeline following the
lord; its content, templates and names are not transcribed into the repository, and the VE series is not made compatible
(`Imperium-Knowledge/01_项目宪章与规范索引.md` L187, R-1030-0021b; `Imperium-Knowledge/现行/流程/借用与第三方.md` L92;
`Imperium-Knowledge/designs/做法史/借用与第三方.md` L41). Each faction having its own layout is the point borrowed from the
reference mods; one base map shared by several factions is not (`Imperium-Knowledge/designs/研究/参照模组/两模组对照.md`
L36).

> [!NOTE]
> **Unverified**: the settlement profile of each faction and a separate study of the pirates are still to be made
> (`Imperium-Knowledge/11_开发进度与未决事项.md` L54). How the tribal compatibility content is to be done later is left
> open, the Empire not being meant to make neolithic things (`Imperium-Knowledge/09_地图生成与CBF技术.md` L294;
> `Imperium-Knowledge/designs/待用/建筑模板图册-2026-10-27.md` L15).

## What they share with the Empire's cities

Rome is the mod's original content: an empire of industrial quality with appliances and machines, and none of the
pre-industrial things such as firewood, fireplaces, kilns or tilers. The medieval style is compatibility content
that borrows only the methods it has in common with Rome: walls built from components, the way spec cards are written,
the idea of growth pieces and CBF's methods of execution. The two are not one logic: Roman cards, rules and
instructions are checked for medieval objects, materials and ways of life, and the medieval style uses none of Rome's
appliances and machines (`Imperium-Knowledge/01_项目宪章与规范索引.md` L183). Neither presets the shape of its wall; the
medieval town grows ring by ring from its centre, and its wall wraps the last ring
(`Imperium-Knowledge/01_项目宪章与规范索引.md` L184).

The medieval, tribal, modern and other non-Roman factions in principle add only behaviour (generation, the lifeline,
what follows when its source is cut) and no new objects; Roman pieces that exist may be reused, and where Rome has none
the object is not used. The mod is of a DLC's kind, not a content pack: Royalty and Ideology changed how existing
factions behave and did not give each faction furniture. The tribal bonfire, for one, is the base game's piece and not a
new stone-ringed fire pit (`Imperium-Knowledge/01_项目宪章与规范索引.md` L188, R-1030-0025b).

All these settlements are generated by Mantle, each culture through its kit: Rome and the medieval town have kits now,
and modern, tribal and tent-camp kits come later (`Imperium-Knowledge/designs/ICF/ICF设计.md` L124-128;
`docs/glossary.md` L184). The skeleton is the base of a civilisation: the medieval skeleton is almost the same as the
Roman one that leans on hills, the modern one may divide by faction, and the five tribal terrains share one idea
(`Imperium-Knowledge/09_地图生成与CBF技术.md` L779, R-1029-1400a). Rome and the modern town are planned types, drawn first
and built after, with straight lines, the modern town carried by electricity; the medieval town and the tribal
settlement are growth types, used first and enclosed after, following the terrain, the medieval town growing along
its roads and the tribe around its fire (`Imperium-Knowledge/designs/ICF/聚落平面语法-v4.md` L108;
`Imperium-Knowledge/09_地图生成与CBF技术.md` L634, R-1029-1818). Set side by side, the medieval town has a road bending
with the terrain as its axis, a market at a node of the road as its centre, and a wall along the edge of what is built
that climbs onto mountains; the modern town has highway and branch roads, its centre at a crossroads or inside its ring,
no wall but checkpoints, and levelled ground; the tribal settlement has no axis but a ring, the great campfire at its
centre, a stockade and ditch only on the open side, and it does not change the terrain
(`Imperium-Knowledge/09_地图生成与CBF技术.md` L634).

> [!NOTE]
> **Deleted**: Rome's water power, and Rome as a planned type carried by water, belonged to the hydraulics the maintainer
> deleted (`Imperium-Knowledge/01_项目宪章与规范索引.md` L183; `Imperium-Knowledge/designs/ICF/聚落平面语法-v4.md` L108;
> `Imperium-Knowledge/09_地图生成与CBF技术.md` L634).

The walls of Rome and of the medieval town follow Imperium's own logic, while their presentation borrows from CBF:
smoothing into long straights, towers counted by perimeter, straight wall beside gates, and component templates
(`Imperium-Knowledge/09_地图生成与CBF技术.md` L194-197). The generic terrain pieces (terrace edge, ramp, low railing,
steps, channel edge, retaining wall) take the skin of each faction: rough stone for the medieval town, steel for the
modern town and rammed earth for tribes (`Imperium-Knowledge/现行/流程/借用与第三方.md` L20).

The settlement design atlas has four series, Roman (R-*), medieval (M-*), modern (X-*) and tribal (T-*), each with small,
medium and large settlements and a plan of supporting facilities, twenty plans in all
(`Imperium-Knowledge/designs/聚落设计图/README.md` L8; `Imperium-Knowledge/designs/聚落设计图集.md` L20;
`Imperium-Knowledge/目录/美术.md` L21-35). Each plan has three columns (key parameters, the numbers on the plan, a legend);
the numbers match white circles on the plan, and loopholes and arrow slits are drawn as wall cells with a black line for
the direction of fire (`Imperium-Knowledge/designs/聚落设计图/README.md` L12). The generation spec has a part for each
style: medieval compatibility content (village, market town, fortress city), modern (no city wall; crossroads village,
main-street town, ring-road city) and tribal neolithic compatibility content (river-bank long-row camp, longhouse
stockade, cliff village, with the ring and family-compound villages only sketched in `T-F`)
(`Imperium-Knowledge/目录/规格.md` L7-49). Its values carry three markings: decided ([定]); atlas values, which are
adjustable targets ([图]); and defaults added for checking, which are adjustable ([推]); the user's view of the pictures
overrides the [图] and [推] values. The current round's instruction ranks first, the city plan data and approved sketches
second and the atlas third (`Imperium-Knowledge/designs/instructions/生成具象规格-现行版.md` L15-31).

For each example three items are measured (wall ring closed, towers reachable, empty ground), applied by style: the
medieval town measures empty ground inside the wall at no more than 0.20; the modern town builds no wall, so the three
items do not apply and the picture is scored against the feature list; and the tribal settlement measures whether its
stockade is closed and its entrance. The other rules are followed without measuring each number
(`Imperium-Knowledge/designs/instructions/生成具象规格-现行版.md` L108, L618). The `Modern` fence, outer line, fire points,
bunkers, mortars and inner stronghold are already superseded by the modern and tribal rules and are changed when those
styles are made; the parameters of the forward-position commission (`Modern_ForwardPosition`: fire points, mortars,
landing zone, flipped trenches and so on) are left to the later M3 batch of fine adaptation of commissions
(`Imperium-Knowledge/designs/instructions/生成具象规格-现行版.md` L687-688).

## Lifelines

Each faction fills one lifeline (命脉线) on the same skeleton of source, trunk, the places where it shows, and exit
(`Imperium-Knowledge/designs/ICF/聚落平面语法-v4.md` L108). Mantle's general concept is in mantle.md.

> [!NOTE]
> **Deleted**: the first lifelines of these cultures: for the medieval town wells and a mill on the river, then the road
> from the gate through the market street to the market, the church forecourt and the inn and out at the opposite gate,
> a blocked road leaving the market without goods; for the tribe hearth and river, then fire alone, from the great fire
> along paths to the family hearths, cutting it leaving the camp cold and dark
> (`Imperium-Knowledge/09_地图生成与CBF技术.md` L579, L633). They were replaced by the lord and by the fire with its
> chieftain (`Imperium-Knowledge/09_地图生成与CBF技术.md` L665-666, R-1030-0021, R-1030-0025).

> [!NOTE]
> **Deleted**: the contrast of the medieval and tribal lifelines with Rome, whose city stops only when its water is cut
> while its people fight on, rested on the Roman lifeline of water, which belonged to the hydraulics the maintainer
> deleted (`Imperium-Knowledge/09_地图生成与CBF技术.md` L665-666).

The medieval lifeline is the lord (领主). The road shapes the town and nothing more: the town grows on the road, the
market sits at the road's nodes, houses line the road first and the wall comes last along the outer edge of what is
built. The lifeline and the cutting of its source go only through the lord: the source is the lord in the castle, the
trunk the main road from the castle down to the market and on to the gate, the places where it shows the market and the
forecourt of the church (flags, guards), and the exit the city gate. Taking the lord, by knocking down or capturing him,
makes the defending militia and guards flee or surrender, through the base game's mechanism for fleeing raiders with a
changed trigger and no new system. Blocking the road does not cut the source, and there are no trade consequences on
the world layer (`Imperium-Knowledge/09_地图生成与CBF技术.md` L665, R-1030-0021;
`Imperium-Knowledge/designs/ICF/聚落平面语法-v4.md` L118; `Imperium-Knowledge/现行/索引.md` L1374-1375). Where the road
runs is set by the terrain: the entry segment of a world
road where there is one, otherwise the line of least effort between the two most natural entrances, with the market at a
node such as a ford, a crossing, the foot of a slope or a spring (`Imperium-Knowledge/designs/ICF/聚落平面语法-v4.md`
L118). A medieval town hangs on one person, so taking its lord is how it falls; the details come in the medieval round
(`Imperium-Knowledge/09_地图生成与CBF技术.md` L665).

The tribal lifeline is the great fire with the chieftain as a second guarantee. One great fire stands in the middle of
the camp, made for now of base-game pieces with no new object, and the chieftain stays by it. If the fire stands and the
chieftain falls, another becomes chieftain and returns to the fire, and the tribe fights on; if the fire is out and the
chieftain lives, the tribe does not break up; if the fire is out and the chieftain has fallen, the tribe flees, through
the base game's logic for a defending leader with a switching condition, the same code as the medieval lord. Cutting the
source thus scatters the tribe rather than leaving it cold and dark (`Imperium-Knowledge/09_地图生成与CBF技术.md` L666,
R-1030-0025; `Imperium-Knowledge/designs/做法史/现代与部落.md` L16). The line runs from the great fire along paths to each
family's hearth, to the hearths and torches, with no exit; the tents ring the fire, and a river decides only where the
camp stands (`Imperium-Knowledge/designs/ICF/聚落平面语法-v4.md` L119). A fire alone would be too fragile on open ground,
where one grenade destroys it; so the tribe is harder to scatter than the medieval town, which falls through one person,
since it scatters only when both the fire and its keeper are taken (`Imperium-Knowledge/09_地图生成与CBF技术.md` L666).

The modern lifeline is electricity: generator, wires, then lights, turrets and workshops, with no exit. The base game's
power network is used unchanged, and the lifeline only decides where things stand; cutting the source is a blackout
(`Imperium-Knowledge/designs/ICF/聚落平面语法-v4.md` L117; `Imperium-Knowledge/09_地图生成与CBF技术.md` L633).

## Medieval settlements

### A town that grows

The medieval town grows. It does not follow the Roman method, in which the street net comes first and plots are cut along
it, the logic of a planned city. It grows as CBF's towns do: the centre is placed first and houses outward from it, each
house finds a road to its door or pulls a lane, and the wall is wrapped round what has been built last. Medieval
Overhaul's plan sets the rules, the building lists and the counts, and the community screenshots
`Imperium-Knowledge/designs/聚落设计图/地形模板草图/社区参考-1.png` and
`Imperium-Knowledge/designs/聚落设计图/地形模板草图/社区参考-2.png` set the look. Paths in the open are not straightened:
gate roads and the tracks to farms and mills bend with the terrain. The history drawn on is the burgage plot (front house,
back yard, garden and shed in one strip per household), the suburb along the road outside the gates, the gate at the
bridgehead and the mill by the river (`Imperium-Knowledge/designs/medieval-cards/中世纪集镇试做-已定与依据.md` L8-12).
Its outline is not square but natural: it follows coast, river bank and rock edge, its wall runs along those edges, it may
cross a river with bridges joining its parts, what is built reaches the water, and a mountain serves as wall
(`Imperium-Knowledge/09_地图生成与CBF技术.md` L425, R-1028-0041).

The medieval town seeks defensible places: a river bend, a peninsula, a ridge, the foot of a lone hill, a cliff edge. Its
castle or cathedral takes the highest point, its outline is pushed out by what is built and may be a long strip or
irregular, it may cross a river in parts, and where it touches a mountain the mountain is its wall; small hills are kept
for a castle or holding point (`Imperium-Knowledge/09_地图生成与CBF技术.md` L459, R-1028-0826). The river stays as it is
(`Imperium-Knowledge/09_地图生成与CBF技术.md` L460). The town removes only small pieces of terrain that nearly fit, within
5% of its area: stray rock, small puddles and thin teeth of rock; it does not remove the main mass, level hills, fill
lakes or make terraces, and where pieces are removed the ground outside is lowered within 8 to 12 cells so that the rock
edge recedes naturally (`Imperium-Knowledge/designs/instructions/生成第2轮重做-第一段批准与第二段补充.md` L128-137;
`Imperium-Knowledge/designs/instructions/生成具象规格-现行版.md` L84; `Imperium-Knowledge/09_地图生成与CBF技术.md` L506).
Rock beyond that 5% is passed round by the outline, leaving no holes in the town
(`Imperium-Knowledge/09_地图生成与CBF技术.md` L465). On hill tiles a stretch of mountain serves directly as the wall
(`Imperium-Knowledge/designs/instructions/生成具象规格-现行版.md` L491).

The outline (城区轮廓) of the medieval town is the thin ring of the second stage, as in the samples R1 and S49: its edge
keeps close to the feet of slopes and to shores, grown by the same method as Rome's with parameters by grade, and it is
written into a card when the medieval work starts (`Imperium-Knowledge/09_地图生成与CBF技术.md` L812, R-1110-1238b;
`Imperium-Knowledge/09_地图生成与CBF技术.md` L819, R-1110-1308a; `Imperium-Knowledge/designs/做法史/中世纪.md` L20-22)
(replaces `Imperium-Knowledge/09_地图生成与CBF技术.md` L817, the wall that hugs the ring). Its references are the images
`Imperium-Knowledge/designs/city-plans/第二段-R1-Medieval-L-Terrain-map300.png`,
`Imperium-Knowledge/designs/city-plans/第二段-S49-MM-River-map250.png` and
`Imperium-Knowledge/designs/city-plans/图三-配合地形的城区.png` (`Imperium-Knowledge/09_地图生成与CBF技术.md` L807,
R-1110-1027), and the left image of `Imperium-Knowledge/designs/回报/Code-第二段轮廓-校准与核心/校准-R1-第四轮.png`
(`Imperium-Knowledge/09_地图生成与CBF技术.md` L818-819).

> [!NOTE]
> **Unverified**: the images R1, S49 and image three are accepted as references, but how they are to be read is left
> for the user to confirm (`Imperium-Knowledge/09_地图生成与CBF技术.md` L807).

> [!NOTE]
> **Deleted**: the medieval part of the second round of generation: anchors for the bridge site and the bridge gate, the
> site of church or castle on high ground or by rock, the field zone and the stretches the town leans on, and the
> fortress city's net area cut from 23,000 to 16,000 cells with its field zone and inner ring
> (`Imperium-Knowledge/designs/instructions/生成第2轮重做-第一段批准与第二段补充.md` L59-61, L203-209, L642). It was
> replaced when the third round turned to Rome alone and the fixed examples became Roman only
> (`Imperium-Knowledge/designs/instructions/生成第2轮重做-第一段批准与第二段补充.md` L315, R-1029-1307).

### Layers, centre and streets

Medieval Overhaul's plan, taken from the CBF fortress-city sample `CBF_Plan_FortressCity_New`, grows the town in three
layers. Layer 1 is the centre and castle: a keep of 22×20, 2 barracks, an armoury, a vault, 1-3 noble houses, a
guildhall, a tavern, a church, a smithy, 1-3 workshops and a monument, with 6-14 burgher houses and 0-6 small yards as
filler. Layer 2 is houses and workshops: 28-36 commoner houses as filler, with a tavern, 1-2 storehouses, a bakery, a
tailor, a smithy, a kitchen hut and 0-2 places of entertainment. Layer 3 lies outside the town: 1-2 farmsteads, a mill,
a pasture with barn and hut, a graveyard, 2-3 huts at the edge, a winery and a hunting lodge. Medieval Overhaul puts the
graveyard in layer 3, while Imperium puts it inside the town beside the church. Its built-up target is 0.62 inside and
0.32 in the suburb, and commoner and burgher houses may join into blocks with shared walls. The sample has no plan for
the market town or the village; the market town's list was set from layer 2 and the generation spec's 2.2, awaiting a
check by Code against CBF itself (`Imperium-Knowledge/designs/medieval-cards/中世纪集镇试做-已定与依据.md` L15-24). In the community
pictures, houses are blocks of halls with several rooms set tightly in rows, the gaps between them are streets paved
with stone, the centre is a square paved plaza, the keep is symmetrical with corner towers and is the most conspicuous
building, the walls step along hills and rivers, and what is built reaches the water's edge
(`Imperium-Knowledge/designs/medieval-cards/中世纪集镇试做-已定与依据.md` L26).

The core of the medieval town is its castle or church; its open spaces are the market and the space before the church;
its axis is the road from the gate to the market and on to the castle
(`Imperium-Knowledge/designs/ICF/聚落平面语法-v4.md` L56, L65, L97). Its boundary is a solid wall
(`Imperium-Knowledge/designs/ICF/聚落平面语法-v4.md` L143).

Streets are graded, paved and bend with the terrain: the main street is 3 wide, branches and lanes 2; they are paved
with stone slab or gravel, the main street differing from branches and lanes and all from the colour of the ground; dirt
roads are used only for the roads outside the gates and the paths outside the town
(`Imperium-Knowledge/designs/instructions/生成具象规格-现行版.md` L481-484). The medieval town has no ring passage around the
city (`Imperium-Knowledge/designs/instructions/生成具象规格-现行版.md` L533).

### Walls, towers and gates

The medieval wall follows Imperium's own logic with CBF's presentation
(`Imperium-Knowledge/09_地图生成与CBF技术.md` L194-197). It grows: the village or town grows first, and the wall then
wraps the outer edge of its groups and is smoothed by the rules of the wall batch, rounded overall and using only
horizontal, vertical and 45° lines (`Imperium-Knowledge/designs/instructions/生成具象规格-现行版.md` L473, L747;
`Imperium-Knowledge/09_地图生成与CBF技术.md` L151, L235; `Imperium-Knowledge/designs/聚落设计图/README.md` L41). The
outline may have right angles, and diagonal edges appear only
where it follows a mountain or water, as steps (`Imperium-Knowledge/designs/instructions/生成具象规格-现行版.md` L477;
`Imperium-Knowledge/designs/instructions/生成第2轮重做-第一段批准与第二段补充.md` L280). Only the large tier has two
rings, and its outer ring is always a fully closed ring (`Imperium-Knowledge/09_地图生成与CBF技术.md` L198;
`Imperium-Knowledge/designs/instructions/生成具象规格-现行版.md` L527) (replaces the outer ring of two kinds on the
plan, `Imperium-Knowledge/designs/聚落设计图/README.md` L6). The village and market town never have parallel double
walls (`Imperium-Knowledge/designs/instructions/生成具象规格-现行版.md` L536).

> [!NOTE]
> **Deleted**: the first line for the medieval wall, in which the walls of village, market town and fortress city
> reproduced CBF's Village, Market Town and Fortress City (`Imperium-Knowledge/09_地图生成与CBF技术.md` L138), was replaced
> by Imperium's own wall logic with CBF's presentation (`Imperium-Knowledge/09_地图生成与CBF技术.md` L194-197,
> R-1027-02).

The towers follow CBF's square and round towers: the village after `PalisadeTower` 5×5 or 7×7, the market town after
`TownTower` 7×7 or 9×9, the fortress city after `FortressTower` 9×9, converted into Imperium's own template Defs with
materials and furnishing by Imperium's profiles (配置档) (`Imperium-Knowledge/designs/instructions/生成具象规格-现行版.md` L474-475;
`Imperium-Knowledge/09_地图生成与CBF技术.md` L213, R-1027-03). A tower is a room with a door, never an empty frame, and corner
towers are larger than towers in the middle of a wall (`Imperium-Knowledge/designs/instructions/生成具象规格-现行版.md` L476).
The corner is the weakest place of a town, so every outward corner of a walled stretch takes a corner tower that
projects beyond the wall and is one size larger than the middle towers, mostly round and sometimes square: in the
village 7 at a corner and 5 in the middle, in the market town 9 and 7, in the fortress city 11 (its own round tower, a
default for checking) and 9 (`Imperium-Knowledge/designs/instructions/生成具象规格-现行版.md` L477;
`Imperium-Knowledge/designs/instructions/生成第2轮重做-第一段批准与第二段补充.md` L278-280). The wall carries no wall armour, no plasteel
and no gun platforms (`Imperium-Knowledge/designs/instructions/生成具象规格-现行版.md` L479;
`Imperium-Knowledge/designs/聚落设计图/README.md` L13, L42). Its arrow slits are the same loophole wall segment as Rome's, in
medieval stone: one every 4 cells on the outer line where the wall has a walkway, and on the fronts, sides and corners
of towers (`Imperium-Knowledge/designs/聚落设计图/README.md` L43; `Imperium-Knowledge/designs/instructions/生成具象规格-现行版.md`
L740-741).

Towers are counted by the formula max(4, corners + wall-axis cells ÷ max(tower side + 4, 12)), corners first and middle
towers after, and the numbers on the plans are only a reference; the village has at least 4 towers
(`Imperium-Knowledge/designs/instructions/生成具象规格-现行版.md` L478, L502;
`Imperium-Knowledge/designs/聚落设计图/README.md` L6). The unstored rewrite of this section would change the count and
the rounding; it is given under its own heading below.

A gate is a gatehouse that straddles the gateway: the passage runs through its middle with a door at front and back and
small paved rooms on either side, not two towers flanking a gate
(`Imperium-Knowledge/designs/instructions/生成具象规格-现行版.md` L480). The village has 1-2 gates, the market town 3-4, the
fortress city 3-4 in its outer ring and at most 2 in its inner ring; they are opened according to the routes of
approach, with no symmetry presupposed (`Imperium-Knowledge/designs/instructions/生成具象规格-现行版.md` L493, L689-691;
`Imperium-Knowledge/11_开发进度与未决事项.md` L33). A gate stands at the bridgehead
(`Imperium-Knowledge/designs/ICF/聚落平面语法-v4.md` L215; `Imperium-Knowledge/designs/medieval-cards/中世纪集镇试做-已定与依据.md` L12).

### The three sizes

The village (村庄, MV; plan `Imperium-Knowledge/designs/聚落设计图/M-S.png`) has a wall of rough stone, `RB_RusticWall`, one
cell thick in dark stone, with no arrow slits in the wall itself, only in the towers, and no moat. Inside it measures
about 64×66 with 10 corners, as an atlas target. A palisade gatehouse, 5×9 in the atlas, stands at each end of the
village road, which passes through its middle. Its towers are 5×5 or 7×7 with slits at front and sides. The main village
road is 3 wide, paved, and winds through the whole village, joining dirt roads beyond the gates. The church `Church_A`
(14×15) has its graveyard right beside it; in the atlas a tavern of 17×14, a smithy of 12×9 and houses of 9×8, 8×9 and
10×9 line both sides of the road in rows with shared walls; leftover blocks of at least 40 cells get plantable soil, a
default for checking. Outside, in the atlas a sawmill stands by a stream, or at the forest edge where there is none, and
there is one animal pen; its fields follow `Village_New` (`Imperium-Knowledge/designs/instructions/生成具象规格-现行版.md`
L495-507)

The market town (集镇, MM; plan `Imperium-Knowledge/designs/聚落设计图/M-M.png`) has a wall of 1×3, wall, walkway and wall,
with the walkway paved in stone and a stone slit every 4 cells on the outer line. Inside it measures about 90×86 with 13
corners, as an atlas target. It has 3-4 gates, gatehouses after CBF's `Gatehouse` from 5×11 to 9×17 (9×13 in the atlas).
Its corner towers are 9×9 and its middle towers 7×7, with slits at front and sides; CBF's measured tower spacing is a
reference for the look, not a hard target. Its moat lies tight against the foot of the wall, 1-2 cells away, of shallow
water near water and of mud otherwise, with an earth bridge left before each gate; the moat is 3 wide in the atlas. Main
streets 3 wide wind from each gate to the market square, and branches and lanes are 2 wide. In the atlas the market
square is an irregular polygon of about 22×14 in the centre; the church has its graveyard right beside it; in the atlas
a tavern of 17×14 opens on the square, there is a storehouse hall of 16×11, and houses stand in rows with shared walls
along the streets (`Imperium-Knowledge/designs/instructions/生成具象规格-现行版.md` L509-521)

The fortress city (要塞城, ML; plan `Imperium-Knowledge/designs/聚落设计图/M-L.png`) has two rings: the old inner town grows
compact first, and the outer ring grows from the suburb outside the inner gates. The outer ring is closed and lies at
least 8 cells from the inner one by default; about 84×62 inside and 156×148 outside in the atlas. Its outer wall is 1×5,
laid out after CBF's `TownWall_1x5`, the inner 1×3, each with a slit every 4 cells on the outer line. The outer ring has
3-4 gates after CBF's `FortressGate` from 9×13 to 15×17, and the main gate has an outwork (外堡), 15×15 with a gateway 3
wide in the atlas; the inner ring has at most 2 gates, 7×11 in the atlas. Its towers follow `FortressTower` 9×9, with
projecting round corner towers of 11 cells, its own and a default for checking; the atlas draws the inner ring with 7×7
square towers where the instruction asks for 9×9. The moat lies tight against the foot of the outer wall, 4 wide in the
atlas. In the atlas the inner ring (the old town) has two main streets 3 wide crossing, a market square of 18×12, the
cathedral with its graveyard, the lord's hall of 13×12 with a vault of 11×10, and houses with shared walls; in the atlas
the outer ring (the suburb) has four main streets running from the outer gates to the inner gates, two barracks of 16×11
by the outer gates, two storehouse halls, workshops of 12×9 and 14×11 and houses for the rest
(`Imperium-Knowledge/designs/instructions/生成具象规格-现行版.md` L523-536). The outwork at the fortress city's main gate is
kept; that Roman cities have no outwork applies only to Rome (`Imperium-Knowledge/09_地图生成与CBF技术.md` L417, R-1027-2325;
`Imperium-Knowledge/designs/做法史/罗马城·墙外.md` L33-34).

The atlas draws the village at 136×124 cells, the market town at 196×176 with four gatehouses of 9×13 and square and
round towers mixed, and the fortress city at 250×236; the plan `Imperium-Knowledge/designs/聚落设计图/M-F.png` (150×104)
shows the three wall sections with stone arrow slits on the outer line, the gatehouse of each tier, and how five kinds of
tower are slit and where they fire (`Imperium-Knowledge/designs/聚落设计图/README.md` L47-52).

### Outside the walls

Outside the medieval town lies a suburb, with farmsteads along the road
(`Imperium-Knowledge/designs/instructions/生成具象规格-现行版.md` L485). The fields follow CBF's method directly, from
Medieval Overhaul's plan and a community template, with no design of Imperium's own. Farmsteads are Medieval Overhaul's
`Farmstead` and the community template `Bauernhof`, from 12×9 to 15×10, and each farmstead has a field of its own
(`PlaceFarmPlots`): the block is the farmstead's size grown by 10 cells, plus 0-16 cells at random on each axis, with a
30% chance of one axis doubled; its edge is drawn in by a sine of 0.8 to 2.4 cells and rounded, so the field is not a
block; it lies only on dry ground, not over walls, with at least 100 crop cells, and far fields lie 4-30 cells from their
farmstead. Where a road crosses a field its cells are removed; pieces at least 2 wide are kept, the largest and any of at
least max(30 cells, 20%); each piece holds one crop, and it is fenced with the fence gate on a fence cell next to the
road. The numbers follow Medieval Overhaul's plans: the village (`Village_New`) 2-4 farms, 2-3 mills, 1-2 vineyards and a
pasture; the market town (`MarketTown_New`) 3-4 farms, a mill, a vineyard and a pasture; the fortress city (`Fortress`)
2-3 farms and a pasture (`Imperium-Knowledge/designs/instructions/生成具象规格-现行版.md` L485-490;
`Imperium-Knowledge/09_地图生成与CBF技术.md` L416, R-1027-2314c). Imperium's path does not generate these fields yet;
they are to be transcribed into it (`Imperium-Knowledge/09_地图生成与CBF技术.md` L416).

The medieval town uses the same layering from outside to inside as the Roman city, set apart from it by its grown and
rounded wall line, CBF's square and round towers, a moat tight against the foot of the wall in the market town and
fortress city only, gate roads of earth that bend with the terrain, the graveyard inside the town beside the church, and
CBF's suburb content, which is kept (`Imperium-Knowledge/09_地图生成与CBF技术.md` L235, R-1027-05;
`Imperium-Knowledge/designs/ICF/聚落平面语法-v4.md` L269; `Imperium-Knowledge/designs/聚落设计图/README.md` L44).

> [!NOTE]
> **Deleted**: the strip fields of the medieval town, as the wall batch, the grammar and the plans give them, and the
> first idea of one fenced group of fields per farmstead (`Imperium-Knowledge/09_地图生成与CBF技术.md` L235, L416;
> `Imperium-Knowledge/designs/ICF/聚落平面语法-v4.md` L269; `Imperium-Knowledge/designs/聚落设计图/README.md` L44), were
> replaced by CBF's method of fields (`Imperium-Knowledge/09_地图生成与CBF技术.md` L416, R-1027-2314c;
> `Imperium-Knowledge/designs/聚落设计图/README.md` L6).

### Buildings and spec cards

The medieval cards start from the union of CBF's Medieval Overhaul set and the atlas's `CBF_Vanilla` medieval set,
taking the better one for each use and changing the original. Dwarf types, tent camps, slave pens, catapult positions and
gun positions are left out, the last two because the medieval town has no turrets
(`Imperium-Knowledge/designs/medieval-cards/中世纪规格卡通用规则.md` L6-8;
`Imperium-Knowledge/09_地图生成与CBF技术.md` L485-488). They are made by groups of use: low-priority originals are
removed first, one template is chosen in each group and the rest become its variants, each keeping its own outline and
changed by the template's rules (`Imperium-Knowledge/designs/medieval-cards/中世纪规格卡通用规则.md` L9-11). Their
recognition words (辨识词) are: the hall as core, one strip per household, irregular additions, and the landmark taking
shape (`Imperium-Knowledge/designs/medieval-cards/中世纪规格卡通用规则.md` L12). Three kinds of keyword serve them: the
style's recognition words, the tags by which the generator picks templates, and terms for searching the workshop
(`Imperium-Knowledge/09_地图生成与CBF技术.md` L485-488).

Each card is written as a core plus growth pieces (生长件), and a random number of growth pieces are added at generation:
at most 4 in a village, at most 2 in a market town or fortress city; the core alone already works, with door, bed and
hearth complete (`Imperium-Knowledge/designs/medieval-cards/中世纪规格卡通用规则.md` L13-15). Rooms complement each
other: they need not be square, one yields a corner for another to nest in, and another juts outward, as in real houses
with a hearth alcove projecting from the wall, a porch outside the front door, a lean-to beside the main house and a later
room nested into the yielded corner; two neighbouring buildings may interlock
(`Imperium-Knowledge/designs/medieval-cards/中世纪规格卡通用规则.md` L16-18). Outside, porch, small yard, pen and
vegetable strip layer outward, so a house does not touch bare open ground; kitchen plots seldom have fences, are small
stepped strips beside walls or water with a ring of dug soil, and a hut's plot is never larger than the hut
(`Imperium-Knowledge/designs/medieval-cards/中世纪规格卡通用规则.md` L19-20). Empty outside walls carry clutter, and
only outside: a run of at least 3 cells of outer wall with open ground beyond, more than 2 cells from doors and fence
gates, gets one item every 3 cells, chests, barrels and sacks as placeholders, and the base game's flower pots and wood
piles (`Imperium-Knowledge/designs/medieval-cards/中世纪规格卡通用规则.md` L21-23). Objects come from the base game or a
DLC, then ReBuild, then a placeholder; the fireplace is `RB_Fireplace`, and the well and the clutter start as placeholders
(`Imperium-Knowledge/designs/medieval-cards/中世纪规格卡通用规则.md` L24-26). Villages have rough stone outer walls and
wooden inner walls, market towns and fortress cities stone walls of the plot's stone; doors are always wooden; living
rooms have wooden floors and kitchens and sheds stone slab
(`Imperium-Knowledge/designs/medieval-cards/中世纪规格卡通用规则.md` L27-30). Every card carries seven labels: use, tier
(档位), size tier, city layer (Medieval Overhaul's layer 1, 2 or 3), door face, rotation and mirroring, and terrain
(`Imperium-Knowledge/designs/medieval-cards/中世纪规格卡通用规则.md` L31).

Non-Roman factions, the medieval style among them, in principle add only behaviour and no new objects; Roman pieces that
exist may be reused, and where Rome has none the object is not used (`Imperium-Knowledge/01_项目宪章与规范索引.md` L188,
R-1030-0025b) (replaces `Imperium-Knowledge/designs/medieval-cards/中世纪规格卡通用规则.md` L23, the mod's own components to
come).

The medieval style uses no electricity. Electric things are swapped for ones without power (an autodoor for a wooden
door, an electric light for a torch lamp, an electric stove for a fuelled one, an electric smithy for a fuelled one, an
electric tailoring bench for a hand one, a hi-tech research bench for a simple one) or removed (television, vitals
monitor, comms console, climate devices, multi-analyzer, sun lamp, hydroponics, orbital trade beacon, electric smelter,
electric crematorium, fabrication and machining benches, sandbags and barricades). Doors are all wooden; metal furniture
becomes wood and stone furniture stays; concrete, paving, metal and sterile tile floors become stone slab (`$STONE`).
Outer and inner walls are kept apart (`$EXTWALL`, `$INTWALL`), the outer walls being found as the cells joined to open
ground from the template's edge, and the church, the lord's hall and the tavern have ornate walls on their fronts
(`Imperium-Knowledge/designs/待用/建筑模板图册-2026-10-27.md` L102-114; `Imperium-Knowledge/09_地图生成与CBF技术.md` L167). The
medieval town therefore has no generator yard (`Imperium-Knowledge/09_地图生成与CBF技术.md` L138). Religious buildings are
generated only when Ideology is loaded, with a substitute layout when it is not (`Imperium-Knowledge/09_地图生成与CBF技术.md`
L168).

Cards are converted thus. Medieval Overhaul's objects are replaced by base-game or DLC ones, with placeholders where none
exists (armour statues, weapon racks, stalls, clutter, wells); the main hall of every building gets a door to the outside,
new if there was none; square buildings get hearth alcoves and lean-tos; tables without chairs get chairs; clutter goes on
empty outside walls; vegetable strips belong only to the farm group. Each group lists its growth pieces, attached at
generation up to the settlement's count. Labels are set automatically: the tier by group; the size tier by cell count
(small under 120, medium under 320, large above); the city layer from Medieval Overhaul's three lists; the door face from
the door nearest an edge; rotation and mirroring allowed; terrain flat, with ports at water and mines at a rock face
(`Imperium-Knowledge/designs/medieval-cards/中世纪规格卡总表.md` L20-37). In the house group three more small houses
became commoner variants of M-H2, the burgher variants are the rest plus nine large houses of the atlas, and five annex
pieces joined the library of growth pieces. In the other groups only two kinds were deleted, those nearly identical to an
original of the same type (outline overlap of 86% or more) and those too small (under 9 interior cells, unless open ground
or decoration; the boathouse kept as an exception). The template of each small group was chosen by room count, variety
of objects, irregularity of outline and size, except that the keep and the church are cards of their own by the word
"the landmark taking shape", and outpost templates become buildings rather than open ground
(`Imperium-Knowledge/designs/medieval-cards/中世纪规格卡总表.md` L4-25, approved 2026-10-28 21:50).

The groups and their tiers are: the houses (burgher, commoner and the annex library); castle and garrison, tier military
(军): keep and lord's hall (growth: corner towers, gatehouse, well in the inner court), barracks, armoury, vault, tourney
ground; nobles, guilds and clerks, tier rich (富): noble house, guild, scriptorium; religion and graves, tier religion:
church (sacristy, bell tower, the graveyard separate), shrine, graveyard (grave-keeper's hut), monuments; squares,
taverns and services, tier common (常): market square (stalls on market days), tavern, entertainment, street decoration,
shops, clinic; workshops, tier work (工): smith and smelting, tailor, food, wood and stone, leather and potions, brewery
and mill; storage, tier work; farming and gathering outside the town, tier common: farmstead, barn and pens, gatherers'
huts; the port, tier work; and outposts and quest sites, tier military, for quest locations and field camps only, not for
town generation. The centre's buildings belong to layer 1; houses, shops, workshops, shrines and storage to layer 2; and
farms, mills, harbours, outposts and the tourney ground to layer 3
(`Imperium-Knowledge/designs/medieval-cards/中世纪规格卡总表.md` L59-426; `Imperium-Knowledge/目录/规格卡.md` L37-53).
The group of city-wall fittings is deleted, since walls are generated from wall components; the infirmary `Hospital_A` is
deleted; the keep and church are cards of their own; and the watermill and cathedral are added
(`Imperium-Knowledge/designs/medieval-cards/中世纪规格卡总表.md` L52-57;
`Imperium-Knowledge/09_地图生成与CBF技术.md` L489-500).

The burgher variants of M-H1 stand in layer 2 (`Imperium-Knowledge/designs/medieval-cards/中世纪规格卡总表.md` L64-75,
approved 2026-10-28 21:50) (replaces `Imperium-Knowledge/designs/medieval-cards/M-H1.md` L45, the label layer 1).

The burgher house (市民宅) M-H1 is a template card in its final, growth form. Its outline is irregular, since the houses of
a community are almost never regular figures and filler houses carry layers of garden outside
(`Imperium-Knowledge/designs/medieval-cards/M-H1.md` L4-6). Its core is the hall and the bedroom: the hall on the
street, the bedroom set 2 cells back, one yielding and one jutting. Its growth pieces are a kitchen wing south of the
hall, offset and sharing a wall with the bedroom (fuelled stove, shelves, butchering spot, lamp; one door to the hall
and one to the back yard); an open back yard east of the kitchen wing with a wood pile and well; a lean-to outside the
hall's east wall, 1 cell back, with two shelves and a door to the hall; and a vegetable garden of 9×4 south of the back
yard with a wooden fence and a gate toward the yard. With the core alone the hall's south wall opens a back door to the
yard; fully grown is its final outline (`Imperium-Knowledge/designs/medieval-cards/M-H1.md` L6-19). It serves as the
burgher house of market towns and fortress cities, where a family lives, cooks and receives in one building with the
hall at its heart; it measures 14×14 (the house about 14×10, the garden 9×4), with a hall of 5×4 (a 2×2 table, four
chairs, fireplace, lamp, the main door in the north wall on the street), a bedroom of 3×4 (double bed, bedside table,
wardrobe, lamp), a lean-to of 2×2, a kitchen wing of 3×3, the back yard and the garden
(`Imperium-Knowledge/designs/medieval-cards/M-H1.md` L20-31). Its recognition words show as all rooms opening off the
hall; a street face in three steps (hall in front, lean-to back 1, bedroom back 2, kitchen wing to the south); and one
strip per household, front door on the street, then back yard, then garden, with the town's zone joining leftover ground
into fenced gardens (`Imperium-Knowledge/designs/medieval-cards/M-H1.md` L32-35). The original's Tudor timber frame and
Medieval Overhaul's furniture are replaced by the base game's, its carpets, cart, bench and bucket are removed for lack
of base-game counterparts, and the well and fireplace are placeholders for now, to be replaced later by the mod's own
components; its labels are residence or burgher house, tier common, size medium, door face north, rotation and mirroring
allowed, terrain flat (`Imperium-Knowledge/designs/medieval-cards/M-H1.md` L36-54). Its plan is the ASCII drawing at
`Imperium-Knowledge/designs/medieval-cards/M-H1.md` L56-78, with a legend of structure, bedroom, hall, kitchen and
lean-to, and yard symbols (`Imperium-Knowledge/designs/medieval-cards/M-H1.md` L56-78).

The commoner house (民宅) M-H2 grows from its core outward and is not fixed beforehand. Its rooms complement each other
after real houses: a hearth alcove projecting where the chimney stands, as in English cross-wing and Wealden hall
houses, a porch outside the front door, an outshut lean-to beside the main house, and a later room nested into the
yielded corner and jutting out. Its core is an irregular single hall from a one-room hut, with fuelled stove, fireplace,
a 1×2 table, chairs, shelves, double bed, bedside table and lamp, a front door to the south, the north-east corner
yielded to the bedroom, a fireplace alcove in the west wall and a porch of 3 cells
(`Imperium-Knowledge/designs/medieval-cards/M-H2.md` L4-16). Its growth pieces are a front yard beyond the porch with a
low wooden fence; a lean-to on the hall's east wall, 1 cell back, 2×2 inside with two shelves and a wood pile beside it;
a bedroom of 3×3 nested in the yielded corner and jutting north and east, with single bed, bedside table, wardrobe and
lamp; a fenced pen for hens and pigs behind the house clear of the bedroom; and a vegetable strip of 4 cells hugging the
wall outside the lean-to, ringed with ploughed soil and unfenced; at most 4 pieces in a village and 2 in a market town
or fortress city (`Imperium-Knowledge/designs/medieval-cards/M-H2.md` L18-26). Its outer walls are rough stone in a
village and stone of the plot in a market town, its inner walls wood in a village, its doors wooden, its floors wood
inside and stone slab in the lean-to; its labels are residence or commoner house, tier common, size small (core) to
medium (grown), layer 2 as filler, door face south, rotation and mirroring allowed, terrain flat. Its fully grown plan
is the ASCII drawing at `Imperium-Knowledge/designs/medieval-cards/M-H2.md` L28-63
(`Imperium-Knowledge/designs/medieval-cards/M-H2.md` L28-63).

The landmark cards are four (`Imperium-Knowledge/designs/medieval-cards/中世纪规格卡总表.md` L39-50). The keep M-K1
(27×23) is a square keep with four corner towers, symmetrical: a great hall with a long table, 8 chairs, a high seat, two
fireplaces and two statues; four corner rooms at the corner towers (the lord's bedroom to the north-west, the armoury to
the south-west, the vault to the north-east, the kitchen to the south-east); an entrance hall to the south; the wing walls
offset by one cell. The church M-C1 (19×28) has a nave with columns and benches, its north end stepped into an apse with
statue and lamps, a square bell tower to the south entered from beneath, and a sacristy projecting east. The watermill
M-W1 (20×15) stands by the river, with 4 wheels in a row outside its east wall and two millstones inside (placeholders), a
granary projecting west, the miller's dwelling to the south and a loading yard to the north, terrain label waterside.
The cathedral M-C2 (27×38) is a cross: a nave of two columns with four rows of benches, transepts with statues at both
ends, a choir with a large statue and seats, the north end stepped into an apse, a south entrance hall between two square
towers and a sacristy east of the choir; it stands only in a big city's church zone, at most one in a city. The sheet is
`Imperium-Knowledge/designs/medieval-cards/sheets/中世纪-地标卡.png`
(`Imperium-Knowledge/designs/medieval-cards/中世纪规格卡总表.md` L39-50).

> [!NOTE]
> **Unverified**: still to be done are the terrain labels (waterside, rock face) of the port, outpost and tourney ground,
> which wait for round 4, the types of tent camp, and the medieval section of the generation spec
> (`Imperium-Knowledge/designs/medieval-cards/中世纪规格卡总表.md` L428-432).

### The rewrite that is not stored

> [!NOTE]
> **Unverified**: a rewrite of the spec's medieval section, draft v3, is not stored: storing it was postponed, and the
> spec's medieval section stays the current text (`Imperium-Knowledge/09_地图生成与CBF技术.md` L577;
> `Imperium-Knowledge/designs/instructions/生成具象规格-现行版.md` L8, L22). It takes as input only the anchors of round 2 (the
> town's range with its area from the site requirements, the edge of the main gate, bridge site and bridge gate, the
> site of church or castle, the field zone, the stretches the town leans on) and derives outline, wall, towers and
> gates. It grows in this order: centre, approach corridors, layer 1, the inner wall of the fortress city, outer
> corridors, layer 2, wrapping and smoothing the wall, gatehouses then towers and gates, seams paved as streets, layer
> 3. Its centres are the church M-C1 with a small square for the village, a market square of about 22×14 (an atlas
> value) with the church for the market town, and the keep M-K1 with the cathedral M-C2 for the fortress city. The
> approach corridors (inferred, 推) are as many as gates, 3 wide and unpaved, and wind by least cost within 0.8R of the
> centre and run straight beyond it to 8 cells outside the range; nothing is built in them and they become main streets.
> The growth radius R is √(net area ÷ π), with layer 1 within 0.6R and layer 2 within 1.05R; buildings stand 0 cells
> apart (a shared wall, burgher and commoner houses only) or 2; every door front stays linked to the centre through free
> cells at least 2 wide; the building list decides what and how many, and a card's city layer only picks its variant
> (`Imperium-Knowledge/designs/medieval-cards/第二节改稿-v3-未落库.md` L4-68).

> [!NOTE]
> **Unverified**: draft v3's wall: it drops the tower formula and "rounded overall" in favour of the rules that follow
> (`Imperium-Knowledge/designs/medieval-cards/第二节改稿-v3-未落库.md` L205-221). The built-up area (inferred, 推) is the
> building cells plus corridor stretches with buildings within 5 on both sides, closed with radius 5 and widened by 2;
> stretches the town leans on are not walled. The smoothing is decided but its numbers are inferred (推): it only pushes
> outward, keeps the inner face at least 2 cells from buildings (at a tower at least its inward reach + 2, at a
> gatehouse 5 + 2), uses only horizontal and vertical lines on open stretches with straights of at least 5 and 45° steps
> only along hills or water, makes every outward corner 90°, leaves no notch of depth 4 or more on open stretches, and,
> for a town whose leaned-on stretches are under 30% of the perimeter, keeps the area at least 0.85 of its convex hull.
> Corner towers stand at every outward turn of an open stretch, turns closer than 24 along the wall merging into one;
> the tower's centre lies where the two wall axes cross and projects at least 2 beyond both outer faces (inferred); at
> least 60% of corner towers are round (inferred); a corner tower keeps 3 cells clear of river, deep water, rock, gate
> corridor and bridge, dropping a size or moving the turn inward when it does not fit. Gatehouses are palisade
> gatehouses of 5×9 in the village, 9×13 in the market town, 9×13 to 15×17 in the fortress city's outer ring with a
> 15×15 barbican at the main gate, and 7×11 in its inner ring; gates sit at corridor crossings with 3 straight cells on
> each side and at least 15 cells of bearing land outside, and the bridge gate on the town side of the bridge. The
> village has no moat, the fortress city a moat only on its outer ring, 1-2 cells from the wall and round the towers, 3
> wide in the market town and 4 in the fortress city (atlas values), of water where there is a river and dry mud
> otherwise, with a 3-wide earth bridge before the gates (`Imperium-Knowledge/designs/medieval-cards/第二节改稿-v3-未落库.md`
> L70-106).

> [!NOTE]
> **Unverified**: draft v3's streets, density, countryside and materials, whose numbers are mostly inferred (推) initial
> values: streets are the seams between houses, the corridors becoming main streets 3 wide and seams 2-3 wide joined to
> a main street or square becoming lanes (dead ends of at most 10 cells, inferred), seams of 1 merging into yards or
> being built over; the strip at least 2 wide inside the wall goes to the adjoining household as back yard, with no ring
> road. Building footprint covers at least 0.55 overall and 0.62 in the centre layer; streets, lanes and squares
> 0.15-0.25; yards and leftover ground at most 0.20, leftover at most 0.05 (these initial values to be re-marked as
> atlas values after measuring the community references); at least 60% of burgher and commoner houses share walls in
> blocks of 2-6; commoner to burgher houses 2.5-3.5 in market town and fortress city (inferred); no garden plots and no
> stands of fruit trees inside the wall, the only vegetable plots being the wall-side strips that come with the cards.
> Outside (inferred), a belt without buildings runs from the wall foot to 3 cells beyond the moat (5 beyond the wall
> without one); gardens of 60-150 cells lie 6-20 cells out, orchards of 100-300 cells of the base game's deciduous trees
> in rows 12-35 out (market town and fortress city), farmsteads and fields at least 20 out; 2-4 small houses line the
> gate road within 30 cells of the wall; the watermill M-W1 stands by a river, or a windmill on high ground without one;
> gate roads and paths get measured bends, the first 6 cells out of a gate straight, and roads are 2-wide dirt crossing
> rivers only at bridges. The town has no electricity, light coming only from torches and fireplaces; firewood and wood
> piles, the wood stove, the kiln (a placeholder), `RB_Fireplace` and wooden doors, floors and walls are medieval only
> and appear nowhere in Roman generation, how Rome treats the fireplace awaiting the user's ruling; special walls go
> only on the fronts of church and lord's hall and two cells either side of the tavern's door
> (`Imperium-Knowledge/designs/medieval-cards/第二节改稿-v3-未落库.md` L108-165)

> [!NOTE]
> **Unverified**: draft v3 leaves to the user the village's number of towers (one 7-cell tower at every outward right
> angle, or 1-2 towers where needed as drawn on `M-S`) and whether Rome bans the fireplace or the fireplace is not
> medieval only (`Imperium-Knowledge/designs/medieval-cards/第二节改稿-v3-未落库.md` L236-239;
> `Imperium-Knowledge/目录/规格卡.md` L83). The building lists of the village and market town wait for a check of CBF's
> `Village_New` and `MarketTown_New` and then the user's decision, and the values of density, shared walls and flavour
> wait for measuring the community references (`Imperium-Knowledge/designs/medieval-cards/第二节改稿-v3-未落库.md` L57,
> L118, L234; `Imperium-Knowledge/designs/medieval-cards/中世纪集镇试做-已定与依据.md` L24).

> [!NOTE]
> **Deleted**: draft v2 of this rewrite and the recommendations of its second review (corner-tower ruling, meander
> factor, church site, initial density values) (`Imperium-Knowledge/designs/medieval-cards/第二节改稿-v2二审-未落库.md`
> L4-35) were followed by draft v3, which lists its changes against the current text
> (`Imperium-Knowledge/designs/medieval-cards/第二节改稿-v3-未落库.md` L205-239).

## Tribal settlements

A tribal settlement picks its layout by the world tile and then gets the terrain of that type, rather than always being a
circle: a tile with a river, lake or coast gives a river-bank long-row camp or a longhouse stockade, chosen by seed; hills
or mountains give a cliff village, the terrain forming a U-shaped bay of cliffs; flat land with an open biome (grassland, shrubland, tundra, desert) a ring village; and anything else
(swamp, ice) a family-compound village, which is also the fallback. Where two types fit, the seed decides. Each type
scales to small, medium and large, with tents, stockade length and bastions after the camp plan and the population
(`Imperium-Knowledge/designs/instructions/生成具象规格-现行版.md` L624-631, R-1027-1601b;
`Imperium-Knowledge/designs/待用/现代与部落布局批次指令-草案-2026-10-27.md` L80). The three sizes were first all circles
and too alike, so the layout follows the terrain while one set of components (wooden stockade, staggered entrance, small
bastion, ditch and stakes, plaza, tent templates) is combined differently
(`Imperium-Knowledge/designs/待用/现代与部落布局批次指令-草案-2026-10-27.md` L68-69). The plans `T-S`, `T-M` and `T-L` each
draw one size of one type: `Imperium-Knowledge/designs/聚落设计图/T-S.png` the river-bank camp as small (104×92),
`Imperium-Knowledge/designs/聚落设计图/T-M.png` the longhouse stockade as medium (156×136),
`Imperium-Knowledge/designs/聚落设计图/T-L.png` the cliff village as large (206×176), and
`Imperium-Knowledge/designs/聚落设计图/T-F.png` (170×118) sketches the five types with their conditions and the shared
parts (`Imperium-Knowledge/designs/instructions/生成具象规格-现行版.md` L632;
`Imperium-Knowledge/designs/聚落设计图/README.md` L71-85).

The longhouse stockade stands only on tiles with a river or lake, the coast counting as near water
(`Imperium-Knowledge/designs/instructions/生成具象规格-现行版.md` L654; `Imperium-Knowledge/09_地图生成与CBF技术.md` L418,
R-1028-0020) (replaces `Imperium-Knowledge/designs/instructions/生成具象规格-现行版.md` L627;
`Imperium-Knowledge/designs/聚落设计图/README.md` L75, the longhouse stockade on wooded flat land).

The outline of a tribal settlement is the thin ring of the second stage: unplanned, scattering along the terrain, grown by
the same method as Rome's and the medieval town's with parameters by grade, and written into a card when the tribal work
starts (`Imperium-Knowledge/09_地图生成与CBF技术.md` L813, R-1110-1238c; `Imperium-Knowledge/09_地图生成与CBF技术.md` L818;
`Imperium-Knowledge/designs/做法史/现代与部落.md` L17). Its core is the chief's yard and the great hearth, its open space a
bonfire plaza with campfire and totem, and its axis earth paths radiating outward
(`Imperium-Knowledge/designs/ICF/聚落平面语法-v4.md` L58, L65, L97). Its boundary depends on its type: ring villages and
longhouse stockades have a solid stockade, cliff villages and river-bank camps a stockade that closes only the open side,
and family-compound villages no outer ring (`Imperium-Knowledge/designs/ICF/聚落平面语法-v4.md` L145).

The parts are shared. The stockade is a log wall one cell thick that follows the terrain and is not straightened into long
runs, unlike Roman and medieval walls; on the side of a river bank or cliff it runs along it, with no ditch there.
Entrances are staggered, either with the stockade's ends overlapping or with a stretch of stockade 4 cells outside the
entrance; on the water side a separate water gate opens without staggering. On the land side only, a ditch 2 wide of mud
lies 2-3 cells outside the stockade, with a ring of stakes (log barricades in every other cell) beyond it, an earth bridge
before the entrance and 4-6 cells cleared; longhouse stockades and river-bank camps dig no ditch. Small bastions of 3×3
logs belong only to ring and cliff villages (`Imperium-Knowledge/designs/instructions/生成具象规格-现行版.md` L633-640;
`Imperium-Knowledge/designs/待用/现代与部落布局批次指令-草案-2026-10-27.md` L84-92). The plaza is of rammed earth or mats
with one or two campfires and a totem, a skull spike when Ideology is loaded and a small sculpture otherwise; the
templates are the 25 of `tribal_cbf.json` without the knight's tent and the trader's tent
(`Imperium-Knowledge/designs/待用/现代与部落布局批次指令-草案-2026-10-27.md` L84-92;
`Imperium-Knowledge/09_地图生成与CBF技术.md` L298). A ring village has 1-2 staggered entrances and a small gate on the
water side (`Imperium-Knowledge/designs/ICF/聚落平面语法-v4.md` L216).

The river-bank long-row camp (河岸长排营) sets tents or longhouses in one or two rows along the bank with doors toward the
water (five in a row with the main tent central on the plan); between houses and water come the campfire, drying racks
(4×1 on the plan) and a canoe beach (about 14×3), with workshops behind the houses. On the land side one arc of protection
meets the bank at both ends, stakes in the small size and a stockade in the medium and large. The graveyard lies outside
the camp by rock or by the road, and a path leads to the woods
(`Imperium-Knowledge/designs/instructions/生成具象规格-现行版.md` L643-648).

The longhouse stockade (长屋寨) is an oblong stockade stretched along its long axis (about 116×52 on the plan), doubled on
the land side with the two lines 2 cells apart (the plan adds stakes 6-7 cells outside). It has a staggered entrance at
one end and a water gate at the other. Its longhouses are the long dwelling tents of `tribal_cbf.json` (17×9, 19×11)
stretched to about 21×9, or at their own size where that does not fit, in two rows along the long axis with doors at both
ends and a row of hearths inside. A council longhouse stands in the middle, with storage pits, and a work area (campfire,
totem, workshop tent, drying rack) lies by the water gate; outside are "three sisters" fields in a large forest clearing
and a graveyard (`Imperium-Knowledge/designs/instructions/生成具象规格-现行版.md` L650-657).

The cliff village (依崖村) sets two rows of houses with shared walls along the foot of the cliff, the back row against the
cliff and doors to the plaza. The plaza has one or two campfires and a totem and is closed on three sides by a feast hall,
the chief's tent and the council tent. Family compounds take the outer half of the bay, each fenced with stakes, 14×12 to
18×16, with 2-3 small tents of 7×7 to 10×10 round a hearth and one gate. Stockade, ditch and stakes close only the open
side, in one arc from cliff to cliff with two staggered entrances and a few small bastions (two on the plan). Outside lie
pens, gardens and a graveyard, and the large size adds a hunting camp (2 tents, a campfire, a drying rack)
(`Imperium-Knowledge/designs/instructions/生成具象规格-现行版.md` L659-665). The ring village has a round or oval stockade
with a 3×3 bastion every 18-24 cells, ditch and stakes on the land side, a plaza in the middle, dwelling tents in a ring
with doors to the plaza and the main tent facing the entrance; the family-compound village has an irregular hedge of
stakes or thorns round several family compounds gathered about the chief's compound and a council square; both are only
sketched on `T-F` (`Imperium-Knowledge/designs/instructions/生成具象规格-现行版.md` L667-670).

Outside a tribal village lie scattered, irregular garden plots near the stockade and the water (the longhouse stockade has
"three sisters" fields in forest clearings), paths of rammed earth radiating from the entrance to water, gardens and
woods, a graveyard on high ground or by a road with base-game graves (with skull spikes when Ideology is loaded) and, in
the large size, a hunting camp (`Imperium-Knowledge/designs/待用/现代与部落布局批次指令-草案-2026-10-27.md` L94-98;
`Imperium-Knowledge/designs/ICF/聚落平面语法-v4.md` L270). The camp plan of Medieval Overhaul's tribal camp is the reference
for later tribal bases: a core of 52-64 cells on a map of 200, one grade each of main road and lane, buildings 2-4 apart,
a built-up rate of 0.32, trees 0.15, 300 guard points, a wealth factor of 0.12, walls weighted as stakes 0.4, barricades
0.3 and wooden fence 0.3, 5-8 guards inside and 2-4 at the gate; in the centre 1 main tent, 1-2 council tents, 1-3
workshop tents, 1-2 campfires and 4-14 dwelling tents; on the outskirts 1-3 guards and 0-3 edge tents; neolithic, open to
all factions by their style of belief (`Imperium-Knowledge/designs/待用/建筑模板图册-2026-10-27.md` L151-158;
`Imperium-Knowledge/09_地图生成与CBF技术.md` L295).

A tribal settlement uses only objects that need no research or only neolithic research: no bedside tables, wardrobes or
shelves, goods lie on the ground; a tent with a fire and no dining table gets one table with wooden stools, while the fire
circle keeps its stools and no table (`Imperium-Knowledge/designs/instructions/生成具象规格-现行版.md` L641;
`Imperium-Knowledge/designs/待用/建筑模板图册-2026-10-27.md` L169, L197;
`Imperium-Knowledge/designs/待用/现代与部落布局批次指令-草案-2026-10-27.md` L125). In the conversion, tent walls and wooden
palisades became log walls, since the base game has no tent wall, so the look leans to log huts; fur beds became bedrolls,
stew pots campfires, anvils and tanning racks crafting spots, and golden skulls skull spikes with Ideology
(`Imperium-Knowledge/09_地图生成与CBF技术.md` L297; `Imperium-Knowledge/designs/待用/建筑模板图册-2026-10-27.md` L175).

> [!NOTE]
> **Base game**: complex furniture (shelf, bedside table, wardrobe, game table, brazier), smithing and complex clothing
> need medieval research, to be checked against `Data/` (`Imperium-Knowledge/designs/待用/建筑模板图册-2026-10-27.md`
> L169; `Imperium-Knowledge/09_地图生成与CBF技术.md` L296).

> [!NOTE]
> **Unverified**: the look of the round log huts is to be checked by screenshot after they are built
> (`Imperium-Knowledge/designs/待用/建筑模板图册-2026-10-27.md` L204); Odyssey has no tents, and the tribal round decides them
> later (`Imperium-Knowledge/14_来源同步与权威.md` L123). The set-aside layout draft names a reference concept for each tribal
> type (the fishing and hunting villages of the North American Northwest Coast and river valleys, Iroquois longhouse
> villages, the cliff dwellings and mesa villages of the American Southwest, the Mandan Huff village, the traditional
> villages of southern Africa) (`Imperium-Knowledge/designs/待用/现代与部落布局批次指令-草案-2026-10-27.md` L74-78).

## Modern settlements

A modern settlement has no city wall. The road net is laid first and the houses are set along the streets with doors to
the street and the same setback of 1-3 cells along each stretch
(`Imperium-Knowledge/designs/instructions/生成具象规格-现行版.md` L546;
`Imperium-Knowledge/designs/待用/现代与部落布局批次指令-草案-2026-10-27.md` L28-34). Density falls from the centre outward:
row houses with shared walls in the centre, detached houses with yards along the branch roads, industry at the edge and
farmland outside (`Imperium-Knowledge/designs/instructions/生成具象规格-现行版.md` L547). Houses are real houses, of 2-3
rooms with inner walls and doors, wooden floors and tiled rooms, and a fenced small yard behind; this is decided for the
medium size and a default for checking in the small and large, and the yard depth of 4 is an atlas value
(`Imperium-Knowledge/designs/instructions/生成具象规格-现行版.md` L557-560). The approach road is the main street and runs
to the map edge; it passes through to the far side only when there are two world-road entries
(`Imperium-Knowledge/designs/instructions/生成具象规格-现行版.md` L561). Its centre is a downtown square; its axis is a
crossroads or one main street in the small size, a main street with branches in the medium, and a ring with radials in the
large (`Imperium-Knowledge/designs/ICF/聚落平面语法-v4.md` L57, L97). Fields lie outside as large rectangles aligned with the
roads, with farmsteads along the road; the modern town keeps its farmsteads, while "only fields outside" applies to Rome
(`Imperium-Knowledge/designs/ICF/聚落平面语法-v4.md` L271;
`Imperium-Knowledge/designs/待用/现代与部落布局批次指令-草案-2026-10-27.md` L36-44).

Defence is three things only, since real modern towns build no walls: checkpoints, a fortified core and, in the large
size only, an outer line (`Imperium-Knowledge/designs/instructions/生成具象规格-现行版.md` L548;
`Imperium-Knowledge/designs/待用/现代与部落布局批次指令-草案-2026-10-27.md` L46). A checkpoint stands at the town's edge across every
road in (in the small size only on the approach road, one or two): barriers staggered on the road force vehicles into an
S, with a sandbag gun position on each side, one of which may take a turret, and a guard booth
(`Imperium-Knowledge/designs/instructions/生成具象规格-现行版.md` L565-571). The fortified core, in the medium and large sizes,
is a courtyard holding a command post, an armoury and barracks (13×12, 12×9 and 16×7 on the plan), ringed by barriers or
sandbags, with a gun position at each corner and one entrance; it stands at a key point marked in stage 2 (bridgehead,
main crossroads, flat ground by rock, river bend; at the main crossroads where there is no river), near the centre but
not blocking the main street (`Imperium-Knowledge/designs/instructions/生成具象规格-现行版.md` L573-576). The outer line, in the
large size only, runs 2-4 cells outside the ring road in horizontal, vertical and true 45° straights, with sandbag gun
positions of 5×5 at corners and road crossings, where checkpoints take over at the roads, and a field of fire cleared of
trees and buildings outside it, its width adjustable and 8 cells by default (inferred, 推)
(`Imperium-Knowledge/designs/instructions/生成具象规格-现行版.md` L578-581).

> [!NOTE]
> **Deleted**: the first line for the modern style followed CBF: the small, medium and large sizes reproduced CBF's
> Modern Village, City and Metropolis in grouping, road skeleton, building kinds, farmland, street scenes and hidden
> conduits, and their defence was a line of sandbags and barricades with turret posts, two rings in the large size
> (`Imperium-Knowledge/09_地图生成与CBF技术.md` L137). It was replaced by the layout and defence given here
> (`Imperium-Knowledge/designs/待用/现代与部落布局批次指令-草案-2026-10-27.md` L50;
> `Imperium-Knowledge/designs/instructions/生成具象规格-现行版.md` L546-548, L687).

Turrets are allowed but limited by defence points: their total strength stays within the defence points times a ratio,
and their points are taken from the garrison's, so the total threat is unchanged. One goes first to each checkpoint, on
the position facing the approach, then to the outer corner of the fortified core facing the main approach, and last to
the corners of the large size's outer line; a position without a turret remains sandbag cover. Only base-game turrets
the faction's technology can build are used, mostly outside and none in the lanes
(`Imperium-Knowledge/designs/instructions/生成具象规格-现行版.md` L549-554;
`Imperium-Knowledge/designs/待用/现代与部落布局批次指令-草案-2026-10-27.md` L53-58). Defence points come from `ThreatPoints` for
contracts and commissions, and from the garrison points given at generation for faction bases, as measured in build 4985
(`Imperium-Knowledge/designs/instructions/生成具象规格-现行版.md` L556).

> [!NOTE]
> **Unverified**: the turret ratios of 10%, 15% and 20% of defence points and the caps of 2, 6 and 10 turrets (small,
> medium, large) are presumed defaults that may be adjusted
> (`Imperium-Knowledge/designs/instructions/生成具象规格-现行版.md` L555;
> `Imperium-Knowledge/designs/待用/现代与部落布局批次指令-草案-2026-10-27.md` L54).

The small size is a crossroads village (plan `Imperium-Knowledge/designs/聚落设计图/X-S.png`, 144×132): the approach road is
a main street 3 wide from the map edge to the village centre, and a branch 2 wide crosses it at the centre, with in the
atlas a trading post and a clinic by the crossing; houses line both roads facing them; in the atlas workshops and the
generator yard stand by the road out; large rectangular fields lie aligned with the roads, with farmsteads and granaries
along them (`Imperium-Knowledge/designs/instructions/生成具象规格-现行版.md` L583-589;
`Imperium-Knowledge/designs/聚落设计图/README.md` L66)

The medium size is a main-street town (plan `Imperium-Knowledge/designs/聚落设计图/X-M.png`, 196×176, redrawn because the
first version was too poor). Its main street is asphalt 4 wide, with a pavement of 1 cell on each side in the central
stretch, bending a little with the terrain and bridging the river; a cross street 3 wide meets it, four branches 2 wide
enclose the centre, and outer residential streets are 2 wide. A paved square with a fountain and trees lies where main and
cross streets meet, with the town hall (`Parliament_B`, 17×14 facing the square on the plan), police, clinic, tavern and
church round it. Shops stand in terraced rows with shared walls along the main street, their doors on the pavement;
houses along the branches and streets are detached with yards; a school or institute with a playground lies at the edge
of the houses; the fortified core backs onto the river and holds the bridgehead on the plan; and the industrial zone
(warehouses, yards, oil tanks, generator yard, landing pad) lies by the road out, inside the checkpoint
(`Imperium-Knowledge/designs/instructions/生成具象规格-现行版.md` L591-603;
`Imperium-Knowledge/designs/待用/现代与部落布局批次指令-草案-2026-10-27.md` L61-66;
`Imperium-Knowledge/designs/聚落设计图/README.md` L67).

The large size is a ring-road city (plan `Imperium-Knowledge/designs/聚落设计图/X-L.png`, 252×236): a ring road with radial
roads and a grid of branches inside (on the plan a ring 3 wide, two arterials 4 wide, two diagonal radials 3 wide and
branches 2 wide), its centre at the crossing of the arterials with the square and public buildings, the fortified core
near the centre but not blocking the arterials (24×20 on the plan), a suburb of lower density than inside the ring
outside it along the radials (inferred, 推), an industrial zone by the road out inside the outer line, which may bulge to
take it in, and a checkpoint on each road in (`Imperium-Knowledge/designs/instructions/生成具象规格-现行版.md` L605-614;
`Imperium-Knowledge/designs/聚落设计图/README.md` L68). The plan `Imperium-Knowledge/designs/聚落设计图/X-F.png` (150×96) shows
the checkpoint, the fortified core, segments of the outer line and the industrial zone with its generator yard
(`Imperium-Knowledge/designs/聚落设计图/README.md` L69).

In the modern style, materials, appliances and furnishings keep the original pieces, only stripped and filled up to the
base game's needs, and the city buildings (police station, bank, council hall, apartment block, garage, entertainment
hall, research centre) belong to the modern style alone
(`Imperium-Knowledge/designs/待用/建筑模板图册-2026-10-27.md` L116-118; `Imperium-Knowledge/09_地图生成与CBF技术.md`
L137, L167).

## Entering settlements to trade

Entering settlements to trade is designed but not scheduled: the rounds of generation are unchanged and nothing is marked
on the maps now (`Imperium-Knowledge/09_地图生成与CBF技术.md` L383-387, R-1027-1914;
`Imperium-Knowledge/designs/待用/进城交易设计-草案-2026-10-27.md` L4-8). The decision is taken half a year later at the
earliest, after seeing what the next official expansion brings: if it brings faction content such as entering settlements
or diplomacy, Imperium only grafts its settlement generation onto the official system and most of this design lapses; if
not, Imperium makes faction interaction itself by this design (`Imperium-Knowledge/designs/待用/进城交易设计-草案-2026-10-27.md`
L9-11).

> [!NOTE]
> **Deleted**: deciding at the same time whether the water axis stays belonged to the hydraulics the maintainer deleted
> (`Imperium-Knowledge/designs/待用/进城交易设计-草案-2026-10-27.md` L12).
It answers the base game's friendly settlements being closed, which leaves the generated cities seen only by besiegers
and at contract sites; inside, the player could walk in the town, trade in its shops and see its people, and all four
styles gain from it (`Imperium-Knowledge/designs/待用/进城交易设计-草案-2026-10-27.md` L17;
`Imperium-Knowledge/09_地图生成与CBF技术.md` L385).

Any faction's settlement can be entered to trade. A big city has branch shops, each selling one class of goods through
the base game's trade window, while a small settlement or a tribe has one merchant. Military strongpoints (Castellum,
Fortlet, modern barracks and the like) can be entered, but only a quartermaster trades there, in small amounts of
military supplies, and the other areas are closed (`Imperium-Knowledge/designs/待用/进城交易设计-草案-2026-10-27.md`
L19-26; `Imperium-Knowledge/09_地图生成与CBF技术.md` L388-390).

> [!NOTE]
> **Unverified**: since pirates are always hostile in the base game, the scope in practice is any non-hostile faction, a
> reading the source marks as its own inference (`Imperium-Knowledge/09_地图生成与CBF技术.md` L388). The rest are
> suggestions not ruled, to be confirmed one by one: an "enter town" button for a caravan on a non-hostile settlement's
> tile, arrival from the nearest gate or map edge, and leaving by the map edge or a button; the map dropped on leaving and
> regenerated from the same seed, with only stock and a little state saved and no raids while the player is in town; all
> shops sharing the settlement's one stock on the world map, a big city's goods split into armoury, clothier, food and
> medicine, raw materials and general goods, shop shelves showing samples that cannot be taken, and shop places by style
> (Roman frontages on the main street, medieval market stalls, modern shops, one tribal merchant); the quartermaster's
> stock and the forbidden barracks, armoury and headquarters; residents of the faction's own pawns, few by map size, with
> civilians in imperial cities and a few guards; goodwill lost for crossing the line, and hostility on killing a resident,
> lasting damage or goodwill falling to hostile; the title permit for trade in an imperial city replaced by Rank; Imperium
> implementing it itself, adapting RimCities' MIT code with attribution and only studying Visit Settlements' behaviour;
> markers the generation side would need in all four styles; and later, renting beds, hiring people, and handing in Orders
> and meeting officials in an imperial city (`Imperium-Knowledge/designs/待用/进城交易设计-草案-2026-10-27.md` L28-101;
> `Imperium-Knowledge/09_地图生成与CBF技术.md` L391).

## Where the work stands

From the third round of generation only Rome is made; the medieval, modern and tribal styles are each designed and
implemented on their own, outside the Roman rounds, in an order not yet set, and the storing of the medieval section's
rewrite and the medieval walls are postponed (`Imperium-Knowledge/09_地图生成与CBF技术.md` L577, R-1029-1307;
`Imperium-Knowledge/designs/instructions/生成具象规格-现行版.md` L22; `Imperium-Knowledge/designs/做法史/中世纪.md` L18-19;
`Imperium-Knowledge/designs/做法史/现代与部落.md` L14-15). The lines of the medieval, tribal and modern styles are paused:
their current cards are written when they reopen, and the medieval cards wait until then
(`Imperium-Knowledge/designs/回报/改法-入口瘦身-2026-11-10.md` L126; `Imperium-Knowledge/14_来源同步与权威.md` L141,
R-1103-0005).

> [!NOTE]
> **Unverified**: only a few conversion templates marked as temporary placeholders remain (the medieval field method,
> the gatehouse blueprint, the contract camp master, the tribal camp), and once the move into Mantle is done the
> transcriptions of CBF and Medieval Overhaul, the decompilation comparisons and the derived templates are all to retire
> into the archive, while Medieval Overhaul's content, templates and names are not transcribed into the repository
> (`Imperium-Knowledge/01_项目宪章与规范索引.md` L185, L187; `Imperium-Knowledge/designs/整理/整理记录-2026-11-02.md` L71-72); the
> folders of the paused lines are listed as deletable but not deleted (`Imperium-Knowledge/designs/tools/目录配置.md` L123).
> The old instruction draft for the modern and tribal layout batch is kept in the on-hold (待用) draft list
> (`Imperium-Knowledge/目录/待用-指令草案.md` L21-37); that batch was to be opened after the wall batch and before the fourth,
> bringing the modern road net first, functional zones, checkpoints and a defended core, no walls, turrets limited by
> defence points and a redrawn medium town, and the tribal layouts by terrain (`Imperium-Knowledge/11_开发进度与未决事项.md`
> L34).