# Templates, kits and spec cards

This section covers the forms in which Imperium's city design is held: the template (版型) that fixes a whole city
site, a culture's kit (套件) and the city file, the skeleton (骨架), the group (组合件), the city grammar
(聚落平面语法), the area spectrum (片区谱) with its fragments (片段), the spec card (规格卡) with its card families,
and the generic pieces (构件) and object roles that cards draw on. What a city is, its eras, and the order in which it
is made and grows are in `cities.md`; site types, map sizes and terrain are in `cities-siting.md`; walls, towers and
gates are in `cities-walls.md`; the core, the palace quarter, squares, streets, households, the fill of plots, the
attraction field and building materials are in `cities-inside.md`; water and the land outside the walls are in
`cities-outside.md`.

## How the forms fit together

A settlement map is made in three layers: GL grows the detail of the landform, the template fixes the whole city site
by designing its terrain big shape together with the city skeleton, and spec cards and groups give the buildings and
yards (`Imperium-Knowledge/09_地图生成与CBF技术.md` L867). A city goes only through a template: an accepted reference
is traced 1:1 into cells and then replaced item by item with Imperium's own items
(`Imperium-Knowledge/09_地图生成与CBF技术.md` L905; `Imperium-Knowledge/designs/tools/方向表.md` L10, L12;
`Imperium-Knowledge/designs/派活/任务书-工具-city命令与校验.md` L10;
`Imperium-Knowledge/designs/回报/调研-自造件全表对社区.md` L160). A city's order is governed by its dependency order,
which `cities.md` describes (`Imperium-Knowledge/09_地图生成与CBF技术.md` L906).

> [!NOTE]
> **Deleted**: The ring generator line: the ring generator `city ring` (排城生成器, with its pieces and inner modes and
> the trial values net=trunk, pal_end and clear), its three outline versions (外形三版), the city-building baseline
> (城建基准) recorded on it, with the bridgehead area as first square, a quay belt, the wall crossing the river with a
> water gate and everything kept inside the ring, and the eight steps of laying a city (排城八步) written for it
> (`Imperium-Knowledge/designs/city-plans/城建基准.md` L6-21; `Imperium-Knowledge/designs/tools/方向表.md` L48-50,
> L53). The ruling that a city goes only through a template abolished the generator, the outline versions and the
> baseline, and the next ruling deleted the eight steps (`Imperium-Knowledge/09_地图生成与CBF技术.md` L905-906, R-1112-0820,
> R-1112-0903; `Imperium-Knowledge/designs/city-plans/城建基准.md` L4;
> `Imperium-Knowledge/designs/做法史/城建·生成流程.md` L11, L26-27).

Generation places three layers period by period and draws the wall last: the skeleton, then the groups, then the
housing base (住宅底子) (`Imperium-Knowledge/现行/城/罗马城-做法与顺序.md` L41). The skeleton fixes the nodes, which
node joins which and what each node leans on in the terrain, without coordinates; a group is a set of buildings with a
fixed shape whose shape and pairings (what it stands beside, how far it keeps from what, in which period it can be
built, its interfaces) are fixed by design, so that generation decides only where it goes; the housing base is laid by
rule, with blocks cut along the streets, one card for each household, density falling outward and lanes through the
blocks (`Imperium-Knowledge/现行/城/罗马城-做法与顺序.md` L41). Design fixes the pairings and the order in which things
unlock, and the generator plays the player and only chooses sites: each item first passes its hard conditions, and
among the qualifying places it is chosen by skeleton order, with no overall score
(`Imperium-Knowledge/现行/城/罗马城-做法与顺序.md` L46). When several places qualify, the item's selection conditions
are compared in their order, the first that separates the places decides, the seed decides when none does, and each
item's reason is written as "chosen by condition N" (`Imperium-Knowledge/现行/城/罗马城-做法与顺序.md` L47;
`Imperium-Knowledge/09_地图生成与CBF技术.md` L763).

What the city framework hands to ICF is a layout table of card, position, use and tier; what is inside the rooms, and
people, goods and guards, belong to ICF (`Imperium-Knowledge/现行/城/城建-生成流程.md` L40). The formats of templates
and area spectra are extensible, so that a new kind of terrain does not change them, and variety comes from several
reference cities, from ranges and relations recorded in the spectra, and from the terrain
(`Imperium-Knowledge/现行/城/城建-生成流程.md` L37). Variety is driven by terrain plus ranges: household counts, row
lengths and use ratios are written as ranges, and cards have variants to choose from
(`Imperium-Knowledge/现行/城/城建-生成流程.md` L38; `Imperium-Knowledge/09_地图生成与CBF技术.md` L938).

## Templates (版型)

### What a template is

A template is a designed layout of a whole city site, its terrain shape and its skeleton together, which generation
picks by world tile and size and may mirror, turn and stretch (`docs/glossary.md` L209). It designs the site's terrain
big shape (river bends, islands, banks, cliffs, rock) together with the city skeleton (core, bridges, palace-quarter
corner, gates, main streets); the author makes it and rules use it, so that the big shape of every city is designed
while its detail grows from the tile (`Imperium-Knowledge/现行/城/地形与选址.md` L33;
`Imperium-Knowledge/09_地图生成与CBF技术.md` L867). A template states which of its parts are re-laid by rule
(`Imperium-Knowledge/09_地图生成与CBF技术.md` L867). Templates are the base layer of ICF's generation and are shared
by all factions, each faction's content following its own idea card; the template format merges the older city file,
replica city (复刻城) and tracing (描线) formats (`Imperium-Knowledge/09_地图生成与CBF技术.md` L867). Templates come in
the tiers large, medium and small (`Imperium-Knowledge/09_地图生成与CBF技术.md` L867), and a further tier, outpost
(哨所), was added (`Imperium-Knowledge/designs/city-plans/kit/版型格式-方案.md` L169, R-1111-1933).

> [!NOTE]
> **Unverified**: The template format (`imperium-template-1`) is marked a draft awaiting the dispatcher's word, and the
> dispatcher has given eight replies to it (`Imperium-Knowledge/designs/city-plans/kit/版型格式-方案.md` L1-2, L161-170). Its
> fuller account of a template is:
> - a template holds the terrain big shape, the skeleton, fixed items, and which parts vary, with a header used for
>   picking it: number, conditions, source, status (`Imperium-Knowledge/designs/city-plans/kit/版型格式-方案.md` L8);
> - its skeleton holds a core (the first square or a ferry crossing), bridges, an optional palace quarter (a small city
>   has none) with a palace gate and a waterside end, gates (at least one land gate), skeleton-level streets (at least
>   one main street; secondary streets and lanes belong to the variable parts), squares and the wall
>   (`Imperium-Knowledge/designs/city-plans/kit/版型格式-方案.md` L43-49);
> - fixed items are large items (大件), cards and groups; a variable part is an area with a range, the rule it is laid by,
>   a trial value for that rule, and the items inside it that stay fixed
>   (`Imperium-Knowledge/designs/city-plans/kit/版型格式-方案.md` L50-51);
> - a template carries a faction, Roman by default, with medieval, tribal, modern and others named as later factions
>   (`Imperium-Knowledge/designs/city-plans/kit/版型格式-方案.md` L26);
> - its status is candidate (候选), kept (留), frozen (冻结) or discarded (弃)
>   (`Imperium-Knowledge/designs/city-plans/kit/版型格式-方案.md` L31);
> - mirroring is an east-west flip, allowed by default, and turns are 0, 90, 180 and 270 degrees clockwise by default
>   (`Imperium-Knowledge/designs/city-plans/kit/版型格式-方案.md` L52-53);
> - stretching is set for each direction N, E, S and W as a range of multipliers (1.0, no stretch, by default) and moves
>   only the half on the side of the anchor, which is the core point; bridge width, street width, gates, towers and
>   fixed items do not stretch, a rule the dispatcher accepted (`Imperium-Knowledge/designs/city-plans/kit/版型格式-方案.md`
>   L16, L54, L167);
> - a template can name direction conditions to keep after stretching or turning, such as the side the river enters from
>   staying the tile's river side (`Imperium-Knowledge/designs/city-plans/kit/版型格式-方案.md` L55);
> - in the merger of the older formats the template is the finished product, the tracing is the hand-made working base,
>   and the replica city is for measuring real cities (`Imperium-Knowledge/designs/city-plans/kit/版型格式-方案.md` L126).

### How a template is used

When a city lands on a map in the game, a template is first picked by world tile and tier, then mirrored, turned and
stretched, and the terrain big shape and city skeleton are laid by it; the variable parts are laid by rule, and the
dependency order does not produce template candidates (`Imperium-Knowledge/现行/城/城建-生成流程.md` L10;
`Imperium-Knowledge/现行/城/地形与选址.md` L33). Where a city has a template, its palace quarter follows the
template's skeleton, and in template No. 1 the palace quarter's outline follows the existing roads
(`Imperium-Knowledge/现行/城/罗马城-城内.md` L53, R-1112-0002, decided by the design session;
`Imperium-Knowledge/designs/回报/进度-城建收尾一.md` L39).

When a template is larger than the map, it is scaled as a whole by one ratio, set only by one household being about
15×15 cells; street widths follow the scale but stay at least 3 for a lane, 5 for a secondary street and 5 for the main
trunk, and gates, towers and bridges keep their widths, so that the city's texture and its relation to the big shape
stay as they were (`Imperium-Knowledge/现行/城/地形与选址.md` L83). The scaled households become plots that are later filled
with Imperium's cards at their own size (`Imperium-Knowledge/现行/城/地形与选址.md` L84); houses are not shrunk; when, after the
screenshot calibration, a city does not fit the 350 map, it places fewer areas and takes its wall in in proportion
(`Imperium-Knowledge/现行/城/地形与选址.md` L88). The ratio is not set from the map edge, and the earlier factor of 0.822 for
template No. 1 is void (`Imperium-Knowledge/09_地图生成与CBF技术.md` L963) (replaces `Imperium-Knowledge/09_地图生成与CBF技术.md` L876
in part). If scaling would require changing the skeleton, a template of the next lower tier is used instead
(`Imperium-Knowledge/现行/城/地形与选址.md` L85).

