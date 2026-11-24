# What Imperium is

This section covers Imperium as a whole: the kind of mod it is and its theme, the principles its content is measured by,
its parts, the colony's choice and the end of the game, how the Empire comes into play over time, its playstyles and
settings, the expansions it requires and works with, and the order of work toward its releases. Where a newer setting
replaced an older line, or the maintainer deleted it, as with the hydraulics, the older line is given once as a Deleted
note; where the root `docs/` files, the newest statements, cover a subject without restating an older passage, the
passage stands with an Unverified note. The setting it plays in is in [world.md](world.md). The Empire's institutions
and people are in [empire.md](empire.md), the colony's relations with the Empire in [relations.md](relations.md), orders
in [orders.md](orders.md), the ruins and techprints in [ruins-and-technology.md](ruins-and-technology.md), the Empire's
mechanoids in [mechanoids.md](mechanoids.md), the framework in [mantle.md](mantle.md), the starting ruins and the core in
[core.md](core.md), the administrative facilities in [administration.md](administration.md) and generated cities in
[cities.md](cities.md).

## A remake of Royalty

Imperium is a mod for RimWorld (`README.md` L3). It is a complete remake of Royalty (`docs/glossary.md` L35): the base
game's mix of science fiction with medieval nobles, thrones and psychic power becomes an empire in the full sense, with
a coherent Roman civilization identity, institutions that really run, and a colony that joins as a whole rather than
through a personal title (`Imperium-Knowledge/01_项目宪章与规范索引.md` L36-37). The Royalty titles of the player and of the
Empire are removed (`Imperium-Knowledge/01_项目宪章与规范索引.md` L41; `Imperium-Knowledge/designs/待用/建筑模板图册-2026-10-27.md`
L122). Imperium reorganizes Royalty's content through its own overrides as its approved design gives, does not restore
the replaced title mechanics for testing, and keeps the base game's interface and wording, with differences only in the
descriptions of its own content (`RimWorld-Imperium/CLAUDE.md` L133). Retired Royalty content is reused only where each
item is approved as an exception (`Imperium-Knowledge/05_Orders与任务规则.md` L108). Royalty's research projects that are not
in Imperium's plan are no longer opened early through their old research path: compatibility-controlled hiding and
lawful authorization are preferred as the replacement, and Defs that other things refer to are not deleted outright
(`Imperium-Knowledge/04_蓝图与科研授权.md` L114).

Imperium is a themed expansion in the manner of Royalty and Anomaly, and the Empire is its theme
(`Imperium-Knowledge/01_项目宪章与规范索引.md` L57, L191, R-1103-1145). The Empire itself is an administrative system plus
machines (机械), and the ruins are a second selling point (`Imperium-Knowledge/01_项目宪章与规范索引.md` L57, L191). Imperium also
carries framework-style content that widens play, such as the techprint layer, and none of its parts has to be made into
a stand-alone play unrelated to the Empire for that reason (`Imperium-Knowledge/01_项目宪章与规范索引.md` L191). Builders and
fighters are both looked after: builders have administration and city building, and fighters have orders, regional
activities, expeditions shown in play and machines (`Imperium-Knowledge/01_项目宪章与规范索引.md` L191;
`Imperium-Knowledge/designs/回报/调研-流程-游戏设计与制作.md` L177). Imperium is an expansion and not a one-to-one reproduction of
Rome: the Empire is the theme and Rome the main flavour, and a decision starts from a guess at what the base game's
makers would put into such an expansion (`Imperium-Knowledge/01_项目宪章与规范索引.md` L202, R-1104-2259;
`Imperium-Knowledge/现行/流程/设计会话工作规矩.md` L126; `Imperium-Knowledge/designs/回报/调研-流程-游戏设计与制作.md` L62).

Imperium is non-commercial: it is free to play and takes no sponsorship (`Imperium-Knowledge/01_项目宪章与规范索引.md` L196,
R-1029-1420; `Imperium-Knowledge/14_来源同步与权威.md` L191, R-1104-1913).

Its code has two layers: Mantle, the framework layer, and Imperium, the content layer that builds on Mantle (`README.md`
L30, L69; `docs/glossary.md` L221). Other mods may extend Imperium, and the framework's first layer (L1) is kept as a
public interface (`Imperium-Knowledge/designs/回报/调研-流程-模组工程.md` L139); the passage calls the framework ICF, the old
name of Mantle (`.github/deprecated-terms.json` L395-408).

Among the directions kept but not built automatically is a stand-alone mod, made after Imperium, that reinforces the base
game's mechanoid system and aims at the appeal of a popular mod (`Imperium-Knowledge/01_项目宪章与规范索引.md` L158, L164,
R-1103-1402). It is not a sub-mod of Imperium: each of the two works alone and they do not clash when used together,
Imperium does not depend on it, and Imperium's machines are always balanced against the pure base game, so that the
other mod neither outdoes them nor makes them too strong (`Imperium-Knowledge/01_项目宪章与规范索引.md` L164). Imperium
itself rolls back some of the base game's later weakening of its mechanoids, which counts as a rollback and not as a
change to the base game (`Imperium-Knowledge/现行/机械体/通则-基线.md` L51; `Imperium-Knowledge/08_机械体设计.md` L443,
R-1110-0207a; replaces the second point of `Imperium-Knowledge/01_项目宪章与规范索引.md` L164). The overhaul mod is meant to
stay in every save that is not locked to the medieval era, and Imperium in every player's game, players of medieval
overhauls included, because its framework generates their medieval settlements; for players who do not use its imperial
content, the framework is Imperium's main selling point (`Imperium-Knowledge/01_项目宪章与规范索引.md` L164). Research into
popular mechanoid mods, and into what players complain of in the base game's mechanoids, comes before any work on it
(`Imperium-Knowledge/01_项目宪章与规范索引.md` L164).

