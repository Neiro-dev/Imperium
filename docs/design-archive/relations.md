# Contact and relations with the Empire

This section covers how the colony stands toward the Empire: what joining it or staying outside means, the first
meeting with the Empire's envoy, joining and leaving later, the Empire's relations with a colony, ill will and the
purge, and dealings with settlements that are left open. The core and the starting ruins that set off the first meeting
are in [core.md](core.md); orders and claims are in [orders.md](orders.md); excavations, claims and techprints are in
[ruins-and-technology.md](ruins-and-technology.md); the parts of Imperium and the end of the game are in
[imperium.md](imperium.md); imperial visits and transits are in [administration.md](administration.md).

## In the Empire or outside it

A colony either joins the Empire, serving it and receiving its commendations, or stays outside it and bears its ill
will and pressure (`docs/imperium.md` L79-82). Membership trades what the colony finds for what the Empire grants: a
colony in the Empire gets its core technology from the Empire's grants, hands over the old empire's technology that it
finds and receives present technology in exchange, and cannot keep found technology by registering it
(`docs/ruins-and-technology.md` L26-29, L32-34, L38-40, L80-84). A colony in the Empire reaches the old empire's sites
through claims and cannot excavate on its own, while a colony outside it reaches them by its own excavations
(`docs/ruins-and-technology.md` L37, L72-73, L81).

In the background, joining is what a state outside the Roman political circle does when it applies on its own to join
and takes on obligations (`Imperium-Knowledge/03_Rank与政治权限.md` L10). In play, the obligation is receiving the
Empire's transit visits, to which the player need not respond; the Empire takes no tax and sets no other compulsory
obligation (`Imperium-Knowledge/03_Rank与政治权限.md` L10, L164;
`Imperium-Knowledge/designs/RankI-设计核对-2026-10-29.md` L25). Dismantling imperial facilities does not by itself take
away the colony's political standing or the delivery duties of contracts already made
(`Imperium-Knowledge/03_Rank与政治权限.md` L20). The cost of joining is that factions hostile to the Empire grow
hostile to the colony as its rank rises, and attack it more often while imperial people are there
(`Imperium-Knowledge/03_Rank与政治权限.md` L164).

> [!NOTE]
> **Unverified**: these statements come from the file whose contact line was deleted (see below), and the root docs
> neither restate nor drop them, so it cannot be told whether they still hold; the changes of goodwill and the
> frequency of attacks that the cost of joining brings are left to be set at implementation by the base game's
> faction relations and raids (`Imperium-Knowledge/03_Rank与政治权限.md` L10, L20, L164).

## The first meeting

Taking the core from the starting ruins sets off the colony's first meeting with the Empire (`docs/core.md` L13).
Once the colony has taken the core, the Empire learns that it is missing and sends its envoy (使节) to investigate the
region (`docs/empire-relations.md` L10, L65-66). The envoy is the same official who reads the emperor's edict when the
colony rises to rank IV (`docs/glossary.md` L52; `Imperium-Knowledge/06_行政设施与地区活动.md` L167, L172). The envoy
offers the colony two choices, to join the Empire or to let the envoy leave, which keeps the core, and the offer says
that the colony can still join later at an imperial settlement (`docs/empire-relations.md` L10-11, L20-23, L67-70).
What joining does with the core is a conflict between two root passages, set out in [core.md](core.md). A colony that
ignores the envoy until its wait times out is treated as Anomaly treats an ignored visitor, and its ill will rises
(`docs/empire-relations.md` L24-26, L71-72, L99).

Joining gives the colony rank I directly; it is the colony's political rank and brings no personal title
(`Imperium-Knowledge/03_Rank与政治权限.md` L12; `RimWorld-Imperium/docs/dromos-integration-v1.md` L9;
`RimWorld-Imperium/docs/imperial-contact-v0.md` L65).

> [!NOTE]
> **Unverified**: that joining gives rank I comes only from passages of the deleted contact line; the root docs keep
> the ranks but do not say at which rank a colony joins (`Imperium-Knowledge/03_Rank与政治权限.md` L12;
> `docs/glossary.md` L67).

> [!NOTE]
> **Base game**: Anomaly has an ignored visitor whose wait times out; the envoy's account rests on this, to be checked
> against `Data/` (`docs/empire-relations.md` L24-26, L71-72).

> [!NOTE]
> **Deleted**: the older line of first contact. The colony built and powered a terminal of its own, the archive office
> (档案署; Dromos in the code-era specification), with the original core, and called the Empire from it; joining was not
> conditioned on the imperial insignia, the imperial area or the landing pads, and there was no second recognition; a
> representative came, negotiated and left, after set response and arrival times (trial values, native acceptance still
> pending), with an 18-hour deadline and a departure timeout; a dialogue offered Join (加入), Decline (拒绝) and Defer
> (保留意见); after a refusal, a missed visit or the representative's death the colony could call again
> (`Imperium-Knowledge/03_Rank与政治权限.md` L12, L16, L20; `Imperium-Knowledge/16_旧日遗迹主轴.md` L19;
> `Imperium-Knowledge/designs/RankI-设计核对-2026-10-29.md` L21, L24-25; `Imperium-Knowledge/06_行政设施与地区活动.md` L197;
> `Imperium-Knowledge/11_开发进度与未决事项.md` L59; `RimWorld-Imperium/docs/imperial-contact-v0.md` L3-7, L32-71, L87-89). The
> envoy whom the Empire sends on its own once the core is missing, and the removal of the archive office and of Dromos,
> replaced it (`docs/empire-relations.md` L8-26, L63-72; `.github/deprecated-terms.json` L342-381, L976-988).

## Joining and leaving later