### Where templates come from

Template candidates come only from tracing an accepted reference image, the way the Anno 117 river-bay city was traced,
and from sketches the design session draws (`Imperium-Knowledge/09_地图生成与CBF技术.md` L875;
`Imperium-Knowledge/现行/城/地形与选址.md` L34; `Imperium-Knowledge/designs/做法史/地形与选址.md` L145).

> [!NOTE]
> **Deleted**: The line of generated template candidates: the template tool first produced a dozen candidates at a time
> with the existing generators (gen, ring), and template No. 2 was to be the confluence-mouth map (汇流河口图), a large
> confluence city with a tributary joining outside the wall downstream, written up as the format's second example
> (`Imperium-Knowledge/09_地图生成与CBF技术.md` L867; `Imperium-Knowledge/designs/city-plans/kit/版型格式-方案.md` L96-122;
> `Imperium-Knowledge/designs/回报/进度-版型工具.md` L87). The candidates came out as a wall ring and area outlines
> with the river as one straight slanted line, nearly alike and none reading as a city; the ruling that followed took
> candidates away from the generators, made the confluence-mouth map no template, kept no candidate batch, and the
> No. 2 line was halted and kept out of the main branch (`Imperium-Knowledge/09_地图生成与CBF技术.md` L875, R-1111-1940;
> `Imperium-Knowledge/designs/city-plans/kit/版型格式-方案.md` L170; `Imperium-Knowledge/designs/回报/进度-版型工具.md` L9, L13, L59; `Imperium-Knowledge/designs/做法史/城建·生成流程.md` L23).

A template is made in this order: requirements are set; candidates are traced from accepted references or drawn by
hand; the user picks which to keep; the big shape is modified and frozen and the variable parts are written; and a
whole-city sample is accepted into the library (`Imperium-Knowledge/现行/城/地形与选址.md` L34). The set is filled by a
coverage table of site type, tier and tile condition, so that templates accumulate and the player does not meet the
same one (`Imperium-Knowledge/现行/城/地形与选址.md` L34).

Earlier rulings of 10-27 and 10-28 on templates (模板), which the history list names by title only and marks current,
are: layout types by terrain; the overlay order of templates and the macro landform; templates modelled on real city
sites; the city decided first, then the terrain made, then the city built; large templates containing small templates;
a first batch of about twenty large templates, with reference images extended to 20 cells and adjusted for
typicality; all 17 biomes compatible and fantasy biomes at minimum compatibility; and Imperium's own houses replacing
CBF's house templates (`Imperium-Knowledge/designs/做法史/地形与选址.md` L63-81). The same list records the medieval
template as finished (`Imperium-Knowledge/designs/做法史/地形与选址.md` L89).

> [!NOTE]
> **Unverified**: These template (模板) rulings of 10-27 and 10-28 come before the template layer (版型) of 11-11 and
> are known here only by their titles; the sources neither restate them under the template layer nor mark them
> replaced (`Imperium-Knowledge/designs/做法史/地形与选址.md` L63-81; `Imperium-Knowledge/09_地图生成与CBF技术.md` L867).

### Template No. 1

Template No. 1 is the Anno 117 river-bay settlement (《Anno117-河湾聚落》), the era river-bay city (纪元河湾城), transplanted by
the colony world's logic into a cell-level sample; later cities are compared side by side with it and proportioned by
it, and the points where it disagrees with the Roman rules are listed for the user to decide by picture
(`Imperium-Knowledge/现行/城/罗马城-做法与顺序.md` L144). The whole city, with its river bay, island and banks, lands in the game
directly as a city, without the city-area outline (城区圈) and the generator re-laying it; the whole city is traced first
and handed to code afterwards, and the whole block of the governor's villa on the north bank is replaced by the palace
quarter (`Imperium-Knowledge/现行/城/罗马城-做法与顺序.md` L144). Its 1:1 wall outer frame is 396×351 and its sample frame 398×359
(`Imperium-Knowledge/现行/城/地形与选址.md` L86).

Its large items are replaced by Imperium's groups by position, and the assembly hall, main-street colonnade, quay
group and bridgehead group that the original image lacks are added slowly, without moving the river bend, bridge or
trunk, so that the big shape is the era's and the city reads as Roman
(`Imperium-Knowledge/现行/城/罗马城-做法与顺序.md` L145). The market inside the south-east gate is replaced by a
spaceport group while the island market stays; the fire station on the island is replaced by a cathedral (主教座堂),
the only great church in the city; and the round colonnaded building in the north-west is replaced by a round square
with a memorial column, a secular landmark counted in the attraction field as a square plus a landmark
(`Imperium-Knowledge/现行/城/罗马城-做法与顺序.md` L146-147).

Its layout is done at 1:1 with the era as the highest authority: the idea is learned first from finished reference
images, then Imperium's own layout is made, the whole city is done before scaling, and what is cut or merged is decided
by Imperium's own placed buildings (`Imperium-Knowledge/现行/城/罗马城-做法与顺序.md` L149). Each plot is first read at
1:1 for the house type the era places on it and why, matched against Imperium's cards, gaps filled and cards filled
step by step, and only then is the city scaled; before cards are filled the city is divided into zones, with key items
replaced by Imperium's items as field sources and households sorted by the attraction field into rich households,
ordinary households, workshops and shopfronts (`Imperium-Knowledge/现行/城/罗马城-做法与顺序.md` L148).

The layout is done by item-by-item replacement (`Imperium-Knowledge/现行/城/罗马城-做法与顺序.md` L151). Only the
road network is kept, and houses are replaced in place by cards following the traced
originals; a card that is too big first goes one size smaller or to a variant, and if it still does not fit an issue is
opened and the road is not moved; one scale factor holds for a whole area; edits are made in place on the whole-city
1:1 replica area by area, the main axes of the road network first and squares added after beside the roads, with houses
drawn as card samples with era-style small yards and annexes (`Imperium-Knowledge/现行/城/罗马城-做法与顺序.md` L151).

> [!NOTE]
> **Deleted**: The trial layout that kept the era's road network and plots and arranged Imperium's cards inside the
> blocks by the era's idea (`Imperium-Knowledge/现行/城/罗马城-做法与顺序.md` L150;
> `Imperium-Knowledge/designs/研究/城/布置思路.md` L15). After the east-square trial the layout returned to item-by-item
> replacement and the trial way is listed as abolished (`Imperium-Knowledge/现行/城/罗马城-做法与顺序.md` L151,
> R-1112-1959; `Imperium-Knowledge/designs/tools/方向表.md` L58).

Template No. 1 is done one area at a time, each shown to the user once after tracing and once after layout, the first
being the area around the east square (`Imperium-Knowledge/现行/城/罗马城-做法与顺序.md` L173). Two ratios are kept apart: when
reading originals and measuring era buildings, one era cell is provisionally 3.7 tracing cells; when placing Imperium's
own houses, one household (one plot) is about 15×15 cells and one era cell about 5 cells; houses are not shrunk
(`Imperium-Knowledge/现行/城/罗马城-做法与顺序.md` L173; `Imperium-Knowledge/designs/研究/城/布置思路.md` L28;
`Imperium-Knowledge/09_地图生成与CBF技术.md` L960) (replaces `Imperium-Knowledge/09_地图生成与CBF技术.md` L930, L936 in part).
Template No. 1 is a large-city template, laid into the large-city map as a whole (`Imperium-Knowledge/现行/城/地形与选址.md`
L86; `Imperium-Knowledge/designs/city-plans/kit/版型格式-方案.md` L72). Its palace quarter takes the whole block around the
north-bank governor's villa that the existing roads enclose (with the land of the zoning's rich household 7), the part
beyond 6% of the land inside the wall being kept as the present woodland, and is recorded in the template
(`Imperium-Knowledge/现行/城/罗马城-做法与顺序.md` L176-177) (replaces `Imperium-Knowledge/designs/city-plans/kit/版型格式-方案.md` L168
and `Imperium-Knowledge/designs/回报/进度-版型工具.md` L88 in part). Its status is written as kept (留), to be frozen only once
the north-bank small palace quarter and the scaling rule are fixed; template 2 stays out of main
(`Imperium-Knowledge/designs/city-plans/kit/版型格式-方案.md` L168; `Imperium-Knowledge/designs/回报/进度-版型工具.md` L8-9).

> [!NOTE]
> **Deleted**: The current card also lists the lifeline among what is added to template No. 1; a Roman city's
> lifeline is its water network, which belonged to the hydraulics (水利, later the imperial aqueducts 帝国水道) the
> maintainer deleted (`Imperium-Knowledge/现行/城/罗马城-做法与顺序.md` L145; `docs/glossary.md` L187;
> `Imperium-Knowledge/15_水利主轴.md` L4).

> [!NOTE]
> **Unverified**: Template No. 1 is not yet frozen. Its scaling ratio is set by household size (replacing the format's
> "rule open until shrink and crop are compared"), but the ratio's final value awaits the user, and no scaled version
> is in the library yet, so cards are filled at 1:1 first and scaled afterwards
> (`Imperium-Knowledge/现行/城/地形与选址.md` L83, L86; `Imperium-Knowledge/designs/city-plans/kit/版型格式-方案.md` L56-57).

## Kits (套件) and city files

