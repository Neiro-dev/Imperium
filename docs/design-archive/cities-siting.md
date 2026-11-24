# City sites and terrain

This section covers how Imperium makes the ground of the maps it generates and where a city stands on that ground:
terrain made before the city, the landform of a city site, natural terrain guided by the city's skeleton, the city
circle within which terrain is changed, how a city meets a river, the district's area and its edges, what stands in for
height, siting by climate, map sizes and fitting a city into them, and failure and retry. It meets `cities.md` (how a
city grows from its core and the shape of its outline), `cities-walls.md` (how walls run on rock, water and openings),
`cities-inside.md` (the palace quarter, terraces and what stands inside the walls), `cities-outside.md` (the river
through the city, its banks, quays and bridges, and the land outside the walls) and `cities-forms.md` (templates and
their format). Older lines that newer settings replaced are given as Deleted notes, each naming what replaced it.

## Terrain before the city

Generating terrain together with the city is the expedition's biggest selling point, and terrain generation serves to
make an expedition destination worth going to (`Imperium-Knowledge/现行/城/地形与选址.md` L12). Every faction
settlement and every Empire quest map the mod generates gets its terrain first, and only then its walls, roads and
buildings, because buildings are what adapts to terrain (`Imperium-Knowledge/现行/城/地形与选址.md` L22;
`Imperium-Knowledge/designs/回报/审查-城建版本盘点-2026-11-10.md` L16). The mod's terrain is not used for the player's
colony, the starting-map contact ruins, underground layers or other mods' settlements
(`Imperium-Knowledge/现行/城/地形与选址.md` L23). It acts at the base game's landform step behind a new switch, and
with the switch off the map is identical to vanilla cell for cell (`Imperium-Knowledge/现行/城/地形与选址.md` L24).

The landform stage fixes the river course, rock bodies, coast, the load-bearing ground of the city area, the corridors
of the roads before the gates, bridge sites and exclusion zones; the building stage makes only structure-like terrain:
moat (壕), canal, pool, earth bridge (土桥) and bridge, clear strip (清空带), paving and tribal ditch (部落沟)
(`Imperium-Knowledge/现行/城/地形与选址.md` L25). The building stage has only four fallbacks, each counted: swapping in
load-bearing ground, sealing rock seams, moving animals away, and recomputing the area with water and rock deducted; on
test terrain the count is 0, and a count above 0 is recorded as ATTENTION
(`Imperium-Knowledge/现行/城/地形与选址.md` L26).

Natural terrain is generated first, then the city, and last the problem segments found are fixed by letting the
natural terrain accommodate the city: the city yields to the terrain first, and only at problem segments does the
terrain yield to the city (`Imperium-Knowledge/现行/城/地形与选址.md` L31;
`Imperium-Knowledge/designs/回报/审查-城建版本盘点-2026-11-10.md` L17; `Imperium-Knowledge/designs/ICF/ICF设计.md`
L118). A medieval settlement grows into a city and deletes only small pieces of terrain that nearly fit
(`Imperium-Knowledge/designs/ICF/ICF设计.md` L118; `Imperium-Knowledge/designs/instructions/生成具象规格-现行版.md` L84).

Geological Landforms (GL) is the terrain base (`Imperium-Knowledge/现行/城/地形与选址.md` L61;
`Imperium-Knowledge/designs/做法史/借用与第三方.md` L29). A map has at most one main landform plus a river layer
(`Imperium-Knowledge/现行/城/地形与选址.md` L66). GL's marks forbidding settlements are not copied: a fit table of
landform against site requirements (需求单) judges by the Roman and medieval ideas, and flat, riverless, inland tiles use
a self-written plain landform (gentle hills, meadow, forest edge) that stays flat and gets no ridges
(`Imperium-Knowledge/现行/城/地形与选址.md` L67). When a GL landform is chosen, Odyssey's landmarks and modifiers each
take up a category (`Imperium-Knowledge/09_地图生成与CBF技术.md` L478). All 17 biomes of the base game and Odyssey are
supported: the base game's 12 fall into five groups with sea ice as a separate fallback, and Odyssey's five
(grassland, glacier plain, scorched ground, glowing forest, lava field) attach to the nearest group as variants, lava
only on the outskirts; glowing forest, scorched ground and lava field are only guaranteed usable and free of errors
(`Imperium-Knowledge/09_地图生成与CBF技术.md` L434; `Imperium-Knowledge/现行/城/地形与选址.md` L73). Pirate camps do
not use Odyssey's interface, since Odyssey's scavengers and outposts exist only at the orbital layer
(`Imperium-Knowledge/09_地图生成与CBF技术.md` L667).

> [!NOTE]
> **Deleted**: the mod's own landform library with its per-kind terrain templates and 30 terrain sketches, including
> the layered templates (flat, hill and mountain base maps with river, coast and landmark layers) that covered the
> vanilla tile features and, when loaded, Odyssey's landmarks, an Odyssey landmark of the same kind as an existing
> large template forcing that template, and the second round's geometric landforms, judged a poor imitation and
> inefficient (`Imperium-Knowledge/09_地图生成与CBF技术.md` L420, L442;
> `Imperium-Knowledge/designs/做法史/借用与第三方.md` L16-19;
> `Imperium-Knowledge/designs/回报/审查-城建版本盘点-2026-11-10.md` L16). Taking GL as the terrain base replaced them
> (`Imperium-Knowledge/designs/做法史/借用与第三方.md` L29; `Imperium-Knowledge/现行/城/地形与选址.md` L61).

> [!NOTE]
> **Base game**: the base game has 12 biomes, sea ice among them, and Odyssey adds five (grassland, glacier plain,
> scorched ground, glowing forest, lava field), 17 in all; Odyssey's scavengers and outposts exist only at the orbital
> layer; to be checked against `Data/` (`Imperium-Knowledge/09_地图生成与CBF技术.md` L434, L667;
> `Imperium-Knowledge/现行/城/地形与选址.md` L73).

## The landform of a city site

Natural terrain first fixes the landform of the city site (城址地貌) from the world tile and then grows the detail
(`Imperium-Knowledge/现行/城/地形与选址.md` L32). One site type (城址型) is chosen for each world tile; the first-draft
list is river through the city (穿城河), confluence (汇流), branching with an island (分汊夹岛), coastal harbour bay
(海岸港湾), rock promontory (岩嘴) and plain (平原) (`Imperium-Knowledge/现行/城/地形与选址.md` L32;
`Imperium-Knowledge/designs/city-plans/kit/版型格式-方案.md` L27). Each type fixes only a few big things (river, island,
bay, rock terrace) by their position relative to the core, their size and their value range; the values are loose and
mirrorable, the detail follows GL noise, and only the big shape is set, never down to the cell
(`Imperium-Knowledge/现行/城/地形与选址.md` L32; `Imperium-Knowledge/09_地图生成与CBF技术.md` L797). The tile's
regularities are kept (which edge the river enters and leaves by, the river's width, the hilliness grade, the side
facing the sea), a tile that does not fit does not produce that type, and rivers are changed with the same restraint
as before (`Imperium-Knowledge/09_地图生成与CBF技术.md` L797). The site landform is the big shape of natural terrain,
not terrain the Roman city reshapes, so the city gets a fitting piece of ground while each game's shape still differs
(`Imperium-Knowledge/09_地图生成与CBF技术.md` L797). Each type is made into a template (版型), the subject of
`cities-forms.md` (`Imperium-Knowledge/现行/城/地形与选址.md` L32). A river split in two by an island inside the city is
the type branching with an island with the variant river bend (河湾), not a type of its own, and template number 1 is
written so (`Imperium-Knowledge/designs/city-plans/kit/版型格式-方案.md` L163).

