# City building

City building (城建) is Imperium's generation of settlements on the map, from their terrain and layout to their walls
and buildings. This file is its entry: what city building makes, the scale of a city and the references it learns from,
the eras of the Roman city, the principles every city keeps, the order in which a city is made and how it grows through
its periods. Where a city stands and on what terrain is in [cities-siting.md](cities-siting.md); walls, towers, gates,
water gates, moats and the clear strip are in [cities-walls.md](cities-walls.md); the core, the palace quarter, plazas,
streets, housing and buildings are in [cities-inside.md](cities-inside.md); the land outside the walls and the rivers,
banks, bridges and harbours of a city are in [cities-outside.md](cities-outside.md); templates, kits, skeletons, spec
cards and the city grammar are in [cities-forms.md](cities-forms.md). The settlements of the other cultures are in
[cultures.md](cultures.md).

## What city building makes

### Rome first

Generation concentrates first on Rome: the City and the three military camps, Castellum, Fortlet and Burgus. The
medieval, modern and tribal settlements are each designed and implemented on their own and do not join Rome's rounds
(`Imperium-Knowledge/现行/城/罗马城-做法与顺序.md` L34, R-1029-1307; `Imperium-Knowledge/09_地图生成与CBF技术.md` L577).
Beyond the City and the camps, Rome is also to have a market town, outposts, estates, relay stations and mines, which are
made later (`Imperium-Knowledge/现行/城/罗马城-做法与顺序.md` L35, R-1029-1400a); the skeleton is the base of a
civilisation, and Rome needs more uses of it (`Imperium-Knowledge/designs/做法史/罗马城·做法与顺序.md` L98). The tiers
are City, Castellum, Fortlet and Burgus, in the sizes S, M and L (`Imperium-Knowledge/designs/tools/审查清单-条文.md`
L21).

Each faction has one theme, its types divided by region and not by period: Rome's two types are those of hot dry regions
and of temperate and colder regions, and the other factions are to follow the same pattern
(`Imperium-Knowledge/01_项目宪章与规范索引.md` L180). One faction
has one kit: Rome has one kit, the arid (干热区) and temperate (温寒区) types are skins of it, and the camp is a tier of
the Roman kit (City, Castellum, Fortlet, Burgus) (`Imperium-Knowledge/designs/ICF/聚落平面语法-v4.md` L372-373). The
four styles, Roman, medieval, modern and tribal, are laid out by the logic of real settlements and the player
community's practice, strengthening what the 2D plan can show, so that each is recognisable at a glance in a panorama
and none looks like another (`Imperium-Knowledge/designs/待用/现代与部落布局批次指令-草案-2026-10-27.md` L18).

> [!NOTE]
> **Unverified**: the order in which the medieval, modern and tribal settlements are implemented is not decided
> (`Imperium-Knowledge/09_地图生成与CBF技术.md` L577).

### Residents

Only the large tier, the City, has residents. The Empire's military strongpoints hold only commanders and machines, and
the Roman small and medium tiers use military strongpoints for now (`Imperium-Knowledge/06_行政设施与地区活动.md`
L186-188). Civilians, craftsmen and residents who do not fight, live only in the Empire's own settlements, are generated
from each settlement's resident anchors and do not go to the player (`Imperium-Knowledge/06_行政设施与地区活动.md` L186).

> [!NOTE]
> **Unverified**: Roman small and medium settlements with residents are not added yet, and the new civilian pawn kind
> they need is not scheduled; until then the resident anchors use existing pawns
> (`Imperium-Knowledge/06_行政设施与地区活动.md` L186-188).

### Audience, variety and uses

The main audience of a Roman city is the besieger and the quest site; the player may not see it often, and it is still
polished in the spirit of a DLC (`Imperium-Knowledge/现行/城/罗马城-做法与顺序.md` L27). A Roman city is a friendly
empire's building: ornate walls are used freely at its key places with no cap on gold, and a player who turns hostile and
takes the city may tear the walls down for their gold (`Imperium-Knowledge/09_地图生成与CBF技术.md` L271, R-1027-08). The
buildings inside the walls of the capital Theodosian (首府 Theodosian) are shelved
(`Imperium-Knowledge/11_开发进度与未决事项.md` L55). Variety is measured by how fresh
the cities are in the player's second and third game, not by how many years it lasts
(`Imperium-Knowledge/现行/城/罗马城-做法与顺序.md` L28; `Imperium-Knowledge/现行/索引.md` L426;
`Imperium-Knowledge/designs/做法史/罗马城·做法与顺序.md` L97).

A city has three uses, all wanted and divided by district: housing districts weigh look, the palace quarter (宫区) and
the market weigh function, and the wall weighs defence (`Imperium-Knowledge/现行/城/罗马城-做法与顺序.md` L161;
`Imperium-Knowledge/09_地图生成与CBF技术.md` L935; `Imperium-Knowledge/designs/tools/方向表.md` L34). The list of
districts follows the zoning of the Anno 117 reference city and is supplemented with Roman meaning, each kind stating
which use it weighs; from the reference the design learns composition and look, while function comes from Imperium's
cards and RimWorld's rules, and missing cards are added district by district as content work
(`Imperium-Knowledge/现行/城/罗马城-做法与顺序.md` L161-162; `Imperium-Knowledge/designs/做法史/罗马城·做法与顺序.md`
L204-205).

### A generated city is fixed

A city is fixed once it is generated. The generator walks the period table (期表) in memory, each period changing the
result of the last and turning what the earlier one left to other use instead of erasing it, and writes only the finished
picture to the map; the same tile and seed give the same city (`Imperium-Knowledge/09_地图生成与CBF技术.md` L787;
`Imperium-Knowledge/现行/城/罗马城-做法与顺序.md` L104; `Imperium-Knowledge/现行/城/地形与选址.md` L105). Effect: a fixed
city reads as an old city that lived through many generations and was enlarged
(`Imperium-Knowledge/09_地图生成与CBF技术.md` L787; `Imperium-Knowledge/designs/回报/审查-规矩分类-2026-11-10.md` L807).

### What a city's things do in the game

The library gives in-game systems to imperial facilities and the defence line among a city's things. For shop fronts,
markets, warehouses, workshop output, gardens, the harbour's water traffic, inns and relay stations, and civilians' work
it says only where they stand and what they adjoin (`Imperium-Knowledge/designs/回报/进度-配套表.md` L18). In template 1
these eight are laid by the existing rules of where they stand and what they adjoin, marked as awaiting a system, and no
system is made up for them (`Imperium-Knowledge/现行/城/罗马城-做法与顺序.md` L179).

> [!NOTE]
> **Deleted**: the hydraulics the maintainer deleted took with it what city building rested on it: the library's line of
> city systems for water and power (`Imperium-Knowledge/designs/回报/进度-配套表.md` L18); the lifeline (命脉线), which
> for a Roman city is its water and also its power grid, among the skeleton's pieces of period 1 and laid as a trunk with
> them (`docs/glossary.md` L187; `Imperium-Knowledge/现行/城/罗马城-做法与顺序.md` L100;
> `Imperium-Knowledge/designs/city-plans/理念与机制对照-草案.md` L35); Rome as an empire of the working fluid (工质)
> with hydropower, a planned city held up by water, and New Rome's water and machinery of the working fluid
> (`Imperium-Knowledge/01_项目宪章与规范索引.md` L182-183; `Imperium-Knowledge/designs/instructions/生成具象规格-现行版.md`
> L128; `Imperium-Knowledge/现行/城/罗马城-做法与顺序.md` L13); the aqueducts taken from the earlier period
> (`Imperium-Knowledge/designs/instructions/生成具象规格-现行版.md` L128); the water palace and canal read from image
> three (`Imperium-Knowledge/现行/城/罗马城-做法与顺序.md` L186); and the open cisterns of the large-piece belt
> (`Imperium-Knowledge/现行/城/罗马城-城内.md` L200).

> [!NOTE]
> **Unverified**: what the eight classes do in the game is decided once, when town trading is scheduled, and is tracked
> as live list #80 (`Imperium-Knowledge/现行/城/罗马城-城内.md` L246; `Imperium-Knowledge/designs/做法史/罗马城·城内.md`
> L210; `Imperium-Knowledge/designs/做法史/罗马城·做法与顺序.md` L187;
> `Imperium-Knowledge/designs/回报/配套表/没进表的.md` L10-19). The rules for entering a town to trade (buttons,
> regeneration by the same seed, shared stock, shop classes, residents and guards, favour penalties, rank permission) are
> suggestions that were not ruled (`Imperium-Knowledge/09_地图生成与CBF技术.md` L391).

## Scale

### Map size by grade

A settlement's map size follows its grade, one size for each grade, and not the player's world setting: a large city
350×350, a medium city 300×300, a small city 250×250 and an outpost 200×200; the 225, 275 and 325 set is not made, and
400 is not used (`Imperium-Knowledge/09_地图生成与CBF技术.md` L873; `Imperium-Knowledge/现行/城/地形与选址.md` L98)
(replaces `Imperium-Knowledge/09_地图生成与CBF技术.md` L871; `Imperium-Knowledge/09_地图生成与CBF技术.md` L785). The
outpost is a new grade whose content is decided separately (`Imperium-Knowledge/09_地图生成与CBF技术.md` L873). Effect:
one grade is the same size in every save, and templates are made for one size
(`Imperium-Knowledge/09_地图生成与CBF技术.md` L873). Roman cities are designed separately for large, medium and small,
and each grade's test terrain follows that grade's map, the existing 325 snapshots serving until they are remade
(`Imperium-Knowledge/现行/城/罗马城-做法与顺序.md` L136; `Imperium-Knowledge/09_地图生成与CBF技术.md` L873).

> [!NOTE]
> **Base game**: the base game's map sizes come in tiers from 200×200 to 400×400, which the four grades are set to
> match, to be checked against `Data/` (`Imperium-Knowledge/09_地图生成与CBF技术.md` L871, L873).

### The area of a city

A large city's wall circle, a river through it included, takes half to two thirds of the map, and its wall, with the
wall band, clear strip and moat, stays at least 10 cells from the map edge (`Imperium-Knowledge/现行/城/地形与选址.md`
L82; `Imperium-Knowledge/09_地图生成与CBF技术.md` L870) (replaces `Imperium-Knowledge/09_地图生成与CBF技术.md` L785).
Effect: the city fills most of the map, and one is soon beneath its walls after entering from the map edge
(`Imperium-Knowledge/现行/城/地形与选址.md` L82).

A city's area is its net buildable area inside the wall, without the wall band, clear strip and moat
(`Imperium-Knowledge/现行/城/地形与选址.md` L80). It is computed on the actual map as its buildable land, the land
without water, rock and marsh, times the ratio in the site requirements; the ratio for a medium city is 0.16, a trial
value, and no aspect ratio is set (`Imperium-Knowledge/现行/城/地形与选址.md` L81;
`Imperium-Knowledge/09_地图生成与CBF技术.md` L785) (replaces
`Imperium-Knowledge/designs/回报/审查-城建版本盘点-2026-11-10.md` L17). Bigger maps and more flat land give bigger
cities (`Imperium-Knowledge/09_地图生成与CBF技术.md` L785). When a city comes out smaller, the skeleton's required pieces,
such as the palace quarter, the first plaza (第一广场) and the cathedral, scale with its area between an upper and a
lower bound, and the city is regenerated on another landform only when they do not fit even at the lower bound
(`Imperium-Knowledge/现行/城/地形与选址.md` L102; `Imperium-Knowledge/09_地图生成与CBF技术.md` L785). Area and scale are
written in one place, the siting card's section on site requirements and area
(`Imperium-Knowledge/09_地图生成与CBF技术.md` L914; `Imperium-Knowledge/designs/回报/进度-一题一家.md` L63).