A kit is a culture's fixed set of generation data, such as its word list, skeleton, groups, fill and wall settings, with
one kit each for Roman, medieval, industrial and tribal settlements (`docs/glossary.md` L184). City data is of two
kinds: the kit, set by design and without coordinates (word list, skeleton, groups, housing base, fill, period table,
wall parameters), and the city file, the result of one map, in which hand layout and code output share one form and each
item records where it lies, which hard conditions it passed and by which condition it was chosen
(`Imperium-Knowledge/现行/城/罗马城-做法与顺序.md` L59; `Imperium-Knowledge/designs/city-plans/kit/城建数据格式-草案.md` L2-11). In ICF a
faction kit (阵营套件) refers to the items listed above it in the table and adds the strategy class names for each stage
(`Imperium-Knowledge/designs/ICF/ICF设计.md` L96).

Hand-laid drafts are written in the city-file form from the first day, each item saying whether it is a skeleton node
or a group, where it lands and by which pairing, as the engine's standard answer
(`Imperium-Knowledge/现行/城/罗马城-做法与顺序.md` L58). Each item records why it is there, the hard conditions it
passed and the pairing that chose it, and the output can show this as an annotation layer in developer mode
(`Imperium-Knowledge/现行/城/罗马城-做法与顺序.md` L65). A city file also keeps a log of re-placements, re-laid terrain
and conservative terrain, each with its reason, and each item records its layer: skeleton street, group, base, small
item or outside (`Imperium-Knowledge/designs/city-plans/kit/城建数据格式-草案.md` L87, L95).

The kit's word list holds the five kinds of face, with what each meets and never meets, and the face rules; the five
kinds of port, the goods port being at least 3 cells wide; the street kinds; and the terrain features (river, bank,
inner bend of a river, rock, rock head, marsh, soft ground, coast, approach, old road)
(`Imperium-Knowledge/designs/city-plans/kit/城建数据格式-草案.md` L26-36). A condition is marked hard, so that a place that
fails it is not a candidate, or pick, compared in order among the places that passed the hard ones, with no combined
score, or null; which conditions are hard and which are pick is not ruled, so for now all are written null to be set at
step ③; each placed item records the hard conditions it passed, the pick condition that chose it and how many places
qualified (`Imperium-Knowledge/designs/city-plans/kit/城建数据格式-草案.md` L32-33, L99).

The Empire's Roman settlements have one Roman kit, and the camp tiers City, Castellum, Fortlet and Burgus are tiers of
that kit (`Imperium-Knowledge/designs/instructions/生成具象规格-现行版.md` L119;
`Imperium-Knowledge/现行/城/罗马城-做法与顺序.md` L12). Form and skin are separate: form comes from the terrain and the
city's layout, skin from the biome, so that any landform can be combined with any climate; the skins are named by
region, hot-dry (干热区) and temperate-cold (温寒区), and at present both versions are shared
(`Imperium-Knowledge/designs/instructions/生成具象规格-现行版.md` L119;
`Imperium-Knowledge/现行/城/罗马城-做法与顺序.md` L18; `Imperium-Knowledge/09_地图生成与CBF技术.md` L469). The two
regional variants J (hot-dry) and B (temperate-cold) govern only materials and furnishings such as stone colour,
plants, fields and gardens, and the forms drawn on their atlas pictures are examples for the terrain drawn, not rules
of the two types (`Imperium-Knowledge/designs/聚落设计图集.md` L31) (replaces `Imperium-Knowledge/designs/聚落设计图集.md` L20).

> [!NOTE]
> **Unverified**: The city data format is a draft in which only the split into two kinds of file is approved; values
> not ruled stay empty until the hand-laid sample and step ③, which conditions are hard and which are pick is not
> ruled, and the parameter values of the attraction field and coverage are not ruled
> (`Imperium-Knowledge/designs/city-plans/kit/城建数据格式-草案.md` L2, L24, L34, L147, L201-203).

## Skeletons (骨架)

A skeleton is the fixed parts of a city's layout, such as its core, palace quarter, gates and main street, recorded as
their relations to each other and to the terrain rather than as coordinates (`docs/glossary.md` L204). A person lays
the skeleton out by hand and the program adapts it; growing a city from rules first is not used, after three
rule-based tries were rejected (`Imperium-Knowledge/designs/整理/城建错题转拦截-2026-11-05.md` L11, L55;
`Imperium-Knowledge/designs/ICF/城骨架格式-v1.md` L4). There is one skeleton for each terrain type (flat, river on one
side, river through the city, sea-facing, backed by hills) and each size, large, medium and small, and it records
relations, not coordinates, such as the main gate facing the approach or which road the fields run along
(`Imperium-Knowledge/现行/城/罗马城-做法与顺序.md` L42). It fixes the nodes, which node joins which,
and what each node leans on in the terrain, and stops there: the groups and the housing base are separate layers
(`Imperium-Knowledge/现行/城/罗马城-做法与顺序.md` L41) (replaces `Imperium-Knowledge/09_地图生成与CBF技术.md` L697 in
part; `Imperium-Knowledge/designs/做法史/罗马城·城内.md` L69). A skeleton writes only what touches the terrain and the
relations between nodes, with no coordinates or sizes, the sizes sitting in the size tiers of the groups
(`Imperium-Knowledge/designs/city-plans/kit/城建数据格式-草案.md` L49).

A skeleton for a terrain type and size lists its nodes, each must-have or conditional; who meets whom; the lifeline
chain from source through trunk and reveal to exit; the order in which nodes give way when space is short; and the
nodes that never give way (`Imperium-Knowledge/designs/city-plans/kit/城建数据格式-草案.md` L38-49). In the hand-laid
form each item adds `rel`, to whom it stands in what relation, and `why`, its reason and source; coordinates only
reproduce one map, and on another map the adaption re-finds positions from the relations
(`Imperium-Knowledge/designs/ICF/城骨架格式-v1.md` L4-6, L26-31). A skeleton holds features (what the map already has:
riverbank, old road, bridge, rock, marsh, ridge, hill), elements (public buildings, squares, gates, the
palace-quarter group, terraces), streets, lifeline nodes (source, trunk, reveal, exit), the wall (wall, towers, gates,
bank strip, moat) and the items outside (bridgehead fort, small fort, cemetery, manor and square fields, the avenue
outside the gate) (`Imperium-Knowledge/designs/ICF/城骨架格式-v1.md` L9-24).

The relations are named by a set of words, with none for height, since RimWorld cannot read height: backs on (背靠,
one side against a cliff, rock or river that shields it), farthest from (离…最远), facing (对, facing the direction
something comes from), adjoins (贴, a long side hard against), end toward (端朝), on (在…上, on a street or water
line), meeting of (交会, where several lines meet), along (沿), between (之间), inside a gate and outside a gate (门内,
门外, beside the gate along the road), downstream (下游, the next station along a line), taken in (收进, enclosed by
the wall without the wall bulging for it), borrows (借, the wall uses rock, marsh or river as its barrier, unbuilt or
undug), and near and far (近, 远, the density gradient) (`Imperium-Knowledge/designs/ICF/城骨架格式-v1.md` L34-51). The
format's own readings include the palace quarter lying farthest from the main gate of the approach, the main gate
facing the approach, an inn inside a gate and a cemetery outside a gate along the road
(`Imperium-Knowledge/designs/ICF/城骨架格式-v1.md` L39-47).

The Roman skeleton's nodes that are always present are the palace quarter, the first square (第一广场, the main core,
facing the main bridge when there is a river), the main street, the second square (with a market, the bath group beside
it), the land gates and the lifeline (命脉线) (`Imperium-Knowledge/现行/城/罗马城-城内.md` L31). Its conditional nodes
are a sanctuary (圣所, if it fits), the pre-existing road (先在路, if a world road passes through), a bridge (if there
is a river), an area on the far bank (described in `cities-outside.md`) and a third square (if the main street is long
enough, often where it meets the pre-existing road) (`Imperium-Knowledge/现行/城/罗马城-城内.md` L31). When space is
short, nodes give way in this order: the third square merges into a fork or junction; the second square shrinks; the
main street narrows from 7 to 5 with a colonnade on one side only; the secondary axis shortens or the sanctuary moves
beside a square; the palace quarter, first square, main street, gates and lifeline never give way
(`Imperium-Knowledge/现行/城/罗马城-城内.md` L31) (replaces `Imperium-Knowledge/09_地图生成与CBF技术.md` L751 in part).
If there is still no room, the city is restarted (`Imperium-Knowledge/09_地图生成与CBF技术.md` L751). A skeleton with
no sanctuary, or with one opened but left unfilled, is only noted, not an error
(`Imperium-Knowledge/现行/城/罗马城-城内.md` L32).

> [!NOTE]
> **Deleted**: The skeleton's Roman lifeline node is the city's water network (see the city grammar below), and the
> skeleton format's water items and the water palace (水宫) that the current card names among a skeleton's relations
> belong to it; all of it belonged to the hydraulics (水利, later the imperial aqueducts 帝国水道) the maintainer deleted
> (`docs/glossary.md` L187; `Imperium-Knowledge/现行/城/罗马城-做法与顺序.md` L42;
> `Imperium-Knowledge/designs/ICF/城骨架格式-v1.md` L19; `Imperium-Knowledge/15_水利主轴.md` L4, L21-32).

> [!NOTE]
> **Unverified**: No area threshold is set for the sanctuary, and the skeleton's sanctuary switch is undecided; the
> check only makes notes (`Imperium-Knowledge/designs/tools/city/说明/check.md` L10, L30). The skeleton format of 10-30,
> with `rel`, `why` and the relation words, is followed by the kit's skeleton file of 11-03, which lists nodes, edges
> (each with a `how`), the lifeline chain and the yield order without listing the relation words; neither marks the
> other replaced beyond the block slots (`Imperium-Knowledge/designs/ICF/城骨架格式-v1.md` L4-6, L34;
> `Imperium-Knowledge/designs/city-plans/kit/城建数据格式-草案.md` L38-49, L211).