> [!NOTE]
> **Deleted**: the hydraulics line. It was the waterworks (水利), renamed the imperial aqueducts (帝国水道): first an axis
> playable without the Empire, then the core of the Empire in the place that psychic power holds in Royalty, unlocked
> by joining and reached outside the Empire only from ruins and quests; a player-side themed play in three layers of
> network, benefit and wonder; grafted onto the power grid as framework-style content; frozen and then unfrozen as the
> third milestone of the route; with its own event multiplier in the mod settings, the merging of fire fighting into one
> building and of fountains into baths, a place among the builders' content, and a judgment that only it could be on the
> player's map every day (`Imperium-Knowledge/01_项目宪章与规范索引.md` L55, L57, L61, L67-69, L174, L189, L191-192;
> `Imperium-Knowledge/11_开发进度与未决事项.md` L14, L47, L62; `RimWorld-Imperium/docs/code-status.md` L86-88;
> `Imperium-Knowledge/裁定归档/2026-10.md` L122, L125;
> `Imperium-Knowledge/designs/研究/主轴对比-工质与自动机传统-2026-11-03.md` L13, L59). The maintainer deleted it (the
> maintainer's direction of 2026-11-24).

> [!NOTE]
> **Unverified**: the root document on Imperium as a whole says what it covers: its design intent, its parts, how the
> Empire shows itself in play and the expansions (`docs/imperium.md` L3-4); only the glossary gives Imperium as a remake
> of Royalty (`docs/glossary.md` L35). The rest of this positioning, the stand-alone mechanoid mod and the openness to
> other mods come from Imperium-Knowledge and are not restated there; nothing marks them dropped.

## The theme

The Empire's theme is a huge machine that keeps going without any one of them: colonists do not differ by identity,
title or attributes, since titles are deleted and the colony joins as a whole, but by their smallness within the machine
and by being able, through effort, to push it a little in the direction they want
(`Imperium-Knowledge/01_项目宪章与规范索引.md` L41). What the Empire is as a machine is in [world.md](world.md).

Four principles of pushing a little (推动一点) bind imperial interaction and the design of campaigns
(`Imperium-Knowledge/01_项目宪章与规范索引.md` L43):

1. Not concrete: there is no one-to-one cause and effect and no lever of the kind "hand in N grain, garrison +M"
   (`Imperium-Knowledge/01_项目宪章与规范索引.md` L44).
2. Not attributable: the machine changes from many inputs, of which the player is one, and nothing gives a number or a
   hint of how much the player contributed (`Imperium-Knowledge/01_项目宪章与规范索引.md` L45;
   `Imperium-Knowledge/designs/回报/调研-流程-游戏设计与制作.md` L129).
3. Delayed: nothing pays back within the same season (`Imperium-Knowledge/01_项目宪章与规范索引.md` L46).
4. Diffuse: results show in places not directly tied to the player's act, such as a road paved, a governor changed or an
   expedition route moved a little, and they are not announced (`Imperium-Knowledge/01_项目宪章与规范索引.md` L47).

Campaigns follow the same principles: a won battle does not make the Empire give a city, and the next expedition's route
only drifts a little (`Imperium-Knowledge/01_项目宪章与规范索引.md` L49).

The player joins, for the sake of their own colony, the political circle of an empire that is strong in military,
industry and administration but conservative from historical trauma, institutional inertia and divided interests
(`Imperium-Knowledge/01_项目宪章与规范索引.md` L53). The colony gains resources through real service and widens its rights
through formal status; its actions may change how resources and interests are shared, and the player does not have to
manage or understand the Empire's internal politics (`Imperium-Knowledge/01_项目宪章与规范索引.md` L53;
`docs/imperium.md` L59-60). A player who ignores the background politics can still understand contracts, production,
trade, exploration and combat, since the political narrative is an optional layer of explanation and not a threshold of
knowledge for normal play (`Imperium-Knowledge/01_项目宪章与规范索引.md` L83). The cognitive load at any one moment is held
down without cutting effective content, lengthening idle waits or forcing grinding
(`Imperium-Knowledge/01_项目宪章与规范索引.md` L83). Political participation, single items and normal research are not merged
into one main-line entrance, while lawful formal permissions, scarce authorizations and prerequisites in real resources
stay (`Imperium-Knowledge/01_项目宪章与规范索引.md` L85). Holding a physical item is not holding the authorization to make
it, and holding the authorization is not having finished the research or the making
(`Imperium-Knowledge/01_项目宪章与规范索引.md` L85).

> [!NOTE]
> **Unverified**: the root document gives the Empire as acting on its own schedule, answering the colony later, showing
> itself without a number for the colony's standing and never asking the player to manage its inner politics
> (`docs/imperium.md` L27-42, L57-71, L97-104). It does not restate the theme, the four principles or the rest of this
> section, and nothing marks them dropped.