### The size of a cell

A cell is sized by things the size of a person. In a reference picture a door, a figure or a tree is one RimWorld cell;
that gives how many pixels one cell is, then how many RimWorld cells the other game's own cell is, and only then are sizes
compared and copies laid out. Another game's cell is never mapped one to one, and the size of one of Imperium's
households is not used to size the houses of a reference (`Imperium-Knowledge/14_来源同步与权威.md` L290;
`Imperium-Knowledge/现行/城/地形与选址.md` L90). This followed a first replica that made the Anno dwellings as large as one
household of 143 cells and came out 597×574 cells, every house far too large
(`Imperium-Knowledge/14_来源同步与权威.md` L290). The person-sized cell anchors the 1:1 size, and the ratio that fits a
city into its map follows on the same scale chain (`Imperium-Knowledge/现行/城/地形与选址.md` L90;
`Imperium-Knowledge/09_地图生成与CBF技术.md` L914).

For Imperium's own layout one household (户), a house with its plot, is about 15×15 cells, the size of one Anno 117
house plot of 3×3 Anno cells, so that one Anno cell comes to about 5 cells (`Imperium-Knowledge/09_地图生成与CBF技术.md`
L960; `Imperium-Knowledge/现行/城/地形与选址.md` L88) (replaces `Imperium-Knowledge/09_地图生成与CBF技术.md` L930;
`Imperium-Knowledge/designs/tools/city/说明/sample.md` L326; `Imperium-Knowledge/designs/tools/city/代码地图.md` L730;
`Imperium-Knowledge/designs/整理/整理记录-2026-11-02.md` L579; `Imperium-Knowledge/designs/研究/城/布置思路.md` L56).
The reasons given are that road widths of 3, 5 and 7 then match the reference's proportions, that a wall circle of about
two thirds of the 350 map holds the whole city without cutting districts, that commoners' inner yards are decent, and
that existing cards can serve as wings (`Imperium-Knowledge/09_地图生成与CBF技术.md` L960). Reading the reference and
laying out Imperium's own houses use two separate ratios on purpose (`Imperium-Knowledge/现行/城/罗马城-做法与顺序.md`
L173; `Imperium-Knowledge/designs/研究/城/布置思路.md` L28; `Imperium-Knowledge/designs/研究/城/片区谱-广场住片.md`
L24). Rich households and large public pieces keep their card sizes; where they do not fit, blocks are merged so that one
piece takes a whole block, only lanes being removed and main and secondary streets left alone; houses are not shrunk, and
a city that does not fit its map places fewer districts (`Imperium-Knowledge/现行/城/地形与选址.md` L88).

When the reference is read, one Anno cell is taken for now as 3.7 trace cells, measured, to be checked against the
user's in-game screenshots (`Imperium-Knowledge/现行/城/罗马城-做法与顺序.md` L173;
`Imperium-Knowledge/09_地图生成与CBF技术.md` L930; `Imperium-Knowledge/designs/整理/整理记录-2026-11-02.md` L610)
(replaces `Imperium-Knowledge/designs/tools/city/说明/sample.md` L281;
`Imperium-Knowledge/designs/研究/城/纪元资料/总督别墅与模块.md` L31;
`Imperium-Knowledge/designs/整理/整理记录-2026-11-02.md` L546;
`Imperium-Knowledge/designs/研究/城/纪元117-设计理念-地图与城建-2026-11-11.md` L46-47;
`Imperium-Knowledge/designs/研究/城/纪元资料/河湾聚落尺度查证.md` L14-18, L30;
`Imperium-Knowledge/designs/研究/城/纪元117-图例-2026-11-12.md` L145, which read about 3.3, 3 to 4, 1.9 to 2.8 and
2.6). Beside it the card records the person scale measured on the five in-game screenshots
`Imperium-Knowledge/designs/city-plans/Anno117-截图-平民-搬迁-一.png`,
`Imperium-Knowledge/designs/city-plans/Anno117-截图-自由民-搬迁-二.png`,
`Imperium-Knowledge/designs/city-plans/Anno117-截图-平民-斜看-三.png`,
`Imperium-Knowledge/designs/city-plans/Anno117-截图-平民-九宫格-四.png` and
`Imperium-Knowledge/designs/city-plans/Anno117-截图-自由民-九宫格-五.png`, on which one Anno cell is about 8.9
person-sized cells, 5.6 to 9.7 (`Imperium-Knowledge/现行/城/罗马城-做法与顺序.md` L173;
`Imperium-Knowledge/09_地图生成与CBF技术.md` L959); the scale page notes that the reference image draws its people
small, a house being six to eight people wide (`Imperium-Knowledge/designs/研究/城/纪元资料/河湾聚落尺度查证.md` L50).

### Templates larger than the map