> [!NOTE]
> **Deleted**: the draft's river-bend site type (河湾), and template number 1 written as river through the city with
> the variant river bend with island (`Imperium-Knowledge/09_地图生成与CBF技术.md` L797;
> `Imperium-Knowledge/designs/city-plans/kit/版型格式-方案.md` L73). The river-bend type became river through the city,
> the river bend having sat in an odd place, and the island case became the variant river bend of branching with an
> island (`Imperium-Knowledge/09_地图生成与CBF技术.md` L806;
> `Imperium-Knowledge/designs/回报/审查-城建版本盘点-2026-11-10.md` L23;
> `Imperium-Knowledge/designs/city-plans/kit/版型格式-方案.md` L163).

> [!NOTE]
> **Base game**: Odyssey's landmarks (peninsula, bay, fjord, lake island) and GL's landform library both fix the big
> shape first and then grow the detail, the precedent the site landform follows, to be checked against `Data/`
> (`Imperium-Knowledge/09_地图生成与CBF技术.md` L797).

A template states the world-tile conditions it fits: river grade (none, stream, river, large river, huge river, several
allowed), the number of rivers, coast (none, or one or more of north, east, south and west), hilliness (flat, small
hill, large hill, mountain, several allowed), biome class and text feature tags such as river bend or confluence; a
missing coast means no coast and a missing biome means any (`Imperium-Knowledge/designs/city-plans/kit/版型格式-方案.md`
L29). The river grades take the base game's names (`Imperium-Knowledge/designs/city-plans/kit/版型格式-方案.md` L164).
A template's terrain can hold water (river, tributary, sea, lake or pond, with its outline, islands as holes, deep and
shallow water, centre line and width), shores (natural, stone, quay, cliff), islands, cliffs with their high side,
rocks each marked as able or not able to serve as wall, terraces in numbered levels with the city floor at 0, and soft
ground and marsh (`Imperium-Knowledge/designs/city-plans/kit/版型格式-方案.md` L36-42).

> [!NOTE]
> **Base game**: the base game names its river grades stream, river, large river and huge river, to be checked against
> `Data/` (`Imperium-Knowledge/designs/city-plans/kit/版型格式-方案.md` L164).

The terrain of the city site is made first at map generation, in the way of community terrain mods with GL as the
baseline, as a piece of land created for the city: river course, banks and terraces, gentle slopes and height, and
rock bodies can all be made from nothing as long as they stay within what the vanilla map tile itself describes (its
landform, river, road and coast), and their size need not follow vanilla (`Imperium-Knowledge/现行/城/地形与选址.md`
L36; `Imperium-Knowledge/09_地图生成与CBF技术.md` L852;
`Imperium-Knowledge/designs/city-plans/kit/版型格式-方案.md` L4). City layout no longer creates terrain objects for a
wall's bend or a trunk road's turn, so the city grows on land that looks prepared for it and its organic outline takes
its reason from the terrain (`Imperium-Knowledge/现行/城/地形与选址.md` L36). No rock, pond or small mound is grown
beside a long straight stretch of an open edge, and the circle is not changed for it
(`Imperium-Knowledge/09_地图生成与CBF技术.md` L832; `Imperium-Knowledge/现行/城/地形与选址.md` L47).

> [!NOTE]
> **Deleted**: growing a rock head, pond or small mound beside a long straight stretch of an open edge and regrowing the
> circle (`Imperium-Knowledge/09_地图生成与CBF技术.md` L830-831; `Imperium-Knowledge/designs/做法史/地形与选址.md`
> L10-11), dropped by the rule that the circle is only a range (`Imperium-Knowledge/09_地图生成与CBF技术.md` L832);
> that rule's base of vanilla map blocks gave way in turn to site terrain made at map generation
> (`Imperium-Knowledge/09_地图生成与CBF技术.md` L852; `Imperium-Knowledge/designs/做法史/地形与选址.md` L132).

When terrain is re-laid, the tile's own regularities are kept: the map edges by which the river enters and leaves, the
river's grade and width, the entry edge and direction of the world roads, the biome, the hilliness grade, the side
facing the sea and the tile's features; what may vary is how the river bends in the middle, where rock outcrops lie and
how big they are (their count and total following the hilliness grade), and how marsh and fertile ground are spread
(`Imperium-Knowledge/现行/城/地形与选址.md` L104). The edge by which the river leaves the map is taken from the world
tile's record, not from which side of the map holds more river cells (`Imperium-Knowledge/现行/城/地形与选址.md` L110).

Rome does not shape a separate site: terrain is only re-laid by the tile's regularities, and terraces exist only as
parts that come with combination pieces such as the palace-quarter group (`Imperium-Knowledge/现行/城/地形与选址.md` L39;
`Imperium-Knowledge/09_地图生成与CBF技术.md` L762, L805). Inside the city the river keeps its course and width, nothing
is levelled because the colony world has no height, and no hill is cut to straighten a wall
(`Imperium-Knowledge/designs/instructions/生成具象规格-现行版.md` L82-83; `Imperium-Knowledge/09_地图生成与CBF技术.md`
L772; `Imperium-Knowledge/designs/tools/审查清单-图面.md` L66). Platforms are only parts of combination pieces, rock
cells are mountain and cannot be built on, and the ground has no stepped artificial terraces
(`Imperium-Knowledge/09_地图生成与CBF技术.md` L805; `Imperium-Knowledge/现行/城/罗马城-城内.md` L177); how terraces are
drawn belongs to `cities-inside.md`.

> [!NOTE]
> **Deleted**: Rome shaping its site: platforms, slope belts of 6 to 10 cells, terraces, quarry cuts and water filled
> into embankments, first above a 20% threshold, then narrowed to three purposes (levelling a landmark terrace, clearing
> marsh and small hills that block the axis, straightening a river through the city) under per-tier caps still to be
> set, with the no-high-ground row's upper city on a levelled landmark terrace; the spec still said so when the card
> review checked it (`Imperium-Knowledge/designs/instructions/生成第2轮重做-第一段批准与第二段补充.md` L97-123, L361,
> L415-420, L428; `Imperium-Knowledge/designs/做法史/地形与选址.md` L51-52, L87, L91;
> `Imperium-Knowledge/designs/做法史/罗马城·墙.md` L44; `Imperium-Knowledge/designs/回报/审查-城卡同类冲突-2026-11-10.md`
> L81), its method supplied by the Roman kit on stage A's temporary grid (`Imperium-Knowledge/designs/ICF/ICF设计.md`
> L118). The rule that Rome does not shape a separate site removed it (`Imperium-Knowledge/09_地图生成与CBF技术.md` L762;
> `Imperium-Knowledge/现行/城/地形与选址.md` L39; `Imperium-Knowledge/designs/instructions/生成具象规格-现行版.md` L82).

## Natural terrain guided by the skeleton

Once the site landform is fixed, natural terrain is guided by the skeleton (骨架): the kinds of rock, river and water,
marsh and soft ground, fertile ground, sand and gravel, and trees follow the tile and landform rules, and their
positions are guided after the skeleton (core, river, gates, main-street direction) is set, looking at the skeleton
only and not at the walls (`Imperium-Knowledge/现行/城/地形与选址.md` L40;
`Imperium-Knowledge/09_地图生成与CBF技术.md` L784). Guiding natural terrain by an idea is what makes it look natural
(`Imperium-Knowledge/designs/回报/审查-城建版本盘点-2026-11-10.md` L21). What the city can use is placed where the city
wants it; what it cannot use keeps off the district, the wall band (墙带) and clear strip, and the approach before the
gates (`Imperium-Knowledge/现行/城/地形与选址.md` L41). It is not regrown outside the city to keep the tile's totals:
terrain is changed only in the city circle and a short transition band, and river, rock and water outside the city stay
as in vanilla (`Imperium-Knowledge/现行/城/地形与选址.md` L37; `Imperium-Knowledge/09_地图生成与CBF技术.md` L806).
Terrain is grown by field, noise and threshold and not drawn as shapes: rock and water come from raising or lowering the
height field locally before they land, with noise on top and thresholds growing them, and nothing is levelled
(`Imperium-Knowledge/现行/城/地形与选址.md` L41; `Imperium-Knowledge/09_地图生成与CBF技术.md` L784). The walls are
wrapped last by the curtain method and borrow rock and water as wall, and problem segments are still fixed by the
natural terrain (`Imperium-Knowledge/09_地图生成与CBF技术.md` L784).