## Principles of design

Player enjoyment comes before matching the base game: Imperium is of expansion standard and so brings new mechanics,
reusing the base game's mechanics serves those new mechanics, and the base game is a reference only for the scale and
quality of content, so that "the base game did it" is no reason by itself to adopt something
(`Imperium-Knowledge/01_项目宪章与规范索引.md` L175; `Imperium-Knowledge/designs/回报/调研-流程-游戏设计与制作.md` L133). When
something goes wrong, it is fixed in the architecture (`Imperium-Knowledge/designs/回报/调研-流程-游戏设计与制作.md` L133,
R-1029-1316, R-1104-0958c). Reaching a goal with the base game's mechanics wherever possible is the essence of the
project: it is measured against the official expansions and extends mechanics only where necessary
(`Imperium-Knowledge/01_项目宪章与规范索引.md` L168; `Imperium-Knowledge/designs/回报/调研-流程-游戏设计与制作.md` L123). Its
framework is complex underneath and simple outside: the number of items and pawns is cut rather than piled up as in a
large mod, and each thing serves either flavour or a new way of playing (`Imperium-Knowledge/01_项目宪章与规范索引.md` L169;
`Imperium-Knowledge/designs/回报/调研-流程-游戏设计与制作.md` L71).

Before any new object is added, three questions are asked (新物件三问): whether the player can use it or it brings a new
decision, whether it is used in more than one place, and whether a base-game object with other materials or paint really
cannot do the job; only an object that passes all three is added (`Imperium-Knowledge/01_项目宪章与规范索引.md` L188,
R-1030-0025b; `Imperium-Knowledge/designs/回报/调研-流程-游戏设计与制作.md` L68). New content offers an independent use, a
real choice or an observable result, and no building, machine or techprint is made to fill a count
(`Imperium-Knowledge/01_项目宪章与规范索引.md` L79). Manufacturing flows and political authorization may be Imperium's own,
but what they produce reuses, as far as possible, the base game's control, bandwidth, charging, repair, logistics,
quests and saves, and no isolated, complete framework for mechanitors or political management is built
(`Imperium-Knowledge/01_项目宪章与规范索引.md` L79). Imperium reuses the base game's quests, traders, mechanoids, transport
and components as far as possible and puts its differences in the rules layer it owns, without hiding the base game's
buttons, swallowing errors or turning off unrelated events to pass a test (`Imperium-Knowledge/02_开发验收与证据规则.md`
L26). Compatibility with third-party mods goes only as far as it is really verified
(`Imperium-Knowledge/01_项目宪章与规范索引.md` L79).

What the player is meant to read, such as what a unit is doing or how it differs from another, shows through the unit
itself: its shape, projectiles, motion and the effects the base game already has; hints, markers, icons or text that the
base game does not have are not added where the unit already reaches the intent
(`Imperium-Knowledge/01_项目宪章与规范索引.md` L199, R-1104-2104). The Empire's advantage comes from standardization,
specialist division of labour, scale of production and real cooperation, not from every unit being generally stronger
than the base game's or from hidden formation auras; its advantage and its cost come from the same mechanism: real
materials, time, fragility, limits of specialty and conditions of use (`Imperium-Knowledge/01_项目宪章与规范索引.md` L77).

## The measure of content

Content tied to techprints is not counted in the quantity of content; other base content, buildings and items, is capped
at the largest count of that kind in any one official expansion; machines have no hard cap
(`Imperium-Knowledge/01_项目宪章与规范索引.md` L172). For machines the test is that every one has its own appeal, not their
number; the base machines of ranks IV and V still follow the one-to-one rule (一对一规则), which the passage notes as
running well (`Imperium-Knowledge/01_项目宪章与规范索引.md` L170). The Empire is a state of people, and its people fill all
of its roles (`docs/setting.md` L96, L101).

> [!NOTE]
> **Deleted**: the line in which the Empire sends no population, so that its machines hold the roles that human pawns
> would hold and it has more machines than an expansion would (`Imperium-Knowledge/01_项目宪章与规范索引.md` L170). The
> root document replaced it: the Empire is a state of people who fill all of its roles (`docs/setting.md` L96, L101).

> [!NOTE]
> **Unverified**: the charter gave the deleted no-population line as the reason why machines have no hard cap
> (`Imperium-Knowledge/01_项目宪章与规范索引.md` L170); the cap rule is restated without that reason in the baseline of
> content (`Imperium-Knowledge/01_项目宪章与规范索引.md` L172), and no passage says whether it outlived the reason.

Core technology is rare and may be made strong: a leaning of at least 45% only lets core technologies into the techprint
pool, where they still have to be drawn by chance, so that they may clearly exceed base content, and a guarantee exists
(`Imperium-Knowledge/01_项目宪章与规范索引.md` L173). The variety of content is measured by how fresh a second and a third game
feel to the player, not by how many years a game can last: variants are made until the second and third game are still
fresh, and then stopped (`Imperium-Knowledge/01_项目宪章与规范索引.md` L197, R-1029-1400). For cities the passage takes a
skeleton plus a reusable library of neighbourhoods (街坊库) as variety enough (`Imperium-Knowledge/01_项目宪章与规范索引.md` L197),
a library the Roman city has since stopped using; its ordinary residences are now placed plot by plot along the street
with spec cards (`Imperium-Knowledge/09_地图生成与CBF技术.md` L714, R-1030-1930; `docs/glossary.md` L167).