## Groups (组合件)

A group is a set of buildings with a fixed shape: design fixes its shape and pairings, and generation decides only
where it goes (`Imperium-Knowledge/现行/城/罗马城-做法与顺序.md` L41). Each group comes in 2 or 3 sizes, its orientation
set by its street front (`Imperium-Knowledge/现行/城/罗马城-城内.md` L138), and has conditions, a phase and an
orientation rule (`Imperium-Knowledge/designs/city-plans/kit/城建数据格式-草案.md` L51-53). Its shape carries the cards
it is made of, its outline with a face on each stretch, its ports, and its inner open ground such as yards, terraces
and small squares (`Imperium-Knowledge/designs/city-plans/kit/城建数据格式-草案.md` L55-60). Medium and small cities take
the groups of phase two (`Imperium-Knowledge/designs/做法史/罗马城·做法与顺序.md` L135).

The first batch of groups is the palace-quarter group, the first-square group, the main-street shop row (主街铺排), the
gate group, the second-square group, the bath group, the quay group, the bridgehead group, the sanctuary group and the
workshop group; what each holds and what it is beside and away from follow R-1103-0016, and the workshop group's place
follows the attraction field (`Imperium-Knowledge/现行/城/罗马城-城内.md` L138) (replaces
`Imperium-Knowledge/designs/做法史/罗马城·做法与顺序.md` L57; `Imperium-Knowledge/designs/做法史/罗马城·城内.md` L51-52;
`Imperium-Knowledge/designs/回报/审查-原意走样二.md` L89). The arena and theatre are not listed, the granary belongs to
the quay group and the store-shops, and the single household belongs to the base
(`Imperium-Knowledge/现行/城/罗马城-城内.md` L138). There is no separate barracks group: barracks stand only beside the
palace gate as the guard's barracks and in the main gate's gate group
(`Imperium-Knowledge/现行/城/罗马城-城内.md` L140).

When a group cannot land, another candidate place on the same terrain is tried first; a part that cannot be made, such
as a block, colonnade, skeleton or wall, is redone on its own; only when the local repair fails does the city go back to
the terrain (`Imperium-Knowledge/现行/城/地形与选址.md` L103; `Imperium-Knowledge/designs/回报/审查-原意走样二.md` L65),
and a restart also follows when a city still does not fit at the lower size limit
(`Imperium-Knowledge/designs/整理/城建错题转拦截-2026-11-05.md` L25).

### Faces and ports

Groups and single-household cards mark faces (面) on their edges and ports (口) on their bodies
(`Imperium-Knowledge/现行/城/罗马城-城内.md` L160) (replaces `Imperium-Knowledge/09_地图生成与CBF技术.md` L748 in part).
There are five faces (`Imperium-Knowledge/现行/城/罗马城-城内.md` L160):

- the street face opens doors and shopfronts and joins a street or square;
- the back-yard face joins another back-yard face, a lane, a garden or the inner ring road, never a main street or
  square;
- the side-wall face joins another side-wall face of the same household into one wall, or a one-cell gap between
  households, a lane or a secondary street, never a main street or square;
- the open face (a colonnade, front court or terrace facing out) joins a square, garden or water;
- the water face (a bank wall, quay or terrace down to the water) meets the water across the bank strip.

The ports are the door port on the street face, joining the street network; the lane port, where a small lane may
pass, both ends joining streets; the goods port of storehouses and workshops, at least 3 cells wide, opening to a
street or quay; and alignment (对位), the end of a street's axis on which the item falls
(`Imperium-Knowledge/现行/城/罗马城-城内.md` L160). Around main streets and squares only street
faces and open faces are allowed, and where two meeting faces are incompatible a lane or garden separates them; the
stepped-back side wall of an oblique main street facing the colonnade floor does not count as a side-wall face on the
main street (`Imperium-Knowledge/现行/城/罗马城-城内.md` L160). How the remaining plots are filled after each period is
in `cities-inside.md`.

> [!NOTE]
> **Deleted**: The fifth port, the water inlet and outlet joining an open channel, connected items to the city's water
> network and belonged to the hydraulics axis the maintainer deleted on 2026-11-24 (`Imperium-Knowledge/现行/城/罗马城-城内.md` L160;
> `Imperium-Knowledge/15_水利主轴.md` L4, L21-32).

> [!

## The city grammar (聚落平面语法)

> [!NOTE]
> **Deleted**: The hand-designed city plan line. The Roman city plan was hand-designed data read and fitted onto the
> terrain, which the settlement plan grammar v4 defined field by field as ICF's L1 plan definition: a skeleton with card
> slots and fixed cards for each Roman row (without high ground A31, A29, A26 and A7; with high ground A31 and A12; A28
> at the crossing of the core street and the axis), block slots, assembly marks, the approach side and the Roman row
> (`Imperium-Knowledge/designs/ICF/聚落平面语法-v4.md` L8, L12, L17, L276-286; `Imperium-Knowledge/designs/ICF/ICF设计.md` L94;
> `Imperium-Knowledge/09_地图生成与CBF技术.md` L594-595). The axis-and-grid plan, in which Rome first draws the axis and the
> grid follows it out to the area of the site sheet, was already changed in v5.1: the city plan is hand-designed data
> and the grid is no longer laid along the axis (`Imperium-Knowledge/09_地图生成与CBF技术.md` L573); the later variants of plan
> v2 (`Imperium-Knowledge/designs/ICF/聚落平面语法-v4.md` L408); the 10-29 survey's five repairs to grammar v3, which the
> ledger took into the grammar (`Imperium-Knowledge/designs/罗马理想城调研-2026-10-29.md` L104-110;
> `Imperium-Knowledge/09_地图生成与CBF技术.md` L606-613); the parameter keys for the core's elevation and the three-sided
> barrier test (`Imperium-Knowledge/designs/ICF/聚落平面语法-v4.md` L322-323); and the grammar's shape text, to be rewritten
> after a hand-laid confluence-mouth city (`Imperium-Knowledge/designs/ICF/聚落平面语法-v4.md` L4). The rulings of 10-30
> deleted it: the skeleton is laid by hand and records relations, the plan is no longer hand-designed data read onto the
> terrain, and the grammar's Roman City shapes give way to the current city cards (`Imperium-Knowledge/09_地图生成与CBF技术.md`
> L697, R-1030-1406; `Imperium-Knowledge/designs/ICF/ICF设计.md` L6, R-1030-1802;
> `Imperium-Knowledge/designs/ICF/聚落平面语法-v4.md` L4, L6). What R-1030-1802 put in its place, a main ring set by the main
> core and a plan generated by weights from the sources, was deleted in turn: a city's area is not grown by tuning
> weights, and a city goes only through a template (`Imperium-Knowledge/现行/城/罗马城-做法与顺序.md` L52, R-1110-1057;
> `Imperium-Knowledge/09_地图生成与CBF技术.md` L905, R-1112-0820).

The grammar builds a settlement from nine primitives (core and open space, street network and axis, lifeline, boundary
and control, density gradient, block slots and block library, outer-wall layering, cards and card slots, assembly),
which the engine's seven stages (landform, siting, assembly, wrapping the wall, lifeline, building, check) know alone,
while each faction's kit fills every primitive with content (`Imperium-Knowledge/designs/ICF/聚落平面语法-v4.md` L8,
L18-28).

> [!NOTE]
> **Unverified**: The grammar's subject, the hand-designed plan, is deleted, and with it the block slots and card slots;
> the sources do not say whether the nine primitives and the seven stages as a frame went with it or stand (`Imperium-Knowledge/designs/ICF/聚落平面语法-v4.md` L6, L8; `Imperium-Knowledge/designs/ICF/ICF设计.md` L6).

The lifeline is the line every settlement has from a source through a main line to the places where it shows and out
again (`docs/glossary.md` L187). Its nodes are of four types, source, trunk, reveal and exit, and the kit's skeleton
records the lifeline's chain in that order (`Imperium-Knowledge/designs/ICF/聚落平面语法-v4.md` L102;
`Imperium-Knowledge/designs/city-plans/kit/城建数据格式-草案.md` L45). There may be several sources, an exit may be a
chain of nodes, nodes may be marked omissible so that their neighbours are joined directly, trunk edges cite street
numbers, and the loss of a source is a check of which node types stall
(`Imperium-Knowledge/designs/ICF/聚落平面语法-v4.md` L103-107). Each faction fills one kind of lifeline in the same
skeleton: modern factions electricity, the medieval faction its lord, tribes fire and their chief
(`Imperium-Knowledge/designs/ICF/聚落平面语法-v4.md` L108).

> [!NOTE]
> **Deleted**: The Roman lifeline is water, which is also the Roman city's power grid: its source is an aqueduct or a
> well at the water tower A31, its trunk the channel along the colonnaded main street, the places where it shows are
> the monument fountain, the square pools and the public baths, and its exit chain runs water-out gate, moat, sluice,
> main canal, branch canal and field; this belonged to the hydraulics axis the maintainer deleted on 2026-11-24 (`docs/glossary.md` L187;
> `Imperium-Knowledge/designs/ICF/聚落平面语法-v4.md` L104, L108, L110; `Imperium-Knowledge/15_水利主轴.md` L4,
> L21-32).

Numbers such as tower spacing, moat, clearing, field share, the caps on growth parts and whether dead ends are allowed
are held in ICF's L1 parameter table, by faction and tier (`Imperium-Knowledge/designs/ICF/ICF设计.md` L93); the values
belong to the sections of the things they measure.

