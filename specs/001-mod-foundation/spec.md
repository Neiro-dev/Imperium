# Feature Specification: Mod foundation

**Feature Branch**: `claude/project-thread-b1vpqw`

**Created**: 2026-11-24

**Status**: Draft

**Input**: Parent roadmap: `ROADMAP.md` → entry **R1**. Imperium loads in RimWorld as a mod that requires Royalty and does not require any other expansion, and is complete with Royalty alone (Imperium-old main, docs/imperium.md lines 108-109). Scope: a loadable mod and its expansion requirements only; all content (Mantle, the Empire faction, starting ruins and the rest) is deferred to later roadmap entries. Game content and the released mod's form follow the base game and official expansions in Data/, then ModUpdating.txt, then Harmony.

## Sources

Each requirement below names its source in brackets. The sources are those the constitution's Source Register gives:

- **[Design]**: Imperium's own design, Imperium-old `main` (20a052b): `docs/imperium.md`, section Expansions
  (lines 108-110); `docs/glossary.md`, Royalty (line 35) and Mantle (line 221); `docs/setting.md`, Politics
  (line 83).
- **[Roadmap]**: `ROADMAP.md`, entry R1, scope boundary.
- **[Data]**: the base game and official expansions in `Data/` of RimWorld 1.7.5014 (`Version.txt`: 1.7.5014
  rev1195): each expansion's `About/About.xml`; the base game's definitions of its expansions in
  `Data/Core/Defs/Misc/ExpansionDefs/ExpansionDefs.xml`; and the base game's mod list and save dialog text in
  `Data/Core/Languages/English/Keyed/Menus_Main.xml` and `Dialogs_Various.xml`.
- **[ModUpdating]**: `ModUpdating.txt` of the same release, sections MOD FILE STRUCTURE and MOD METADATA. Used only
  where [Data] gives no form.
- **[Harmony]**: the Harmony mod (`pardeike/HarmonyRimWorld`, default branch on 2026-11-24): `README.md` and
  `About/About.xml`. Used only where [Data] and [ModUpdating] give no form.
- **[EULA]**: `EULA.txt` of RimWorld (last updated April 7, 2022), which is always followed (constitution, Source
  Register).
- **[Readme]**: `Readme.txt` of the same install, the first testing source (constitution, Source Register).
- **[Test]**: what the game logged in this feature's in-game checks (quickstart.md), run with the testing sources on
  2026-11-24.

Imperium is a remake of Royalty and requires only Royalty [Design: glossary line 35], and in later entries it
replaces the base game's Empire [Design: setting.md line 83]. Game content is judged by what the official
expansions contain (constitution, Source Register), so each requirement below is measured against what the official
expansions do, Royalty first, and not against what an ordinary mod may do. Imperium cannot itself be an official
expansion: its package identifier may not contain "Ludeon" [ModUpdating: line 237]. Where the official expansions'
form is open only to Ludeon's own packages, the next source applies (constitution, Principle III). Being measured
against the official expansions does not make Imperium look official: it is presented as community-created content
[EULA: line 78].

## Clarifications

### Session 2026-11-24

Each answer comes from the source named with it; none is game content left to the maintainer (constitution,
Principle IV).

- Q: How is "no errors or warnings from Imperium" checked? → A: In the game's log [Readme: line 21], which the plan
  locates and reads, against the same launch without Imperium as the baseline, since
  Imperium is measured against the official expansions (Sources, above). Imperium passes when its launch adds no
  error or warning line to the baseline, other than the report FR-005 expects while this feature adds no content.