A cut of content removed the technology chip and leftover cores without a use, removed the Empire faction's armed human
characters, whose military characters are to be designed separately later, stopped using the garrison characters of the
CBF templates for the Empire, merged the manufacturing bays (制造仓) into two kinds, and merged the trade visits into the
imperial goods visit (帝国商货到访) (`Imperium-Knowledge/11_开发进度与未决事项.md` L47, 2026-10-26;
`Imperium-Knowledge/01_项目宪章与规范索引.md` L171; `RimWorld-Imperium/docs/code-status.md` L71-74). The imperial codicil is
one item for each rank (`Imperium-Knowledge/03_Rank与政治权限.md` L170, R-1103-1759; replaces
`Imperium-Knowledge/11_开发进度与未决事项.md` L47, which merged the codicils into one kind).

## The parts of Imperium

Every part of Imperium plays out through the colony's relation to the Empire, and the colony's choice to join or stay
outside starts it (`docs/imperium.md` L14-15). The Empire content falls into three parts along the Empire's time, the
past, the present and the future; new Empire content belongs to one of the three, and content that fits none is not
added (`docs/imperium.md` L75-76). The past is the ruins (旧日遗迹), which the colony enters to excavate technology lost
since the silence (`docs/imperium.md` L77-78; `docs/glossary.md` L154). The present is the Empire of today and its effect
on the colony: a colony that joins serves it and receives its commendations, and a colony that stays outside bears its
ill will and pressure (`docs/imperium.md` L79-82). The future is the end of the game, which decides the fate of the Empire
on this planet (`docs/imperium.md` L83). The parts are not lines of play: a colony in the Empire and a colony outside it
both go through every part (`docs/imperium.md` L88-89). Mantle generates the world the parts take place in, and it runs
whether Empire content is on or off (`docs/imperium.md` L91-92).

Techprints are a layer of technology across the past and the present, and both the Empire and the ruins yield them
(`docs/imperium.md` L95; `docs/ruins-and-technology.md` L63, L94-95). The techprint layer gives technology, buildings,
equipment and machines their real use (`Imperium-Knowledge/01_项目宪章与规范索引.md` L71).

> [!NOTE]
> **Deleted**: the charter's division of the content into axes (主轴): an Empire axis holding orders, requests, visits,
> claims, rank, leaning and influence, into which the ruins, first an axis of their own, were moved as an activity line;
> the waterworks axis; a third axis left open for factions, with diplomacy and dynamic factions as a conditional
> candidate whose timing waited on the next official expansion and was named a project risk; expeditions as an
> appendage of the Empire axis (远征归帝国); and new mechanisms growing only from the axes and the techprint layer
> (`Imperium-Knowledge/01_项目宪章与规范索引.md` L55, L59-62, L64-69, L73, L189, R-1029-2104;
> `Imperium-Knowledge/现行/索引.md` L1350; `Imperium-Knowledge/designs/回报/调研-流程-游戏设计与制作.md` L75). The three parts of the root document replaced it
> (`docs/imperium.md` L73-95; `docs/glossary.md` L154).

> [!NOTE]
> **Unverified**: the names of the three parts are open (`docs/imperium.md` L90, issue #166). The root documents also
> leave parts of the design to pull requests whose text is not in them: the section Ranks of #124, the section Mantle of
> #132, the sections The Empire's mechanoids, Weapons and Appearance of #63, and the section The honor guard of #133
> (`docs/imperium.md` L81-82, L91-92, L111; `docs/setting.md` L69-70, L75-78, L88-89, L102-103).

### Facilities and city building

City building (城建) is a reward the player gives themselves and not a requirement: the player builds because it feels
good, and building is not what makes it good (`Imperium-Knowledge/01_项目宪章与规范索引.md` L64). Other buildings unlock through
the base or through techprints, and the player is not made to build anything (`Imperium-Knowledge/01_项目宪章与规范索引.md` L64).
The Empire's core facilities include the imperial insignia (帝国徽记), the mark of a settlement cooperating with the Empire
and the symbol of its rank, and several landing pads (停泊点), the windows of the Empire's dealings with the colony
(`Imperium-Knowledge/01_项目宪章与规范索引.md` L64).

> [!NOTE]
> **Deleted**: the archive office (档案署), shown in the game as the Tabularium, as the Empire's administrative centre and
> one of its core facilities, with minimal panel interaction, the narrative interface and basic imperial infrastructure
> (`Imperium-Knowledge/01_项目宪章与规范索引.md` L64; `Imperium-Knowledge/designs/研究/帝国/帝国是什么.md` L75;
> `RimWorld-Imperium/docs/code-status.md` L27). It is removed, and its functions are now in the interface that the button
> at the bottom of the screen opens (`.github/deprecated-terms.json` L322-381, L977-988); see
> [administration.md](administration.md).

## The colony's choice and the end

After the colony takes the core from the starting ruins, the Empire's envoy comes, and the player decides whether the
colony joins the Empire or stays outside it, and how far it takes part (`docs/imperium.md` L10-12, L22-23). Joining the
Empire has a cost (`Imperium-Knowledge/11_开发进度与未决事项.md` L43). A colony that stays outside can still play to an end
of the game: after refusing, it can excavate the old empire's ruins and reach an end (`docs/imperium.md` L11-12, L24-25,
L93-94). How a colony joins, leaves and is answered by the Empire is in [relations.md](relations.md), and the starting
ruins and the core are in [core.md](core.md).