A colony outside the Empire can join it later at an imperial settlement by handing over the core, once its ill will is
back at zero (`docs/empire-relations.md` L58-59, L76-77). A colony in the Empire can leave it in the Empire's tab
(`docs/empire-relations.md` L60-61, L78). Leaving the Empire locks the making of all imperial technology, and joining it
locks the making of technology the Empire has not permitted; in either case what the colony already has stays and keeps
working (`docs/empire-relations.md` L48-49, L61-62, L79-81).

## Relations

The Empire's relations with a colony are a system of their own, shown in the faction screen in place of the base
game's goodwill (`docs/empire-relations.md` L85-86; `docs/glossary.md` L25). Positive relations with the Empire are
possible only for a colony in the Empire, and a neutral Empire is passive (`docs/empire-relations.md` L87-88).

> [!NOTE]
> **Deleted**: the older line of relations on the base game's goodwill. The base game's faction relations settled the
> death of the representative or of a promotion visitor in the colony, that joining or promotion failing and open to
> another try, where earlier the death had revoked rank I and turned the Empire hostile; when the colony's faction
> relation with the Empire turned hostile, all imperial interaction paused, with no visits, transits, requests, order
> quotes or claims, leased mechanoids recalled and an order in progress voided, while the colony kept its rank,
> techprints and research and interaction resumed by itself once relations recovered
> (`Imperium-Knowledge/03_Rank与政治权限.md` L16, L18; `Imperium-Knowledge/06_行政设施与地区活动.md` L143, L197;
> `Imperium-Knowledge/designs/RankI-设计核对-2026-10-29.md` L24, L26; `Imperium-Knowledge/11_开发进度与未决事项.md`
> L59; `Imperium-Knowledge/05_Orders与任务规则.md` L20; `RimWorld-Imperium/docs/code-status.md` L28;
> `RimWorld-Imperium/docs/imperial-contact-v0.md` L69-71). The Empire's own relations in place of goodwill replaced
> it (`docs/empire-relations.md` L85-88; `docs/glossary.md` L25).

The Empire's three departments do not appear to the player as persons or separate bodies, so the documents of its
pre-review are not written separately by department (`Imperium-Knowledge/03_Rank与政治权限.md` L121;
`Imperium-Knowledge/裁定归档/2026-10.md` L127). The Empire's offices and the identities of its visitors are not set at
present, and the leaning is no longer shown through the issuing office or the visitor's identity
(`Imperium-Knowledge/裁定归档/2026-11.md` L30; `Imperium-Knowledge/03_Rank与政治权限.md` L121).

## Ill will

Ill will is the counterpart of contribution for what the colony does against the Empire (`docs/empire-relations.md`
L118). It is only ever negative and falls back over time (`docs/empire-relations.md` L92). It works underneath:
players never see it, by name or as a number, only the Empire's reactions and notices (`docs/empire-relations.md`
L93-94).

Ill will rises when the colony excavates ruins of the old empire on its own, claims not counting, sells the core,
ignores the envoy, or attacks the Empire's settlements or caravans (`docs/empire-relations.md` L95-100). When the
Empire finds an excavation it has not permitted, it sends the colony a notice (`docs/empire-relations.md` L40-42,
L101).

The strength of the Empire's attacks follows ill will, and while the colony is a small threat the Empire pays it
little heed (`docs/empire-relations.md` L42-44, L102-103). The Empire presses a colony outside it harder the more it
knows of what the colony does against it, up to a purge; the Empire cannot be beaten in open war, only survived
(`docs/empire-relations.md` L29-31).

## The purge

The top tier of ill will is a purge, carried out with troop ships and orbital bombardment; for a quadrum, troop
landings and bombardment alternate (`docs/empire-relations.md` L107-108). During the purge the Empire, judging the
threat, commits ever stronger forces: first troops drawn from the surrounding regions, later the field army
(`docs/empire-relations.md` L109-110). Orbital bombardment and changes to the environment do damage that has no source,
and shelters protect against it (`docs/empire-relations.md` L111-112). Surviving the purge is a stage on the way to the
end in which the colony ends the Empire's rule on this planet, as [imperium.md](imperium.md) describes
(`docs/empire-relations.md` L113-114).

## Dealings with settlements and other factions

> [!NOTE]
> **Unverified**: entering cities to trade is a draft that is not scheduled. Whether Imperium makes its own faction
> interaction waits on the base game's next official expansion, at the earliest half a year on; if that expansion brings
> faction content of its own, most of the draft falls away (`Imperium-Knowledge/designs/待用/进城交易设计-草案-2026-10-27.md`
> L8-12; `Imperium-Knowledge/designs/待用/README.md` L17; `Imperium-Knowledge/目录/待用.md` L52-68). Its concrete rules on
> entering and leaving, the map's lifecycle, stock, the quartermaster, residents and guards, crossing the line and the
> threshold of an imperial city are suggestions not yet ruled; open within them are whether a shuttle or pod can land in
> town, the number of residents and the rank that stands for the base game's title permit, while the civilian pawn kinds
> are postponed to implementation (`Imperium-Knowledge/designs/待用/进城交易设计-草案-2026-10-27.md` L28, L34, L72-73, L80-81).

> [!NOTE]
> **Unverified**: a comparison of two reference mods names as ideas worth borrowing quests that let the player step
> into other factions' wars and diplomacy, and a permanently hostile faction as a technique for meeting some quests'
> starting conditions; it records that players of one of them asked for a knightly order to join and a ladder of
> titles, which shows such demand exists (`Imperium-Knowledge/designs/研究/参照模组/两模组对照.md` L33-34). None of
> this is ruled as Imperium's design.