A template larger than its map is scaled whole by one ratio: wall, river, island, bridge positions, plazas, streets,
blocks and households together, and equally in both directions so that 45° stays 45°
(`Imperium-Knowledge/09_地图生成与CBF技术.md` L876). The ratio is set only by the household of about 15×15 cells
(`Imperium-Knowledge/09_地图生成与CBF技术.md` L963; `Imperium-Knowledge/现行/城/地形与选址.md` L83) (replaces
`Imperium-Knowledge/09_地图生成与CBF技术.md` L876, which set it by the map edge and the wall's distance to it). Street
widths scale with it but not below 3 for a lane, 5 for a secondary street and 5 for a trunk, and gates, towers and
bridges keep their widths (`Imperium-Knowledge/现行/城/地形与选址.md` L83). Each scaled household becomes a plot that is
later filled with Imperium's cards at their own size, fitted by stretching bays and by small-household cards; a plot
smaller than the smallest household goes to a neighbour or becomes a yard (`Imperium-Knowledge/现行/城/地形与选址.md`
L84). Where a template fits only by changing its skeleton, a template of the next lower grade is used
(`Imperium-Knowledge/现行/城/地形与选址.md` L85). Shrinking the frame while keeping the houses, which removed about a
third of the households, is not done, because the street front broke and the feeling of a city was lost
(`Imperium-Knowledge/09_地图生成与CBF技术.md` L876) (replaces `Imperium-Knowledge/09_地图生成与CBF技术.md` L872, L874).

After the city is placed in its map, the distance from the wall to the map edge is measured segment by segment: gate and
exit-road segments keep enough room, riverside and terrain segments may be short, and where a segment lacks room that
stretch of wall moves or one district at the city's edge is left out, houses and roads never shrinking
(`Imperium-Knowledge/09_地图生成与CBF技术.md` L963; `Imperium-Knowledge/现行/城/地形与选址.md` L87). The wall circle's
share of the map and its distance to the edge are judged when templates and samples are output, the 1:1 version only
reporting them (`Imperium-Knowledge/现行/城/地形与选址.md` L89).

> [!NOTE]
> **Unverified**: the factor that brings template 1, the Anno 117 river-bend city (1:1 wall frame 396×351, sample frame
> 398×359), into the 350 map waits for the user; an earlier 0.822 was ordered back behind the full 1:1 layout, and the
> scaled version is not yet in the library (`Imperium-Knowledge/现行/城/地形与选址.md` L86;
> `Imperium-Knowledge/09_地图生成与CBF技术.md` L876, L914, L963;
> `Imperium-Knowledge/designs/研究/城/纪元资料/河湾聚落尺度查证.md` L50-52). How many cells each wall segment keeps from
> the map edge waits for the user and is left aside while the city is replicated
> (`Imperium-Knowledge/现行/城/地形与选址.md` L87).

### Scale in the studies of real cities

The studies of real cities take one cell as about one metre
(`Imperium-Knowledge/designs/roman-cards/罗马住宅调查-2026-10-28.md` L4), about 1.3 m
(`Imperium-Knowledge/designs/city-plans/街坊外廓-两盛期查证-2026-10-30.md` L4), or 1 to 1.5 m
(`Imperium-Knowledge/designs/instructions/罗马城墙史实核查-2026-10-29.md` L6;
`Imperium-Knowledge/designs/city-plans/现实街坊研究-方法草案-2026-10-30.md` L32, L59). A study window of a real
district is about 100×100 m, about 70 to 90 cells square (`Imperium-Knowledge/designs/city-plans/现实街坊研究-方法草案-2026-10-30.md`
L32). These figures serve to read real cities; angles and sizes are set by the game's effect, as the next section says
(`Imperium-Knowledge/14_来源同步与权威.md` L168).

## References

### What Rome is referenced

Imperium's Rome is New Rome (新罗马). Defaults and first examples take New Rome, naming Constantinople, Thessaloniki and
Smyrna (`Imperium-Knowledge/现行/流程/设计会话工作规矩.md` L103;
`Imperium-Knowledge/designs/instructions/生成具象规格-现行版.md` L128; `Imperium-Knowledge/01_项目宪章与规范索引.md`
L181). What is unique to ancient Rome (古罗马), with ancient Roman cities such as the camp cities and the Aurelian wall,
is not a reference (`Imperium-Knowledge/现行/流程/设计会话工作规矩.md` L109; `Imperium-Knowledge/designs/tools/默认用规则.md`
L35, L90, L165; `Imperium-Knowledge/designs/回报/进度-参照只取继承.md` L33). What New Rome inherited from earlier, and
what both flourishing periods (两盛期) share, may be referenced; what appears only in New Rome's records and scholarship
is not used alone as a basis and needs evidence shared by both periods or the support of a game effect
(`Imperium-Knowledge/现行/流程/设计会话工作规矩.md` L111; `Imperium-Knowledge/09_地图生成与CBF技术.md` L890-891;
`Imperium-Knowledge/designs/回报/参照只取继承/盘点.md` L4; `Imperium-Knowledge/designs/回报/进度-参照只取继承.md` L8,
L23, L33-34). From the earlier period
come the regular grid, colonnades, squares and baths, while a whole city of its small-block insulae is left to the ruins
(`Imperium-Knowledge/designs/instructions/生成具象规格-现行版.md` L128; `Imperium-Knowledge/01_项目宪章与规范索引.md`
L182); ancient Roman places such as Pompeii and Timgad belong to the ruins, which will mostly be ancient Roman, so the two
are kept apart (`Imperium-Knowledge/01_项目宪章与规范索引.md` L181).

The base of references is the provinces outside Italy, the eastern provinces, Gaul, North Africa and Iberia; Italian
cities such as Pompeii and Ostia are content for ruins, not references for cities and buildings, and Britain and Germany
are too remote to use (`Imperium-Knowledge/现行/流程/设计会话工作规矩.md` L109;
`Imperium-Knowledge/09_地图生成与CBF技术.md` L691-692) (replaces `Imperium-Knowledge/14_来源同步与权威.md` L56, which
limited references to the core lands with Italy). Italian homeland sites serve only as remains and comparison, and a
historical statement used as a basis in a city card carries a source checked in the library
(`Imperium-Knowledge/09_地图生成与CBF技术.md` L890-891; `Imperium-Knowledge/现行/流程/设计会话工作规矩.md` L110;
`Imperium-Knowledge/designs/tools/默认用规则.md` L93, L166, L185). The materials of the city and its buildings,
limestone, sandstone and marble masonry, do not follow Italy (`Imperium-Knowledge/现行/城/罗马城-做法与顺序.md` L208;
`Imperium-Knowledge/09_地图生成与CBF技术.md` L691-692).

Having existed is not the same as representing. Only what the large cities outside Italy share enters a rule; the plans
of small towns, camps and veteran colonies, such as the square city of Timgad or the near-round polygon of Nicaea, only
existed and are no rule; lineage is sought among great cities, not by count; and the aim is what can represent Roman
civilisation (`Imperium-Knowledge/现行/流程/设计会话工作规矩.md` L111; `Imperium-Knowledge/14_来源同步与权威.md` L56). A
feature seen in Italy or in textbooks, such as the black basalt streets of Rome and Pompeii or the square military camp,
is not taken as an imperial rule; the first question is whether it is local to Italy or belongs to the whole Empire
(`Imperium-Knowledge/14_来源同步与权威.md` L56). A reference is first judged by what share of the Roman city it covers:
camps, camp cities and palace cities are single cases, a small share of Roman cities, and are neither taken as the body
of a city nor used to push its shape (`Imperium-Knowledge/designs/回报/改法-入口瘦身-2026-11-10.md` L154, L167;
`Imperium-Knowledge/designs/回报/规则表-2026-11-11.md` L39; `Imperium-Knowledge/designs/tools/默认用规则.md` L33, L91,
L167).

Design speaks of Rome by meaning: the standard is whether it reads as New Rome with the Roman civilisation it inherited,
not whether history is right, and history is not verified for design; a historical statement needs a source only where
it is used as a basis or stated as fact (`Imperium-Knowledge/designs/研究/城/布置思路.md` L29;
`Imperium-Knowledge/14_来源同步与权威.md` L303).

### How a reference is used

Before the shape of the Roman city (its outline, walls and districts) is discussed, a reference passes three steps:
history lends only the concept, why it was built that way; the game lends the effect, the pictures of Anno 117 and Nova
Roma; and the result is landed in RimWorld's 2D top-down view, where nothing shows height or facade
(`Imperium-Knowledge/14_来源同步与权威.md` L273; `Imperium-Knowledge/designs/回报/改法-入口瘦身-2026-11-10.md` L156). In
that view walls run in eight directions (`Imperium-Knowledge/14_来源同步与权威.md` L273), and houses in the city take one
of three orientations, horizontal, vertical or 45°, following the street in front of them
(`Imperium-Knowledge/09_地图生成与CBF技术.md` L845) (replaces `Imperium-Knowledge/14_来源同步与权威.md` L273, which
allowed houses only horizontal and vertical).

Imperium learns the meaning of a reference, not its shape: the outlines of reference images, historic cities and
geometric figures are not carried onto a city, the outline is set by the city itself, and the Roman feel does not come
from the outline but from the idea (`Imperium-Knowledge/designs/tools/默认用规则.md` L92, L168, L169;
`Imperium-Knowledge/designs/派活/任务书-外形三版-乙.md` L6; `Imperium-Knowledge/designs/回报/进度-退第一批.md` L28-29). The
errors the user corrected on city shape were taking ancient Rome as reference, taking a single case as the body of the
city, fitting a ready-made shape onto the city, saying the Roman feel comes from the outline, fixing the outline first
and letting the city fill it, taking the user's earlier words or recognised references as the answer, and claiming a
benefit of placing in RimWorld without checking it (`Imperium-Knowledge/designs/回报/工具统计-2026-11-12.md` L134-152).

References and real cities are used for their ideas: why a wall runs as it does, what it attaches to and what it
protects. Angles and scales, such as the 16 directions, tower spacing and cell counts, are fixed by the game's effect and
are not measured from reference images or real cities; rules serve the effect of a Roman city, and where a rule and the
effect conflict, the effect wins (`Imperium-Knowledge/14_来源同步与权威.md` L168;
`Imperium-Knowledge/designs/做法史/罗马城·做法与顺序.md` L46, L147). This does not hold for the Anno sample, whose
proportions are followed (`Imperium-Knowledge/designs/做法史/罗马城·做法与顺序.md` L147, L168). Work on city shape names
first the approved reference picture to open, from the list below (`Imperium-Knowledge/designs/回报/改法-入口瘦身-2026-11-10.md`
L155, L168; `Imperium-Knowledge/designs/回报/规则表-2026-11-11.md` L40).

### The Anno 117 river-bend settlement

The Anno 117 river-bend settlement (《Anno117-河湾聚落》, `Imperium-Knowledge/designs/city-plans/Anno117-河湾聚落.png`)
is an accepted reference for the city, for its idea and not its shape. One reason, the river bend, fixes the whole city:
its districts, the bridge, a main street that crosses the river once, and a wall whose two ends meet the river. The wall
follows the city with unequal sides and obtuse turns, and the city fills the wall. River bend, straight wall runs and the
three scales of dwelling are kept distinct, and large buildings press on the city's edge and corners. Districts and
blocks are not divided equally (`Imperium-Knowledge/现行/城/罗马城-做法与顺序.md` L180;
`Imperium-Knowledge/09_地图生成与CBF技术.md` L793). What cannot be taken are the roofs and tree shadows of its oblique
view; its slanted blocks can be taken (`Imperium-Knowledge/现行/城/罗马城-做法与顺序.md` L180) (replaces
`Imperium-Knowledge/09_地图生成与CBF技术.md` L793, which did not take slanted blocks). The reference city is a player's
city built in the game's demo, where only the first two population tiers were open, so its layout is a player's choices
under Anno's rules (`Imperium-Knowledge/designs/研究/城/纪元117-设计理念-地图与城建-2026-11-11.md` L36).

From Anno 117 only the layout thinking is borrowed; its assets are not used (`Imperium-Knowledge/14_来源同步与权威.md`
L325). Its mechanic of buildings adding and subtracting attributes is not taken, since the user does not want functions
that add numbers directly; what is taken is the principle that where a thing is placed has a reason that can be stated
(`Imperium-Knowledge/designs/回报/配套表/没进表的.md` L48-50;
`Imperium-Knowledge/designs/研究/城/纪元117-设计理念-地图与城建-2026-11-11.md` L22). Houses upgrading by service radius
are not taken either, since Imperium's houses do not upgrade and a radius would make an even grid of 2×3 small blocks,
nor workshops collecting goods within a warehouse's range (`Imperium-Knowledge/designs/回报/配套表/没进表的.md` L48-50).

The settlement is grafted onto RimWorld's logic as a cell-level sample, the Anno sample (纪元样张): its East plaza (东广场)
and West city (西城) blocks with the river and main bridge between them, kept for side-by-side comparison; later city
layouts are compared with it and follow its proportions, and where it differs from the Roman rules the differences are
listed for the user to judge by the picture (`Imperium-Knowledge/现行/城/罗马城-做法与顺序.md` L144;
`Imperium-Knowledge/designs/tools/city/说明/sample.md` L4; `Imperium-Knowledge/designs/做法史/罗马城·做法与顺序.md`
L168). The whole settlement, with its bend, island and banks, becomes template 1, described in
[cities-forms.md](cities-forms.md) (`Imperium-Knowledge/现行/城/罗马城-做法与顺序.md` L144). At 1:1 the Anno reference is
the highest authority: its thinking is learned from the finished picture first, Imperium's own layout is made from what
was learned, the whole city is finished before it is scaled, and what is reduced or merged is decided by Imperium from
the buildings it placed (`Imperium-Knowledge/09_地图生成与CBF技术.md` L915; `Imperium-Knowledge/designs/tools/方向表.md`
L26; `Imperium-Knowledge/designs/研究/城/布置思路.md` L14; `Imperium-Knowledge/现行/城/罗马城-做法与顺序.md` L149). The
second reference city is another Anno 117 showcase city on different terrain, mountain or coast
(`Imperium-Knowledge/现行/城/城建-生成流程.md` L39).

### Approved reference images

Approved reference images and the original images given in conversation are kept under `designs/city-plans/`, and each
round's images are set beside them at the same scale; where a whole city does not match them, several historical city
templates are made, as with the Constantinople base map, to find the reason
(`Imperium-Knowledge/现行/城/罗马城-做法与顺序.md` L200, L203). Approved images are not deleted, whatever replaced method
they belong to (`Imperium-Knowledge/designs/整理/整理方案-2026-11-02.md` L349). The approved images, left where they are,
are (`Imperium-Knowledge/现行/城/罗马城-做法与顺序.md` L184-197):

- `Imperium-Knowledge/designs/city-plans/图三-配合地形的城区.png` (image three), one of three sketches found more useful
  than building by weights, read for terrain change, a river through the city and the old road
  (`Imperium-Knowledge/现行/城/罗马城-做法与顺序.md` L186;
  `Imperium-Knowledge/designs/回报/审查-城建版本盘点-2026-11-10.md` L19).
- `Imperium-Knowledge/designs/city-plans/平地J平面-v10-材质渲染.png`, the finished plan of the flat city among the same
  three (`Imperium-Knowledge/现行/城/罗马城-做法与顺序.md` L188).
- `Imperium-Knowledge/designs/city-plans/constantinople/君士坦丁堡-底图-v3.png`, approved for terrain and city wall
  (`Imperium-Knowledge/现行/城/罗马城-做法与顺序.md` L190) (replaces `Imperium-Knowledge/designs/整理/整理记录-2026-11-02.md`
  L94, L129, the Constantinople 1025 version and terrain-and-wall v2).
- `Imperium-Knowledge/designs/city-plans/图一-城区.png`, its composition taken, three details set separately
  (`Imperium-Knowledge/现行/城/罗马城-做法与顺序.md` L191).
- `Imperium-Knowledge/designs/city-plans/sketches/罗马城-典型-理解草图.png`, accepted with its small lanes kept
  (`Imperium-Knowledge/现行/城/罗马城-做法与顺序.md` L192).
- `Imperium-Knowledge/designs/city-plans/handcity/汇流河口图-生成城-v12乙.png` with
  `Imperium-Knowledge/designs/city-plans/handcity/汇流河口图-骨架-v12乙.json`, kept only for comparison
  (`Imperium-Knowledge/现行/城/罗马城-做法与顺序.md` L193).
- `Imperium-Knowledge/designs/city-plans/handcity/汇流河口图-墙草图-v4.png`, kept to show that an empty city whose wall is
  drawn first is at most a neat fortress (`Imperium-Knowledge/现行/城/罗马城-做法与顺序.md` L194).
- `Imperium-Knowledge/designs/city-plans/Anno117-河湾聚落.png`, read as above
  (`Imperium-Knowledge/现行/城/罗马城-做法与顺序.md` L195).
- `Imperium-Knowledge/designs/city-plans/第二段-R1-Medieval-L-Terrain-map300.png` (R1), the medieval large-city middle
  image of the second stage (`Imperium-Knowledge/现行/城/罗马城-做法与顺序.md` L196).
- `Imperium-Knowledge/designs/city-plans/第二段-S49-MM-River-map250.png` (S49), the medieval medium-city middle image of
  the second stage (`Imperium-Knowledge/现行/城/罗马城-做法与顺序.md` L197).

The city outlines of R1 and S49 were grown from the core, and they serve as samples that output is set beside
(`Imperium-Knowledge/现行/城/罗马城-做法与顺序.md` L52; `Imperium-Knowledge/designs/回报/审查-城建版本盘点-2026-11-10.md`
L8). An image marked abolished is not a reference (`Imperium-Knowledge/现行/城/罗马城-做法与顺序.md` L201).

> [!NOTE]
> **Deleted**: the octagonal plain city, the approved references
> `Imperium-Knowledge/designs/city-plans/plain/平原城-宫区收进城内.png` and
> `Imperium-Knowledge/designs/city-plans/sketches/平地J-街网草图-v8.png` (`Imperium-Knowledge/现行/城/罗马城-做法与顺序.md`
> L187, L189), was abolished, and new work neither compares with it nor lays out by it
> (`Imperium-Knowledge/09_地图生成与CBF技术.md` L903-904; `Imperium-Knowledge/designs/tools/方向表.md` L13, L51-52).

Five images the user gave in conversation were not kept: the section of a city-gate palace tower, a group of waterside
public buildings with a lighthouse, a church group with courtyard and cloisters, a Roman city on an island, and a bird's
eye view of a river around a city. The river view gives the skeleton, the island city the flesh and public core, a
reconstruction plan of Constantinople the streets and density, and the gate section and church group the manner of
building (`Imperium-Knowledge/现行/城/罗马城-做法与顺序.md` L142;
`Imperium-Knowledge/designs/整理/复盘-城建-近百版的基础错-2026-11-05.md` L62). The reading of them draws a skeleton of a
river winding from where it enters the map, a palace quarter at a river bend by the water, a harbour basin cut into the
city, a small district on the far bank joined by two or three bridges, and a wall laid last following the city
(`Imperium-Knowledge/designs/city-plans/罗马理想城-参照图读法-2026-10-30.md` L7-15). Not learned from them are cliffs
with upper and lower cities, circus and amphitheatre, the coloured roofs, domes, spired castles and wholly grown streets
of the river view, and ships, of which only the harbour basin and quay are made
(`Imperium-Knowledge/现行/城/罗马城-做法与顺序.md` L143).

The four settlement design atlases of 2026-10-27, Roman, medieval, modern and tribal, each in small, medium and large
with facilities, twenty images in all, are sketches rather than game screenshots; their numbers follow the batch
instructions, and deliveries were set beside the drawings of the same name (`Imperium-Knowledge/09_地图生成与CBF技术.md`
L321-323; `Imperium-Knowledge/11_开发进度与未决事项.md` L34). They are kept in `Imperium-Knowledge/designs/聚落设计图/`,
indexed by `Imperium-Knowledge/designs/聚落设计图/README.md`; their Roman sheets, a Justinian and a Basil set, belong to
the two-set line deleted below (`Imperium-Knowledge/09_地图生成与CBF技术.md` L321).

### Community references

Community references are used only for what will be seen in the game, and none of the community's methods is adopted:
hand-made templates assembled at random by tag and count are not Imperium's way, circles are not drawn on purpose,
Imperium's taste rests on what could be achieved in reality, every place needs a real reason, and plain permutation is
of no use; what can be used are facts about rendering limits
(`Imperium-Knowledge/designs/city-plans/社区参照-罗马城与聚落生成-2026-10-30.md` L6).

> [!NOTE]
> **Unverified**: these reports are not ruled. The report on why city-builder walls are expressive says that city-builder
> games support "the city grows first, the wall wraps it after", taking only ideas, not sizes or geometry
> (`Imperium-Knowledge/designs/city-plans/社区参照-城建游戏城墙表现力-2026-11-03.md` L2, L6). The reports on Anno 117
> read it as follows: the generator behaves like a reasonable player, starting from port, bridgehead and approach road,
> growing along the road, filling what the terrain encloses and stopping at constraints, so that a plain with few
> constraints has no reason for an organic outline; limited buildable space is the source of the puzzle; island size and
> house size are decided together, as a city's households and their size are to be fixed with its site; the grid is kept
> and only 45° is added, houses following roads; services follow the road, so roads come first; Anno builds the city first
> and the wall after; and a hand touch layer cannot be kept for every generated map and is to be replaced by placement
> rules (`Imperium-Knowledge/designs/研究/城/纪元117-设计理念-地图与城建-2026-11-11.md` L8-21, L29, L34, L77). The
> report on the Anno city's whole form proposes picture checks: the city fills the ground enclosed by water, rock and soft
> ground; housing ground and wall colour are pressed to one or two kinds with large pieces standing out; and each large
> piece takes a whole block ringed by garden, trees or plaza at the edge, corner or end of an axis
> (`Imperium-Knowledge/designs/研究/城/纪元117-罗马城整体造型-2026-11-10.md` L146-150), with readings A1 to A8 for
> RimWorld (`Imperium-Knowledge/designs/研究/城/纪元117-罗马城整体造型-2026-11-10.md` L88-102); the recommendations
> and two alternatives wait for the user
> (`Imperium-Knowledge/designs/回报/调研-纪元117罗马城整体造型.md` L20-24). Which of the officially chosen Anno player
> cities the user picks, and what is learned from them, is open
> (`Imperium-Knowledge/designs/研究/城/纪元117-聚光城单-2026-11-12.md` L5, L36-40).

### Historical replication and city measuring

Historical replication serves only to draw out what Roman builders had in common in building walls, building cities and
dividing city areas, grafted onto the Roman kit; no sample is divided or labelled by era, and which cities are replicated
and in what order the user decides (`Imperium-Knowledge/现行/城/罗马城-做法与顺序.md` L212;
`Imperium-Knowledge/09_地图生成与CBF技术.md` L721). Antioch and Alexandria are not made
(`Imperium-Knowledge/09_地图生成与CBF技术.md` L721). Only city walls and terrain are replicated, the terrain restored on
the real outline at 325×325 cells, Thessaloniki first (`Imperium-Knowledge/designs/city-plans/history/进度.md` L4).
Replication is faithful, neither stylised nor corrected to Imperium's rules; where history and the rules conflict this is
noted for the user and history is not changed to fit; replication yields only replica images and logic cards, kept in
`designs/city-plans/history/<city>/`, and touches neither the hand-laid cities, the main-line generator nor the rules, a
finding that calls for a rule change going into the logic card for the user to decide
(`Imperium-Knowledge/现行/城/罗马城-做法与顺序.md` L215-216).

Thessaloniki is replicated for New Rome about 1025: the research defines the new period as the 10th to 11th century and
the old as the 1st to 2nd, covers walls and terrain only, and found no full reconstruction drawing of the circuit for the
new period (`Imperium-Knowledge/designs/city-plans/history/塞萨洛尼基/史料-墙与地形.md` L4-7, L325). On the base map at
9 m per cell the ring is about 8.7 km, about 262 ha inside, with 57 towers
(`Imperium-Knowledge/designs/city-plans/history/进度.md` L7-11).

> [!NOTE]
> **Unverified**: whether the Thessaloniki replica looks right waits for the user
> (`Imperium-Knowledge/designs/city-plans/history/进度.md` L11).

City measuring (量城) measures replicas of real Roman cities and the design's wall sketches and skeletons with one ruler,
item by item side by side, to read the idea: the numbers show how the Romans laid things out, such as the share of wall
touching landforms or how many stops a main street strings, and a real city's angles and sizes are not moved into
Imperium's cities (`Imperium-Knowledge/designs/city-plans/量城/README.md` L4;
`Imperium-Knowledge/现行/城/罗马城-做法与顺序.md` L213-214). Quantities that terrain decides, such as the share of land
wall or the core's distance from water and from the land wall, are only references, and only methods that do not change
with terrain enter rules (`Imperium-Knowledge/现行/城/罗马城-做法与顺序.md` L135).