The end of the game decides whether the Empire keeps or loses this planet, not the fate of the Empire as a whole: the
colony is one of many places the Empire governs, its end stays that size, and neither end describes anything beyond this
planet (`docs/imperium.md` L46-55). The end is one of two: the Empire, helped by the colony, takes the planet back and
the colony rises to a high standing with it; or the colony ends the Empire's rule here, after which no one takes its
place and the planet sinks deeper into disorder (`docs/imperium.md` L84-86). The time target is that a player who
actively takes orders enters the endgame in the fourth to fifth year, between day 240 and day 300, with the days and
thresholds of each rank set by measurement (`Imperium-Knowledge/03_Rank与政治权限.md` L80).

> [!NOTE]
> **Unverified**: how the game reaches either end is open (`docs/imperium.md` L87, issue #164). The later content, the
> rank IV campaign and a rank V to be redesigned, is to be decided later (`Imperium-Knowledge/01_项目宪章与规范索引.md` L36,
> L160). The trigger and play of the triumph, where the capital is, and the content of rank V and of the endgame are to be
> set later; rank V is the endgame, marked by power outside war, and the earlier "rebuild the administrative network" is
> to be reviewed (`Imperium-Knowledge/03_Rank与政治权限.md` L60, L65). The research note on what the Empire is leaves two
> directions for the endgame: that intermediaries are necessary but dangerous, as the logic of the old guard suppressing
> the player at rank V, and rank V's power outside war as the machine's regional functions passing through the player's
> settlement (`Imperium-Knowledge/designs/研究/帝国/帝国是什么.md` L77-80).

## The Empire in play

The Empire's people and business come to the colony whether or not the colony is ready, and the Empire answers what the
colony has done to it later, sometimes long after, so that the player meets an empire far older and stronger than the
colony, one that does not wait on it (`docs/imperium.md` L29-33, L99-100). Imperial visits keep coming even when the
colony asks the Empire for nothing, and an attack on an imperial caravan is answered later (`docs/imperium.md` L35-36,
L40-42). How the Empire shows itself through its people, events and notices, with no number for the colony's standing, is
in [empire.md](empire.md).

State institutions have their own activity and do not start to run only because of the player
(`Imperium-Knowledge/01_项目宪章与规范索引.md` L87). Background patrols and administrative transits may carry no reward or
notice, and they do not obstruct normal colony life (`Imperium-Knowledge/01_项目宪章与规范索引.md` L87). There is no
compulsory tax, no extra bar of faction relations and no hidden score of administrative compliance
(`Imperium-Knowledge/01_项目宪章与规范索引.md` L87). Imperial population is scarce, and gifts, rations and the like do not give
the player new settlement population (`Imperium-Knowledge/01_项目宪章与规范索引.md` L87).

After joining, play opens in steps: first orders and regular visits, then requests once the imperial insignia and a
landing pad are built (`Imperium-Knowledge/06_行政设施与地区活动.md` L14-15). Purely background visits, such as patrols and
transits, send no letter; only those that need the player's response do (`Imperium-Knowledge/06_行政设施与地区活动.md` L17).
Orders are quoted one every three to five days, one at a time, and the orders themselves set the pace
(`Imperium-Knowledge/03_Rank与政治权限.md` L167, R-1029-2131; `Imperium-Knowledge/05_Orders与任务规则.md` L114, R-1103-2244).

### The rhythm prototype

A minimal prototype of the imperial rhythm (帝国节律原型), approved as a draft, rests on the theme, the four principles of
pushing a little and the lineage test (`Imperium-Knowledge/designs/帝国节律原型.md` L4, L6). Its city runs on the imperial
calendar by itself, whether or not the player is there, not waiting for the player and giving no notice; only when an
event happens does something move on the world map (`Imperium-Knowledge/designs/帝国节律原型.md` L10). The calendar has six
events, each naming its ancestor in the Roman line (`Imperium-Knowledge/designs/帝国节律原型.md` L6, L12-17):

1. A garrison rotation each spring and autumn: one troop leaves the city gate for the border fort and another returns,
   visible on the world map, and the garrison in the city changes with it (`Imperium-Knowledge/designs/帝国节律原型.md` L12).
2. A supply convoy after the autumn harvest, from the city along the official road toward the capital
   (`Imperium-Knowledge/designs/帝国节律原型.md` L13).
3. A tax collector once a year, with two guards, walking the official road settlement by settlement, entering the
   colony if it is a client (客属) and otherwise passing its door (`Imperium-Knowledge/designs/帝国节律原型.md` L14).
4. An inspector every two years, an official with a retinue touring the province and staying several days in the city,
   which is busy meanwhile (`Imperium-Knowledge/designs/帝国节律原型.md` L15).
5. A festival on two fixed days a year, with flags at the gate, people in the plaza and no trade caravan that day
   (`Imperium-Knowledge/designs/帝国节律原型.md` L16).
6. A patrol once a season, a small team going round the official road and passing near the player's colony
   (`Imperium-Knowledge/designs/帝国节律原型.md` L17).

One hidden variable, provincial attention (行省注意度), has no name and is not shown: it drifts at random each season,
standing for the inputs of many others, the player's acts add or take away a little (handing in grain and beating off its
enemies add, dealing with the enemy and sheltering deserters take away), and it affects the outputs only a year later
(`Imperium-Knowledge/designs/帝国节律原型.md` L21). It has two outputs. Roads: supply convoys and patrols choose their routes
weighted by attention, so that with high attention they pass the player's door more often and about three years later
the imperial work team paves that stretch of official road with stone slabs, without notice, while with low attention
the road goes around and the door slowly empties (`Imperium-Knowledge/designs/帝国节律原型.md` L22). Visitors: the tax
collector comes alone or with documents, or the inspector stops by, and the tone of letters runs from official to
greeting, the cause never told (`Imperium-Knowledge/designs/帝国节律原型.md` L23). Neither output can be traced back, since a
change may come from the player, from a border war or from a new governor, which meets the four principles
(`Imperium-Knowledge/designs/帝国节律原型.md` L24). The prototype's scope is one city, six calendar events, one hidden
variable and two outputs (`Imperium-Knowledge/designs/帝国节律原型.md` L38).