> [!NOTE]
> **Deleted**: regrowing what the city cannot use outside the city so that each class keeps the tile's totals, as the
> r3 trial and the generator did, with that trial's compressing of high ground and pressing out of thin rock inside the
> city zone (`Imperium-Knowledge/09_地图生成与CBF技术.md` L784; the clause of `Imperium-Knowledge/现行/城/地形与选址.md`
> L41; `Imperium-Knowledge/designs/city-plans/handcity/2026-11-03/整城v3/r3-进度.md` L8-10;
> `Imperium-Knowledge/designs/tools/city/说明/gen.md` L11). Changing terrain only in the city circle and its transition
> band, and clearing the district of natural obstacles, replaced it (`Imperium-Knowledge/09_地图生成与CBF技术.md` L806,
> L834; `Imperium-Knowledge/现行/城/地形与选址.md` L37, L43).

Rock at the city edge either hugs the wall line and is thick enough to serve as wall, or lies outside the clear strip,
never half on the wall band; no rock is left on the approach before a gate or on a main-street line
(`Imperium-Knowledge/现行/城/地形与选址.md` L42; `Imperium-Knowledge/09_地图生成与CBF技术.md` L784). When an approach
road enters the circle at a point against rock the city edge has borrowed, that is accepted: the road keeps its course
and the gate opens on the land wall beside the rock (`Imperium-Knowledge/现行/城/地形与选址.md` L42;
`Imperium-Knowledge/09_地图生成与CBF技术.md` L839).

The natural terrain passes when it looks like the landform type of its tile and looks natural, with the terrain
objects the city does not use still lying scattered about rather than each one fitting the city; terrain and city then
show cause and effect (`Imperium-Knowledge/现行/城/地形与选址.md` L44; `Imperium-Knowledge/09_地图生成与CBF技术.md`
L784).

## The city circle: changing terrain where it is used

Terrain is changed only where it is used: the city circle (城区圈) plus a small transition band (过渡带); outside,
river, rock and water stay as in vanilla, and the city grows inside the circle without leaving it
(`Imperium-Knowledge/现行/城/地形与选址.md` L37; `Imperium-Knowledge/09_地图生成与CBF技术.md` L806). When the site is
chosen, the most buildable open land goes inside the district, the big flat land of the map going to the city first
(`Imperium-Knowledge/09_地图生成与CBF技术.md` L806;
`Imperium-Knowledge/designs/回报/审查-城建版本盘点-2026-11-10.md` L23). The site landform is read only through the
circle the generator grows (`Imperium-Knowledge/09_地图生成与CBF技术.md` L841;
`Imperium-Knowledge/designs/tools/city/说明/gen.md` L64).

A river that already crosses the circle is not moved (`Imperium-Knowledge/现行/城/地形与选址.md` L38;
`Imperium-Knowledge/designs/tools/city/说明/gen.md` L68). If the tile has a river that is not near the city, the first
square (第一广场) is placed on the approach at the point nearest the river and the city grows across it; only if the
river still does not cross the circle is one stretch of the original river moved into the circle by a displacement
field (位移场), at the place needing the least movement and only inside the default transition band, and if it cannot
be moved in, the site is reported and the band is not widened (`Imperium-Knowledge/现行/城/地形与选址.md` L38;
`Imperium-Knowledge/09_地图生成与CBF技术.md` L821, L841). The transition band is 0.5 times the circle's equivalent
radius (`Imperium-Knowledge/designs/tools/city/说明/gen.md` L67; `Imperium-Knowledge/09_地图生成与CBF技术.md` L841).
Inside the circle the river passes 0.3 to 0.6 of the radius from the core, to one side, with only a gentle bend and not
wrapping round the city (`Imperium-Knowledge/09_地图生成与CBF技术.md` L806); a moved river passes the core side at a
distance of at least the quay belt plus the shortest bridgehead street plus one cell plus half the river's width plus a
margin, enters and leaves the circle once each and keeps a minimum turning radius
(`Imperium-Knowledge/designs/tools/city/说明/gen.md` L69). The displacement field pushes the original stretch over,
keeping its width, bank roughness and shallows, rather than drawing a new river
(`Imperium-Knowledge/09_地图生成与CBF技术.md` L806). Small patches of rock, soft ground and marsh touching the circle or
an approach road are cleared to flat ground (`Imperium-Knowledge/designs/tools/city/说明/gen.md` L71). The river then
reads as a city built at a ford, not a river dragged beside a road (`Imperium-Knowledge/现行/城/地形与选址.md` L38;
`Imperium-Knowledge/09_地图生成与CBF技术.md` L821). The quay walls, docks, bridge and long straight wall-face banks of
the river inside the city are made when the city is laid out, while outside the river bends as before, so the river
reads half natural and half changed by the city (`Imperium-Knowledge/09_地图生成与CBF技术.md` L806); these works belong
to `cities-outside.md`.

The circle's area target is 1.5 times the district area (trial value); each map takes the largest multiple that fits,
and neither the distance to the map edge nor the minimum distance of the core from water is relaxed for it; on the
seven test maps only 1.09 to 1.41 times fit (`Imperium-Knowledge/现行/城/地形与选址.md` L91;
`Imperium-Knowledge/09_地图生成与CBF技术.md` L838; `Imperium-Knowledge/designs/回报/Code-第二段轮廓-五轮.md` L3). The circle is
only an upper bound: the city grows inside it until it reaches the district area, the city, its streets, walls and
towers have no cell outside it, and borrowing terrain decides only how the city grows inside the circle, never the
circle itself, so the city can choose a direction and the wall follows the city rather than tracing the circle
(`Imperium-Knowledge/现行/城/地形与选址.md` L91; `Imperium-Knowledge/09_地图生成与CBF技术.md` L829).

> [!NOTE]
> **Deleted**: picking a site and drawing a circle when no circle is given, and the district taken as the circle's
> mask (`Imperium-Knowledge/09_地图生成与CBF技术.md` L821; `Imperium-Knowledge/designs/tools/city/说明/gen.md` L62).
> Reading the site only through the generator's circle, with the circle an upper bound inside which the city grows,
> replaced it (`Imperium-Knowledge/09_地图生成与CBF技术.md` L829, L841; `Imperium-Knowledge/现行/城/地形与选址.md` L91).

The circle does not hug the map edge: a medium or small city leaves at least the wall band, the clear strip and one band
of gardens and cemeteries in depth (trial value 30 cells) from the edge; if it does not fit, the core is moved first,
and if it still does not fit, the failure and retry applies, the circle never being squeezed toward the edge
(`Imperium-Knowledge/现行/城/地形与选址.md` L92; `Imperium-Knowledge/09_地图生成与CBF技术.md` L820). On a fixed test
map where the circle cannot be placed, the case is recorded as a failure and no outline is produced
(`Imperium-Knowledge/designs/回报/Code-第二段轮廓-二轮.md` L3). The city then reads
as standing in the land, the map edge does not cut it, and an enemy or caravan entering from the edge walks a while
before reaching the wall (`Imperium-Knowledge/现行/城/地形与选址.md` L92; `Imperium-Knowledge/09_地图生成与CBF技术.md`
L820). For a large city the wall, with its wall band, clear strip and moat, keeps at least 10 cells from the map edge
(`Imperium-Knowledge/现行/城/地形与选址.md` L82).