The measured set is the Constantinople replica of about 1025, the hand-laid wall sketch v3 and the skeleton v12乙 of the
confluence-estuary map (汇流河口图) (`Imperium-Knowledge/designs/city-plans/量城/README.md` L9-17), with the Anno 117
settlement measured on its own card. The Constantinople replica has a wall of 917 cells in 45 segments, 31.7% of it on
land, no rock as wall, six land gates, 75 towers and the Augustaion as its first square
(`Imperium-Knowledge/designs/city-plans/量城/君士坦丁堡-量数卡.md` L8-14, L66); its tower spacing is the drawing rule of
its base-map script, not history, and it has no sea gates or approach roads
(`Imperium-Knowledge/designs/city-plans/量城/README.md` L42-46). The skeleton v12乙 has a wall of 508.2 cells in 14
segments, 62.2% on land, every corner at 45°, 24 towers and five gates
(`Imperium-Knowledge/designs/city-plans/量城/骨架-v12乙-量数卡.md` L8-14, L35, L53). The Anno settlement has a closed wall of
1730.9 cells in 75 segments, 87.9% on land and without towers, six gates, a ratio of 1.114 along the water, its first
core at the east square of the main bridge where the ferry crossed, and a typical household, the craftsman house with
L-shaped yard (A2), of 143 cells (11×13) (`Imperium-Knowledge/designs/city-plans/量城/Anno117-河湾聚落-量数卡.md`
L4-14, L55, L68-72, L85-98, L147-149). Where the three measured cities fall in one band the result is only a common-point candidate;
whether it is a Roman rule is for the literature and the user to judge
(`Imperium-Knowledge/designs/city-plans/量城/对照-君士坦丁堡-草图v3-骨架v12乙.md` L4, L40-72).

The study of ten real city sites across the two flourishing periods, from public web literature without elevation maps
(`Imperium-Knowledge/designs/city-plans/真城址研读-文献-2026-10-30.md` L4-5), found that large rivers lie outside a city
or at its edge and what is enclosed is mostly small streams, that no river was turned into a water line, supply always
coming from aqueducts, springs, wells or cisterns, and that outlines are mostly irregular, from coast or peninsula, hills
and citadels, enclosed suburbs or buildings, and late shrinking, while the street grids inside are often regular
(`Imperium-Knowledge/designs/city-plans/真城址研读-文献-2026-10-30.md` L110-113). A survey of how emperors founded and
rebuilt cities draws twelve ideas as concepts, among them an axis that comes before everything with palace, plazas and
gates hung on it, a palace group at one corner or side beside water, a grid following the long side of the main terrain,
older roads crossing the grid diagonally, and a wall built last that encloses more than the built area
(`Imperium-Knowledge/designs/罗马理想城调研-2026-10-29.md` L61-74).

## The eras of the Roman city

### One set of rules

