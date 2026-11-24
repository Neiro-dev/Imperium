# Feature Specification: Mantle as a mod of its own

**Feature Branch**: `claude/project-thread-048ozg`

**Created**: 2026-11-24

**Status**: Draft

**Input**: Parent roadmap: `ROADMAP.md` → entry **R14**, Mantle as a mod of its own. Mantle loads as a mod of its own,
apart from Imperium, that requires no expansion, as Harmony is a mod of its own that the mods built on it depend on
(the maintainer's broad direction; Harmony mod README lines 3-4 and 10-11; `ModUpdating.txt` lines 230 and 267).
Scope: a loadable Mantle mod and its requirements, and where its folder lives in the repository. Deferred: all its
content (R13, R2). R13, templates and kits, waits for this feature's folders and package identifier.

## Sources

Each requirement below names its source in brackets. The sources are those the constitution's Source Register gives:

- **[Design]**: Imperium's own design, Imperium-old `main` (20a052b): `docs/imperium.md`, section Parts (lines 91-92)
  and section Expansions (lines 108-110); `docs/glossary.md`, Mantle (line 221).
- **[Roadmap]**: `ROADMAP.md`, entry R14 (intent and scope boundary), entries R2, R13 and R15, and its section
  Releases.
- **[R1]**: the mod foundation, `specs/001-mod-foundation/` (spec and research), whose forms this feature gives Mantle
  where the same sources settle the same question.
- **[Data]**: the base game and official expansions in `Data/` of RimWorld 1.7.5014 (`Version.txt`: 1.7.5014
  rev1195): the folder `Data/`, which holds each package in a folder of its own named after it; each package's
  `About/About.xml`; and the base game's mod list and save dialog text in
  `Data/Core/Languages/English/Keyed/Menus_Main.xml` and `Dialogs_Various.xml`.
- **[ModUpdating]**: `ModUpdating.txt` of the same release, sections MOD FILE STRUCTURE and MOD METADATA. Used only
  where [Data] gives no form.
- **[Harmony]**: the Harmony mod (`pardeike/HarmonyRimWorld`, `master` on 2026-11-24): `README.md`,
  `About/About.xml` and `Release-payload.json`. Used only where [Data] and [ModUpdating] give no form.
- **[EULA]**: `EULA.txt` of RimWorld, which is always followed (constitution, Source Register).
- **[GitHub]**: GitHub Docs (`github/docs`, `main` on 2026-11-24): Hello World
  (`content/get-started/using-github/hello-world.md` line 34), Licensing a repository (lines 27 and 31) and About
  READMEs (lines 24-33).
- **[Spec Kit]**: Spec Kit v1.4.3: the plan template's Project Structure, and `docs/how-to/monorepo.md` line 3.
- **[Testing]**: `Readme.txt` of the same install (lines 21, 27-38 and 58-60), then RimBridgeServer
  (`pardeike/RimBridgeServer` `README.md`, section Local Deploy Targets, lines 118-129) with GABS.

Mantle is the framework layer of Imperium's code, which the content layer builds on [Design: glossary line 221], and
Imperium is complete with Royalty alone, Mantle included [Design: line 109]. Mantle is therefore part of the Imperium
project, while it is released as a mod of its own that requires no expansion [Roadmap: R14, Releases], as the Harmony
mod is a mod of its own that the mods built on it depend on [Harmony: `README.md` lines 3-4 and 10-11]. Like Imperium,
Mantle is game content, judged by what the official expansions contain (constitution, Source Register; [R1: spec,
Sources]), so each requirement below takes the official expansions' form first.

## Clarifications

### Session 2026-11-24

Each answer comes from the source named with it; none is game content left to the maintainer (constitution,
Principle IV).

- Q: Does Mantle get a repository of its own? → A: No. A repository usually groups together the items that belong to
  the same project [GitHub: Hello World line 34], and Mantle is part of the Imperium project [Design: glossary line
  221; line 109]. One Spec Kit project, this repository's `.specify/`, holds the roadmap that both mods' entries belong
  to [Spec Kit: `monorepo.md` line 3; Roadmap].
- Q: Where do the two mods' folders sit in the repository? → A: Side by side, each a folder of its own named after its
  mod, with `About/About.xml` at its root and neither inside the other, as `Data/` holds Core and each official
  expansion [Data: the folder `Data/`; ModUpdating: lines 68-81]. Imperium's mod files therefore leave the repository
  root for a folder of their own (FR-013), and the repository's own files stay at the root (FR-014).
- Q: Does this feature make Imperium require Mantle? → A: No. Imperium requires Mantle from the first slice whose
  content uses it [Roadmap: Releases], which is R13 (`specs/002-templates-and-kits/research.md` R-1). Until then the
  two mods name neither the other.
- Q: Which files count as one mod's own files (FR-014)? → A: the folders a mod holds for the game, `About/`, `Defs/`,
  `Textures/`, `Sounds/`, `Patches/` and `Languages/`, and for its code `Source/` and `Assemblies/` [ModUpdating:
  lines 75-151], with its README and license (FR-009, FR-015). Files that serve the repository or both mods rather
  than one mod, such as Spec Kit's files, the specifications and a development tool that checks both mods, are not
  one mod's own and stay at the repository root, where Spec Kit's plan template puts a project's code by default
  [Spec Kit: plan template, Project Structure, "Single project (DEFAULT)"].

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Turn Mantle on with the base game alone (Priority: P1)

A player who owns only the base game finds Mantle in the game's mod list, turns it on, and starts or loads a game
without problems.

**Why this priority**: the alpha is Mantle alone, as a mod of its own that requires no expansion [Roadmap: Releases],
and every later Mantle entry is content inside this mod [Roadmap: R13, R2].

**Independent Test**: put Mantle's folder in the game's mods, turn on Core and Mantle only, restart, and start a new
game; the game loads with no errors from Mantle, as it does with Core alone, and the mod list shows no missing
requirement for it.

**Acceptance Scenarios**:

1. **Given** Mantle is installed, **When** the player opens the mod list, **Then** Mantle is listed by its name, apart
   from Imperium.
2. **Given** only Core and Mantle are active, **When** the player looks at Mantle in the mod list, **Then** no missing
   requirement is shown [Data: Menus_Main.xml line 146, `ModUnsatisfiedDependency`].
3. **Given** only Core and Mantle are active, **When** the game restarts and a new game starts, **Then** it loads with
   no errors or warnings from Mantle.
4. **Given** a game saved with Mantle active, **When** it is loaded again with the same mods, **Then** it loads with
   no errors or warnings from Mantle.

---

### User Story 2 - Mantle with the official expansions and other mods (Priority: P2)

A player who owns expansions uses Mantle with any of them, and places it where the mods that depend on it can follow.

**Why this priority**: Mantle's content uses expansion content where it is marked, and acts on Royalty's Empire where
Royalty is active [Roadmap: R13, R2], so it must load after them; the mods built on it, Imperium first, come after it
[Roadmap: Releases].

**Independent Test**: load Mantle with each combination of Royalty, Ideology, Biotech, Anomaly and Odyssey added to
Core; each loads with no errors from Mantle, after every active official expansion, with no missing requirement and no
load-order warning. Then place Mantle directly after the last official expansion, ahead of an ordinary mod; the mod
list shows no load-order warning.

**Acceptance Scenarios**:

1. **Given** any of the five official expansions are active, **When** the game loads, **Then** Mantle loads with no
   errors, after every active official expansion, and the mod list shows no load-order warning for it [Data:
   Menus_Main.xml line 143, `ModOrderingWarning`].
2. **Given** an ordinary mod is also active, **When** Mantle is placed directly after the last active official
   expansion and ahead of that mod, **Then** the mod list shows no load-order warning and the game loads with no errors
   from Mantle.

---

### User Story 3 - Each mod from its own folder (Priority: P3)

The developer keeps Mantle and Imperium in one repository, and puts each mod into the game, and later releases it, from
its own folder, which holds that mod and nothing else.

**Why this priority**: Mantle is released apart from Imperium [Roadmap: R14, Releases], and a mod is the folder in the
game's mods that holds its `About/About.xml` [ModUpdating: lines 68-81].

**Independent Test**: put Mantle's folder and Imperium's folder into the game's mods, each on its own; each is listed
as its own mod, neither folder holds a file of the other mod or of the repository's own development, and with Core,
Royalty, Imperium and Mantle active the game loads with no errors from either beyond the reports that each loaded no
content.

**Acceptance Scenarios**:

1. **Given** the repository, **When** the developer looks at its root, **Then** Mantle and Imperium each have a folder
   of their own there, named after the mod, each with `About/About.xml` at its root.
2. **Given** Imperium's folder alone is in the game's mods, **When** the player turns on Core, Royalty and Imperium,
   **Then** Imperium behaves as R1 set it: it loads, and with Royalty off it shows Royalty as a missing requirement
   [R1: spec FR-001 to FR-005].
3. **Given** both folders are in the game's mods, **When** Core, Royalty, Imperium and Mantle are active, **Then** the
   game loads with no errors or warnings from either, other than each one's report that it loaded no content.

---

### Edge Cases

- Mantle is placed above an official expansion in the load order: the game shows that it must be loaded after that
  expansion, by refusing the move or by a load-order warning with auto-sort, as for any mod out of order [Data:
  Menus_Main.xml lines 95, 139 and 143].
- Mantle and Imperium are both active, in either order relative to each other: no warning, since neither names the
  other in this feature; R13 adds Imperium's requirement on Mantle and its place after it [Roadmap: Releases;
  `specs/002-templates-and-kits/research.md` R-1].
