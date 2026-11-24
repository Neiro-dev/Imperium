# Orders and quests

This section covers orders (委托), the expedition contracts the Empire entrusts to the colony: what an order is, how
its quotes are offered and accepted, the templates of each department and rank, challenge and rewards, travel and the
sites of orders, and claims, which merge into orders. Requests, the Empire's business on the colony's own map, are in
[administration.md](administration.md); the Empire's relations with the colony and how the colony joins are in
[relations.md](relations.md); what claims lead to is in
[ruins-and-technology.md](ruins-and-technology.md); the mechanoids and equipment named here are in
[mechanoids.md](mechanoids.md) and [military.md](military.md).

## What an order is

Orders are expedition contracts that the Empire entrusts to the colony (`docs/glossary.md` L64). They are voluntary
quotes for cooperation within the regular business of the imperial bodies, not a compulsory daily routine, a fixed
choice among three or a main line of saving the nation (`Imperium-Knowledge/05_Orders与任务规则.md` L8).

Each order is the colony doing business for the Empire: every template states what the Empire gets from it, and what
brings the Empire nothing is not made an order (`Imperium-Knowledge/05_Orders与任务规则.md` L114, R-1103-2244;
`Imperium-Knowledge/现行/索引.md` L1456). An order is regular business, not an emergency: quotes come one every 3-5 days and
only one at a time, and a quote that expires unaccepted is no failure (`Imperium-Knowledge/05_Orders与任务规则.md` L114).

All orders are expeditions, usually by imperial shuttle there and back, and everything done on the colony's own map is
a request (`Imperium-Knowledge/05_Orders与任务规则.md` L45; `Imperium-Knowledge/11_开发进度与未决事项.md` L27). Once an
order is accepted, the base game's quest carries its site, pawns, transport, supplies, combat and settlement
(`Imperium-Knowledge/05_Orders与任务规则.md` L8). Orders and requests are separate classes, and claims merge
into orders, as [Claims](#claims) describes (`Imperium-Knowledge/05_Orders与任务规则.md` L102;
`Imperium-Knowledge/16_旧日遗迹主轴.md` L159).

## Quotes

The functions of the removed Dromos, Tabularium and archive office (档案署) are now in the interface that the button at the
bottom of the screen opens, which the imperial insignia brings up once it is built (`.github/deprecated-terms.json`
L342-381, L976-988; `docs/glossary.md` L57). Quotes do not come by letter: they refresh and expire on their own, so that
the player sees the Empire at work, and they are seen in that interface and in the base game's quest page
(`Imperium-Knowledge/05_Orders与任务规则.md` L115, R-1029-2125; `Imperium-Knowledge/现行/索引.md` L1353).

> [!NOTE]
> **Deleted**: the archive office (档案署; Tabularium, and Dromos in the code-era specification), the building and window
> where the colony saw and accepted orders, with its own layout of orders on one side and support on the other,
> influence shown as ten cells and the current rank in its header (`Imperium-Knowledge/05_Orders与任务规则.md` L8, L102,
> L115; `Imperium-Knowledge/03_Rank与政治权限.md` L168-169; `RimWorld-Imperium/docs/dromos-integration-v1.md` L22-32;
> `Imperium-Knowledge/裁定归档/2026-11.md` L46), and its branch office, placed in the governor's office (长官府)
> (`Imperium-Knowledge/裁定归档/2026-11.md` L26). It was removed, and its functions are now in the interface that the button
> at the bottom of the screen opens (`.github/deprecated-terms.json` L342-381, L976-988).

A quote freezes its main target, its term, its actual reward and the inputs of wealth and difficulty it used; once it
is accepted, the target is not quietly raised, the reward not cut and the difficulty not rolled again
(`Imperium-Knowledge/05_Orders与任务规则.md` L10). Its text gives only the target, the reward and the term for
completion, and states any techprint that comes with it; a needed state of the operation can be shown apart, but no
risk rating, enemy strength, recommended equipment or internal probability (`Imperium-Knowledge/05_Orders与任务规则.md`
L10, L83; `Imperium-Knowledge/designs/RankI-设计核对-2026-10-29.md` L124). Reward, term and acceptance state sit with
the quote; while the order runs, loading, boarding and delivery show through the base game's quest and inspect panes
rather than being repeated on each button, ordinary patrols, stays and changes of shuttle are not announced, and a
danger or interaction that needs the player's attention keeps its feedback
(`Imperium-Knowledge/10_文本命名与界面规范.md` L86).