In growing the circle, crossing a river adds no cost and the river is not counted in the net area; the core is no
nearer water than the quay belt (码头带) plus the bridgehead street (桥头街) plus half the first square; and the circle
bends only at nodes (节点), where it crosses a river or road and at the ends of edges that borrow rock or water, its
other stretches being straightened, with a straight stretch longer than the limit bending only at a change of
direction (`Imperium-Knowledge/现行/城/地形与选址.md` L93; `Imperium-Knowledge/09_地图生成与CBF技术.md` L840). No city
centre sits against the river bank: the main core lies about where the approach crosses the river, separated from it by
the quay belt (`Imperium-Knowledge/designs/回报/审查-原意走样二.md` L49).

A site is decided by the site requirements and the particular map; the wall method governs only the wall and does not
delimit the site, and the city is not pressed into a narrow wedge marked out by the wall method
(`Imperium-Knowledge/现行/城/地形与选址.md` L94; `Imperium-Knowledge/designs/整理/城建错题转拦截-2026-11-05.md` L23).

> [!NOTE]
> **Unverified**: the outline reports left to the design side whether the windmill-like octagon with four notches
> that an empty plain gives is to be made regular, whether the T1 snapshot is replaced by one exported under the new
> deep-water rule, and whether the T4 confluence is read at the flood-meeting point or at the actual fork
> (`Imperium-Knowledge/designs/回报/Code-第二段轮廓-二轮.md` L25; `Imperium-Knowledge/designs/回报/Code-测试地形快照.md`
> L19, L22). Their question of the circle multiple is settled by taking the largest multiple that fits each map
> (`Imperium-Knowledge/designs/回报/Code-第二段轮廓-五轮.md` L20; `Imperium-Knowledge/09_地图生成与CBF技术.md` L838).

> [!NOTE]
> **Unverified**: how candidate sites are compared is not written; the version inventory recommends a line-by-line
> comparison: buildable open land, then fewer problem segments, then nearness to the approach
> (`Imperium-Knowledge/designs/回报/审查-城建版本盘点-2026-11-10.md` L122, L165).

## Where the city stands on a river

On a plains map with a river, the river comes to the city rather than the city going to the river: terrain generation
lets the river pass naturally through the middle of the map, the city stands in the middle, and the city spans the
river with the river running through it, since a city going to the river would squeeze into a corner of the map
(`Imperium-Knowledge/现行/城/罗马城-河与水.md` L12-13; `Imperium-Knowledge/09_地图生成与CBF技术.md` L728;
`Imperium-Knowledge/现行/城/地形与选址.md` L50). The river winds at random from where it enters the map, with no bend
angle prescribed and no hard right-angle bend (`Imperium-Knowledge/现行/城/罗马城-河与水.md` L19;
`Imperium-Knowledge/09_地图生成与CBF技术.md` L734). The core, the palace quarter and the public core stand on one bank,
on the inside of the bend where there is one; how large each bank is and whether the far bank becomes a district are
read from the terrain and the approach roads of the map, with no preset large and small bank, the same for large,
medium and small cities (`Imperium-Knowledge/现行/城/罗马城-河与水.md` L23; `Imperium-Knowledge/09_地图生成与CBF技术.md`
L808). The banks, quays, bridges and water gates of such a city belong to `cities-outside.md` and `cities-walls.md`.

> [!NOTE]
> **Deleted**: the earlier river lines: a city built on one bank of a large river, with a harbour band, a bridgehead
> fort across and small forts watching the bridge, laid for the first hand-placed city after a literature study found
> large rivers mostly outside a city or along its edge (`Imperium-Knowledge/09_地图生成与CBF技术.md` L426, L682;
> `Imperium-Knowledge/裁定归档/2026-10.md` L139); the first cross-river rule, with the river through the middle as the
> long axis, the main bank holding most of the city and the far bank a second district
> (`Imperium-Knowledge/09_地图生成与CBF技术.md` L727, L806); and the river winding about 90° round the city
> (`Imperium-Knowledge/09_地图生成与CBF技术.md` L733). The river winding at random, with the banks read from terrain
> and approach roads, replaced them (`Imperium-Knowledge/09_地图生成与CBF技术.md` L734, L808;
> `Imperium-Knowledge/现行/城/罗马城-河与水.md` L19, L23).

The reading of five test terrains looked only at where the roads come from and where they cross the river, whether the
river can be waded, and whether rock is thick enough (`Imperium-Knowledge/designs/研究/城/五张测试地形读法-2026-11-05.md`
L10-14). Its common points are these: the city centre sits where a road crosses the river, at the bridgehead on all
three maps with a bridge; the far bank counts as a district only if a road comes from that bank and the bridge crosses,
so wedge land with water on two sides but no road is not enclosed; when both banks are districts the river is the long
axis inside the city and only two water gates, in and out, need defence, and on a confluence map the city's upstream
edge is drawn below the confluence so that only one river crosses it; and rock heads become wall by their distance from
the centre and their thickness (`Imperium-Knowledge/designs/研究/城/五张测试地形读法-2026-11-05.md` L26-31), their other
use in that reading, as a base, being deleted as noted under the district's edges. The per-map reading is drawn in
`Imperium-Knowledge/designs/研究/城/图/五张测试地形读法-2026-11-05.png`, where red dots mark road entries, yellow frames
bridges, orange pentagons the read city centres and light purple the land the river cuts off without a road
(`Imperium-Knowledge/designs/研究/城/五张测试地形读法-2026-11-05.md` L6, L18-24).

> [!NOTE]
> **Base game**: every river in RimWorld can be waded, shallow water and chest-deep rapids being passable and only deep
> water blocking, so a river slows an enemy and makes him fight standing in water but does not stop him, to be checked
> against `Data/` (`Imperium-Knowledge/designs/研究/城/五张测试地形读法-2026-11-05.md` L13).

> [!NOTE]
> **Unverified**: the five-terrain reading left open the actual road lines, since the snapshots recorded only entry
> points, and T1's deep-water rule, which differs from the other four maps
> (`Imperium-Knowledge/designs/研究/城/五张测试地形读法-2026-11-05.md` L33-36); which of three versions of the T2 case at
> 28% is taken (harbour; straddling with the same core; straddling with the seed at the north bank of the bridgehead)
> is left to the user (`Imperium-Knowledge/designs/回报/Code-第二段轮廓-校准与核心.md` L32).

> [!NOTE]
> **Unverified**: whether a plain includes small hills, what a plain without a river does, the default for hill,
> mountain and coast tiles, how "no hard bend" is measured and the river's cross-section are open, tracked as live list
> #71 (`Imperium-Knowledge/现行/城/地形与选址.md` L129; `Imperium-Knowledge/现行/城/罗马城-河与水.md` L31;
> `Imperium-Knowledge/09_地图生成与CBF技术.md` L728). The version inventory reads the first as no longer meaningful and
> the default for hills, mountains and coast as answered by the outline growing on vanilla terrain
> (`Imperium-Knowledge/designs/回报/审查-城建版本盘点-2026-11-10.md` L119).

## The district's area and its edges

The district area (城区面积) is the net buildable area inside the walls; the wall band, clear strip and moat are not
counted and are added when a site is sought (`Imperium-Knowledge/现行/城/地形与选址.md` L80). It is computed from the
actual map as buildable land (land cells less water, rock and marsh) times the ratio in the site requirements, 0.16
for a medium city (trial value, taken from the samples R1 and S49 as net area over buildable land), with no limit on the
aspect ratio; the site requirements do not fix an area, and the district is not first drawn as a circle
(`Imperium-Knowledge/现行/城/地形与选址.md` L81; `Imperium-Knowledge/09_地图生成与CBF技术.md` L808). A large city's
wall circle, the river through it included, takes half to two thirds of the map, so one reaches the foot of the city as
soon as one enters from the edge (`Imperium-Knowledge/现行/城/地形与选址.md` L82;
`Imperium-Knowledge/09_地图生成与CBF技术.md` L870). Each user of site selection has its site requirements, one Def
each, stating district size, preferred landform, hard requirements and site rules
(`Imperium-Knowledge/现行/城/地形与选址.md` L79).