- Royalty is active with Mantle: nothing changes in the game's world yet, since this feature adds no content; Mantle
  creates worlds without the base game's Empire from R2 [Roadmap: R2, R14].
- The game version is not 1.7: the mod list shows that Mantle was not made for that version [Data: Menus_Main.xml line
  147, `ModNotMadeForThisVersion`; ModUpdating: line 253].
- Two copies of Mantle are installed (one local, one from the Workshop): only one of them can be active [ModUpdating:
  line 244; Data: Menus_Main.xml line 144, `ModWithSameIdAlreadyActive`].
- Mantle is turned on or off for a save made with a different set of mods: the game shows its mods-mismatch warning,
  and the save loads with no errors from Mantle [Data: Dialogs_Various.xml line 126; Roadmap: R14].
- A copy of the whole repository is put in the game's mods: it is not a mod, since its root holds no `About/`; each mod
  goes into the game's mods by its own folder [ModUpdating: lines 68-81; Testing: RimBridgeServer `README.md` lines
  118-129].

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: Mantle MUST be a mod of its own, apart from Imperium: a folder of its own with its own `About/About.xml`
  and its own package identifier, which the player turns on and off in the mod list apart from Imperium [Roadmap: R14;
  ModUpdating: lines 68-81 and 229-244].
- **FR-002**: Mantle MUST be listed in RimWorld 1.7's mod list and load, and MUST support 1.7 only, as each official
  expansion does [Data: `Version.txt`; each expansion's `About/About.xml` lists only `1.7`].
- **FR-003**: Mantle MUST NOT require any expansion or any other mod [Roadmap: R14, Releases].
- **FR-004**: Mantle MUST load after Core and after every official expansion, as each official expansion loads after
  every one that came before it [Data: `About/About.xml` lines 9-11 of Royalty and 9-15 of Odyssey], because its
  content uses expansion content where marked and acts on Royalty's Empire where Royalty is active [Roadmap: R13, R2].
- **FR-005**: With Core and Mantle active, starting a new game and loading a saved one MUST produce no errors or
  warnings from Mantle, except the one error in which the game reports that Mantle loaded no content, as it reported
  for Imperium while R1 added none [R1: spec FR-005]. The first roadmap entry that adds content to Mantle removes it.
- **FR-006**: With any combination of the five official expansions also active, FR-005 MUST still hold, since Mantle
  requires none of them [Roadmap: R14, Releases] and Imperium, Mantle included, runs with each other expansion that is
  active [Design: lines 109-110].
- **FR-007**: Mantle MUST add no game content in this feature [Roadmap: R14, "Deferred: all its content"].
- **FR-008**: Wherever the game shows Mantle, it MUST be presented as community-created content, and never as
  official or made by Ludeon [EULA: lines 57 and 78].
- **FR-009**: The disclaimer the EULA gives MUST be displayed on or reasonably in connection with Mantle [EULA: lines
  32-34].
- **FR-010**: Mantle MUST have one package identifier, different from Imperium's, that is unique, meets the game's
  format, does not contain "Ludeon", and does not change once released [ModUpdating: lines 229-244].
- **FR-011**: Mantle MUST be able to load directly after the last active official expansion and ahead of the mods that
  depend on it and every ordinary mod placed after them, and its load order MUST name no package that is not Ludeon's,
  as R1 set for Imperium [R1: spec FR-011]. Players are told this place where they read about Mantle, as the Harmony
  mod tells players to enable it above the mods that depend on it [Harmony: `README.md` lines 3-4].
- **FR-012**: Mantle and Imperium MUST be kept in this one repository [GitHub: Hello World line 34; Design: glossary
  line 221; line 109; Spec Kit: `monorepo.md` line 3].
- **FR-013**: Each of the two mods MUST be a folder of its own at the repository root, named after its mod, with
  `About/About.xml` at its root, and neither MUST be inside the other [Data: the folder `Data/`; ModUpdating: lines
  68-81].
- **FR-014**: Each mod's folder MUST hold only that mod's own files, its folders for the game and for its code, its
  README and its license, so that it is a complete mod when it alone is put into the game's mods [ModUpdating: lines
  68-81 and 96-151; Harmony: `README.md` line 10]. Files that serve the repository or both mods, those of Spec Kit,
  the roadmap, the specifications, a development tool that checks both mods, and the repository's own README and
  license file, MUST stay at the repository root, outside both [Spec Kit: plan template, Project Structure; GitHub:
  Licensing a repository line 27, About READMEs line 31]; each mod folder holds its own README and a copy of the
  license (FR-009, FR-015).