- Q: Which game versions does Imperium support? → A: 1.7 only, as each official expansion lists only `1.7` among its
  supported versions [Data: each expansion's `About/About.xml`; `Version.txt`].
- Q: What happens when Imperium is turned on or off for a save made with a different set of mods? → A: The game shows
  its mods-mismatch warning, as it does for any change in the active set, official expansions included
  [Data: Dialogs_Various.xml line 126, `ModsMismatchWarningText`]. Because this feature adds no content, the save
  then loads with no errors from Imperium [Roadmap: R1].
- Q: What keeps Imperium the same mod across releases? → A: Its package identifier, by which the game and other mods
  refer to it [ModUpdating: line 230]. It is unique, follows the format the game requires and does not contain
  "Ludeon" [ModUpdating: lines 231-237], and it does not change once released. Its exact value belongs to
  `/speckit-plan`.

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Turn Imperium on with Royalty (Priority: P1)

A player who owns Royalty finds Imperium in the game's mod list, where the official expansions are listed too, turns
it on together with Royalty, and starts or loads a game without problems.

**Why this priority**: every later roadmap entry is content inside this mod, so nothing else can be played or tested
until the mod loads [Roadmap: every other entry depends on R1, directly or through another entry].

**Independent Test**: put Imperium in the game's mods, turn on Core, Royalty and Imperium only, restart, and start a new
game; the game loads with no errors from Imperium, as it does with Royalty alone.

**Acceptance Scenarios**:

1. **Given** Imperium is installed, **When** the player opens the mod list, **Then** Imperium is listed by its name.
2. **Given** Core, Royalty and Imperium are active, **When** the game restarts and a new game starts, **Then** it
   loads with no errors or warnings from Imperium.
3. **Given** a game saved with Imperium active, **When** it is loaded again with the same mods, **Then** it loads with
   no errors or warnings from Imperium.

---

### User Story 2 - Royalty is required (Priority: P2)

A player who tries to use Imperium without Royalty is told by the game that Imperium needs Royalty.

**Why this priority**: Imperium is a remake of Royalty and requires it [Design: line 108; glossary line 35]; the
player must not end up in a broken game without it.

**Independent Test**: turn on Imperium with Royalty off; the mod list shows that Imperium requires Royalty.

**Acceptance Scenarios**:

1. **Given** Royalty is not active, **When** the player turns on Imperium, **Then** the mod list shows that Imperium
   requires Royalty, in the way the game shows any missing requirement [Data: Menus_Main.xml line 146,
   `ModUnsatisfiedDependency`].
2. **Given** Royalty is active, **When** the player looks at Imperium in the mod list, **Then** no missing requirement
   is shown.

---

### User Story 3 - No other expansion is required (Priority: P3)

A player who owns only Royalty can use Imperium, and a player who owns more expansions can use it with any of them.

**Why this priority**: the design requires no other expansion, and expects Imperium to run with any other expansion
that is active [Design: lines 108 and 110].

**Independent Test**: load Imperium with Royalty alone, then with every combination of Ideology, Biotech, Anomaly and
Odyssey added; each loads with no errors from Imperium and shows no missing requirement. Then place Imperium directly
after the last official expansion, ahead of an ordinary mod; the mod list shows no load-order warning.

**Acceptance Scenarios**:

1. **Given** only Core and Royalty are active, **When** Imperium is turned on, **Then** no missing requirement is shown
   and the game loads.
2. **Given** any of Ideology, Biotech, Anomaly or Odyssey are also active, **When** the game loads, **Then** Imperium
   loads with no errors, after every active official expansion, and the mod list shows no load-order warning for it
   [Data: Menus_Main.xml line 143, `ModOrderingWarning`].
3. **Given** an ordinary mod is also active, **When** Imperium is placed directly after the last active official
   expansion and ahead of that mod, **Then** the mod list shows no load-order warning and the game loads with no
   errors from Imperium [Data: Menus_Main.xml line 143].

---

### Edge Cases

- Imperium is placed above an official expansion in the load order: the game shows that it must be loaded after that
  expansion, either by refusing the move or by a load-order warning with auto-sort, as it does for any mod out of
  order [Data: Menus_Main.xml lines 95, 139 and 143].
- An ordinary mod builds on Imperium and must load after it: that mod says so with its own `loadAfter`, as any mod
  does for a mod it must follow [ModUpdating: lines 308-309]; Imperium names no ordinary mod (FR-011).
- The game version is not 1.7: the mod list shows that Imperium was not made for that version, as it does for other
  mods [Data: Menus_Main.xml line 147, `ModNotMadeForThisVersion`; ModUpdating: line 253].
- Two copies of Imperium are installed (one local, one from the Workshop): only one of them can be active, as for any
  package that is not Ludeon's [ModUpdating: line 244; Data: Menus_Main.xml line 144, `ModWithSameIdAlreadyActive`].
- Imperium is turned on or off for a save made with a different set of mods: the game shows its mods-mismatch
  warning, as for any change in the active set, and the save loads with no errors from Imperium [Data:
  Dialogs_Various.xml line 126; Roadmap: R1].

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: Imperium MUST be listed in RimWorld 1.7's mod list and load, and MUST support 1.7 only, as each
  official expansion does [Data: `Version.txt`; each expansion's `About/About.xml` lists only `1.7` as its supported
  version].
- **FR-002**: Imperium MUST require Royalty, so that the game shows it as a missing requirement when Royalty is not
  active [Design: line 108; Data: Menus_Main.xml line 146]. No official expansion requires another, so [Data] gives
  no form for a requirement, and the form comes from [ModUpdating: lines 266-268].
- **FR-003**: Imperium MUST NOT require any expansion other than Royalty [Design: line 108].
- **FR-004**: Imperium MUST load after Core and after every official expansion, as each official expansion loads
  after every one that came before it [Data: `About/About.xml` lines 9-12 of Ideology, 9-13 of Biotech, 9-14 of
  Anomaly and 9-15 of Odyssey], and because it adds content to each other active expansion [Design: line 110].
- **FR-005**: With Core, Royalty and Imperium active, starting a new game and loading a saved one MUST produce no
  errors or warnings from Imperium [Design: line 109, complete with Royalty alone], except the one error in which the
  game reports that Imperium loaded no content [Test: quickstart check 1, "Mod Imperium did not load any content"].
  That report states what FR-007 sets for this feature, and the first roadmap entry that adds content removes it.
- **FR-006**: With any combination of the other official expansions also active, FR-005 MUST still hold
  [Design: lines 108 and 110].
- **FR-007**: The mod MUST add no game content in this feature; content belongs to later roadmap entries
  [Roadmap: R1, "Deferred: all content"].
- **FR-008**: Wherever the game shows Imperium, it MUST be presented as community-created content, and never as
  official or made by Ludeon [EULA: lines 57 and 78].
- **FR-009**: The disclaimer the EULA gives MUST be displayed on or reasonably in connection with Imperium
  [EULA: lines 32-34].
- **FR-010**: Imperium MUST have one package identifier that is unique, meets the game's format, does not contain
  "Ludeon", and does not change once released, because the game and other mods refer to it by that identifier
  [ModUpdating: lines 229-237].
- **FR-011**: Imperium MUST be able to load directly after the last active official expansion and ahead of every
  ordinary mod placed after them, the place nearest to the official expansions' own that a mod can take, since
  Imperium is measured against them (Sources, above). Its load order MUST name no package that is not Ludeon's, so
  that nothing puts it behind an ordinary mod. The game's load-order fields each name single packages, and none places
  a mod ahead of every other [Data: each expansion's `About/About.xml`; ModUpdating: lines 300-314], so players are
  told where to place it, as the Harmony mod tells players its own place [Harmony: `README.md`, "Enable it above Core
  and mods that depend on Harmony"].

### Key Entities

- **Imperium**: a remake of Royalty, measured against the official expansions; it holds Mantle and the Empire content
  in later entries [Design: glossary lines 35 and 221; line 109, "Imperium, Mantle included"]. It is identified by
  its package identifier (FR-010).
- **Royalty**: the official expansion Imperium remakes and requires, and the closest one to measure it against
  [Design: line 108; glossary line 35].
- **Other official expansions**: Ideology, Biotech, Anomaly and Odyssey, none of which Imperium requires and all of
  which it loads after [Data: the expansion folders in `Data/` and their `About/About.xml`; Design: line 108].
- **Ordinary mods**: every mod that is not Ludeon's. The Harmony mod is one, and loads before Core by its own
  `loadBefore` [Harmony: `About/About.xml`]; the ordinary mods FR-011 concerns are those placed after the official
  expansions.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: With Core, Royalty and Imperium active, a new game starts and a save loads, and the game's log
  [Readme: line 21] has zero error or warning lines beyond the same launch with Core and Royalty alone, other than
  the no-content report (FR-005).
- **SC-002**: With Royalty off, Imperium shows a missing requirement for Royalty in 100% of attempts, and for no other
  expansion.
- **SC-003**: Across every combination of the four other official expansions added to Core and Royalty, none included
  (16 combinations), every one loads with zero error or warning lines in the log beyond the same combination without
  Imperium, other than the no-content report (FR-005), with Imperium after every active official expansion and no
  load-order warning for it.
- **SC-004**: Nothing the game shows for Imperium states or implies that it is official or made by Ludeon, and the
  EULA's disclaimer is displayed with it.
- **SC-005**: With an ordinary mod active, Imperium placed directly after the last active official expansion and ahead
  of that mod loads with zero error or warning lines beyond the same launch without Imperium, other than the
  no-content report (FR-005), and with no load-order warning, and the place is stated where players read about
  Imperium.

## Assumptions

- The mod's name in the mod list is Imperium, the name the design uses throughout [Design: `docs/imperium.md` title].
- Each official expansion presents itself with a label, a description of what it contains, an icon and preview
  images [Data: ExpansionDefs.xml lines 13-39 for Royalty, and the same parts for each other expansion]. Imperium's
  description and images take the parts of that form a community mod can use, within FR-008 (research.md R-8).
  Because each official description lists only what that expansion contains, and this feature adds no content, they
  are written with the content they describe in later entries [Roadmap: R1, "Deferred: all content"].
- Imperium lists the Harmony mod as a requirement only from the first entry whose code uses Harmony, because a
  requirement is a mod that must be active for Imperium to function [ModUpdating: lines 266-267] and the Harmony mod
  is enabled above the mods that depend on it [Harmony: `README.md`]; this feature adds no code (FR-007). The Harmony
  mod loads before Core [Harmony: `About/About.xml`, `loadBefore` `Ludeon.RimWorld`], so Imperium, which loads after
  Core, needs no load-order entry for it.
- Testing in the game follows the constitution's testing sources: first `Readme.txt` line 58 (the `-quicktest`
  launch option starts the game into a tiny, fast-loading map), then RimBridgeServer with GABS; the setup belongs
  to the plan.