> [!NOTE]
> **Deleted**: the district area fixed by the site requirements, with the city's scale always following them, and for
> a large city 0.33 of buildable land capped at 40% of the map, with a 30-cell band of gardens and cemeteries kept to
> the map edge (`Imperium-Knowledge/designs/做法史/地形与选址.md` L22, L27, L53-54, L84, L86;
> `Imperium-Knowledge/09_地图生成与CBF技术.md` L820). The area computed from the map, and the large city's wall circle
> taking half to two thirds of the map with its wall at least 10 cells from the edge, replaced it
> (`Imperium-Knowledge/现行/城/地形与选址.md` L81-82; `Imperium-Knowledge/09_地图生成与CBF技术.md` L870).

The district's outline grows on the original terrain: the site is chosen on natural terrain first, the district grows
outward from the core and stops at hill feet and shorelines, which become its edge, and rock serves as wall unbuilt
while the water side is built along the bank (`Imperium-Knowledge/09_地图生成与CBF技术.md` L808). The second-stage
outline method (edges split into hill, water and opening, thin strips removed, mountains pulled only at problem
segments) is joined back to the Roman line, with R1, on a 300 map with a large-hills plot, and S49, on a 250 map with
flat ground and a lone mountain, as its samples (`Imperium-Knowledge/09_地图生成与CBF技术.md` L807-808;
`Imperium-Knowledge/designs/回报/审查-城建版本盘点-2026-11-10.md` L119); the shape of the Roman circle itself is in
`cities.md` (`Imperium-Knowledge/现行/城/罗马城-做法与顺序.md` L129).

The district edge is of three kinds: mountain (rock at least 5 cells thick at its thinnest, counted outward from the
edge line), water (deep water that cannot be waded) and opening (开口, everything else); an edge within 12 cells of a
mountain foot or shoreline reaches over to hug it, and how the Roman wall runs on each kind is in `cities-walls.md`
(`Imperium-Knowledge/现行/城/地形与选址.md` L45). Rock bodies are graded by their number of connected cells: scattered
rock (零星岩) under 100, small hill (小丘) 100 to 1500, and main mountain (主山体) over 1500 or connected to the map edge
(`Imperium-Knowledge/现行/城/地形与选址.md` L120).

The growing circle does not stop at small things: scattered rock on a plain and small puddles, each under 100 cells
(trial value), are filled in, the city grows over them, and their original place becomes a wall node where a tower
stands and the wall turns; they are not enlarged by noise (`Imperium-Knowledge/现行/城/地形与选址.md` L46;
`Imperium-Knowledge/09_地图生成与CBF技术.md` L823). Rock or water that the circle borrows as an edge is large: rock at
least 300 cells and at least 5 cells thick, water at least 300 cells (trial values)
(`Imperium-Knowledge/现行/城/地形与选址.md` L46). Wall bends thus have a source, small features are not enlarged into
other terrain, and enlarging does not use up district area (`Imperium-Knowledge/09_地图生成与CBF技术.md` L823). A circle
with fewer than 3 usable nodes on its outer edge (gates, river closures, rock edges, filled-in small features; trial
value) counts as a failure and is generated again, and regularity without a cause is not accepted
(`Imperium-Knowledge/现行/城/地形与选址.md` L107; `Imperium-Knowledge/09_地图生成与CBF技术.md` L825).

> [!NOTE]
> **Deleted**: small puddles kept as open cisterns, and features slightly too small enlarged by noise until they could
> be borrowed (`Imperium-Knowledge/09_地图生成与CBF技术.md` L822). Filling them in as wall nodes without enlarging
> replaced it (`Imperium-Knowledge/09_地图生成与CBF技术.md` L823).

> [!NOTE]
> **Base game**: vanilla plains usually carry scattered rock and small puddles, so a plain without them is generated
> again, to be checked against `Data/` (`Imperium-Knowledge/09_地图生成与CBF技术.md` L825).

Natural terrain is pulled to suit the city, pulling the mountain (拉山), only at the problem segments (问题段) found, of
three kinds: a hook, an opening segment that reaches out at least 3 cells to meet mountain or water and folds back; a
run of short openings, opening segments of 5 cells or less on the same side separated by mountain, at least two in a
row; and a gate against a mountain, within 3 cells of where it meets the mountain, where the gate is moved and the
mountain is not pulled (`Imperium-Knowledge/现行/城/地形与选址.md` L47). Prevention comes first: parts of the district
narrower than 8 cells are cut off to the outside, and sites with fewer problem segments are preferred
(`Imperium-Knowledge/现行/城/地形与选址.md` L47; `Imperium-Knowledge/designs/回报/审查-城建版本盘点-2026-11-10.md` L17).
Pulling adds rock in the band 8 cells outside the city edge up to a thinnest thickness of 5, and an opening of 12 cells
or less with mountain at both ends is closed by mountain; it is done by terrain generation, raising the field locally
and layering noise so that rock grows by threshold before rock lands, on stage A's temporary grid, and terrain Rome
changes while building the city is not natural terrain (`Imperium-Knowledge/现行/城/地形与选址.md` L47;
`Imperium-Knowledge/designs/ICF/ICF设计.md` L118). Whether a barrier counts is judged by
pathfinding: once an opening is closed, no one can enter the city from outside without mining or breaking a wall
(`Imperium-Knowledge/现行/城/地形与选址.md` L48). No mountain is pulled on gate-road corridors, bridge sites, river
courses, field zones or the map edge (`Imperium-Knowledge/现行/城/地形与选址.md` L49).

Natural obstacles inside the district (rock, scattered rock and small hills included; marsh, soft ground, small
puddles) are cleared by default when the city is laid out, and the cleared land is laid with blocks as usual; the river
still passes through the city, rock and mountains outside the district edge still serve as its edge, and rock the city
does not need still keeps off the district (`Imperium-Knowledge/现行/城/地形与选址.md` L43;
`Imperium-Knowledge/09_地图生成与CBF技术.md` L834). Clearing obstacles does not count as changing terrain or making
terrain objects, and the city is one whole buildable area whose shape is set only at the edge by rock, water and
approach roads (`Imperium-Knowledge/现行/城/地形与选址.md` L43; `Imperium-Knowledge/09_地图生成与CBF技术.md` L834).
Nothing inside the city is placed by rock: no rock is kept beside the core for the palace quarter (宫区) or sanctuary
(圣所), and the rock of a city backed by rock is only the edge of its district
(`Imperium-Knowledge/09_地图生成与CBF技术.md` L835; `Imperium-Knowledge/现行/城/罗马城-城内.md` L112;
`Imperium-Knowledge/designs/做法史/罗马城·城内.md` L181).