Quotes rotate each on its own, with no promise of one for each department, and the colony's leaning (倾向) shapes new
quotes (`Imperium-Knowledge/05_Orders与任务规则.md` L16; `Imperium-Knowledge/designs/RankI-设计核对-2026-10-29.md` L119). In the
code-era specification, a new quote is tried every 3-4 days at random; the first time the colony qualifies, it gets
exactly one genuine first quote, unless existing offers, order IDs or history already show an opportunity; when the
quotes are full, an attempt is skipped with no backlog; attempts and expiry go on while an order runs
(`RimWorld-Imperium/docs/dromos-integration-v1.md` L36). One order runs at a time: while it runs, and while it is
processed afterwards, it holds the accepting slot, and the other quotes stay visible, cannot be accepted and keep
rotating (`Imperium-Knowledge/05_Orders与任务规则.md` L17; `RimWorld-Imperium/docs/dromos-integration-v1.md` L40). Accepting
a quote removes only that one; opening the window, a promotion or closing a case does not refresh all of them
(`Imperium-Knowledge/05_Orders与任务规则.md` L18). The concrete numbers are initial values of the configuration, calibrated
by measurement (`Imperium-Knowledge/05_Orders与任务规则.md` L21).

> [!WARNING]
> **Conflict**: how many quotes there are and how long they last.
> - At most three quotes; a quote that is not accepted expires after some days
>   (`Imperium-Knowledge/05_Orders与任务规则.md` L16, L18; `Imperium-Knowledge/designs/RankI-设计核对-2026-10-29.md`
>   L119-121).
> - Three quotes at ranks I to III and four at ranks IV and V; a new quote lasts 10-14 days
>   (`RimWorld-Imperium/docs/dromos-integration-v1.md` L36).

When an order ends, in success or in failure, an administrative processing period (行政处理期) follows; it is shown
without numbers, only roughly, as processing or nearly done, and at its end the Empire sends a shuttle with
the reward, whose landing tells the player that processing is over (`Imperium-Knowledge/03_Rank与政治权限.md` L169,
R-1029-2137) (replaces the administrative lock (行政锁) of about 2 days only after failure or abandonment,
`Imperium-Knowledge/05_Orders与任务规则.md` L19). In the code-era specification, processing lasts 0.5-0.8 days after
success and 2-3 days after failure or abandonment (`RimWorld-Imperium/docs/dromos-integration-v1.md` L46).

The older rules for orders while the colony was hostile belong to the deleted line of relations on the base game's
goodwill, described in [relations.md](relations.md). Orders and requests run independently, and the Empire does not stop because the colony has taken an order
(`Imperium-Knowledge/06_行政设施与地区活动.md` L143).

## Templates

Orders and requests share one structure: at rank I each department has two templates, six in all, and each rank adds
one more per department (`Imperium-Knowledge/05_Orders与任务规则.md` L41;
`Imperium-Knowledge/designs/RankI-设计核对-2026-10-29.md` L108). The number of templates is not the number of quotes
(`Imperium-Knowledge/05_Orders与任务规则.md` L41). A higher rank only adds templates and removes none of the lower
ranks', and later content prefers stronger tiers and variants of existing tasks to new tasks
(`Imperium-Knowledge/05_Orders与任务规则.md` L43).

Templates of the same kind merge into strength tiers (强度档) of one template, and a higher rank brings the stronger tiers
by itself; the strength field takes real effect, with higher threat and a reward that rises with the threat on the base
game's curve, which is decided but not yet implemented (`Imperium-Knowledge/05_Orders与任务规则.md` L47, L85;
`RimWorld-Imperium/docs/code-status.md` L46). Each merged family will need one name; this is decided but not yet
implemented (`Imperium-Knowledge/designs/待用/文本盘点-2026-10-27.md` L652). The merged families are these:

- Outpost clearing (前哨清剿) takes in the reinforced outpost (`Imperium-Knowledge/05_Orders与任务规则.md` L27, L48).
- Obstacle clearing/strike (清障/打击) takes in blockade lifting and the reinforced blockade, and is one contract with
  two targets: removing an obstacle, or destroying the enemy's communications and putting up an imperial beacon
  (`Imperium-Knowledge/05_Orders与任务规则.md` L28, L49, L51).