- **FR-015**: Each mod's folder MUST hold the repository's license, since the license requires its notice in all
  copies or substantial portions of the software [`LICENSE` lines 12-13; GitHub: Licensing a repository line 31], as
  the Harmony mod's released files hold its license [Harmony: `Release-payload.json`].
- **FR-016**: Imperium, moved into its own folder, MUST keep everything R1 gave it [R1: spec FR-001 to FR-011].

### Key Entities

- **Mantle**: the framework layer of Imperium's code, which the content layer builds on [Design: glossary line 221],
  released as a mod of its own that requires no expansion [Roadmap: R14]. It is identified by its package identifier
  (FR-010).
- **Imperium**: the remake of Royalty, which requires Royalty [R1]; from R13 it also requires Mantle [Roadmap:
  Releases].
- **Mod folder**: the folder in the game's mods that holds one mod, with `About/About.xml` at its root [ModUpdating:
  lines 68-81]; in the repository, one for each of the two mods (FR-013).
- **The repository**: this repository, which holds the Imperium project, Mantle included, with its Spec Kit project,
  roadmap and specifications at its root (FR-012, FR-014).
- **Official expansions**: Royalty, Ideology, Biotech, Anomaly and Odyssey, none of which Mantle requires and all of
  which it loads after [Data; Roadmap: R14].