Building cities, building walls and dividing city areas are not divided by era; the Roman kit has one set of rules
(`Imperium-Knowledge/现行/城/罗马城-做法与顺序.md` L12). Ancient Rome (古罗马) and New Rome (新罗马) separate only the
skin and content of cities and objects: ancient Rome is the old empire and its ruins, with temples and ancient Roman
roadside graves; New Rome is the present Empire and its living cities, with churches and cemeteries in the city; a
living city also has cemeteries outside its gates, the base game's graves and sarcophagi taking New Rome's look
(`Imperium-Knowledge/现行/城/罗马城-做法与顺序.md` L13; `Imperium-Knowledge/designs/回报/参照只取继承/盘点.md` L93,
L143). The whole city takes New Rome's skin, and its feeling of age comes only from card details and how new or old the
shop fronts are (`Imperium-Knowledge/09_地图生成与CBF技术.md` L749). New Rome is a living city whose legitimacy is its
continuity: old walls and gates are maintained heritage, and decay is given only to ancient Roman ruins
(`Imperium-Knowledge/现行/城/罗马城-城内.md` L201; `Imperium-Knowledge/09_地图生成与CBF技术.md` L788).

> [!NOTE]
> **Deleted**: the two-set line, in which Rome had two sets by period, a Justinian or ancient set and a Basil or later
> set, called J and B: J the colonial city planned frame first, B the fortress city grown from a citadel and a straight
> street, each with its own order of generation, rows, examples and settlement sheets, and the two periods named old and
> new peak (`Imperium-Knowledge/09_地图生成与CBF技术.md` L145-147, L321-323, L427, L555-561;
> `Imperium-Knowledge/designs/instructions/生成第2轮重做-第一段批准与第二段补充.md` L457-579, L588-637;
> `Imperium-Knowledge/01_项目宪章与规范索引.md` L180). One Roman kit with regional skins and the names ancient Rome and
> New Rome, which separate only skin and content, replaced it (`Imperium-Knowledge/09_地图生成与CBF技术.md` L581, L724;
> `Imperium-Knowledge/现行/城/罗马城-做法与顺序.md` L12-13, L18), and the type identifiers JustinianCity and BasilCity
> were renamed arid and temperate (`.github/deprecated-terms.json` L597-622).

### The two flourishing periods

The design draws on the two flourishing periods of Rome as concepts: the old period of the 1st to 2nd century and the
new of the 10th to 11th (`Imperium-Knowledge/designs/city-plans/真城址研读-文献-2026-10-30.md` L4-5;
`Imperium-Knowledge/designs/罗马理想城调研-2026-10-29.md` L4); the survey of Roman houses takes the first as the 1st
century BC to the 2nd century and the second as the 6th century and the 10th to 12th
(`Imperium-Knowledge/designs/roman-cards/罗马住宅调查-2026-10-28.md` L2-10, L52-53). In the old period emperors built new
colonnaded avenues and plazas, city public buildings and aqueduct-fed monumental fountains, with wall circles very large
or absent; in the new they laid no new street grids, funded palace, monastery and charity groups inside existing cities,
and made recovered cities seats of military districts with weight on citadel and walls
(`Imperium-Knowledge/designs/罗马理想城调研-2026-10-29.md` L4, L76-77).

> [!NOTE]
> **Unverified**: the study of what the two periods share is a first round and is not ruled. It lists eight shared
> traces: a main street with colonnades and shops inside them; shops below and living above, with shops, workshops and
> houses mixed in one street; houses turned inward on a yard with few openings to the street; public water points and
> private water, with cisterns and wells taking over when aqueducts fail; one ceremonial avenue stringing gates, squares
> and palace; palace and circus as a group; gardens and land inside the wall, with large open cisterns; and colonnaded
> streets and squares taken over bit by bit by shops, tolerated while they do not block the way
> (`Imperium-Knowledge/designs/city-plans/罗马痕迹-两盛期共同规律查证-2026-10-30.md` L4-19); the method draft before it
> had found in both periods a house round a courtyard, with well and hearth in the new period and a peristyle garden in
> the old, and street-front rooms as shops and workshops mixed along the street
> (`Imperium-Knowledge/designs/city-plans/现实街坊研究-方法草案-2026-10-30.md` L28). It lists differences:
> graves outside the city on the great roads in the old period and beside churches and monasteries in the new; one
> central square against several church-centred blocks; paved secondary streets against unpaved ones squeezed between
> houses; a large wall circle against a small walled city of citadel and lower town; many public baths against few held
> by monasteries; markets in squares against large gatherings outside the wall
> (`Imperium-Knowledge/designs/city-plans/罗马痕迹-两盛期共同规律查证-2026-10-30.md` L21-30). Its next round was to
> redraw real windows, write the shared traces as cause, result and what shows on the plan, and turn the differences into
> two skins (`Imperium-Knowledge/designs/city-plans/罗马痕迹-两盛期共同规律查证-2026-10-30.md` L59-62). Whether "shops
> below, home above" holds for the great cities of both periods is still to be checked
> (`Imperium-Knowledge/designs/city-plans/罗马痕迹-两盛期共同规律查证-2026-10-30.md` L13).

### Form and skin

Form is set by terrain and by the layout inside the city, skin by the biome; the skins are named by region, arid and
temperate, and at this stage the two versions are shared (`Imperium-Knowledge/现行/城/罗马城-做法与顺序.md` L18). Skin
governs only material colour, plants, kinds of field, gardens and the cemetery's position; any landform with any climate
can make a city, and changing the skin leaves the form unchanged, for all four factions
(`Imperium-Knowledge/designs/ICF/聚落平面语法-v4.md` L12, L372-373;
`Imperium-Knowledge/designs/instructions/生成第2轮重做-第一段批准与第二段补充.md` L332, L386-390). The city's form is
written in two rows, one without high ground and one with it (`Imperium-Knowledge/09_地图生成与CBF技术.md` L801;
`Imperium-Knowledge/designs/instructions/生成第2轮重做-第一段批准与第二段补充.md` L292, L332). Humid hot biomes take the
arid skin by temperature, their fields and crops unchanged, and extreme cold, tundra, ice sheet and sea ice, builds no
City but only Castellum, Fortlet and Burgus (`Imperium-Knowledge/01_项目宪章与规范索引.md` L182).

> [!NOTE]
> **Unverified**: the two skins are to be refined by region later; at present both are generic
> (`Imperium-Knowledge/14_来源同步与权威.md` L77).

## Principles

### As it could be in reality

The floor of the city's look is to make it as it could be achieved in reality, without hand-made templates and random
permutation and without drawing circles on purpose (`Imperium-Knowledge/现行/城/罗马城-做法与顺序.md` L26;
`Imperium-Knowledge/designs/整理/城建错题转拦截-2026-11-05.md` L39). Artistic expression comes before realism: things
that exist in reality but look cluttered, such as dead-end lanes, are not made. Rome is the planned type, drawn first
and then built, in straight lines; the medieval city is the grown type
(`Imperium-Knowledge/designs/instructions/生成具象规格-现行版.md` L128; `Imperium-Knowledge/01_项目宪章与规范索引.md`
L182).

### Rome and the medieval city

Rome is the mod's own content, with electrical equipment and machinery and without firewood, fireplaces, kilns, tilers
or other pre-industrial things. The medieval city is compatibility content and borrows from Rome only methods the two
share, such as wall components, the writing of spec cards, growth pieces and the execution method; the two are not one
logic. Before a Roman card, rule or instruction is written it is checked that no medieval object, material or way of
life has crept in, and the medieval city likewise uses no Roman electrical appliances or machinery
(`Imperium-Knowledge/01_项目宪章与规范索引.md` L183-184).

### The ground of the rules

A city's rules rest on the real Roman building law and trade practice (建筑法与行规); the "ideal city" (理想城) only names
pulling a result toward Roman style when it is too far off (`Imperium-Knowledge/现行/城/罗马城-做法与顺序.md` L29-30;
`Imperium-Knowledge/designs/做法史/罗马城·做法与顺序.md` L140; `Imperium-Knowledge/现行/索引.md` L437).

> [!NOTE]
> **Unverified**: the report on Roman building law and trade practice is a list of candidates for the user to choose
> from, not a ruling, and takes only the idea behind each article without turning its measures into cells
> (`Imperium-Knowledge/designs/city-plans/罗马建筑法与行规-理念.md` L4). It gathers its ideas under dwellings, workshops
> and trades, streets and colonnades, sight and light, and walls and gates (`Imperium-Knowledge/目录/城-住宅与建筑法.md`
> L30-61). Its five ideas that most make a city read as Roman are: public places not taken privately, with the main-street
> colonnade unbroken from gate to gate; houses with a gap and no shared wall, which conflicts with the joined side faces
> of neighbouring households in the cards and was to be ruled first; one trade gathered in an appointed place, prestigious trades near the palace and great avenue; good
> sightlines to water, landmarks and open squares; and noisy workshops drawn back behind garden or stack yard
> (`Imperium-Knowledge/designs/city-plans/罗马建筑法与行规-理念.md` L182-188), with the sightline candidate written out in
> full (`Imperium-Knowledge/designs/city-plans/罗马建筑法与行规-理念.md` L134-171). Floors, height limits, balconies,
> outside stairs and kinds of window cannot be shown from above and are dropped, their ideas merged into the items on
> house gaps, doors and yards (`Imperium-Knowledge/designs/city-plans/罗马建筑法与行规-理念.md` L180); the draft that
> pairs ideas with mechanisms drops the same, with smoke, smell, noise and two walls side by side shown as no shared wall
> (`Imperium-Knowledge/designs/city-plans/理念与机制对照-草案.md` L80-86), and only parts of that draft are adopted
> (`Imperium-Knowledge/designs/city-plans/理念与机制对照-草案.md` L4).

### Effect, readability and lasting order

Each shape rule carries one sentence on its effect, and a rule whose effect cannot be written is not admitted; each
ruling names its origin, effect, resolving a conflict, filling a gap or a copied number, and the last three are listed
for review (`Imperium-Knowledge/现行/城/罗马城-做法与顺序.md` L73; `Imperium-Knowledge/09_地图生成与CBF技术.md` L772).
Feedback leads first to its cause, and is not stacked into new rules for an algorithm to fit
(`Imperium-Knowledge/现行/城/罗马城-做法与顺序.md` L74). A city's shape is not set by ratio, since the Romans did not
build by ratio (`Imperium-Knowledge/designs/回报/审查-城卡同类冲突-2026-11-10.md` L30;
`Imperium-Knowledge/现行/城/罗马城-做法与顺序.md` L126). District rules are written as cause, result and what can be
seen on the plan, without ratios, the ratios growing out of the causes
(`Imperium-Knowledge/designs/city-plans/现实街坊研究-方法草案-2026-10-30.md` L40-41). A district is read not for what a
Roman city looks like but for why each thing in it is where it is: who lives there, what they live on, where the door
faces, where the water comes from, whose the garden is and whom the street is opened for; the answer is to hold in both
flourishing periods, and what holds in only one is recorded as a difference between them
(`Imperium-Knowledge/designs/city-plans/现实街坊研究-方法草案-2026-10-30.md` L6, L10, L39).