> [!NOTE]
> **Unverified**: the root document's account of the Empire in play does not restate the rules of this section after its
> first paragraph or the rhythm prototype, and nothing marks them dropped (`docs/imperium.md` L97-104). The player's
> path through imperial cities and imperial interaction is to be re-analysed by psychology once rank is done, starting
> from the living-city survey's sequence of curiosity, understanding, gain, intervention and return; the skeleton that
> keeps an imperial city alive is set after that and not before (`Imperium-Knowledge/01_项目宪章与规范索引.md` L51;
> `Imperium-Knowledge/11_开发进度与未决事项.md` L13). The survey weighs three candidate skeletons, A, B and C, and the base game
> has no precedent for any of them, so each would be built anew: A meets understanding, gain and intervention but lacks
> the return visit, since what is lost on leaving may not be there next time unless saved apart; B meets curiosity and
> part of understanding but lacks gain and intervention, no praise for pure rhythm was found, smooth background
> behaviour tends to go unnoticed, and its technical cost is the lowest; C meets the return visit and gain on the world
> layer but lacks understanding inside the city and intervention with immediate feedback
> (`Imperium-Knowledge/designs/研究/帝国/活城调研.md` L14, L52, L66-68). The rhythm prototype's implementation is still to be
> scheduled (`Imperium-Knowledge/designs/帝国节律原型.md` L4; `Imperium-Knowledge/designs/整理/整理方案-2026-11-02.md` L83), and its
> playtest judgment, that a playtester says unprompted "it seems to be because of me", is not used as acceptance
> (`Imperium-Knowledge/designs/帝国节律原型.md` L28; `Imperium-Knowledge/01_项目宪章与规范索引.md` L195). The research report
> recommends four aesthetics, fantasy, discovery, challenge and expression, and not fellowship because the game is
> single-player; how progress is made visible to the player under the principle of not attributable is left to the
> re-analysis of rank, and the report notes a tension between progress systems such as promotion and excavation and that
> principle (`Imperium-Knowledge/designs/回报/调研-流程-游戏设计与制作.md` L129, L344).

> [!NOTE]
> **Base game**: a faction base allows only trade on the world map, gifts and attack; peaceful entry into a friendly
> settlement is not possible; the only thing that changes over time is the trade stock, every 30 days; nothing that runs
> inside a settlement was found; and a base destroyed and left disappears, so that none of the three skeletons has a
> precedent to borrow, to be checked against `Data/` (`Imperium-Knowledge/designs/研究/帝国/活城调研.md` L8-11, L14, L56).

## Playstyles and settings

Imperium has playstyles for its Empire content, modeled on Anomaly's (`docs/playstyles.md` L51). In the standard
playstyle the game has the starting ruins, so the Empire content is there from the start, and the quest to the starting
ruins appears (`docs/playstyles.md` L9-13, L17, L55). In distant empire the starting ruins do not appear and Empire
content comes less often, as Anomaly's threats do in ambient horror (`docs/playstyles.md` L21-26, L30-33, L59-60). In
custom difficulty the player sets the share of Empire content and Empire content follows that share, as Anomaly's threat
sliders do for its threats (`docs/playstyles.md` L36-47, L64-65).

> [!NOTE]
> **Base game**: Anomaly has playstyles of its own, among them ambient horror, in which its threats are rare, and custom
> difficulty has an Anomaly threats setting for the share of major threats that come from Anomaly, to be checked against
> `Data/` (`docs/playstyles.md` L23, L51, L60, L64-65; `docs/glossary.md` L11, L13).

The mod settings offer one multiplier each for imperial visits, requests and the threat of the ruins, with the designed
value as the default (`Imperium-Knowledge/01_项目宪章与规范索引.md` L174; `Imperium-Knowledge/11_开发进度与未决事项.md` L43).

> [!NOTE]
> **Unverified**: the root playstyles document, the newest statement on how players set the amount of Empire content,
> does not mention these multipliers, and nothing marks them dropped (`docs/playstyles.md` L49-65).