> [!NOTE]
> **Deleted**: rock and small hills used inside the city: a large rock head kept upstream beside the core as base or
> back wall for the palace quarter or sanctuary, rock heads as bases for palace gardens, churches and the cathedral, the
> sanctuary check listing the rock pieces inside the wall, and small hills inside the city made into terraces or laid
> over without terracing (`Imperium-Knowledge/09_地图生成与CBF技术.md` L689, L784, L800, L805;
> `Imperium-Knowledge/designs/做法史/地形与选址.md` L29, L41, L101, L114, L117;
> `Imperium-Knowledge/designs/做法史/罗马城·城内.md` L34, L36, L40, L55, L71;
> `Imperium-Knowledge/designs/研究/城/五张测试地形读法-2026-11-05.md` L14;
> `Imperium-Knowledge/designs/tools/city/说明/check.md` L10;
> `Imperium-Knowledge/designs/city-plans/城市建筑学对照-罗马城理念-2026-10-30.md` L45;
> `Imperium-Knowledge/designs/tools/city/check-覆盖表.md` L420). Clearing the district of natural obstacles and placing
> nothing in the city by rock replaced it (`Imperium-Knowledge/09_地图生成与CBF技术.md` L834-835;
> `Imperium-Knowledge/现行/城/地形与选址.md` L43).

## Height and what stands in for it

The colony world shows no height, so terrain is read only as the shapes of land and water, and neither the city nor the
palace quarter is placed on a ridge or at the highest place (`Imperium-Knowledge/现行/城/地形与选址.md` L115;
`Imperium-Knowledge/现行/城/罗马城-做法与顺序.md` L48; `Imperium-Knowledge/09_地图生成与CBF技术.md` L700;
`Imperium-Knowledge/designs/整理/城建错题转拦截-2026-11-05.md` L26). Before a real city's logic that comes from terrain
height is borrowed, what stands in for that height in the colony world is fixed first: water, rock, soft ground, or the
terrace that comes with a combination piece; the feel of sloping land is offset by the colony world's own strengths
(`Imperium-Knowledge/现行/城/罗马城-做法与顺序.md` L48; `Imperium-Knowledge/designs/整理/城建错题转拦截-2026-11-05.md`
L38).

> [!NOTE]
> **Deleted**: siting by height: the acropolis, palace quarter and water tower at the highest point given by siting,
> and the siting preference for high ground (`Imperium-Knowledge/designs/instructions/生成具象规格-现行版.md` L355;
> `Imperium-Knowledge/designs/instructions/生成第2轮重做-第一段批准与第二段补充.md` L362, L657;
> `Imperium-Knowledge/designs/整理/城建错题转拦截-2026-11-05.md` L60). The rule that the colony world reads no height
> and nothing is sited for it replaced it (`Imperium-Knowledge/09_地图生成与CBF技术.md` L700;
> `Imperium-Knowledge/现行/城/地形与选址.md` L115; `Imperium-Knowledge/designs/instructions/生成具象规格-现行版.md` L4).

> [!NOTE]
> **Deleted**: the water palace (水宫), that is the water tower (分水塔), which the same rule keeps off ridges and the
> highest place, belonged to the hydraulics the maintainer deleted (`Imperium-Knowledge/现行/城/罗马城-做法与顺序.md` L48;
> `Imperium-Knowledge/designs/整理/城建错题转拦截-2026-11-05.md` L26).

> [!NOTE]
> **Base game**: RimWorld has no terrain height, so rock is what reads as high ground, to be checked against `Data/`
> (`Imperium-Knowledge/designs/city-plans/罗马城排法-算法.md` L17).

In reading terrain, water (the shore direction of river, sea and lake) and the position and direction of bridges come
first; rock, marsh, soft ground and deep water are immovable obstacles; rock stands for high ground and its edge for a
ridge, shallow streams and soft belts for a valley; and approach roads are the entry points and directions of the world
roads (`Imperium-Knowledge/designs/city-plans/罗马城排法-算法.md` L16-18). A real city's mountains, ridges and citadel
heights become stretches of rock with the wall following the rock edge, its valleys and lowlands shallow streams and
soft belts, and its upper city and terraces terraces made of borrowed pieces
(`Imperium-Knowledge/designs/city-plans/罗马城排法-算法.md` L95-99).

A city's form takes one of two rows by its terrain, a no-high-ground row (无高地行) and a high-ground row (有高地行)
(`Imperium-Knowledge/09_地图生成与CBF技术.md` L801; `Imperium-Knowledge/designs/instructions/生成具象规格-现行版.md`
L121-124), and in the colony world high ground means rock (`Imperium-Knowledge/designs/city-plans/罗马城排法-算法.md`
L17). In the no-high-ground row a city by water has its long axis and main street along the water, with no fixed
aspect ratio (`Imperium-Knowledge/现行/城/罗马城-做法与顺序.md` L127; `Imperium-Knowledge/09_地图生成与CBF技术.md` L801).
In the high-ground row a city backed by hills (背山城) on a rock-promontory site has its first square on open land before
the rock and grows outward from it until it stops at the rock edge, the rock serving only as the edge of the district,
with S49, R1 and image three as samples; that the first square lies about equally far from the district edge in four
directions is checked (`Imperium-Knowledge/现行/城/罗马城-做法与顺序.md` L128; `Imperium-Knowledge/现行/城/罗马城-城内.md`
L112). The core from which a city grows is the first square, not an acropolis (卫城) or palace quarter
(`Imperium-Knowledge/现行/城/罗马城-做法与顺序.md` L84; `Imperium-Knowledge/09_地图生成与CBF技术.md` L809). The
high-ground row's upper city is an acropolis with its own inner wall, gate and towers, the rock face side unbuilt and
the cliff serving as its second line (`Imperium-Knowledge/designs/instructions/生成具象规格-现行版.md` L121-124;
`Imperium-Knowledge/designs/instructions/生成第2轮重做-第一段批准与第二段补充.md` L362).

> [!NOTE]
> **Unverified**: the current cards do not restate the high-ground row's acropolis with its own inner wall, so whether
> it was dropped or only not restated cannot be told (`Imperium-Knowledge/现行/城/罗马城-做法与顺序.md` L84, L127-128;
> `Imperium-Knowledge/designs/回报/审查-城卡同类冲突-2026-11-10.md` L61). The research on mature city generation, in its
> list of its own decisions, places Constantinople in the high-ground row for its land wall over ridges and judges
> regular four-sided cases as having existed
> (`Imperium-Knowledge/designs/研究/城/成熟城建生成-外形与城墙-2026-11-11.md` L164-168).

> [!NOTE]
> **Deleted**: a city by water stretched to about 1.5:1, with only a city on pure flat ground nearly round about its
> core (`Imperium-Knowledge/designs/city-plans/罗马城排法-算法.md` L19); no fixed aspect ratio, with the outline coming
> from the city's growth and its planning conditions, replaced it (`Imperium-Knowledge/09_地图生成与CBF技术.md` L735,
> L801; `Imperium-Knowledge/现行/城/罗马城-做法与顺序.md` L127).

> [!NOTE]
> **Deleted**: a hand-drawn plan fitted onto the terrain and turned by assembly to parallel the site's waterline
> or, without a waterline, to the longest straight edge of the buildable site
> (`Imperium-Knowledge/designs/ICF/聚落平面语法-v4.md` L32-40;
> `Imperium-Knowledge/designs/instructions/生成具象规格-现行版.md` L183-185; `Imperium-Knowledge/裁定归档/2026-11.md`
> L40-42); voided when the plan stopped being hand data
> fitted onto terrain, the city growing from its core instead (`Imperium-Knowledge/designs/ICF/聚落平面语法-v4.md` L6;
> `Imperium-Knowledge/现行/城/罗马城-做法与顺序.md` L84).

The historical cases the sources give for the shape of cities on flat ground are great cities such as Alexandria and
Antioch stretched along a coast or river with their grid parallel to the long side, and Nicaea measured as an irregular
pentagon of about 5 km rather than a near circle (`Imperium-Knowledge/14_来源同步与权威.md` L56). For now only plains
cities, a river through the city included, are handled; cities on rock or mountain-top sites and on wide river mouths
come later (`Imperium-Knowledge/现行/城/城建-生成流程.md` L46).

## Siting by climate, and learning from real sites