> [!NOTE]
> **Unverified**:
> - The dead-end rules of the medieval, modern and tribal factions, parameter 15 (the modern faction's firing range,
>   a design-session initial value) and parameter 18 (the tribal stockade's control points) wait for those factions'
>   own rounds (`Imperium-Knowledge/designs/ICF/聚落平面语法-v4.md` L318-324).
> - Whether review checklists use the rows without and with high ground (无高地行, 有高地行) or the regions hot-dry and
>   temperate-cold is undecided, and the generation spec still says Rome shapes the terrain
>   (`Imperium-Knowledge/designs/回报/审查-城卡同类冲突-2026-11-10.md` L80-81).

## Area spectra (片区谱) and fragments (片段)

The unit learned from the era city is the area (片区): which items an area holds, what coordinates each takes and how
they relate, not what a single house should be paired with; each item can state its reason in that area, and a loose
item without a reason is not placed (`Imperium-Knowledge/现行/城/罗马城-做法与顺序.md` L160;
`Imperium-Knowledge/designs/tools/方向表.md` L27). What is learned is recorded as an area spectrum by area type, one for
each type, common to later cities, and an area's household count and the size of each household are set by the
spectrum of its type (`Imperium-Knowledge/现行/城/罗马城-做法与顺序.md` L171; `Imperium-Knowledge/09_地图生成与CBF技术.md` L918). The types first follow the reference's dense core, city-edge housing, island, palace quarter and garden
(`Imperium-Knowledge/09_地图生成与CBF技术.md` L918). A spectrum records what an area holds and the coordinates and
relations of its parts, keeps no loose items without a reason, and writes household counts and sizes; the first is
learned from the east square (`Imperium-Knowledge/designs/回报/进度-东广场片区谱.md` L91). The grass standard values are
a reference, not a threshold, and a value out of range is given a sentence of reason; the layout principles the user
has stated are collected on the page "layout thinking" (布置思路) (`Imperium-Knowledge/现行/城/罗马城-做法与顺序.md` L171;
`Imperium-Knowledge/09_地图生成与CBF技术.md` L934).

A reference area is traced only as far as blocks, house groups, yards and roads, not building by building
(`Imperium-Knowledge/现行/城/罗马城-做法与顺序.md` L172). Each building or group is given a use first, housing, shop
front, workshop, tavern, market, public, annex or attic, or unclear, with a one-sentence basis, by the wiki and without
measuring each building; if more than three tenths of an area is unclear, its image goes to the user to mark, and
within three tenths the uses are settled against the wiki (`Imperium-Knowledge/现行/城/罗马城-做法与顺序.md` L172;
`Imperium-Knowledge/09_地图生成与CBF技术.md` L934, L937). Positions are then set by the relation the spectrum gives
for that use, and an item with no use is not placed, so layout is not filling in blanks
(`Imperium-Knowledge/现行/城/罗马城-做法与顺序.md` L172; `Imperium-Knowledge/09_地图生成与CBF技术.md` L934). From the
reference, combination and look are learned, while function comes from Imperium's cards and RimWorld's rules, and the
cards missing for an area are made for it (`Imperium-Knowledge/现行/城/罗马城-做法与顺序.md` L162;
`Imperium-Knowledge/09_地图生成与CBF技术.md` L937).

An area is 2800 to 9200 cells, floating with the attraction field's weight, so that areas near the core and the main
street are small and outlying ones large; the strength of the weighting is a trial value to be set after the user has
seen the images (`Imperium-Knowledge/现行/城/罗马城-城内.md` L23; `Imperium-Knowledge/09_地图生成与CBF技术.md` L863) (replaces
`Imperium-Knowledge/09_地图生成与CBF技术.md` L861). A building with its annex and small yard counts as one item
(`Imperium-Knowledge/designs/研究/城/布置思路.md` L13). Several roof blocks that adjoin tightly with slightly offset
coordinates are one household and one building, whose outline they make together, and tracing, samples and card filling
follow the household's outline, not squares (`Imperium-Knowledge/现行/城/罗马城-做法与顺序.md` L153;
`Imperium-Knowledge/09_地图生成与CBF技术.md` L953).

An area is laid by its spectrum by first trying three steps: households come out of the spectrum, then each is given its
tier, then households are merged; if the look is wrong, the order changes to merging first and then applying the
spectrum, the user judging by picture (`Imperium-Knowledge/现行/城/罗马城-做法与顺序.md` L174). The tiers and uses come from the
attraction field (`Imperium-Knowledge/现行/城/罗马城-做法与顺序.md` L148), and in template 1's zoning rich households are merged by
block (`Imperium-Knowledge/现行/城/罗马城-做法与顺序.md` L175). The east square's spectrum is taken as a general spectrum for
small-square housing areas, which any housing area around a small square can use; the first square, the largest and most
formal in the city, gets another reference and is recorded as its own type; and which building forms a square's front is
decided when the area is laid (`Imperium-Knowledge/现行/城/罗马城-做法与顺序.md` L174; `Imperium-Knowledge/09_地图生成与CBF技术.md`
L932-933). The earlier reading of the east square and its fronting long house as the first-square group is void
(`Imperium-Knowledge/09_地图生成与CBF技术.md` L932-933).

Variety goes through a fragment library (片段库): house groups are cut into fragments, which can be mirrored, turned,
stretched along the street and given card variants, while the area spectrum only picks cards and checks counts and
does not arrange positions (`Imperium-Knowledge/现行/城/罗马城-做法与顺序.md` L159;
`Imperium-Knowledge/designs/tools/方向表.md` L37). In item-by-item replacement the positions follow the tracing and the
building groups are cut into fragments (`Imperium-Knowledge/designs/研究/城/布置思路.md` L16).

Card replacement takes the 1:1 building as its standard: the outer frame differs by at most 1 cell on each side,
buildings at 45° are placed at 45°, and a card may be mirrored so that its door is on the original's side; only the
house is replaced, while the household's yard, yard wall, gate, trees and annexes stay as in the 1:1 original unless
an annex has a card of its own; a household that stretching, a card swap and variants cannot fit keeps its 1:1 form,
recorded as a missing card variant, so that no hole is left and the look after replacement is no worse than the 1:1
sample (`Imperium-Knowledge/现行/城/罗马城-做法与顺序.md` L152; `Imperium-Knowledge/09_地图生成与CBF技术.md` L950). The
outline taken is that of the whole household, tightly adjoining blocks counted as one
(`Imperium-Knowledge/09_地图生成与CBF技术.md` L953) (replaces `Imperium-Knowledge/09_地图生成与CBF技术.md` L950 in
part). While filling, cards are supplemented: an existing card is first changed if it can be (stretch grades, door
position, an annex added or removed, a slant variant), and only then is a new card made; a new card gives every room a
use, follows the existing cards' drawing and rules and does not copy the reference's squares; filling comes first and
supplementing after, so that missing cards follow the city and no card library is made idly
(`Imperium-Knowledge/现行/城/罗马城-做法与顺序.md` L162; `Imperium-Knowledge/09_地图生成与CBF技术.md` L951). When a card
is split, the main way is to cut one big card into several complete small cards, and the secondary way is to keep the
card and change only its outer edge to share walls and yards with the neighbouring household
(`Imperium-Knowledge/现行/城/罗马城-做法与顺序.md` L173; `Imperium-Knowledge/09_地图生成与CBF技术.md` L920;
`Imperium-Knowledge/designs/研究/城/布置思路.md` L35; `Imperium-Knowledge/designs/回报/进度-拷打入账.md` L19).

> [!NOTE]
> **Unverified**: The first area spectrum, the small-square housing area learned from the east square, is marked a
> proposal, including its format: one type per file with the fields type, learned from, scale, contents, households,
> relations, change of land, division of work and unsure, where a new reference city adds a row to "learned from" and
> to the evidence of "relations", a new terrain adds a row to "change of land" or a column to "relations", and old
> fields and rows are never renamed or changed in meaning
> (`Imperium-Knowledge/designs/研究/城/片区谱-广场住片.md` L1-6). Its fragment table cuts the east square into ten
> building-group fragments, 甲 to 癸 (main-street west column, square north column, west-edge pair, long-field east
> column, junction courtyard house, wedge walled court, access-lane row, oblique-lane pair with shared yard,
> oblique-street straight pair, street-corner single), each with the road it meets, its orientation, its stretch range,
> its seam and the deformations it allows, such as mirroring, stretching along the street or lane, and turning 90° or
> 45° (`Imperium-Knowledge/designs/研究/城/片区谱-广场住片.md` L95-110).

## Spec cards (规格卡)

### What a spec card holds

A spec card is a design card that fixes one building of a generated settlement, its plot, rooms and contents
(`docs/glossary.md` L206). Roman cities use only spec cards, and CBF's houses are no longer used for them
(`Imperium-Knowledge/09_地图生成与CBF技术.md` L449; `Imperium-Knowledge/designs/做法史/罗马城·城内.md` L103-104). The
templates converted from CBF (the Custom Base Framework mod) are a temporary placeholder, to be replaced step by step by
Imperium's own (`Imperium-Knowledge/14_来源同步与权威.md` L45). Every style's cards are made by first writing the use
and the reason, then the rooms and features (`Imperium-Knowledge/09_地图生成与CBF技术.md` L449).

A card is cut from a block sketch: the sketch draws one or two blocks with their streets, lanes and squares, every
building numbered and typed; the user approves some buildings, and only those become cards, each taking the building
itself plus one cell in front of its door and no neighbours; the buildings not chosen stay in the sketch as a reference
for filling; and Roman, medieval, tribal and modern cards are all made this way
(`Imperium-Knowledge/14_来源同步与权威.md` L55). A card has an
odd outline and its door on the street face, carries seven tags, passes the automatic check, can be placed alone, and
can be mirrored and rotated (`Imperium-Knowledge/14_来源同步与权威.md` L55). The seven tags are use, tier, size class,
city-zone layer, facade, rotation and mirroring, and terrain (`Imperium-Knowledge/designs/ICF/聚落平面语法-v4.md` L276).