> [!NOTE]
> **Base game**: the multipliers rest on Anomaly's first events having come too densely and an intensity setting having
> been added later, to be checked against `Data/` (`Imperium-Knowledge/01_项目宪章与规范索引.md` L174).

## Requirements and expansions

Imperium requires Royalty and no other expansion, and with Royalty alone Imperium, Mantle included, is complete
(`docs/imperium.md` L108-109; `docs/glossary.md` L35). In the game's mod list, Harmony, Royalty and Imperium are
activated, which Imperium requires, and Biotech and Odyssey are optional (`README.md` L45-46). Harmony is the only
third-party prerequisite; no other third-party dependency is added, frameworks such as VEF included, and third-party
code serves at most as a reference for mechanisms, implemented independently (`Imperium-Knowledge/01_项目宪章与规范索引.md` L81).
Imperium and Dubs Bad Hygiene do not interfere with each other and are not bridged (`Imperium-Knowledge/01_项目宪章与规范索引.md`
L81).

> [!NOTE]
> **Deleted**: the line in which the official expansions required were Royalty, Biotech and Odyssey, always on in the
> compatibility matrix, because Imperium is a remake of Royalty and Biotech and Odyssey are the pair the store recommends
> with high ownership, with Biotech carrying the imperial mechanoid line and Odyssey the generation of ancient buildings
> for claims and the wasp drones (`Imperium-Knowledge/01_项目宪章与规范索引.md` L81, L186;
> `Imperium-Knowledge/14_来源同步与权威.md` L118). The root document replaced it: Royalty is the only expansion required, and
> each other active expansion adds content (`docs/imperium.md` L108-112; `docs/glossary.md` L14, L28, L35).

Each other expansion that is active adds Empire content that deepens that expansion's own play (`docs/imperium.md` L110).
Biotech, when it is active, lets the colony make and control imperial mechanoids and adds the Empire's mechanoids whose
counterparts come with it; the root document places the rest of what it adds in the section The Empire's mechanoids of
pull request #63 (`docs/glossary.md` L14; `docs/imperium.md` L111). Odyssey, when it is active, adds ruins of the old
empire that stay where they are on the world map and yield techprints that come only with it (`docs/glossary.md` L28;
`docs/imperium.md` L112). Ideology and Anomaly are optional, each with limited compatibility: extra content when loaded,
no dependence when absent (`Imperium-Knowledge/01_项目宪章与规范索引.md` L186; `Imperium-Knowledge/14_来源同步与权威.md` L118,
R-1029-2026; `Imperium-Knowledge/designs/回报/调研-流程-游戏设计与制作.md` L72). The Vanilla Expanded mods and other
third-party mods get no compatibility at present, and this is to be decided later
(`Imperium-Knowledge/01_项目宪章与规范索引.md` L186; `Imperium-Knowledge/14_来源同步与权威.md` L118). Imperial facilities cannot
be built on a gravship (`Imperium-Knowledge/11_开发进度与未决事项.md` L43).

> [!NOTE]
> **Base game**: gravships come with Odyssey, to be checked against `Data/`
> (`Imperium-Knowledge/11_开发进度与未决事项.md` L43; `docs/glossary.md` L28).

> [!NOTE]
> **Unverified**: the root document on expansions does not restate the third-party policy, the limited compatibility of
> Ideology and Anomaly beyond its rule for every other active expansion, or the rule on gravships, and nothing marks them
> dropped (`docs/imperium.md` L106-112).

A Roman city has one cathedral and no district churches or chapels, and without Ideology the cathedral is still
generated, only altars and other furnishings that only Ideology has being replaced with ordinary ones
(`Imperium-Knowledge/09_地图生成与CBF技术.md` L764, R-1103-0718; `Imperium-Knowledge/09_地图生成与CBF技术.md` L884, R-1111-2221;
`Imperium-Knowledge/09_地图生成与CBF技术.md` L887, R-1111-2232).

> [!NOTE]
> **Deleted**: the line in which religious buildings were generated only when Ideology is loaded, with a substitute
> layout without it, the Roman spec cards marked † were generated only with Ideology, and a district chapel in the block
> library was swapped for a district bath or a yard without Ideology (`Imperium-Knowledge/09_地图生成与CBF技术.md` L168,
> L653; `Imperium-Knowledge/designs/roman-cards/罗马规格卡总表.md` L8, L12, L14-16, L19). The later rulings on the
> cathedral replaced it (`Imperium-Knowledge/09_地图生成与CBF技术.md` L764, L884, L887).

## Order of work and releases

The order of work is the route's milestones (`Imperium-Knowledge/11_开发进度与未决事项.md` L8-10, R-1030-0008b;
`Imperium-Knowledge/designs/整理/整理方案-2026-11-02.md` L62, L275):

- Milestone 1: the Roman city goes into the game, Rome only: three offline cases in round 3, their approval, then
  building in the game (`Imperium-Knowledge/11_开发进度与未决事项.md` L12).
- Milestone 2: rank is finished: the imperial system of rank, orders, requests and leaning stands on its own, not
  grafted onto generated cities, and an imperial city being alive is an output that follows
  (`Imperium-Knowledge/11_开发进度与未决事项.md` L13).