The city ideas are all gone over with urban architecture, which here concerns only the abstract placing of buildings
(`Imperium-Knowledge/designs/city-plans/城市建筑学对照-罗马城理念-2026-10-30.md` L4, L51). A city is readable: roads
clearly start and end, every turn has a formed node, the wall is a continuous edge, and each district has one theme of
building (`Imperium-Knowledge/designs/city-plans/城市建筑学对照-罗马城理念-2026-10-30.md` L16, L46). The lasting order
of a city is street over plot over building: the direction of old roads is hardest to change, monuments and fixed
activities are fixed points of growth, housing districts are replaceable fill, and the form stays while the function
changes (`Imperium-Knowledge/designs/city-plans/城市建筑学对照-罗马城理念-2026-10-30.md` L14). Every piece gets a use
before it gets a position, and a piece without a reason for being where it is is not placed
(`Imperium-Knowledge/designs/研究/城/布置思路.md` L12; `Imperium-Knowledge/现行/城/罗马城-做法与顺序.md` L160).

### When requirements conflict

When requirements conflict they give way from hard to soft, the earlier never yielding to the later: nothing lies outside
the circle (圈); laying out the city neither changes the circle nor makes terrain, its base being the terrain made for the
site when the map is generated, and natural obstacles inside the city area are cleared by default without counting as a
terrain change; the city is one connected whole and fills its wall; the outline is set by the city and every bend has a
source; then the Roman feel; then measured numbers (`Imperium-Knowledge/现行/城/城建-生成流程.md` L17).

### Checks

The base of the city is written as checks that must pass before delivery: blocks all of one size or aspect ratio, one
equidistant grid over the whole map, blocks beside slanted streets, banks or rock without a slanted edge, and a walled
buildable area larger than the grown city by a set proportion are errors, and each round runs at least two maps
(`Imperium-Knowledge/现行/城/罗马城-做法与顺序.md` L68; `Imperium-Knowledge/09_地图生成与CBF技术.md` L792). What is
expected is blocks of unequal size, block edges that can be oblique, and land inside the wall about equal to the city
that grew (`Imperium-Knowledge/designs/整理/复盘-城建-近百版的基础错-2026-11-05.md` L18). A city is checked for a street
network connected over the whole city (S5), a river crossing the wall (W17), the core's placement (I10), the skeleton's
required pieces (I11) and a centred core (I12); the shortest bridgehead street of 5 and the centring ratio of 0.6 are
trial values, and the list of required pieces is in `designs/tools/city/城检-参数表.json`
(`Imperium-Knowledge/14_来源同步与权威.md` L271). The orderly look, the share of straight main and secondary streets,
whether long straight streets of 40 cells or more end on something that closes the view, the spread of tower spacing,
the outline, the composition of housing and the wall's distance from the built area, is reported only, without targets
(`Imperium-Knowledge/designs/tools/city/说明/check.md` L10, L89-96). Generated blocks are set beside a real window at the
same scale and judged by the picture, checks only stopping obvious errors
(`Imperium-Knowledge/designs/city-plans/现实街坊研究-方法草案-2026-10-30.md` L46); a review first asks by eye whether it
looks like a capital, whether it has order and whether its outline has reasons, and only then reads the measures
(`Imperium-Knowledge/现行/城/城建-生成流程.md` L32).

> [!NOTE]
> **Unverified**: the thresholds of the city check and of the texture and order figures are trial values
> (`Imperium-Knowledge/14_来源同步与权威.md` L271; `Imperium-Knowledge/designs/tools/city/说明/check.md` L10, L89-96).
> The city-check row that the ring generator printed for each case was dropped with it; whether the city check itself
> stays is not restated (`Imperium-Knowledge/09_地图生成与CBF技术.md` L905).
> Base checks on the palace quarter's place relative to the main gate, the first plaza's offset from the centroid, a main
> street hugging the river wall, one long river wall in a single direction, and ponds and rock patches enclosed by the
> wall are not yet written, their thresholds undecided
> (`Imperium-Knowledge/designs/整理/城建错题转拦截-2026-11-05.md` L4, L17, L22, L33-34).

## How a city is made

### Inside first, the wall last

The city's interior is laid first and the wall is pulled last (先内后墙), and every review judges the whole city
(`Imperium-Knowledge/现行/城/罗马城-做法与顺序.md` L80; `Imperium-Knowledge/designs/city-plans/罗马城排法-算法.md` L4;
`Imperium-Knowledge/designs/整理/城建错题转拦截-2026-11-05.md` L10, L12) (replaces
`Imperium-Knowledge/designs/整理/城建错题转拦截-2026-11-05.md` L55, the order of wall first, then pieces and streets,
then households). A city is not made wall first, drawing the outer frame or wall and then filling it; the houses come
first and the wall is pulled to the outermost blocks (`Imperium-Knowledge/designs/tools/红线表.md` L20;
`Imperium-Knowledge/designs/tools/审查清单-图面.md` L42). Each period lays its interior first, fills the seams once and
pulls its wall last (`Imperium-Knowledge/现行/城/罗马城-做法与顺序.md` L98).

### Skeleton, composite pieces and housing base

The Roman city is built in three layers, sited period by period: skeleton (骨架), composite pieces (组合件), housing base
(住宅底子), and the wall last. The skeleton is written by design as nodes, who connects to whom and what terrain each
touches, with no coordinates. A composite piece is a group of buildings with a fixed shape; design fixes its shape and
its pairings, what it touches, what it keeps away from, in which period it can be built and its interfaces, and
generation decides only where it goes. The housing base is laid by rule: plots cut along the streets, one household one
card, density falling outward, lanes passing through blocks (`Imperium-Knowledge/现行/城/罗马城-做法与顺序.md` L41;
`Imperium-Knowledge/09_地图生成与CBF技术.md` L740; `Imperium-Knowledge/designs/做法史/罗马城·做法与顺序.md` L130). Design
fixes pairings and the order of unlocking, and the generator acts as a player only in siting: each piece passes its hard
conditions first and is then chosen among the qualifying places by the skeleton's order, with no overall score
(`Imperium-Knowledge/现行/城/罗马城-做法与顺序.md` L46; `Imperium-Knowledge/09_地图生成与CBF技术.md` L740). Streets and
public facilities come first and houses after: the skeleton and composite pieces are laid first, then the attraction
field, coverage and connections are computed from what is laid, then plots are cut, tiers set and cards placed
(`Imperium-Knowledge/designs/city-plans/理念与机制对照-草案.md` L35). The buildings follow the Roman spec-card master
table v3.1 (`Imperium-Knowledge/现行/城/罗马城-城内.md` L4, L12). What the skeleton, pieces and cards are is in
[cities-forms.md](cities-forms.md), and how housing is laid in [cities-inside.md](cities-inside.md).

> [!NOTE]
> **Deleted**: the hand-drawn plan line, in which the Roman City's interior was hand-designed plan data
> that generation stretched to the terrain, cropped at mountain or water and wrapped with the wall last, with a skeleton
> of fixed slots, neighbourhood slots filled from a block library and share limits per card, together with the Roman City
> writing of that time in the ICF design, the settlement grammar and the generation spec, such as two main axes of equal
> rank and the siting of water tower, palace quarter and citadel on the highest ground
> (`Imperium-Knowledge/designs/instructions/生成具象规格-现行版.md` L173-182; `Imperium-Knowledge/designs/ICF/ICF设计.md`
> L4; `Imperium-Knowledge/designs/instructions/生成具象规格-现行版.md` L4). The void notes of those files replaced it: the plan is
> generated from the main core with the wall last, there is no block library, and ordinary housing is laid household by
> household along the street, the rules in force being the cards under `现行/城/`
> (`Imperium-Knowledge/designs/instructions/生成具象规格-现行版.md` L6; `Imperium-Knowledge/designs/ICF/ICF设计.md` L6;
> `Imperium-Knowledge/designs/ICF/聚落平面语法-v4.md` L4-6).

### Road network first

The trunk is laid first, from the bridgehead through the first plaza to each gate, then secondary streets and lanes
between the trunks, then the houses along the roads, and the outline and wall after. Effect: houses stand in rows along
the roads, and the road network is the skeleton of the city (`Imperium-Knowledge/现行/城/罗马城-做法与顺序.md` L90;
`Imperium-Knowledge/09_地图生成与CBF技术.md` L847). Roads are traced first as a network of nodes and joins, their widths
set by grade; a road does not give way to a house, and its two ends rest on a road, a gate or the map edge
(`Imperium-Knowledge/现行/城/城建-生成流程.md` L12).

### Dependency order

Everything in the city area is generated in an order of dependence: road (路), then plot (地块), then the houses touching
the plot edge, then the yard (院), then green and small decoration in the land that is left; each thing's position is set
by what is there before it, and the list of pieces decides only what to place
(`Imperium-Knowledge/现行/城/城建-生成流程.md` L11; `Imperium-Knowledge/designs/tools/方向表.md` L11;
`Imperium-Knowledge/09_地图生成与CBF技术.md` L899; `Imperium-Knowledge/designs/研究/城/布置思路.md` L8). The order of
laying a city is only this one (`Imperium-Knowledge/现行/城/罗马城-做法与顺序.md` L94;
`Imperium-Knowledge/现行/城/城建-生成流程.md` L13).

### Tracing a reference and replacing its pieces

Once templates exist, the game picks a template by world tile, mirrors, turns and stretches it, lays its large terrain
form and city skeleton, and lays the variable parts by rule; template candidates come only from tracing an approved
reference or from the design session's hand drawing, not from the dependency order or the old layout generator
(`Imperium-Knowledge/现行/城/城建-生成流程.md` L10; `Imperium-Knowledge/designs/回报/规矩落地与流程工具/判断类裁定盘点.md`
L61). An approved reference is traced 1:1 into cells, by household, a few very tightly packed roofs being recorded as one
household and one building, and then each piece is replaced by Imperium's own; the traced examples are distilled into a
generation order for cities without a reference (`Imperium-Knowledge/现行/城/城建-生成流程.md` L11;
`Imperium-Knowledge/designs/tools/方向表.md` L10; `Imperium-Knowledge/designs/回报/进度-读地块入口.md` L14). The
self-check adds whether the city looks grown: the share of shared walls or aligned houses, on how many sides a yard is
enclosed, into how many pieces green space breaks, into how many segments a road is cut, and how many kinds of element
there are, with the traced Anno version as the standard (`Imperium-Knowledge/现行/城/城建-生成流程.md` L11;
`Imperium-Knowledge/09_地图生成与CBF技术.md` L899). Effect: it looks grown, neither empty nor cluttered
(`Imperium-Knowledge/现行/城/城建-生成流程.md` L11). The grass standard is a reference, not a threshold; beyond its range
one sentence says why (`Imperium-Knowledge/现行/城/罗马城-做法与顺序.md` L171;
`Imperium-Knowledge/designs/回报/进度-拷打入账.md` L23).

> [!NOTE]
> **Unverified**: the standard values of visible green inside the wall are proposals inferred from the reference, "由用户定":
> dense core about 10 to 18%, edge housing 13 to 33%, island 7 to 19%, palace and gardens about 17 to 20%; the same page
> also gives corrected values of about 18 to 20% for the palace and 8 to 20% for the island, and the sample's green
> exceeded the reference in all nine boxes (`Imperium-Knowledge/designs/研究/城/纪元资料/河湾聚落尺度查证.md` L81-86,
> L106, L111). Whether the palace standard is quoted with the water misreading removed or measured again is for the user
> to choose (`Imperium-Knowledge/designs/回报/草地量具独立核.md` L15).