Roman siting prefers candidate sites with water, which gives the city its water gate, and pure flat ground without
water is the fallback (`Imperium-Knowledge/designs/instructions/生成第2轮重做-第一段批准与第二段补充.md` L657;
`Imperium-Knowledge/designs/instructions/生成具象规格-现行版.md` L90); the city is not sited for height, as said above
(`Imperium-Knowledge/现行/城/地形与选址.md` L115).

> [!NOTE]
> **Deleted**: Rome's siting idea of 10-28, preferring open flat ground, river plains and coastal flat ground
> (`Imperium-Knowledge/现行/城/地形与选址.md` L114; `Imperium-Knowledge/09_地图生成与CBF技术.md` L459); the later
> preference for sites with water, pure flat ground being the fallback, replaced it
> (`Imperium-Knowledge/designs/instructions/生成第2轮重做-第一段批准与第二段补充.md` L657;
> `Imperium-Knowledge/designs/instructions/生成具象规格-现行版.md` L90).

> [!NOTE]
> **Deleted**: the other reasons that preference gives, high ground for the landmark terrace and water tower and water
> for the water source, belonged to the hydraulics the maintainer deleted
> (`Imperium-Knowledge/designs/instructions/生成第2轮重做-第一段批准与第二段补充.md` L657).

Biomes that by nature lack rock and water, such as desert and ice sheet, are set apart
(`Imperium-Knowledge/现行/城/地形与选址.md` L107; `Imperium-Knowledge/09_地图生成与CBF技术.md` L825). A desert follows
the banding of Anno 117's Aegyptus (Dawn of the Delta): from the water outward come the river, the farmland belt, and
the city on dry ground, so the city does not hug the river bank, and trade roads give the wall nodes
(`Imperium-Knowledge/现行/城/地形与选址.md` L108; `Imperium-Knowledge/09_地图生成与CBF技术.md` L827). Only the banding is
borrowed, not the flooding, and the desert city reads as living by water
(`Imperium-Knowledge/09_地图生成与CBF技术.md` L827). An ice sheet produces only medium and small settlements
(`Imperium-Knowledge/现行/城/地形与选址.md` L108; `Imperium-Knowledge/09_地图生成与CBF技术.md` L826), and in extreme
cold (tundra, ice sheet, sea ice) no City is sited, though a castellum, fortlet or burgus may be
(`Imperium-Knowledge/designs/instructions/生成第2轮重做-第一段批准与第二段补充.md` L658).

> [!NOTE]
> **Deleted**: the desert's water line, brought in from the map edge or from deep wells where there is no river, with
> waterwheels, cisterns and canal heads on it as wall nodes and fields following the cisterns, and the earlier imperial
> water line of aqueducts and water tower that it replaced, belonged to the hydraulics the maintainer deleted
> (`Imperium-Knowledge/现行/城/地形与选址.md` L108; `Imperium-Knowledge/09_地图生成与CBF技术.md` L826-827).

> [!NOTE]
> **Base game**: the base game has no flooding, which is why the desert takes only Anno's banding, to be checked
> against `Data/` (`Imperium-Knowledge/09_地图生成与CBF技术.md` L827).

> [!NOTE]
> **Unverified**: which cold biomes the ice-sheet rule covers and which settlement tiers they match is open, tracked as
> live list #76 (`Imperium-Knowledge/现行/城/地形与选址.md` L108; `Imperium-Knowledge/09_地图生成与CBF技术.md` L827).

Real-site snapshots (真城址快照), made from public elevation data and open street-map water and paired across the two
eras where possible, let the design session trace historical walls, main streets, palaces and squares to learn how
terrain and walls relate, and the generator is run on the real sites to compare its walls with the historical ones;
ancient shorelines are edited by hand (`Imperium-Knowledge/09_地图生成与CBF技术.md` L677;
`Imperium-Knowledge/现行/城/地形与选址.md` L124). The first ruling named eight sites (Constantinople, Ephesus, Corinth,
Thessalonica, Nicaea, Antioch, Amorium, Pompeii), and Adrianople and Rome were added
(`Imperium-Knowledge/09_地图生成与CBF技术.md` L677, L680). What terrain decides, such as the land wall's share and the
core's distance from water and from the land wall, cannot be learned from a real city and serves only as reference;
only methods that do not change with terrain enter the rules (`Imperium-Knowledge/现行/城/罗马城-做法与顺序.md` L135;
`Imperium-Knowledge/09_地图生成与CBF技术.md` L729).

> [!NOTE]
> **Unverified**: the literature study listed what to check on the plans once the elevation snapshots return: whether
> Constantinople's land-wall corners sit on ridges and the Mese runs along one, how Antioch's wall meets its river,
> whether Ephesus's Curetes street is a valley line, how Adrianople's square city sits by its river bend, what terrain
> Nicaea's pentagon corners mark, whether Thessalonica's main street follows the contours, and whether Pompeii's
> distribution tower stands at the highest point (`Imperium-Knowledge/designs/city-plans/真城址研读-文献-2026-10-30.md`
> L125-133).

## Map size and fitting a city into it

A landform is first judged by its form for which tier of settlement it fits (City, medium, small), and an unfit tier is
not chosen (`Imperium-Knowledge/现行/城/地形与选址.md` L98). Map size is set by tier, one size per tier and not by the
player's world setting: large city (大城) 350×350, medium city (中城) 300×300, small city (小城) 250×250 and guard post
(哨所) 200×200, matching the base game's four sizes (`Imperium-Knowledge/现行/城/地形与选址.md` L98;
`Imperium-Knowledge/09_地图生成与CBF技术.md` L873; `Imperium-Knowledge/designs/tools/city/说明/template.md` L26;
`Imperium-Knowledge/designs/tools/city/说明/sample.md` L255). Cities are designed separately for large, medium and
small, and the test terrain of each tier takes that tier's map, the existing 325 snapshots serving until they are made
again (`Imperium-Knowledge/现行/城/罗马城-做法与顺序.md` L136; `Imperium-Knowledge/09_地图生成与CBF技术.md` L873). In a
large city's map the walled city fills half to two thirds of the map (`Imperium-Knowledge/现行/城/地形与选址.md` L82;
`Imperium-Knowledge/designs/tools/方向表.md` L25).

> [!NOTE]
> **Deleted**: the earlier map sizes: a large city defaulting to 325×325 with 325 as its test terrain, a fitting
> landform enlarging the map up to 325 for City and 275 for medium, the map following the player's world setting, and
> tiers of 325, 275 and 225 (`Imperium-Knowledge/09_地图生成与CBF技术.md` L670, L785, L871;
> `Imperium-Knowledge/designs/做法史/地形与选址.md` L15, L55, L83;
> `Imperium-Knowledge/designs/city-plans/kit/版型格式-方案.md` L58). One size per tier, 350, 300, 250 and 200, replaced
> them (`Imperium-Knowledge/09_地图生成与CBF技术.md` L873; `Imperium-Knowledge/现行/城/地形与选址.md` L98).

> [!NOTE]
> **Base game**: the base game's map sizes include 200, 250, 300 and 350 cells a side, to be checked against `Data/`
> (`Imperium-Knowledge/现行/城/地形与选址.md` L98; `Imperium-Knowledge/09_地图生成与CBF技术.md` L871, L873).