- Mining (采矿) takes in the old mine and the large old mine, with one mining logic in which the old mine is only a
  larger version with several work areas: rank I a single vein, the higher tiers an old mine with several work areas
  that may meet armed interference (`Imperium-Knowledge/05_Orders与任务规则.md` L30, L50).

The advance position (先遣阵地), judicial arrest (司法缉捕) and local rebuilding (地方重建) are each retained
(`Imperium-Knowledge/05_Orders与任务规则.md` L51). Local rebuilding takes place at a distant site and stays an expedition
order of civil administration, instead of moving to requests (`Imperium-Knowledge/05_Orders与任务规则.md` L35, L45).

Military contracts are kept apart from the base game's bandit-camp quests, which run beside them: imperial friendly
forces appear only in templates that themselves contain imperial units, such as guarding engineers, ballistae
suppressing first, or holding until relieved (`Imperium-Knowledge/05_Orders与任务规则.md` L53-54;
`Imperium-Knowledge/11_开发进度与未决事项.md` L27) (replaces the rule, quoted in
`Imperium-Knowledge/05_Orders与任务规则.md` L54, that from rank II about half the military contracts had an imperial
auxiliary mechanoid squad, and its reward formula). Each military template has a target of the Empire's own: outpost
clearing clears the field and recovers captured imperial equipment, obstacle clearing/strike guards imperial engineers
removing an obstacle or destroys the enemy's communications and puts up an imperial beacon, and the advance position
holds until relieved (`Imperium-Knowledge/05_Orders与任务规则.md` L55).

From rank II judicial arrest has a convoy (押解) variant: a shuttle takes the team to an imperial site to receive
prisoners, who are walked to a handover point; accomplices may try to free them on the way, and the order needs the
prisoner handed over alive (`Imperium-Knowledge/05_Orders与任务规则.md` L57). Judicial arrest, its convoy variant, the
circuit court and Alarius's capture of prisoners make up the judicial line (`Imperium-Knowledge/05_Orders与任务规则.md` L57).

The escort orders (护送), fixed and moving, are retired and replaced at civil administration rank I by recover the
missing official (寻回失踪官员): an imperial official has gone missing in the wild or in ruins, and the team searches
for the official, gives treatment and brings the official back; the weight is on searching and medicine, and the
injury worsens with time (`Imperium-Knowledge/05_Orders与任务规则.md` L34, L51;
`Imperium-Knowledge/designs/待用/文本盘点-2026-10-27.md` L648). The old civil administration order confiscate certified
equipment (制式物资收缴) is retired (`Imperium-Knowledge/05_Orders与任务规则.md` L33;
`Imperium-Knowledge/designs/待用/文本盘点-2026-10-27.md` L54, L647).

Further contracts fill the ranks (`Imperium-Knowledge/05_Orders与任务规则.md` L59-64):

- Fortress assault (要塞攻坚), military rank III: breaking into a fortified strongpoint, with imperial ballistae and the
  like suppressing it first, in step with the regular legions and mechanoid artillery of rank III
  (`Imperium-Knowledge/05_Orders与任务规则.md` L60).
- Pass supply (隘道补给), merchant rank I, first named trade-route escort: an imperial strongpoint on the border has lost
  its landing pad and its supply is cut; supplies are flown to the nearest landing pad and carried overland from there
  by a convoy of caravan mechanoids made for NPC use only (design pending), with one or two light escort mechanoids that
  cannot stop a real ambush; the convoy waits at each rest point and moves on only once the colony's people have reached
  the next one; dangerous stretches may hold ambushes, which the player may scout ahead; goods can be brought along and
  traded at the strongpoint's trader at war-zone prices, the difference going to the colony; all of it takes place on
  one map (`Imperium-Knowledge/05_Orders与任务规则.md` L61).
- Ransom stolen cargo (赎回被劫货物), merchant rank II: a main task of reaching the holder's strongpoint and carrying the
  marked imperial goods back to the shuttle, with one or two modules drawn each time: buying the goods back in the trade
  window with a ransom the Empire advances, the saving shared with the Empire, when the holder is a faction one can
  trade with, while pirates can only be fought; reinforcements; a third party; scattered cargo; a timed transfer. There
  are no hostages, no truce on one map and no floating price (`Imperium-Knowledge/05_Orders与任务规则.md` L63).