The unit of learning is the district: what a district holds, the coordinates of its pieces and their relations, not what
one house should have; each piece can state its reason for being in the district, and scattered pieces without a reason
are not placed (`Imperium-Knowledge/现行/城/罗马城-做法与顺序.md` L160; `Imperium-Knowledge/designs/tools/方向表.md`
L27; `Imperium-Knowledge/designs/研究/城/布置思路.md` L9; `Imperium-Knowledge/designs/回报/进度-拷打入账.md` L21). What is
learned is recorded by district type as a district spectrum (片区谱), shared by later cities, which sets how many
households a district has and how large each is (`Imperium-Knowledge/现行/城/罗马城-做法与顺序.md` L171;
`Imperium-Knowledge/designs/tools/方向表.md` L28; `Imperium-Knowledge/designs/做法史/罗马城·做法与顺序.md` L195-196);
variety goes through a library of fragments, the spectrum only choosing cards and checking numbers
(`Imperium-Knowledge/designs/做法史/罗马城·做法与顺序.md` L209), and the spectrum's form is in
[cities-forms.md](cities-forms.md). A reference district is traced only to blocks, building groups, yards and roads, not
building by building; each piece first gets its use, and is then placed by that use's relations in the spectrum
(`Imperium-Knowledge/现行/城/罗马城-做法与顺序.md` L172; `Imperium-Knowledge/designs/研究/城/布置思路.md` L11-12).

Before a piece is placed it is checked: it has a use and is positioned by the spectrum's relation row; its step in the
dependency order is kept; it can say why it is there, or it is a stray and not placed; household count, mix and size
agree with the spectrum; a building with its annex and yard is one piece; a road has a grade before a width, and widths
are odd unless a source gives an even one; building counts per card stay within the cap and neighbouring same cards have
variants; green lies only in leftover land, none in the district's centre; and changed terrain follows the spectrum's
row for it, checking both the row with high ground and the row without
(`Imperium-Knowledge/designs/研究/城/布置思路.md` L50-59).

Template 1 is first read at 1:1, why each Anno plot holds its house, matched to Imperium's cards, its gaps filled step by
step and only then scaled (`Imperium-Knowledge/现行/城/罗马城-做法与顺序.md` L148). Imperium's own layout first tried
keeping the reference's road network and plots and laying its cards inside them by the reference's thinking, learning
meanwhile how the coordinates and relations of the reference's pieces form (`Imperium-Knowledge/现行/城/罗马城-做法与顺序.md`
L150; `Imperium-Knowledge/09_地图生成与CBF技术.md` L916; `Imperium-Knowledge/designs/回报/进度-拷打入账.md` L20)
(replaces `Imperium-Knowledge/09_地图生成与CBF技术.md` L898, in part); after the East plaza was tried the work returned to
replacing piece by piece, keeping only the road network and swapping the houses in place for cards by the traced
original, and the details of that are in [cities-forms.md](cities-forms.md)
(`Imperium-Knowledge/现行/城/罗马城-做法与顺序.md` L151-152). The work goes district by district, each traced and shown
to the user, then laid out and shown again before the next, the first being the East plaza area
(`Imperium-Knowledge/现行/城/罗马城-做法与顺序.md` L173; `Imperium-Knowledge/09_地图生成与CBF技术.md` L919;
`Imperium-Knowledge/designs/回报/进度-拷打入账.md` L22, L25).

### Laying a city by hand first

A whole city is first laid by hand on one real terrain snapshot and turned into rules only after the user has seen and
accepted it, and the generator's output on the same snapshot is compared with it cell by cell to measure reproduction
(`Imperium-Knowledge/现行/城/罗马城-做法与顺序.md` L53; `Imperium-Knowledge/09_地图生成与CBF技术.md` L676). The approved
sketches are first dissected, what, where and why, then a city is laid by hand on real terrain for the user to approve,
then rules are drawn back out of it, the algorithm first having to reproduce the hand-laid map
(`Imperium-Knowledge/09_地图生成与CBF技术.md` L693-696). The aim is a reproducible template that learns the Roman way of
building a city as a whole and builds by it; a result unlike what was imagined does not pass
(`Imperium-Knowledge/现行/城/罗马城-做法与顺序.md` L54). A city is not measured in area and single-colour rectangles; it
has content (`Imperium-Knowledge/designs/tools/红线表.md` L22; `Imperium-Knowledge/designs/整理/城建错题转拦截-2026-11-05.md`
L16, L57). The base for changes is the user-approved templates and traced lines
(`Imperium-Knowledge/现行/城/城建-生成流程.md` L21; `Imperium-Knowledge/designs/city-plans/城建基准.md` L4). For now only
plain cities, a river through them included, are handled, and sites where rock or mountain presses on the city and wide
river mouths come later (`Imperium-Knowledge/现行/城/城建-生成流程.md` L46).

> [!NOTE]
> **Unverified**: the card still states the comparison with a generator's output, while the ring generator was dropped
> and the city now goes only by templates; whether that comparison stays is not restated
> (`Imperium-Knowledge/现行/城/罗马城-做法与顺序.md` L53; `Imperium-Knowledge/09_地图生成与CBF技术.md` L693-696, L905).

> [!NOTE]
> **Deleted**: the build-by-weights line (按权建城), the RC1 city laid by an algorithm that read the
> terrain, placed citadel, city centre and main streets by weight, grew the city by weight into a band along the avenue,
> straightened dike and river by weight and pulled the wall last, its units area and single-colour rectangles and its
> blocks drawn as equal squares (`Imperium-Knowledge/09_地图生成与CBF技术.md` L689-696;
> `Imperium-Knowledge/designs/整理/城建错题转拦截-2026-11-05.md` L61). It was stopped because the weights were guessed
> numbers, three earlier sketches being found more useful, and the weights came back only to decide what goes inside the
> circle (`Imperium-Knowledge/09_地图生成与CBF技术.md` L696, L700, L711;
> `Imperium-Knowledge/designs/回报/审查-城建版本盘点-2026-11-10.md` L19;
> `Imperium-Knowledge/designs/整理/原意走样排查-2026-11-06.md` L14; `Imperium-Knowledge/designs/整理/整理方案-2026-11-02.md`
> L463; `Imperium-Knowledge/designs/回报/审查-原意走样二.md` L66; `Imperium-Knowledge/现行/索引.md` L451).

> [!NOTE]
> **Deleted**: the ring line, in which the `city ring` generator grew a circle and laid the city inside it: with it went
> the city-building baseline (城建基准) and its outline faults, the three outline versions and the outline trials (the
> outline retreating along roads and water, the cut-corner rectangle), the v3A whole-city line and the ring grown by
> patches, the road-network-first switch, the city-check row it printed for each case, its order of first plaza,
> patches, trunk, palace quarter, large pieces, secondary streets and blocks, wall, the eight steps of laying out a city,
> the research recommendation to grow its outline as a union of pieces under a larger circle, and the questions its
> trials left open (`Imperium-Knowledge/designs/city-plans/城建基准.md` L4-30;
> `Imperium-Knowledge/designs/研究/城/成熟城建生成-外形与城墙-2026-11-11.md` L8-16, L112-137;
> `Imperium-Knowledge/designs/回报/调研-成熟城建生成.md` L21-25;
> `Imperium-Knowledge/designs/派活/放弃分支.md` L34, L39-40; `Imperium-Knowledge/designs/回报/试做-切角长方形.md` L4;
> `Imperium-Knowledge/designs/回报/试做-路网先成.md` L13-15; `Imperium-Knowledge/designs/回报/试做-圈内排城.md` L19-23;
> `Imperium-Knowledge/designs/回报/Code-第二段轮廓-导出.md` L20; `Imperium-Knowledge/designs/回报/Code-第二段轮廓复用.md`
> L31; `Imperium-Knowledge/designs/回报/基准改外缘.md` L10;
> `Imperium-Knowledge/designs/做法史/城建·生成流程.md` L12, L26; `Imperium-Knowledge/designs/tools/方向表.md` L53). A
> ruling dropped the generator, its outlines and the outline versions and sends the city only by templates, and a later
> one deleted the eight steps (`Imperium-Knowledge/09_地图生成与CBF技术.md` L905;
> `Imperium-Knowledge/designs/整理/整理记录-2026-11-02.md` L381-470, L517; `Imperium-Knowledge/现行/城/城建-生成流程.md`
> L13, L21; `Imperium-Knowledge/现行/城/罗马城-做法与顺序.md` L94).

### From framework to ICF

The city-building line works until its framework is complete, then turns to filling content, then to ICF and to
repairing ICF. The framework is complete when three things hold: tracing a reference, recording its spectrum, laying it
out, scaling it and placing it in the 350 map run through with tools and can be reproduced, one district run through to
the end sufficing, the East plaza from tracing to the 350 map, all other districts counting as content; at least two
reference cities are done, the second with no new tools; and the same kind of district spectrum laid on two different
pieces of land looks different and still reads as a Roman city (`Imperium-Knowledge/现行/城/城建-生成流程.md` L36;
`Imperium-Knowledge/designs/做法史/城建·生成流程.md` L28, L31; `Imperium-Knowledge/designs/回报/进度-拷打入账.md` L27;
`Imperium-Knowledge/designs/回报/进度-拷打入账二.md` L24, L47). The formats of template and spectrum are extensible, a
new kind of terrain not changing them, and variety comes from several reference cities, from ranges and relations
recorded in the spectrum and from terrain (`Imperium-Knowledge/现行/城/城建-生成流程.md` L37-38;
`Imperium-Knowledge/designs/研究/城/布置思路.md` L30; `Imperium-Knowledge/designs/做法史/城建·生成流程.md` L29).
Diversity matters more than speed (`Imperium-Knowledge/designs/研究/城/布置思路.md` L30). What the framework hands to ICF
is the layout table, cards, positions, uses and tiers, while room contents, people, goods and guards belong to ICF
(`Imperium-Knowledge/现行/城/城建-生成流程.md` L40). ICF is the general framework that generates fitting land for imperial
content from the plot onward and works with the whole city system; once it is done the names CBF and GL no longer appear
(`Imperium-Knowledge/designs/回报/规矩落地与流程工具/判断类裁定盘点.md` L56).

## How a city grows

### From the core

A city grows outward from its core, and the core is the first plaza, the main core (主核心), not the acropolis or the
palace quarter. The core's position is fixed at the start and the city expands outward only when its area runs short; it
is not strung inward from gates and approach roads segment by segment, and it is not pulled into a band along old roads
or great roads (`Imperium-Knowledge/现行/城/罗马城-做法与顺序.md` L84; `Imperium-Knowledge/09_地图生成与CBF技术.md` L796,
L809; `Imperium-Knowledge/designs/tools/红线表.md` L24). The old road decides by which gate it enters and the direction of its stretch through the town, and the city still grows from the
core (`Imperium-Knowledge/designs/整理/城建错题转拦截-2026-11-05.md` L24, L27). The plaza is the core because it needs
open ground to grow on every side, at the approach road and the river crossing; effect: the city grows into one mass,
where a core against rock would grow in one direction only (`Imperium-Knowledge/09_地图生成与CBF技术.md` L809). The
core is set first, and with it the city's bound and the gate positions, the actual wall being drawn last along the
bound; the concept behind it is the Roman founding that ploughed the boundary furrow and lifted the plough at the gates,
with the core set where water and roads meet (`Imperium-Knowledge/designs/city-plans/城市建筑学对照-罗马城理念-2026-10-30.md`
L8, L22).