In ICF a spec card has four layers, structure, floor, roof and objects, whose object symbols point only to object roles,
and it carries the seven tags, its tier, era, growth parts and terrain tag (`Imperium-Knowledge/designs/ICF/ICF设计.md`
L89). The material tiers are common, rich, workshop, military, imperial and city defence, and they map to wall, floor,
paint and mask colour (`Imperium-Knowledge/designs/ICF/ICF设计.md` L92); materials belong to the card and the kit
(`Imperium-Knowledge/designs/ICF/聚落平面语法-v4.md` L286), and the materials themselves are in `cities-inside.md`. The room
uses are bedroom, hall (reception), dining room, kitchen, servants, shop front, storage, workshop, warehouse, worship
hall, apse, entrance hall, gateway, colonnade (portico), bath, cistern, courtyard, colonnaded courtyard, garden and
other (`Imperium-Knowledge/designs/roman-cards/zones_v3.md` L81).

A building is built from one spec card at the card's scale, not assembled from several small independent houses, and
single cards are not laid out as an even-spaced array (`Imperium-Knowledge/designs/instructions/生成具象规格-现行版.md` L140-143). The lower limits of the main outlines are A3 mansion 17×14, A4 cathedral 17 wide by 22 long, A7 council hall
13×12, A8 bishop's residence 22×15, A9 courtyard house 9×8 and A12 governor's seat 17×14, and the current sizes are
those of the card table (`Imperium-Knowledge/designs/instructions/生成具象规格-现行版.md` L141).

### How Roman cards are drawn

The new Roman cards A23 to A26 of 10-28 07:15 were voided and redone as a high-technology Rome (new A23 big workshop,
A24 camp infirmary, A25 camp mess) (`Imperium-Knowledge/09_地图生成与CBF技术.md` L450-451). Function is the skeleton of a card;
courtyard, colonnade, portico and rows of columns give the Roman flavour; the outline comes from rooms of unequal size,
annexes, L shapes, projecting porches and side rooms; an apse is only for ceremonial rooms; ornate walls, quoins and
large ornate doors are only for core buildings; corners are not cut at 45°; eastern Rome is Rome, in two periods; and
the history need not be fully reproduced, function coming first (`Imperium-Knowledge/09_地图生成与CBF技术.md` L451). Ordinary
buildings get their Roman feel from ring colonnades, a symmetric front door on the central axis, a shallow pool in the
yard and statues (`Imperium-Knowledge/09_地图生成与CBF技术.md` L452). Card A1 loses its own colonnade, the colonnade belonging
to the city (`Imperium-Knowledge/09_地图生成与CBF技术.md` L477). Houses are made as a core plus growth parts (生长件), which give
their variants (`Imperium-Knowledge/09_地图生成与CBF技术.md` L510; `Imperium-Knowledge/designs/roman-cards/罗马规格卡总表.md` L8).

A card's body width and depth are always odd and at most 25×20; the door is a single door on the central axis, and
shopfronts and storage doors use a double door across the whole face, not aligned with a column (A14's north store takes
a single door to clear the corner column); three exceptions follow 09§8
(`Imperium-Knowledge/designs/roman-cards/罗马规格卡总表.md` L95). The apse of public and rich-household cards is 9 to 11 wide
outside; cards at most 17 wide take an outer width of 9 as the lower limit; A20's outer width of 5 is an exception as an
insert in A11's courtyard, and A8's small chapel apse of outer width 5 is a block attached at the side
(`Imperium-Knowledge/designs/roman-cards/罗马规格卡总表.md` L96). Columns stand 3 apart, with a central bay of 4 in front of a
door; they sit on the structure layer, end columns do not touch side walls except as antae, and columns do not take the
left and right edge cells (`Imperium-Knowledge/designs/roman-cards/罗马规格卡总表.md` L97).

### The Roman card set

The current Roman card set is 52 cards in six tiers (档位): public and imperial (公共/帝国) 17, rich households (富户) 12, common people
(常民) 13, storage and workshops (仓坊) 5, military (军) 4 and city defence (城防) 1, with
`Imperium-Knowledge/designs/roman-cards/roman_cards_v3.json` (version 3.1) as the data
(`Imperium-Knowledge/designs/roman-cards/罗马规格卡总表.md` L4). After the 10-28 review there were 30 cards, 13 new
numbers and 3 variants (A3v, A2b, A2c), 46 in all; on 10-30 A36方 and A37方 were added, and then the square-hall
versions of A3, A3v, A34 and A35 as variants, making 52 (`Imperium-Knowledge/designs/roman-cards/罗马规格卡总表.md` L130; `Imperium-Knowledge/designs/tools/city/说明/cards.md` L22). Rich-household houses mainly use the rear-hall (apse
hall) versions of A3, A3v, A34 and A35, A36 and A37 use the square hall, and the other version of each is kept as a
variant (`Imperium-Knowledge/现行/城/罗马城-城内.md` L152; `Imperium-Knowledge/designs/roman-cards/罗马规格卡总表.md` L130).

> [!NOTE]
> **Deleted**: The v2 card line: the v2 card table and data with 34 cards, among them A1c, the graveyard church A6 and
> the almshouse A16, and the first A23 to A26 of 10-28 07:15 (a bakery with mill, a big workshop, a camp infirmary and a
> camp kitchen with mess) (`Imperium-Knowledge/09_地图生成与CBF技术.md` L449, L510). The 10-28 redraw as high-technology Rome
> voided those first A23 to A26, and the v3.1 table replaced the v2 table, deleting A1c (overlapping A27b), A6, and A16
> (overlapping A24), merging A1b into A1 and folding the three shopfronts into A27b
> (`Imperium-Knowledge/09_地图生成与CBF技术.md` L450-451, L574; `Imperium-Knowledge/designs/roman-cards/罗马规格卡总表.md` L2, L67).

Card numbers keep their old numbers, new cards are numbered from A32 in tier order, and the temporary numbers of the new
candidates map to their card numbers: N1 to A3, N5 to A2, N6 to A2b, N7 to A1, N10 to A32, N11 to A33, N2 to A34, N16 to
A35, N14 to A36, N17 to A37, N3 to A38, N4 to A39, N15 to A40, N12 to A41, N13 to A42, N8 to A43 and N9 to A44
(`Imperium-Knowledge/designs/roman-cards/罗马规格卡总表.md` L8, L105-123; `Imperium-Knowledge/designs/整理/整理方案-2026-11-02.md`
L152). The table gives for each card its name, tier, body size (not counting the one cell in front of the door), how it
is used in the J and B types of city, a lineage over the two peak periods (peak two first), its growth parts or
variants, its source and its batch status (`Imperium-Knowledge/designs/roman-cards/罗马规格卡总表.md` L8-10). The lineage names
one real example for each of the two peak periods, peak two first; the cathedral A4, for example, names a Justinian-era
church with a forecourt and the Basilica Ulpia (112), matching in function and place
(`Imperium-Knowledge/designs/roman-cards/罗马规格卡总表.md` L12). Lineage notes such as "survey A5, B1" are the type numbers of
the housing survey, not card numbers (`Imperium-Knowledge/designs/roman-cards/罗马规格卡总表.md` L8). Cards marked † are
generated only when Ideology is loaded (`Imperium-Knowledge/designs/roman-cards/罗马规格卡总表.md` L8).

The cards remade in v3 are the public bath A26 (25×19, cold, warm and hot pools on one axis with the door, the hot pool in a
semicircular apse, a colonnaded exercise yard), the citadel governor's residence A12 (19×17, door, four-column atrium,
hall with an archive sub-office and apse on one axis), the mansion A3 (with A3v, the turning-entrance version), the
headquarters A19 (17×17, porch, colonnaded yard, transverse hall and standards apse on one axis, archive sub-office), the
bishop's residence A8 (main yard, east-wing chapel with a small apse reaching north), the monastery A11 (colonnaded
yard on four sides with A20 standing in it, projecting yard gate), the craftsman house A2 (with A2b and the small
household A2c) and the warehouse yard A14 (15×11, in segments, with a four-corner columned yard, colonnaded gates at the
ends and a stepped east wing) (`Imperium-Knowledge/designs/roman-cards/罗马规格卡总表.md` L127). Fifteen cards were
changed slightly, five kept as they were, and the v3.1 review added further corrections
(`Imperium-Knowledge/designs/roman-cards/罗马规格卡总表.md` L128-131).

The row cottages A27 are units of 7×9 in three kinds, dwelling, shopfront and workshop, sharing walls with their
neighbours and able to stand as 9×7; they fill the street frontage and the shops on main streets and square edges that
the big cards cannot (`Imperium-Knowledge/09_地图生成与CBF技术.md` L469). The camp mess A25 is a long hall with two long tables
and stools, an apse with the officers' seat at the east end, a kitchen wing set off to the north and a four-column porch
on the south door (`Imperium-Knowledge/09_地图生成与CBF技术.md` L480), now 19×15
(`Imperium-Knowledge/designs/roman-cards/罗马规格卡总表.md` L62). The four-sided gate A28 has four ornate octagonal piers at
the crossing with a roofed crossing, in three sizes by street width (`Imperium-Knowledge/09_地图生成与CBF技术.md` L480-481).
The monument fountain A29 is a gold-trimmed niche with four statues and a pool, and the monument column A30 is
represented by a grand statue, to be replaced later by an imperial monument-column piece
(`Imperium-Knowledge/09_地图生成与CBF技术.md` L480). The medium workshop and the port warehouse with a quay face were added as
new cards (`Imperium-Knowledge/09_地图生成与CBF技术.md` L510, L574).