- Crashed freighter salvage (坠毁货船打捞), merchant rank III: recovering the cargo of a crashed imperial freighter before
  scavengers do (`Imperium-Knowledge/05_Orders与任务规则.md` L62).
- Epidemic relief (疫区救治), civil administration rank III: going to an imperial strongpoint where an epidemic has broken
  out, isolating and treating the sick until the epidemic ends (`Imperium-Knowledge/05_Orders与任务规则.md` L64).

> [!NOTE]
> **Unverified**: the caravan mechanoids of the pass-supply convoy are a design still pending
> (`Imperium-Knowledge/05_Orders与任务规则.md` L61).

Business that is not an expedition moves into requests: buying in steel, components and fuel, and the old bulk
purchases of steel, supervised purchase and large purchase, become the merchant rank I request bulk supply (大宗供货),
and industrial contract-manufacturing joins bulk supply as its imperial supply contract-manufacturing (帝国供料代工)
variant from rank II (`Imperium-Knowledge/05_Orders与任务规则.md` L31-32, L45;
`Imperium-Knowledge/11_开发进度与未决事项.md` L27; `Imperium-Knowledge/designs/待用/文本盘点-2026-10-27.md` L651).
Until that
move is made, they stay order quotes (`Imperium-Knowledge/designs/待用/文本盘点-2026-10-27.md` L651). The eight old
contract templates of ranks II and III are kept, priced again on the base game's basis, as expedition variants of the
higher ranks, and those among them that are not expeditions move to requests
(`Imperium-Knowledge/05_Orders与任务规则.md` L84). Old saves need no compatibility with this change
(`Imperium-Knowledge/05_Orders与任务规则.md` L37).

> [!NOTE]
> **Deleted**: the procurement orders of the code-era specification, small procurement of steel or chemfuel and bulk
> procurement collected by imperial shuttles under a cargo term of ten days, with their pickup controls, and its
> ladder of separate old-mine, blockade and larger templates (`RimWorld-Imperium/docs/dromos-integration-v1.md` L38,
> L40, L42, L87). The move of procurement into the request bulk supply and the merging of templates into strength
> tiers replaced them (`Imperium-Knowledge/05_Orders与任务规则.md` L27-32, L45, L47-50).

The catalogue of expeditions is as follows (`Imperium-Knowledge/05_Orders与任务规则.md` L66-72;
`Imperium-Knowledge/designs/RankI-设计核对-2026-10-29.md` L110-114):

| Department | Rank I | Rank II | Rank III |
| --- | --- | --- | --- |
| Military | Outpost clearing; obstacle clearing/strike | Advance position | Fortress assault |
| Merchant | Mining (an old mine with several work areas at higher tiers); pass supply | Ransom stolen cargo | Crashed freighter salvage |
| Civil administration | Judicial arrest (with the convoy variant from rank II); recover the missing official | Local rebuilding | Epidemic relief |

> [!NOTE]
> **Unverified**: the orders and requests of ranks IV and V are to be set with the campaign and the rebuilding design,
> and each template's numbers, site generation and texts are to be refined at implementation
> (`Imperium-Knowledge/05_Orders与任务规则.md` L74; `Imperium-Knowledge/06_行政设施与地区活动.md` L105). Campaign and
> reconstruction have only a direction, without authority for full new templates
> (`Imperium-Knowledge/05_Orders与任务规则.md` L112).

> [!NOTE]
> **Unverified**: the detailed play of the advance position is a draft instruction that was not sent. In it, the
> enemy has built the position facing the imperial side; the colony takes it and holds it, and wins by holding long
> enough, while the enemy counterattacks from behind it. Each wave enters on foot from the map edge of the main attack,
> where it meets the enemy's supply route, the rest spread by default over a third of that edge around that point. Imperial shuttles land one by
> one with the waves on the imperial side, by default one per wave and half a game hour after it, sharing the
> reinforcing mechanoids evenly; the mechanoids first defend the imperial side and go over to the attack after the
> last shuttle lands; victory stays with the hold timer, and if all of them die the order goes on and later shuttles
> still land; the military muster has a timeout and a fallback, leaving with the mechanoids at hand or cancelling with a refund. Quote and quest text say from which direction the
> counterattack comes and that imperial reinforcements arrive in batches
> (`Imperium-Knowledge/designs/待用/M3任务批次指令-草案.md` L4, L9, L14-17, L21-24, L27-29, L32-34, L38-39). Its
> delays, spread, timeouts and defence points are left to a table of parameters for the user to tune
> (`Imperium-Knowledge/designs/待用/M3任务批次指令-草案.md` L57-58, L72).

