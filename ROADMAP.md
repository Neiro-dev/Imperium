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
| R13 | Templates and kits | The designed layouts of city sites, each a terrain shape with a skeleton (templates), and each culture's fixed set of generation data (kits) are data that Mantle's generation uses, checked outside the game against the game's own definitions before Mantle uses them, and the cities Mantle lays out from them are compared outside the game with the reference cities the templates are drawn from (glossary "template", "kit", "skeleton"; constitution, Source Register, "Testing outside the game"; the maintainer's broad direction, constitution, Principle IV) | In: the forms of templates, kits and the cities laid out from them, and their check outside the game against `Data/`, which sets a laid-out city beside its reference; and the first kit and template, the Empire's kit and the river-bend town's template, written from its screenshot and render. Deferred: the other cultures' kits and templates, tribal, industrial, pirate, medieval, and Odyssey's Traders Guild and Salvagers on the Orbit layer, as later work (the maintainer's broad direction); which templates and kits the alpha holds, and generation, which picks templates, may mirror, turn and stretch them, and lays out cities from them (R2); the check in the game, which is the final one, once R2 places them | R1 | in-progress | specs/002-templates-and-kits/ |
| R2 | Mantle | Mantle generates the world the parts take place in, and runs whether Empire content is on or off (`docs/imperium.md` lines 91-92; glossary "Mantle", "city building") | In: the generation layer, its on/off independence, the settlements it generates from R13's templates and kits with no Empire content, laid out in R13's form for its check, first the river-bend town from R13's first template, which calibrates the method before anything else and then ships (the maintainer's broad direction), which the alpha opens (glossary "city building"), and the alpha's description, which says that it holds only part of Imperium (`EULA.txt` line 79; `specs/001-mod-foundation/research.md` R-8). Open: the settlements of every other faction that has them, on the surface and in orbit, as their kits and templates come (the maintainer's broad direction), and what else it generates (the section Mantle of draft #132) | R1, R13 | planned | — |
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

The first slice is R1, the only one with no dependencies. Templates and kits (R13) come before Mantle (R2), since
generation picks templates and may mirror, turn and stretch them (glossary "template"; spec-of-specs, The roadmap pass,
step 4). They are checked outside the game against `Data/` first, and in the game once R2 places them, which is the
final check (constitution, Source Register, "Testing outside the game"). City building, Mantle's generation of
settlements, starts in R2; R4 is its first use by the Empire content.

## Releases

The first release is an alpha of Imperium that opens part of its content: Mantle (R2) with its templates and kits
(R13), on the mod foundation (R1). Which content a release opens is game content that no design document settles, so it
follows the maintainer's broad direction (constitution, Principle IV). It changes no dependency: R2 and R13 depend on no
slice of the Empire content, so they can be built before them (spec-of-specs, The roadmap pass, step 4), and Mantle must
already run with the Empire content off (`docs/imperium.md` lines 91-92), which is how the alpha has it.

The alpha is the same mod as every later release, so it requires Royalty (`docs/imperium.md` line 108), and its
description says that it holds only part of Imperium (`EULA.txt` line 79). Later releases add the slices of the Empire
content.