- **Ordinary mods**: every mod that is not Ludeon's; the mods that depend on Mantle are among them, Imperium first
  [Roadmap: Releases].

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: With Core and Mantle active, a new game starts and a save loads, and the game's log has zero error or
  warning lines beyond the same launch with Core alone, other than the no-content report (FR-005).
- **SC-002**: Mantle shows no missing requirement in any launch of SC-001, SC-003 and SC-005.
- **SC-003**: Across every combination of the five official expansions added to Core, none included (32
  combinations), every one loads with zero error or warning lines in the log beyond the same combination without
  Mantle, other than the no-content report, with Mantle after every active official expansion and no load-order
  warning for it.
- **SC-004**: Nothing the game shows for Mantle states or implies that it is official or made by Ludeon, and the
  EULA's disclaimer is displayed with it.
- **SC-005**: With an ordinary mod active, Mantle placed directly after the last active official expansion and ahead
  of that mod loads with zero error or warning lines beyond the same launch without Mantle, other than the no-content
  report, and with no load-order warning, and the place is stated where players read about Mantle.
- **SC-006**: Imperium's folder, put alone into the game's mods, passes R1's SC-001 and SC-002 again; with Core,
  Royalty, Imperium and Mantle active, the log has zero error or warning lines beyond the same launch without either,
  other than the two no-content reports; the repository root holds the two mod folders side by side and no `About/` of
  its own; and each mod folder holds only the files FR-014 names for it.

## Assumptions

- The mod's name in the mod list is Mantle, the name the design gives the framework layer [Design: glossary line 221].
- Each official expansion presents itself with a label, a description, an icon and preview images [Data:
  `ExpansionDefs.xml`]; as for Imperium, a community mod takes only the parts of that form it can use, within FR-008
  [R1: research R-8]. Mantle's description says what the alpha is, Mantle alone, a part of Imperium, whose worlds hold
  no base-game Empire, and is written with that content in R2 [Roadmap: R2].
- Mantle lists the Harmony mod as a requirement only from the first entry whose code uses Harmony, as R1 set for
  Imperium [R1: research R-9]; this feature adds no code (FR-007).
- R13's merged documents (`specs/002-templates-and-kits/`) place Mantle's files in a repository of Mantle's own and
  Imperium's at the repository root, and leave Mantle's paths to this feature; they follow this feature's layout once
  it is merged [Roadmap: R13 depends on R14].
- Testing in the game follows the constitution's testing sources: `Readme.txt` (the `-quicktest` launch option and
  `-savedatafolder`), then RimBridgeServer with GABS, whose local development puts a mod under development into the
  game's mods by copying it there [Testing: RimBridgeServer `README.md` lines 118-129]; the setup belongs to the plan.
  Testing outside the game comes first and holds each `About/About.xml` against the official ones in `Data/`
  (constitution, Source Register).