## Challenge and danger

An ordinary contract aims at about twice the overall challenge of a comparable base-game quest at the same wealth and
storyteller difficulty, reusing the base game's valuation, which already weighs wealth and difficulty, without
multiplying wealth again (`Imperium-Knowledge/05_Orders与任务规则.md` L78;
`Imperium-Knowledge/designs/RankI-设计核对-2026-10-29.md` L127). Combat challenge comes from real threats, defences and the
makeup of the target; a contract without combat raises preferably one main load of work, supplies, transport or control,
rather than stacking several multipliers without grounds (`Imperium-Knowledge/05_Orders与任务规则.md` L78). A well-prepared
rank I colony is meant to be able to complete it legitimately, and it does not implicitly require rank II technology
(`Imperium-Knowledge/05_Orders与任务规则.md` L78).

A contract can bring a fair sudden danger, more often one that comes with a techprint; it is judged at most once per
contract and not rolled again each day, and it is used only where the business's causes and preconditions hold, never
to change the main target (`Imperium-Knowledge/05_Orders与任务规则.md` L80). When real combat alert is raised in the
outpost clearing prototype, real reinforcements can come and enter the map; their probability and scale are initial
values calibrated by measurement (`Imperium-Knowledge/05_Orders与任务规则.md` L80).

Leaving before the target is done counts as abandonment, which brings no reward
(`Imperium-Knowledge/05_Orders与任务规则.md` L86; `RimWorld-Imperium/docs/code-status.md` L51). When the members sent
out are all confirmed dead, the order fails at once; this holds for the military templates and for judicial arrest and
local rebuilding, and members alive or only downed do not set it off (`Imperium-Knowledge/05_Orders与任务规则.md` L87;
`Imperium-Knowledge/synced/IMPERIUM_STATE.md` L71; `RimWorld-Imperium/docs/code-status.md` L31). After such a wipe-out
the site, the map, the bodies and the items follow the base game's own lifecycle, with no recovery protection and no
forced deletion of the map (`Imperium-Knowledge/synced/IMPERIUM_STATE.md` L71). Mining and combat expeditions carry a
duty to reach the target and come back (`RimWorld-Imperium/docs/dromos-integration-v1.md` L40).

## Rewards

The reward for double challenge keeps the result of the base game's reward curve, which, falling off, comes to about
1.4-1.6 times the base game's reward at the same threat; the rest is made up by shuttle transport, techprints and
contribution (`Imperium-Knowledge/05_Orders与任务规则.md` L83; `Imperium-Knowledge/designs/RankI-设计核对-2026-10-29.md`
L128). Combat orders use the same formula as the base game's bandit-camp quests, the base reward curve times 1.75; the
earlier extra premium of 1.5 times on orders outside the core set is cancelled, so all orders stand on the base game's
basis and a higher rank pays through higher threat, techprints and contribution
(`Imperium-Knowledge/05_Orders与任务规则.md` L84, L96; `Imperium-Knowledge/11_开发进度与未决事项.md` L30;
`RimWorld-Imperium/docs/code-status.md` L47). The combat and procurement orders were checked to stand on the base
game's basis and are left unchanged (`Imperium-Knowledge/11_开发进度与未决事项.md` L30). Local rebuilding has no advance payment and settles once on
completion (`Imperium-Knowledge/05_Orders与任务规则.md` L88; `RimWorld-Imperium/docs/code-status.md` L50).

For the actual contracts of the Alpha stage, the rewards, compensations and valued gains take as reference the market
values of the base game and the official expansions in use, and comparable quest or service valuations; no arbitrary
imperial price list is made, double challenge does not mean a doubled reward, and where a custom task cannot take a
formula directly, the real item or service it maps to is recorded (`Imperium-Knowledge/05_Orders与任务规则.md` L92).
Techprints, one-off authorizations, political authority and influence, which have no reliable silver reference in the
base game, keep "no direct price yet" and are not turned into cash, silver floors or refunds; background activity
without a contract for the player need not give a reward (`Imperium-Knowledge/05_Orders与任务规则.md` L94). The approved
Alpha balance stays stable in principle and Beta assesses it systematically with real player data; confirmed
implementation errors, conservation or compatibility defects and newly approved changes are still to be fixed
(`Imperium-Knowledge/05_Orders与任务规则.md` L98).