When a template is larger than the map it is scaled as a whole by one ratio, which is set only by one household of
about 15×15 cells; street widths shrink with it but not below lane 3, secondary street 5 and trunk 5, while gates,
towers and bridges keep their width (`Imperium-Knowledge/现行/城/地形与选址.md` L83;
`Imperium-Knowledge/09_地图生成与CBF技术.md` L963). Each household after scaling becomes a plot, later filled with the
mod's cards at their own size (`Imperium-Knowledge/现行/城/地形与选址.md` L84;
`Imperium-Knowledge/09_地图生成与CBF技术.md` L876). Houses are not shrunk: if the city does not fit, fewer patches are
placed (`Imperium-Knowledge/现行/城/地形与选址.md` L88; `Imperium-Knowledge/designs/tools/方向表.md` L25). Once the
whole city is placed in the 350 map, the wall's distance to the map edge is measured segment by segment, gate segments
and road-out segments keeping enough and river or terrain segments allowed to be short; where a segment falls short,
that wall segment is moved or one patch at the city edge is left out, without shrinking houses or roads
(`Imperium-Knowledge/现行/城/地形与选址.md` L87; `Imperium-Knowledge/09_地图生成与CBF技术.md` L963).

> [!NOTE]
> **Deleted**: the earlier ways of fitting a template: shrinking the frame and removing houses, or placing it unscaled
> and reducing the buildings, then a ratio set by the map edge and the wall keeping 10 cells from it, with 0.822 for
> template number 1 and a secondary-street floor of 4 (`Imperium-Knowledge/designs/做法史/地形与选址.md` L8, L13-14;
> `Imperium-Knowledge/09_地图生成与CBF技术.md` L876; `Imperium-Knowledge/designs/tools/city/说明/template.md` L103,
> L109). The ratio set only by one household, the floors of 3, 5 and 5, and measuring the wall to the map edge segment
> by segment replaced them (`Imperium-Knowledge/09_地图生成与CBF技术.md` L963; `Imperium-Knowledge/现行/城/地形与选址.md`
> L83, L87).

> [!NOTE]
> **Unverified**: the scale factor for placing template number 1 in the large city's 350 map is not settled: the
> current card leaves its final value to the user, and the direction table gives 0.81 provisionally, to be calibrated
> by screenshot once the east square is placed in the 350 map (`Imperium-Knowledge/现行/城/地形与选址.md` L86;
> `Imperium-Knowledge/designs/tools/方向表.md` L25).

> [!NOTE]
> **Unverified**: how many cells each wall segment keeps to the map edge after the city is fitted into 350 is not
> fixed; replicating the city comes first (`Imperium-Knowledge/现行/城/地形与选址.md` L87;
> `Imperium-Knowledge/09_地图生成与CBF技术.md` L971).

## Failure and retry

A city's size is computed per map from its site requirements and area, and the skeleton's indispensable pieces scale
with the district area between their limits; only when they do not fit at the lower limit is the city started again
(`Imperium-Knowledge/现行/城/地形与选址.md` L102). When part of a Roman city cannot be made, a combination piece that
does not fit is first tried at other candidate positions on the same terrain, blocks, colonnades, skeleton or wall that
cannot be made are first redone alone, and only when the local repair fails does generation go back to the terrain
(`Imperium-Knowledge/现行/城/地形与选址.md` L103). Retries are capped at three, and the fourth uses a conservative
terrain (保守地形) that keeps the tile's regularities, a gentle river and large rock away from the district, keeps
scattered rock and small puddles by biome as wall nodes, and always fits the skeleton
(`Imperium-Knowledge/现行/城/地形与选址.md` L106; `Imperium-Knowledge/09_地图生成与CBF技术.md` L825).

> [!NOTE]
> **Deleted**: the earlier fallbacks: changing to a candidate landform, then seeking a site on vanilla terrain, then
> using the current generation, and a conservative terrain that cleared scattered rock as well
> (`Imperium-Knowledge/designs/做法史/地形与选址.md` L53, L86; `Imperium-Knowledge/09_地图生成与CBF技术.md` L754).
> Retrying locally before going back to the terrain, and a conservative terrain that keeps scattered rock and puddles as
> nodes, replaced them (`Imperium-Knowledge/现行/城/地形与选址.md` L103, L106;
> `Imperium-Knowledge/09_地图生成与CBF技术.md` L825).

## Reports not ruled

> [!NOTE]
> **Unverified**: the community-terrain report, a reference report not ruled, was made on the direction to follow the
> community's idea of first making land suited to a city and then building on it
> (`Imperium-Knowledge/designs/研究/城/社区造地形-城址-2026-11-11.md` L2, L5). It finds four kinds of community terrain
> creation, landform by tile feature as in GL, player tweaks as in Map Designer, land reserved for buildings by clearing
> a rectangle as in RimCities and KCSG, and picking without making as with GL's nearby search and vanilla landmarks; it
> takes the first as the one wanted, in line with the site landform rule, reads the second as in line with re-laying
> within the tile's rules, and calls the third the look to avoid
> (`Imperium-Knowledge/designs/研究/城/社区造地形-城址-2026-11-11.md` L9, L23-30). It names landforms suited to city
> sites in a no-high-ground row (confluence, river split by an island, ordinary river, cove, coast corner, peninsula or
> land bridge, lake, and the three self-written plains) and in a high-ground row read as rock (cliff, cliff corner,
> cliff and coast, valley, lone mountain), and landforms unfit for a large city because they are enclosed or too narrow
> at the exit, have too little land, are cut up as a delta is, or are not load-bearing or too fragmentary
> (`Imperium-Knowledge/designs/研究/城/社区造地形-城址-2026-11-11.md` L36-61). It finds that a city-site landform can be
> added in GL's XML form, the landform picking the core by itself and handing it to the city through a named output,
> with the world-tile requirement nodes holding the line of not going beyond the tile
> (`Imperium-Knowledge/designs/研究/城/社区造地形-城址-2026-11-11.md` L65-67).

> [!NOTE]
> **Unverified**: the same report proposes three plains tiers with trial sizes not yet shown in an image: re-paving
> only (a world road bending once or twice to the first square, one forest-edge line, up to three stray rocks or small
> puddles), adding one borrowable piece on small-hill, swampy or pond tiles (a rock head of 300 to 1500 cells, a marsh
> of 300 to 800 cells or a pond of at least 300 cells, 20 to 50 cells beside the core), and a city-site skeleton for
> tiles with two roads (the two roads crossing at the first square and one oblique band of soft ground or gravel)
> (`Imperium-Knowledge/designs/研究/城/社区造地形-城址-2026-11-11.md` L93-105, L120), with how each tier shows from above
> (`Imperium-Knowledge/designs/研究/城/社区造地形-城址-2026-11-11.md` L107-115). It reads as deliberate objects strung
> along the circle's edge, set at city corners or at equal spacing, present only at the city edge and not outside, or in
> straight rows or symmetric about the centre, and as not deliberate objects grown from noise and threshold, density per
> tile over the whole map, and few objects each matching an item of the tile
> (`Imperium-Knowledge/designs/研究/城/社区造地形-城址-2026-11-11.md` L84-91). It reads the Roman city's shape from the
> two rows, the outline given by water and roads in the no-high-ground row and one side backed by rock in the
> high-ground row (`Imperium-Knowledge/designs/研究/城/社区造地形-城址-2026-11-11.md` L15). The Anno 117 report, also a
> reference report not ruled, reads the district's edge as something to read from terrain, river and approach roads,
> not from an invisible circle (`Imperium-Knowledge/designs/研究/城/纪元117-设计理念-地图与城建-2026-11-11.md` L2, L20).

> [!NOTE]
> **Unverified**: open in the community-terrain report: whether a city-site landform is mounted as a tile mutator and
> which name the player sees on the world map; whether a flat tile may carry one rock head of 300 cells; the full list
> of landmarks a flat vanilla tile can carry; the reading of hilliness as the vanilla enumeration 1 to 5 with 6 as GL's
> cave tier; and its reading of the vanilla tile text (biome, hilliness, world roads, swampiness, rainfall, rock type and
> landmarks such as pond and wetland) as all a plains city can draw on
> (`Imperium-Knowledge/designs/研究/城/社区造地形-城址-2026-11-11.md` L34, L68, L70-82, L119-123).