- Milestone 4: the ruins and claims, redesigned: claims merge into orders as a site survey (遗址勘探) template, after the
  whole flow of rank II (`Imperium-Knowledge/11_开发进度与未决事项.md` L15).
- Milestone 5: the second stage of the migration of the framework onward, which the passage calls ICF, now Mantle; the
  first stage, the move, is brought forward to after round 3 and before round 4 (`Imperium-Knowledge/11_开发进度与未决事项.md`
  L16; `.github/deprecated-terms.json` L395-408).

The third milestone belonged to the hydraulics; see the Deleted note under [A remake of Royalty](#a-remake-of-royalty).

As a list of content, the older table of phases names: settlement generation brought to completion and a formal
deployment; rank II, with seven machines and their facilities, the full promotion from I to II and one rewrite of the
game's text; the imperial faces, officials, commanders and civilians in place of Royalty's characters, with raids,
escorts and garrisons turned into mechanoids led by commanders; the framework built in; orders and the promotion from II
to III; the Empire's own components; rank III; the ruins; ranks IV and V and the end; and work on terrain templates and
settlements between these (`Imperium-Knowledge/裁定归档/2026-10.md` L110-121, L123;
`Imperium-Knowledge/11_开发进度与未决事项.md` L10).

> [!NOTE]
> **Deleted**: the order of the older table of phases and the rulings on it, which put generation first, then rank II,
> the imperial faces, rank III, the ruins and ranks IV and V, with art in the order mechanoids, clothing, building
> components (`Imperium-Knowledge/裁定归档/2026-10.md` L106-127). The milestones replaced that order, and the table stays
> only as a list of content (`Imperium-Knowledge/11_开发进度与未决事项.md` L8-10).

Within the milestones, settlement generation first reaches nine tenths of its design target, rounds 8, the performance
batch and round 9 follow, and the first implementation batch is the machine content of rank II together with the
promotion from I to II (the record of contribution, pre-review, application, inspector, ceremony, imperial codicil and
the integrated research of rank II), so that normal play reaches rank II; the promotions from II to V follow in later
batches (`Imperium-Knowledge/11_开发进度与未决事项.md` L45). The machines of rank III wait: rank II is finished first, then
rank III is examined again against the Empire's foundation as it was set anew, and then built
(`Imperium-Knowledge/11_开发进度与未决事项.md` L64, R-1103-1455).

Art starts in earnest only once the design reaches at least about rank IV (`Imperium-Knowledge/14_来源同步与权威.md` L191,
R-1104-1913). Art comes first for the mechanoids and buildings, with clothing scheduled separately; until that art is
done, base-game art or borrowed community art stands in, and once it is done an alpha opens
(`Imperium-Knowledge/11_开发进度与未决事项.md` L66, R-1104-1919). The alpha is a small closed test among a few to a dozen or so
acquaintances, not on the Workshop, and its package may carry borrowed pieces (`Imperium-Knowledge/14_来源同步与权威.md` L193,
R-1104-1924). About three months later the mod goes onto the Workshop as a beta, with every borrowed piece replaced by
Imperium's own (`Imperium-Knowledge/11_开发进度与未决事项.md` L66; `Imperium-Knowledge/14_来源同步与权威.md` L193;
`Imperium-Knowledge/designs/回报/调研-流程-游戏设计与制作.md` L158, L321).

During development, ready-made Workshop assets may stand in as placeholders (`Imperium-Knowledge/现行/流程/借用与第三方.md`
L11). Only generic pieces of the kind an official expansion would add are borrowed: usable by every faction and map,
recoloured by material and few in number; pieces with a look that marks one mod, or that pull in a whole set, are not,
and base-game pieces with paint are tried first (`Imperium-Knowledge/现行/流程/借用与第三方.md` L13-14, R-1029-2055). A
borrowed object becomes a Def in Imperium's namespace without a build category, so the generator can place it and
players cannot build it (`Imperium-Knowledge/现行/流程/借用与第三方.md` L18, R-1029-2053). Borrowed Defs may go into the
alpha package, and the beta package carries none (`Imperium-Knowledge/14_来源同步与权威.md` L193, R-1104-1924; replaces
`Imperium-Knowledge/现行/流程/借用与第三方.md` L19, which kept them out of every release package). ReBuild's components (the
ornamented door, ornamented wall, high-window wall, double door, fireplace, floor lamp, rough-stone wall and wall armour)
are to be made later as Imperium's own imperial base content, with its own Defs, code and art, and ReBuild is not a
prerequisite (`Imperium-Knowledge/现行/流程/借用与第三方.md` L50). The official release does not refer to ReBuild, and until
Imperium's own versions are done the switches that concern them are off in the release
(`Imperium-Knowledge/现行/流程/借用与第三方.md` L52).

> [!NOTE]
> **Unverified**: three milestones, M1 art start (美术开工), M2 alpha opening (开阿尔法) and M3 Workshop release (上工坊),
> and three lines, city building, machines and content, are named in a task brief marked as a draft, with no dates
> because none are set (`Imperium-Knowledge/designs/派活/任务书-入账-线与里程碑.md` L1, L7, L11, L26). The eighteen pending
> items of the rank I design check stay shelved (`Imperium-Knowledge/11_开发进度与未决事项.md` L59). The content of rank III
> waits for rank II and its re-examination (`Imperium-Knowledge/11_开发进度与未决事项.md` L64).