The main core fixes the main circle, and the circle of a secondary core (辅核心) lies inside the main circle; the main
circle fixes only area and core and does not generate the wall's shape (`Imperium-Knowledge/现行/城/罗马城-做法与顺序.md`
L86). A city of small area needs no secondary core (`Imperium-Knowledge/09_地图生成与CBF技术.md` L711), and whether a
city has one is in [cities-inside.md](cities-inside.md). Rome fixes its core from the start and only expands outward
when area runs short, while the medieval city grows from village to town to city and later clears its core and rebuilds
it regularly (`Imperium-Knowledge/09_地图生成与CBF技术.md` L700).

### The outline

The outline is grown. The attraction field and weights decide only what is placed inside the circle and do not grow the
outline; the outer edge decides only which places are to be enclosed and roughly where the guide line runs. Extension
blocks stretch along the roads, the outer ends of rows and columns differ in length, the edge is not flush, and blocks
are not lined up side by side in vertical rows. Effect: the city reads as grown from the core, and the wall as several
continuous lines of defence (`Imperium-Knowledge/现行/城/罗马城-做法与顺序.md` L85; `Imperium-Knowledge/09_地图生成与CBF技术.md`
L796; `Imperium-Knowledge/designs/整理/原意走样排查-2026-11-06.md` L14, L28;
`Imperium-Knowledge/designs/整理/城建错题转拦截-2026-11-05.md` L28) (replaces `Imperium-Knowledge/09_地图生成与CBF技术.md`
L772, the city growing block by block to an edge of grid steps). Fixing the outer shape first and letting the city fill
it is a rejected way of working (`Imperium-Knowledge/designs/tools/默认用规则.md` L170;
`Imperium-Knowledge/designs/做法史/罗马城·做法与顺序.md` L154).

With equal cost on all four sides the edge lies about equally far from the core and the city comes out roughly round; this
is a result of how it grows, not a goal. Departure from it has only two kinds of cause: force majeure, water, cliff, rock
or soft ground in the way, and actively borrowing an advantage, following a road, lying beside water, or taking rock and
water that defend themselves (`Imperium-Knowledge/现行/城/罗马城-做法与顺序.md` L118;
`Imperium-Knowledge/09_地图生成与CBF技术.md` L801) (replaces `Imperium-Knowledge/09_地图生成与CBF技术.md` L702;
`Imperium-Knowledge/designs/做法史/罗马城·墙.md` L9; `Imperium-Knowledge/14_来源同步与权威.md` L56, the ideal city close
to a circle and roundness as no goal). The shape is not fixed by proportion and comes from growing out of the city's
centre; without high ground, a city beside water has its long axis and its main street along the water, and no ratio of
length to width is set, since 1.5:1 came from Damascus alone (`Imperium-Knowledge/现行/城/罗马城-做法与顺序.md` L126-127;
`Imperium-Knowledge/09_地图生成与CBF技术.md` L801) (replaces `Imperium-Knowledge/designs/做法史/罗马城·墙.md` L9, the
shape stretched to about 1.5:1). With high ground, the first plaza of a city backed by a mountain lies on the open ground
in front of the rock, the city grows from the plaza and stops at the rock's edge, and the rock is only the edge of the
city area; the samples are S49, R1 and image three, the approved images listed under References
(`Imperium-Knowledge/现行/城/罗马城-做法与顺序.md` L128; `Imperium-Knowledge/09_地图生成与CBF技术.md` L809). The first
plaza is about equally far from the city area's edge in four directions, checked by I12
(`Imperium-Knowledge/现行/城/罗马城-做法与顺序.md` L128).

The city's outline grows on the terrain made for the site when the map is generated: it grows outward from the core,
stops at mountain foot or shore and takes them as edges, and the wall follows the city; it does not grow by tuning
weights (`Imperium-Knowledge/现行/城/罗马城-做法与顺序.md` L52). Rome's circle folds regularly, with edges only
horizontal, vertical and 45°, straight runs, and folds where terrain and direction change, so that it does not grow into
a round on flat land; the sample is the right-hand image of
`Imperium-Knowledge/designs/回报/Code-第二段轮廓-校准与核心/校准-R1-第四轮.png`, and the circle keeps the city from
leaving it throughout the ICF framework (`Imperium-Knowledge/现行/城/罗马城-做法与顺序.md` L129). Variants come from each
map's roads, rivers and rock making the city grow differently, and the circle is not changed to force a shape
(`Imperium-Knowledge/现行/城/城建-生成流程.md` L45). How the circle and the site are found is in
[cities-siting.md](cities-siting.md), and how the wall is laid round the city in [cities-walls.md](cities-walls.md).

> [!NOTE]
> **Unverified**: a report proposes, without a ruling, that
> where terrain gives an edge the city fill that ground, and only sides without a terrain edge grow toward a round
> (`Imperium-Knowledge/designs/研究/城/纪元117-罗马城整体造型-2026-11-10.md` L149, L168, L211).

### The period table

The period table has four periods (`Imperium-Knowledge/现行/城/罗马城-做法与顺序.md` L99-103;
`Imperium-Knowledge/09_地图生成与CBF技术.md` L752):

1. Founding (一期·立城): the whole skeleton (palace quarter, first plaza, main street, second plaza, main bridge, gate
   positions), the densest grid ring around the core, quay walls and quays on the river reach inside the
   city, a cemetery along the road outside the gate, and the first wall pulled at the end
   (`Imperium-Knowledge/现行/城/罗马城-做法与顺序.md` L100; `Imperium-Knowledge/09_地图生成与CBF技术.md` L801).
2. Expansion (二期·扩城): the grid grows outward, aligned slightly offset from period 1; the bath group, quays and arrival
   place, sanctuary, the district on the far bank and secondary bridges; the outer wall pulled at the end
   (`Imperium-Knowledge/现行/城/罗马城-做法与顺序.md` L101).
3. Filling (三期·填充): lanes through blocks, shops on secondary streets encroaching on the street, one small plaza with
   fountain and market for each housing district, the workshop group, and gardens near the core filled by new
   households (`Imperium-Knowledge/现行/城/罗马城-做法与顺序.md` L102).
4. Outside the city (四期·城外): gate gardens and orchards, estates along the great road, fields, which a large city does
   not place, no added cemetery outside the gates for a large city, and road beautification
   (`Imperium-Knowledge/现行/城/罗马城-做法与顺序.md` L103); a large city keeps outside its wall only the roads from its
   gates, and what lies outside each city is in [cities-outside.md](cities-outside.md)
   (`Imperium-Knowledge/现行/城/罗马城-墙外.md` L13-14).

These replace the earlier period 3 with a barracks group, a monastery on the garden belt and a district church for each
housing district, and the earlier period 4 with pasture and woodland
(replaces `Imperium-Knowledge/09_地图生成与CBF技术.md` L752; `Imperium-Knowledge/designs/做法史/罗马城·做法与顺序.md` L56,
L133); the Empire keeps no animals (`Imperium-Knowledge/现行/城/罗马城-墙外.md` L12). The period table describes how a
city grows over its periods and the traces each leaves, while a city in the game is fixed when generated
(`Imperium-Knowledge/designs/整理/原意走样排查-2026-11-06.md` L19; `Imperium-Knowledge/designs/回报/审查-城卡同类冲突-2026-11-10.md`
L27).

A large city is enlarged once; a medium city has no period 2 and only one wall; a small city has only period 1 and the
filling. Medium and small cities take the composite pieces that period 2 needs into period 1 as needed, a tier smaller,
with no enlargement and no second wall (`Imperium-Knowledge/现行/城/罗马城-做法与顺序.md` L105-107;
`Imperium-Knowledge/09_地图生成与CBF技术.md` L749, L756). They have no old wall line, and where their large pieces go is
in [cities-inside.md](cities-inside.md) (`Imperium-Knowledge/现行/城/罗马城-城内.md` L110-111).

### Enlargement and its traces

From period 2 the wall line of period 1 becomes the old-town boundary ring (旧城界环): the old gate positions become round
plazas, the old wall belt becomes the large-piece belt (大件带), holding garden plots with the base game's crops, of which
there may be many, and depots, and the ring street may be broken (`Imperium-Knowledge/现行/城/罗马城-城内.md` L200;
`Imperium-Knowledge/designs/city-plans/城市建筑学对照-罗马城理念-2026-10-30.md` L23, L51) (replaces
`Imperium-Knowledge/designs/city-plans/城市建筑学对照-罗马城理念-2026-10-30.md` L52, the old wall line as a ring street
with the gate arch kept). The large-piece belt exists only from period 2; against the present wall only
the ring road (环城路) is left, with no garden between wall and blocks, and the city inside the first wall is full
(`Imperium-Knowledge/designs/回报/审查-城卡同类冲突-2026-11-10.md` L28, L32, L41, L43;
`Imperium-Knowledge/09_地图生成与CBF技术.md` L789). Around a wall, inside and outside, the things that need much land
gather first, and the next enlargement takes them in (`Imperium-Knowledge/designs/city-plans/城市建筑学对照-罗马城理念-2026-10-30.md`
L13).

Period 2 also leaves these traces: several stretches of old wall are kept as maintained monuments and district
boundaries, with streets passing through newly opened arches; an old gate made a round plaza keeps its gate tower; the
straight street of period 1 meets the old wall line at a T-junction, so that the grid of period 2 reads as added later;
and the outer wall's gates open where the old approach roads cross it, new gate, old gate and the street between them in
one line (`Imperium-Knowledge/现行/城/罗马城-城内.md` L201; `Imperium-Knowledge/09_地图生成与CBF技术.md` L788). The
cemetery that period 1 laid along the road outside the gate is enclosed by the outer wall and kept as a church graveyard
(`Imperium-Knowledge/现行/城/罗马城-城内.md` L202; `Imperium-Knowledge/designs/回报/审查-城卡同类冲突-2026-11-10.md` L27).
Effect: the city of period 2 shows an old city boundary and its gates (`Imperium-Knowledge/09_地图生成与CBF技术.md`
L788).

The planned grid is the oldest layer and later things lie over it: lanes split out of blocks, secondary streets taken by
shops, the old wall line and old gates, a church standing where an old public building stood, and shop fronts of mixed
age; the colonnades of the main street stay continuous, and shops encroach on the street only on secondary streets
(`Imperium-Knowledge/现行/城/罗马城-城内.md` L195; `Imperium-Knowledge/09_地图生成与CBF技术.md` L749). Each period
fills the gaps once, and garden plots near the core that earlier periods left are filled by new households later
(`Imperium-Knowledge/现行/城/罗马城-城内.md` L196). Where a river runs through the city, whether the far bank becomes a
district and how the wall encloses it is in [cities-outside.md](cities-outside.md)
(`Imperium-Knowledge/现行/城/罗马城-做法与顺序.md` L108).

> [!NOTE]
> **Unverified**: the open items of the city cards are tracked on live lists #71, #72 and #73
> (`Imperium-Knowledge/现行/城/罗马城-做法与顺序.md` L224).