Success places the compensation at the colony by itself, mining returning the actual ore unloaded from the return
shuttle; a placement that fails is retried automatically without another cargo submission or payment click, and a
techprint reward does not by itself authorize technology (`RimWorld-Imperium/docs/dromos-integration-v1.md` L46). A
successful order adds to the colony's contribution (贡献) the valuation frozen when its quote was made, the base game's
reward value for the frozen threat points, counted once (`Imperium-Knowledge/03_Rank与政治权限.md` L70;
`Imperium-Knowledge/designs/RankI-设计核对-2026-10-29.md` L132; `Imperium-Knowledge/synced/IMPERIUM_STATE.md` L41).
Contribution is one ledger, a silver value that only grows and is not split by department
(`Imperium-Knowledge/synced/IMPERIUM_STATE.md` L41). When an order is accepted, its point of leaning goes to the
department that leads it (`Imperium-Knowledge/designs/RankI-设计核对-2026-10-29.md` L132;
`Imperium-Knowledge/03_Rank与政治权限.md` L117, L131).

> [!NOTE]
> **Base game**: the base game's bandit-camp quests reward by its reward curve times 1.75, and its reward curve falls
> off as threat rises; the rewards above rest on this, to be checked against `Data/`
> (`Imperium-Knowledge/05_Orders与任务规则.md` L83, L96).

> [!NOTE]
> **Unverified**: the balance of orders is recorded as unfinished: the full matrix of inputs and rewards for obstacle
> clearing/strike, judicial arrest and the escort orders, a second kind of ore-body terrain for mining, statistics over
> 30 and 60 days across several wealth levels and seeds, and the overall balance of rank I
> (`Imperium-Knowledge/synced/IMPERIUM_STATE.md` L59). The code-era specification says the probabilities, work, capacity
> and balance limits of orders are in `orders-content-v1.md` (`RimWorld-Imperium/docs/dromos-integration-v1.md` L38).

## Travel

Inside the area the Empire controls, the Empire always carries the colony's people by its shuttles, cargo ships or
troop carriers, and where it clearly cannot go, it takes them to the nearest place it controls; this holds for orders,
excavations, campaigns and the triumph at the capital, and distance from home is not a design concern, while the
independent line (独立线) travels the base game's way (`Imperium-Knowledge/05_Orders与任务规则.md` L12;
`Imperium-Knowledge/designs/RankI-设计核对-2026-10-29.md` L125).

The order's shuttle follows the base game's imperial quest shuttle and its quest stages, and is not replaced by an
ordinary transport; loading, boarding, manual or automatic launch, pausing, unloading, dismantling, disabling and
leaving reuse the base game's components as far as possible, and a difference the business needs is handled minimally in
an approved rule layer of the mod that keeps the base game's interaction (`Imperium-Knowledge/10_文本命名与界面规范.md` L94;
`Imperium-Knowledge/designs/RankI-设计核对-2026-10-29.md` L125). For an expedition with passengers, the player picks the
shuttle, opens its loading manifest and chooses Launch expedition or Return expedition; full loading alone never
launches it (`RimWorld-Imperium/docs/dromos-integration-v1.md` L44). Every new order's shuttle link waits for a valid
Stathmos, and its reward is held on account without being lost; a voyage already generated keeps its frozen position
(`Imperium-Knowledge/synced/IMPERIUM_STATE.md` L71).

> [!NOTE]
> **Base game**: the order's shuttle is compared with the base game's imperial quest shuttle and the same quest stages,
> and loading, boarding, manual or automatic launch, pausing, unloading, dismantling, disabling and leaving reuse the
> base game's native components as far as possible; to be checked against `Data/` (`Imperium-Knowledge/10_文本命名与界面规范.md`
> L94).

## Sites of orders

Pirate camps are destinations of imperial orders, ransom stolen cargo among them, and where their loot yard and prisoner
pen lie decides between slipping in and an open assault (`Imperium-Knowledge/09_地图生成与CBF技术.md` L667). For modern-style
defender sites, turrets are limited: the sum of turret combat power may not exceed a share of the defence points (small
10%, medium 15%, large 20%), with a cap of 2/6/10 turrets, inferred defaults that can be tuned; in the scenes of orders
and contracts the defence points are the scene's threat points (`Imperium-Knowledge/09_地图生成与CBF技术.md` L310).