> [!NOTE]
> **Deleted**: These card passages rest on the city's water network and its powered equipment, which belonged to the
> hydraulics axis the maintainer deleted on 2026-11-24 (`Imperium-Knowledge/15_水利主轴.md` L4, L21-32):
> - A29's pool is fed from its back wall and its outflow joins the main-street channel
>   (`Imperium-Knowledge/09_地图生成与CBF技术.md` L480);
> - A31, the water palace (水宫), formerly the water-distribution tower (分水塔), 13×13, has a central chamfered pool joined
>   to the outlets on its faces by culverts, one inlet and three outlets, and the city's only hydraulic generator
>   (`Imperium-Knowledge/09_地图生成与CBF技术.md` L480; `Imperium-Knowledge/designs/roman-cards/罗马规格卡总表.md` L26, L98);
> - the big workshop A23 and the row workshop unit A27c carry a street-side water inlet and outlet and a placeholder for
>   a hydraulic power unit (`Imperium-Knowledge/designs/instructions/生成具象规格-现行版.md` L450;
>   `Imperium-Knowledge/09_地图生成与CBF技术.md` L477);
> - the rainwater pool, a new card added on 10-28, was first meant as the water source for the water tower when the
>   hot-dry type J has no river, matching B's aqueduct, and was later ruled to serve only as storage
>   (`Imperium-Knowledge/09_地图生成与CBF技术.md` L510);
> - a pool and its water outlet are joined by a culvert, with no water line drawn across the ground
>   (`Imperium-Knowledge/09_地图生成与CBF技术.md` L481; `Imperium-Knowledge/designs/roman-cards/罗马规格卡总表.md` L98).

Eighteen further candidate cards are in the data and not counted: the street-corner shrine A47, the small street pool
A48, the neighbourhood bath A50, the variants A34后 and A34铺, the bakery A45, the colonnade stall A46, the corner shop
A49, and the plot cards A51a to A51e and A52a to A52e (`Imperium-Knowledge/designs/roman-cards/罗马规格卡总表.md` L65;
`Imperium-Knowledge/designs/tools/city/说明/cards.md` L22). With them the card set has 70 cards and 336 rooms
(`Imperium-Knowledge/designs/roman-cards/zones_v3.md` L79).

> [!NOTE]
> **Unverified**:
> - 120 rooms of the cards are still pending review, among them those of the square-hall variants
>   (`Imperium-Knowledge/designs/roman-cards/zones_v3.md` L30-41, L79).
> - The table names three exceptions to the footprint and door rules "per 09§8" without listing them
>   (`Imperium-Knowledge/designs/roman-cards/罗马规格卡总表.md` L95); the ledger has three exceptions of 10-28 on yard columns
>   and the symmetry axis, and the table does not say whether these are the ones meant
>   (`Imperium-Knowledge/09_地图生成与CBF技术.md` L549-552).
> - The archive office (档案署) and the inn (客栈) were noted as having no card of their own (专卡), and this was entered as
>   item 35 of the list awaiting the user's ruling (`Imperium-Knowledge/designs/整理/删除核对-2026-11-03.md` L20).
> - The housing survey suggests how many cards each house type suits, such as three slices of the atrium house and two
>   each of most others (`Imperium-Knowledge/designs/roman-cards/罗马住宅调查-2026-10-28.md` L114-129), and a later report
>   proposes which cards suit living cities and which ruins, and for A38 and A39 follows the user's addition that, Ostia
>   being in Italy itself, their form belongs to ruins
>   (`Imperium-Knowledge/designs/city-plans/罗马大城住宅类型-查证-2026-11-03.md` L158-186). The values of household width and
>   depth for the near, middle and far grades in the task book are not ruled (`Imperium-Knowledge/designs/整理/回报/城卡.md`
>   L28).

### Cards in the city

There is no block library: common dwellings are not built as whole block modules, but the land enclosed by streets is
divided into households along the street, each household getting one spec card by the size of its plot, its door and
street-front wall facing the street; internally structured groups, such as a church with a small square or a workshop
with a works yard, are building-group cards (建筑群卡); and the 23 modules already made serve only as household samples
and comparisons (`Imperium-Knowledge/现行/城/罗马城-城内.md` L130; `Imperium-Knowledge/09_地图生成与CBF技术.md` L714;
`Imperium-Knowledge/designs/city-plans/现实街坊研究-方法草案-2026-10-30.md` L4;
`Imperium-Knowledge/designs/整理/整理方案-2026-11-02.md` L463).

> [!NOTE]
> **Deleted**: The block library line. Common housing was to be built as whole block modules assembled from spec cards:
> a block library (街坊库) for each faction kit, 6 to 8 modules in each slot tier (for Rome small block, large block and
> warehouse strip), drawn by seed into block slots (街坊槽) of the plan and the skeleton, old-peak modules along the
> avenues and in the old heart and new-peak ones outside, households dropped from a module to leave a yard, empty slots
> left as garden or paving, a cap on one card's share among the modules, card variants made in the library before
> round 4, block sketches kept as references for assembling blocks in round 4
> (`Imperium-Knowledge/14_来源同步与权威.md` L55), a smaller module size to be added first, and the grammar's keys for the block radius and the modules per
> tier (`docs/glossary.md` L167-168; `Imperium-Knowledge/designs/ICF/ICF设计.md` L95;
> `Imperium-Knowledge/designs/ICF/城骨架格式-v1.md` L57-66; `Imperium-Knowledge/designs/instructions/生成具象规格-现行版.md` L176-180; `Imperium-Knowledge/designs/ICF/聚落平面语法-v4.md` L311-312, L344-345;
> `Imperium-Knowledge/09_地图生成与CBF技术.md` L660, L712). The ruling of 10-30 19:30 deleted it: there is no block
> library, households take one card each along the streets, block slots and all that hung on them are void, and the
> data format of 11-03 carries none of it (`Imperium-Knowledge/09_地图生成与CBF技术.md` L714, R-1030-1930;
> `Imperium-Knowledge/designs/ICF/聚落平面语法-v4.md` L6; `Imperium-Knowledge/designs/ICF/ICF设计.md` L6;
> `Imperium-Knowledge/designs/ICF/城骨架格式-v1.md` L59; `Imperium-Knowledge/designs/instructions/生成具象规格-现行版.md` L6; `Imperium-Knowledge/designs/city-plans/kit/城建数据格式-草案.md` L211).

One card makes up at most 15% of the buildings inside the wall, and the buildings of one card have variants with a
different interior layout, door position and street-front wall, and annexes, not copies of one room
(`Imperium-Knowledge/现行/城/罗马城-城内.md` L149). A stretched card is still the same card
(`Imperium-Knowledge/现行/城/罗马城-城内.md` L149), and so is a slant card with its upright card
(`Imperium-Knowledge/designs/tools/city/说明/cards.md` L36). The count takes only buildings inside the wall whose card
has a wall or a door, so a pool such as A48 or a memorial column such as A30 does not count; each card in a group counts
as one building; and the outside of the city is not counted (`Imperium-Knowledge/现行/城/罗马城-城内.md` L149;
`Imperium-Knowledge/designs/tools/city/说明/check.md` L10).

A card can be stretched by inserting seams, while the spec card itself is not changed: floor or wall is inserted only
into seams where both sides are of the same kind (the floor of one room, or a wall running across) and that do not cut
furniture or doors; by default a card widens by at most 4 and deepens by at most 2, some cards are held to 2, and a card
with an axis of symmetry inserts in pairs (`Imperium-Knowledge/现行/城/罗马城-城内.md` L150). Furniture, doors and columns stay
where they were; a seam does not run where one side is a vertical wall and the other floor, and does not cut a door, a
multi-cell object, a pool or two columns; A2, A9a, A9b, A41 and A45 widen by at most 2; and a card with a central yard
stretches symmetrically about the yard's midline (`Imperium-Knowledge/designs/tools/city/说明/cards.md` L28). The method
is adopted and the numbers are trial values (`Imperium-Knowledge/designs/tools/city/说明/cards.md` L28;
`Imperium-Knowledge/designs/city-plans/kit/城建数据格式-草案.md` L101). Streets, plots and groups without cards do not stretch,
and widening the bakery A45 (13×11) by 2 and deepening it by 1 makes it 15×12
(`Imperium-Knowledge/designs/city-plans/kit/城建数据格式-草案.md` L101-109).

> [!WARNING]
> **Conflict**: The tier of the row workshop unit A27c. Neither side dates its tier: the stretch scan's only ruling id
> dates the stretch method, not the grouping.
> - The card table puts it in storage and workshops (`Imperium-Knowledge/designs/roman-cards/罗马规格卡总表.md` L56); the
>   water-coverage rule, which belonged to the deleted hydraulics, also calls it workshop tier and not a household
>   (`Imperium-Knowledge/designs/tools/city/说明/draft.md` L48).

### Slant cards (斜卡)

A slant card is the 45° version of an upright card, made only for the house types that fall on 45° plots: small
dwellings, street-front shopfronts and small workshops; large items are placed horizontally or vertically and the land
is cut to fit them (`Imperium-Knowledge/现行/城/罗马城-城内.md` L132). A slant card is generated from the upright card's source
as a variant beside stretching: the frame turns 45°, the walls step in eight directions, the furniture stands horizontal
or vertical, the triangle left by a wall serves as a storage or yard corner, sizes are measured on the slanted land, and
small dwellings get one narrower size (`Imperium-Knowledge/现行/城/罗马城-城内.md` L133;
`Imperium-Knowledge/designs/回报/进度-斜卡工具.md` L116-117).

