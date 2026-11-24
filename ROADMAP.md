# Roadmap: Imperium rebuild

The rebuild implements the design on Neiro-dev/Imperium-old's default branch (`main`, at 20a052b), which is too large
for one Spec Kit cycle. It is split into slices as Spec Kit's
[How to break a large feature into smaller specifications](https://github.com/github/spec-kit/blob/v1.4.3/docs/how-to/spec-of-specs.md)
describes, ordered so that prerequisites come first. This file names and orders the slices; it does not design them.
Each slice is designed when it runs through `/speckit-specify`, from the sources the constitution's Source Register
gives: Imperium's own design from Imperium-old, and other game content from `Data/`, then `ModUpdating.txt`, then
Harmony. Only what none of these settles is marked `[NEEDS CLARIFICATION]` for the maintainer's broad direction
(constitution, Principle IV).

Sources for the slices: the meaning of the design documents in `docs/` on Imperium-old `main`, not its code or
implementation (constitution, Source Register, "Imperium's own design"). Its unmerged design-draft pull requests are
not design. Where a design document points to one of them, the slice lists it as open.

**Status legend**: planned · in-progress · done

| ID | Sub-feature | Intent | Scope boundary | Depends on | Status | Sub-spec |
|----|-------------|--------|----------------|-----------|--------|----------|
| R1 | Mod foundation | Imperium loads as a mod that requires Royalty and no other expansion, and is complete with Royalty alone (`docs/imperium.md` lines 108-109) | In: a loadable mod and its requirements. Deferred: all content | — | done | specs/001-mod-foundation/ |
| R13 | Templates and kits | The designed layouts of city sites, each a terrain shape with a skeleton (templates), and each culture's fixed set of generation data (kits) are data that Mantle's generation uses, checked outside the game against the game's own definitions before Mantle uses them, and the cities Mantle lays out from them are compared outside the game with the reference cities the templates are drawn from (glossary "template", "kit", "skeleton"; constitution, Source Register, "Testing outside the game"; the maintainer's broad direction, constitution, Principle IV) | In: the forms of templates, kits and the cities laid out from them, and their check outside the game against `Data/`, which sets a laid-out city beside its reference; the Empire's kit and the river-bend town's template, written from its screenshot and render, which calibrate the method first and come with Imperium (R15); and the tribal culture's kit and its first templates, one for each attitude of its factions (`Data/`, `Core/Defs/FactionDefs/Factions_Misc.xml` lines 445, 480 and 504), which the alpha opens (the maintainer's broad direction). Deferred: the other cultures' kits and templates, industrial, pirate, medieval, and Odyssey's Traders Guild and Salvagers on the Orbit layer, as later work (the maintainer's broad direction); generation, which picks templates, may mirror, turn and stretch them, and lays out cities from them (R2); the check in the game, which is the final one, once R2 places the tribal culture's settlements and R15 the Empire's | R1, R14 | in-progress | specs/002-templates-and-kits/ |
| R2 | Mantle | Mantle generates the world the parts take place in, and runs whether Empire content is on or off (`docs/imperium.md` lines 91-92; glossary "Mantle", "city building") | In: the generation layer, its on/off independence, the settlements it generates from R13's templates and kits with no Empire content, laid out in R13's form for its check, first the tribal culture's, which the alpha opens (glossary "city building"; the maintainer's broad direction); that, where Royalty is active, the worlds it creates hold no base-game Empire, which does not exist in Imperium's world (`docs/setting.md` line 83), with whether the world-creation faction list can still add it checked in the game; and the alpha's description, which says that it is Mantle alone, a part of Imperium, and that its worlds hold no base-game Empire (`EULA.txt` line 79; `specs/001-mod-foundation/research.md` R-8). Open: the settlements of every other faction that has them, on the surface and in orbit, as their kits and templates come (the maintainer's broad direction); what of Royalty's content only the base game's Empire gives, such as the techprints it alone holds, in Mantle without Imperium; and what else it generates (the section Mantle of draft #132) | R13, R14 | planned | — |
| R3 | The Empire faction | The present Empire replaces the base game's Empire, leans toward New Rome, carries no guns (`docs/setting.md` sections Rome, Weapons, Politics) | In: the faction and its rules. Open: mechanoids, appearance, honor guard (drafts #63, #133) | R1 | planned | — |
| R4 | Starting ruins | A non-expiring quest leads to ruins near the colony that Mantle generates as a decayed town, different each game, which hold the core and disappear once it is taken (`docs/core.md` lines 59-63) | In: quest, site, town generation. Deferred: the core's uses | R2 | planned | — |
| R5 | The core | The core cannot be destroyed, drops or returns with its building, and can be sold (`docs/core.md` lines 73-80) | In: keeping and selling. Deferred: insignia (R6), analysis device (R7), ultraheavy mechanoid (R9) | R4 | planned | — |
| R6 | Envoy, joining and leaving | Taking the core sends the envoy; the colony joins or refuses, and can join or leave later (`docs/empire-relations.md` sections The envoy, Joining and leaving; `docs/core.md` line 67) | In: envoy, joining, leaving, imperial insignia | R3, R5 | planned | — |
| R7 | Excavations and technology | Excavations and claims, techprints, the analysis device, and grants in exchange for finds (`docs/ruins-and-technology.md` sections The ruins, Excavations, Technology in and outside the Empire; `docs/core.md` line 69) | In: quest-led ruins. Deferred: Odyssey's ruins that stay (R10) | R3, R5 | planned | — |
| R8 | Relations, ill will and the purge | The Empire's own relations system, ill will and its notices, and the purge (`docs/empire-relations.md` sections Relations, Ill will, The purge; `docs/imperium.md` lines 99-104) | In: relations, ill will, purge | R6, R7 | planned | — |
| R9 | Expansion content | Each other active expansion adds Empire content that deepens its play, such as the core in an ultraheavy mechanoid with Biotech (`docs/imperium.md` line 110; `docs/core.md` line 72) | In: Biotech. Open: the rest (draft #63) | R5 | planned | — |
| R10 | Ruins that stay (Odyssey) | With Odyssey, ruins that stay on the world map yield techprints that come only with Odyssey (`docs/ruins-and-technology.md` lines 60-67) | Open: what else they give (Imperium-old issue #208) | R7 | planned | — |
| R11 | Playstyles | Standard, distant empire and custom difficulty for the Empire content (`docs/playstyles.md`) | In: the three playstyles | R4, R8 | planned | — |
| R12 | The end | One of two ends decides the Empire's rule on this planet (`docs/imperium.md` lines 83-88, 93) | Open: how either end is reached (Imperium-old issue #164) | R6, R8 | planned | — |
| R14 | Mantle as a mod of its own | Mantle loads as a mod of its own, apart from Imperium, that requires no expansion, as Harmony is a mod of its own that the mods built on it depend on (the maintainer's broad direction; Harmony mod README lines 3-4 and 10-11; `ModUpdating.txt` lines 230 and 267) | In: a loadable Mantle mod and its requirements, and where its folder lives in the repository. Deferred: all its content (R13, R2) | — | in-progress | specs/003-mantle-mod/ |
| R15 | The Empire's cities | Mantle lays out the Empire's settlements from the Empire's kit and templates, first the river-bend town's, as Imperium's content (glossary "kit", "template"; the maintainer's broad direction) | In: the Empire's settlements and their check in the game. Open: the Empire's other templates as they come | R2, R3, R13 | planned | — |

The first slices are R1 and R14, the only ones with no dependencies. Templates and kits (R13) come before Mantle (R2),
since generation picks templates and may mirror, turn and stretch them (glossary "template"; spec-of-specs, The roadmap
pass, step 4). They are checked outside the game against `Data/` first, and in the game once R2 or R15 places them,
which is the final check (constitution, Source Register, "Testing outside the game"). City building, Mantle's
generation of settlements, starts in R2; R4 and R15 are its first uses by the Empire content.

## Releases

The first release is an alpha of Mantle alone: Mantle (R2) with its templates and kits (R13), first the tribal
culture's, as a mod of its own (R14). Which content a release opens, and that the tribal culture comes first, are
settled by no design document, so they follow the maintainer's broad direction (constitution, Principle IV). A framework
comes as a mod of its own that other mods depend on, as Harmony does (`pardeike/HarmonyRimWorld` README lines 3-4 and
10-11).

The alpha requires no expansion. The requirement of Royalty binds Imperium (`docs/imperium.md` line 108), and a mod is
the one its `packageId` names, whose requirements are the mods it needs to function (`ModUpdating.txt` lines 230 and
267), so Mantle's own mod is not bound by it. Mantle must already run with the Empire content off (`docs/imperium.md`
lines 91-92), which is how the alpha has it. Imperium is a remake of Royalty (glossary "Royalty"), Mantle comes with it
as the framework layer of its code (glossary "Mantle"), and Mantle generates the world Imperium's parts take place in
(`docs/imperium.md` line 91), in which the base game's Empire does not exist (`docs/setting.md` line 83). So where
Royalty is active, Mantle creates its worlds without the base game's Empire, as the game does when a player turns a
faction off in world creation (`Royalty/Defs/FactionDefs/Faction_Empire.xml` lines 184-185;
`Core/Languages/English/Keyed/Menus_Main.xml` line 409), and an empire appears only with Imperium (R3). Mantle's
settlements go to every faction that has a kit. The alpha's description says that it is Mantle alone, a part of
Imperium, and that its worlds hold no base-game Empire (`EULA.txt` line 79).

Imperium requires Royalty and no other expansion (R1), and requires Mantle from the first slice whose content uses it,
as the mods built on Harmony depend on Harmony, of which one copy is enabled (the same README lines; constitution,
Principle V). With Royalty alone, Imperium, Mantle included, is complete (`docs/imperium.md` line 109). Imperium brings
the new Empire (R3) with its kit and templates (R15): the river-bend town calibrates the method outside the game first
(R13), and is checked in the game once R15 places it. Later releases add the slices of the Empire content.