> [!NOTE]
> **Unverified**: the site templates of orders are left to a later series that tunes each order by its scene. Nine of
> the thirteen order scenes lie at enemy bases or in the wild and use placeholders; only the imperial frontier base,
> used by pass supply, the convoy, epidemic relief and local rebuilding, needs a Roman card, and the documents never
> said which buildings such a base holds, nor gave it a rest point, a handover point or an isolation ward. Whether the
> order scenes need rework after the review of 2026-10-27 is also open (`Imperium-Knowledge/11_开发进度与未决事项.md`
> L53).

## Claims

A claim (Claim) is an excavation of a site of the old empire that the Empire sends the colony on (`docs/glossary.md`
L46). Claims merge into orders as a site survey (遗址勘探) template, in a redesign of the ruins and of claims that is
placed after the whole flow of rank II (`Imperium-Knowledge/16_旧日遗迹主轴.md` L159, 2026-10-29;
`Imperium-Knowledge/11_开发进度与未决事项.md` L15; `Imperium-Knowledge/designs/RankI-设计核对-2026-10-29.md` L185).
Excavations, claims among them, follow the base game's quest form, and a colony in the Empire reaches through claims
the same sites that a colony outside it reaches by its own excavations (`docs/ruins-and-technology.md` L71-74). No claim is issued at ranks I and II; claims come
after rank III, with the ruins (`Imperium-Knowledge/05_Orders与任务规则.md` L104;
`Imperium-Knowledge/designs/RankI-设计核对-2026-10-29.md` L182).

> [!NOTE]
> **Deleted**: claims as a class of their own beside orders and requests, running in parallel, taking no quote place
> or accepting slot of orders, untouched by the orders' administrative lock and listed apart at the archive office
> (`Imperium-Knowledge/05_Orders与任务规则.md` L102; `Imperium-Knowledge/designs/RankI-设计核对-2026-10-29.md` L183).
> The merge of claims into orders replaced it (`Imperium-Knowledge/16_旧日遗迹主轴.md` L159;
> `Imperium-Knowledge/11_开发进度与未决事项.md` L15).

> [!NOTE]
> **Unverified**: the redesign that merges claims into orders is to be written after the flow of rank II; until then,
> what follows comes from the current text on claims (`Imperium-Knowledge/16_旧日遗迹主轴.md` L159;
> `Imperium-Knowledge/11_开发进度与未决事项.md` L15).

There is about one chance of a claim per quadrum of 15 game days; its department is drawn by the weight of the
colony's leaning, and when the colony leans toward a department by 45% or more, that department's claim can go to the
deepest layer revealed so far (`Imperium-Knowledge/05_Orders与任务规则.md` L106). The content of claims comes from the
axis of the old ruins (旧日遗迹), and the department shapes only the wording and the kind of ruin; the claim is the
Empire's way into the ruins, the Empire line (帝国线) going through claims and the independent line exploring on its own, both
to the same sites and with no separate reward system (`Imperium-Knowledge/05_Orders与任务规则.md` L108) (replaces the
three departments' own claim plays, as `Imperium-Knowledge/05_Orders与任务规则.md` L108 records). Super-rare technology
is usually the reward of a campaign's winner, and reusing retired Royalty content needs approval item by item as a
lawful exception (`Imperium-Knowledge/05_Orders与任务规则.md` L108). An excavation is not written as a political probe
or as a peerless technology beyond the modern Empire (`Imperium-Knowledge/05_Orders与任务规则.md` L110). Before
publication there is no compatibility with old saves, so the historical recovery claims of old saves are not kept
(`Imperium-Knowledge/05_Orders与任务规则.md` L110, R-1103-2046c; `Imperium-Knowledge/03_Rank与政治权限.md` L171)
(replaces their keeping in migration, `Imperium-Knowledge/05_Orders与任务规则.md` L110;
`Imperium-Knowledge/designs/RankI-设计核对-2026-10-29.md` L184). Tests always start a new save, while the rule that a
historical implementation is not deleted by a document alone, and the keeping of state across saving and loading
within one save, stand as before (`Imperium-Knowledge/03_Rank与政治权限.md` L171, R-1103-2046c).