The slant cards cover seven target cards, the second round having added A2c, A2, A9a and A44, and each room keeps at
least 0.6 of its upright area (`Imperium-Knowledge/designs/tools/city/说明/cards.md` L42, L49). A slant card can be
stretched within the same limits as its upright card, and the stretched version is the same card
(`Imperium-Knowledge/designs/tools/city/说明/cards.md` L44, L50).

> [!NOTE]
> **Base game**: Wall cells that touch only corner to corner still enclose a room, but a pawn cannot pass through a
> diagonal seam, to be checked against `Data/` (`Imperium-Knowledge/designs/tools/city/说明/cards.md` L34).

> [!NOTE]
> **Unverified**: In the slant-card rounds the 15% cap could not be met (A27b at 44% on the island and A27a at 32% in
> the north part of the west city), and the reports leave to the user whether to repair the slant-card generator and
> make slant cards for the shopfront and rich tiers first or add cards first, or to loosen the cap; whether long slant
> houses may join into a neighbouring block's free ground; whether back houses and lanes join the long houses; whether
> blocks without cards keep the reference's 1:1 houses; whether empty blocks, which become courts of about 200 cells,
> get cards of their own; and whether the comparison table gets presets beyond the 15% cap and the share of the three
> tiers (`Imperium-Knowledge/designs/回报/进度-斜卡三轮.md` L106-111; `Imperium-Knowledge/designs/回报/进度-斜卡四轮.md` L110-114).

## Card families

- The row cottages A27a (dwelling), A27b (shopfront, with three shopfront forms) and A27c (workshop) are laid mixed in
  rows (`Imperium-Knowledge/designs/roman-cards/罗马规格卡总表.md` L47-48, L56). On an oblique street, neighbouring row
  cottages on one street front join into one long slant house (长斜房) divided into households, with a stepped wall
  round the whole, shared party walls and a street door for each household
  (`Imperium-Knowledge/现行/城/罗马城-城内.md` L164).
- The four-sided gates (四面门) A28, A28b and A28c differ in size, 5×3, 5×5 and 3×3, and all stand at the cross of
  main streets (`Imperium-Knowledge/designs/roman-cards/罗马规格卡总表.md` L21-23).
- The craftsman houses A2 (L-shaped yard), A2b (U-shaped yard, A2 with a room added at its north-east corner) and A2c
  (the small household) are one family (`Imperium-Knowledge/designs/roman-cards/罗马规格卡总表.md` L42-44).
- A9a, A9b and A41 form the small-yard house series, a core plus added rooms
  (`Imperium-Knowledge/designs/roman-cards/罗马规格卡总表.md` L45-46, L52).
- The courtyard house A34 grows a walled rear garden into A35, can turn its two front bedrooms into street shops (A34铺)
  and, in its square-hall form, can open a back door to the garden (A34后)
  (`Imperium-Knowledge/designs/roman-cards/罗马规格卡总表.md` L33-35).
- The tenements A38 (enclosed) and A39 (U-shaped) turn into each other
  (`Imperium-Knowledge/designs/roman-cards/罗马规格卡总表.md` L49-50).
- The rich-household houses have rear-hall and square-hall versions (`Imperium-Knowledge/designs/roman-cards/罗马规格卡总表.md` L29-40, L130).

The plot card family (地块卡族) is ten candidate cards, the free citizens' A51a to A51e and the commoners' A52a to A52e,
each 15×15 for one household's plot, kept out of the table's count; the things in a plot are interchangeable (livestock
pen, shed with shelves, garden, colonnade, workshop shed, barrel, well) (`Imperium-Knowledge/09_地图生成与CBF技术.md` L964).
The 15×15 is the household's plot, not a square house: the house follows the household's outline, made of several roof
blocks of differing shape and position (a long strip, an L, a U, two blocks with a passage between them, or a few
scattered), and occupies only those roof blocks; the house's walls enclose only the house; elsewhere in the plot are
yard, garden, shed, pen, barrel and lamp; the plot edge is not walled all round, only where the enlarged picture shows a
wall, fence or flower bed; and the cards have distinct outer shapes and a use for every room
(`Imperium-Knowledge/09_地图生成与CBF技术.md` L968; `Imperium-Knowledge/现行/城/罗马城-做法与顺序.md` L168) (replaces
`Imperium-Knowledge/09_地图生成与CBF技术.md` L964 in part). Vine trellises and shrines in the plots are not made for now
(`Imperium-Knowledge/现行/城/罗马城-做法与顺序.md` L168).

The plot cards follow the bright daytime pictures, not the dark ones, and railings, fences, low walls and walls are told
apart: something see-through with posts is a railing or fence, something solid and low is a low wall, and only a house's
outer wall is a wall; an item that cannot be recognised is written "unclear" and not placed
(`Imperium-Knowledge/09_地图生成与CBF技术.md` L973; `Imperium-Knowledge/现行/城/罗马城-做法与顺序.md` L169). On A52a the
dark vertical strip at the colonnade's west end is a railing, and on A51a the row of stakes on the west wing's north
edge is a fence, so that edge becomes railing; the square opening in the middle of A51a's pyramidal roof is a chimney or
skylight and nothing is placed, and the two round objects in its yard are ignored
(`Imperium-Knowledge/09_地图生成与CBF技术.md` L974). A52a and A51a were redone from daytime screenshots, and the other
eight, A51b to A51e and A52b to A52e, were redone 1:1 from the Anno 117 game data: the house variant and its rotation are
first recognised from the nine-grid image, the house takes only the cells its body module's outline falls on, props,
walls and railings are placed by each item's position and rotation, yard paving and grass are read from the ground
decals, and one game cell is 5 card cells (`Imperium-Knowledge/09_地图生成与CBF技术.md` L977;
`Imperium-Knowledge/现行/城/罗马城-做法与顺序.md` L169) (replaces `Imperium-Knowledge/09_地图生成与CBF技术.md` L973 in
part; `Imperium-Knowledge/designs/做法史/罗马城·做法与顺序.md` L231). The plot cards of the first and second levels are
kept as fill for the band along the wall's outer edge and for the workshop areas
(`Imperium-Knowledge/现行/城/罗马城-做法与顺序.md` L167). The cards are in
`Imperium-Knowledge/designs/roman-cards/roman_cards_v3.json` and their pictures in
`Imperium-Knowledge/designs/roman-cards/cards-v3` (`Imperium-Knowledge/09_地图生成与CBF技术.md` L964).

> [!NOTE]
> **Base game**: The plot cards' railings and fences use the base game's Fence, to be checked against `Data/`
> (`Imperium-Knowledge/现行/城/罗马城-做法与顺序.md` L169; `Imperium-Knowledge/09_地图生成与CBF技术.md` L973).

## Generic pieces (构件) and object roles

A piece is a generic building element of generated settlements that the base game lacks, such as a terrace edge, a
ramp or a courtyard wall, shared by every kit and skinned by faction (`docs/glossary.md` L194). The part table lists
only generic pieces that the base game cannot express and that all four eras use, like those an official DLC would
add; the form is common and the skin follows the faction's materials; borrowed pieces are only generated and the player
cannot build them (`Imperium-Knowledge/designs/ICF/构件需求表-v1.md` L4). Whether a base-game piece with a paint finish
can stand in is checked first, and if it can, nothing is borrowed or made; pieces are wanted in order: walls and
terraces first, then what cards need to enter a city, then what the medieval, tribal and modern kits need when each is
made (`Imperium-Knowledge/designs/ICF/构件需求表-v1.md` L4).

The table's pieces are given by their Roman, medieval, modern and tribal material where each is used, and those that
stand are (`Imperium-Knowledge/designs/ICF/构件需求表-v1.md` L6-27):

- the terrace edge, ramp and stairs, borrowed;
- a retaining wall, not made for now;
- a low parapet, wood and iron from the base game's fence with paint and stone from an already borrowed stair
  handrail;
- a low yard wall, one piece borrowed after viewing;
- no colonnade roof, since a ground band plus a row of columns is the base game's way to show a colonnade;
- the arch gate or gatehouse, with ReBuild's arch for comparison;
- the fountain and pool group, the pool being shallow water and one fountain piece borrowed after viewing;
- statue groups and monument columns, the base game first;
- paving variants, borrowed;
- and, for later rounds, the tent, stake fence and pointed stakes, hearth or campfire, drying rack and storage pit,
  sandbags, barricade and checkpoint, and a flag or flagpole of Imperium's own art.

> [!NOTE]
> **Deleted**: The table's water pieces, wanted in round 3 with walls and terraces (the aqueduct arch after round 3),
> served the city's water network: the surface water channel for the street, workshop and field channels (its water the
> base game's moving shallow water, its edge borrowed as curb pieces, also used for the pool group), the small bridge
> over a channel, and the Roman aqueduct arch; they belonged to the hydraulics axis the maintainer deleted on 2026-11-24
> (`Imperium-Knowledge/designs/ICF/构件需求表-v1.md` L4, L8-10, L19; `Imperium-Knowledge/15_水利主轴.md` L4, L34-36).

An object role (物件角色) names a thing, such as a floor lamp or a stone shelf, and has a candidate chain:
Imperium's own piece, then the base game or a DLC, then ReBuild (only when switched on and loaded), then a placeholder,
with a material rule (`Imperium-Knowledge/designs/ICF/ICF设计.md` L91). The released version does not depend on
ReBuild, so every role falls to a base-game piece or a placeholder (`Imperium-Knowledge/designs/ICF/ICF设计.md` L99).

> [!NOTE]
> **Base game**: The part table rests on what the base game has: shallow water, the fence (since 1.3), doors, large and
> small statues and Ideology's totems, the campfire, sandbags and barricades; stone tiles and flagstones and Ideology's
> flags stand only by half, and walls exist only as room walls; to be checked against `Data/`
> (`Imperium-Knowledge/designs/ICF/构件需求表-v1.md` L6-27).