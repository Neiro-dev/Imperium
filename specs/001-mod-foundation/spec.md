# Feature Specification: Mod foundation

**Feature Branch**: `claude/project-thread-zww76k`

**Created**: 2026-11-24

**Status**: Draft

**Input**: Parent roadmap: `ROADMAP.md` → entry **R1**. Imperium loads in RimWorld as a mod that requires Royalty and does not require any other expansion, and is complete with Royalty alone (Imperium-old main, docs/imperium.md lines 108-109). Scope: a loadable mod and its expansion requirements only; all content (Mantle, the Empire faction, starting ruins and the rest) is deferred to later roadmap entries. Game content and the released mod's form follow the base game and official expansions in Data/, then ModUpdating.txt, then Harmony.

## Sources

- Imperium's own design (constitution, Source Register): Imperium-old `main` (20a052b), `docs/imperium.md`, Expansions:
  Imperium requires Royalty and no other expansion, and with Royalty alone it is complete, Mantle included.
- The released mod (constitution, Source Register): the base game and official expansions in `Data/` of RimWorld
  1.7.5014 (`Version.txt`: 1.7.5014 rev1195), then `ModUpdating.txt`, then Harmony.

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Turn Imperium on with Royalty (Priority: P1)

A player who owns Royalty finds Imperium in the game's mod list, turns it on together with Royalty, and starts or
loads a game without problems.

**Why this priority**: every later roadmap entry is content inside this mod, so nothing else can be played or tested
until the mod loads.

**Independent Test**: put Imperium in the game's mods, turn on Core, Royalty and Imperium only, restart, and start a new
game; the game loads with no errors from Imperium.

**Acceptance Scenarios**:

1. **Given** Imperium is installed, **When** the player opens the mod list, **Then** Imperium is listed by its name.
2. **Given** Core, Royalty and Imperium are active, **When** the game restarts and a new game starts, **Then** it
   loads with no errors or warnings from Imperium.
3. **Given** a game saved with Imperium active, **When** it is loaded again with the same mods, **Then** it loads with
   no errors or warnings from Imperium.

---

### User Story 2 - Royalty is required (Priority: P2)

A player who tries to use Imperium without Royalty is told by the game that Imperium needs Royalty.

**Why this priority**: the design requires Royalty; the player must not end up in a broken game without it.

**Independent Test**: turn on Imperium with Royalty off; the mod list shows that Imperium requires Royalty.

**Acceptance Scenarios**:

1. **Given** Royalty is not active, **When** the player turns on Imperium, **Then** the mod list shows that Imperium
   requires Royalty, in the way the game shows any missing requirement.
2. **Given** Royalty is active, **When** the player looks at Imperium in the mod list, **Then** no missing requirement
   is shown.

---

### User Story 3 - No other expansion is required (Priority: P3)

A player who owns only Royalty can use Imperium, and a player who owns more expansions can use it with any of them.

**Why this priority**: the design requires no other expansion; it limits what the mod may depend on.

**Independent Test**: load Imperium with Royalty alone, then with each of Ideology, Biotech, Anomaly and Odyssey added,
then with all of them; each loads with no errors from Imperium and shows no missing requirement.

**Acceptance Scenarios**:

1. **Given** only Core and Royalty are active, **When** Imperium is turned on, **Then** no missing requirement is shown
   and the game loads.
2. **Given** any of Ideology, Biotech, Anomaly or Odyssey are also active, **When** the game loads, **Then** Imperium
   loads with no errors and is listed in a valid load order.

---

### Edge Cases

- Imperium is placed above Royalty in the load order: the game shows the load order problem and how to fix it, as it
  does for other mods.
- The game version is not 1.7: the mod list shows that Imperium was not made for that version, as it does for other
  mods.
- Two copies of Imperium are installed (one local, one from the Workshop): the game loads only one, as it does for
  any mod.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: Imperium MUST be a mod that RimWorld 1.7 lists in its mod list and loads.
- **FR-002**: Imperium MUST require Royalty, so that the game shows it as a missing requirement when Royalty is not
  active.
- **FR-003**: Imperium MUST NOT require any expansion other than Royalty.
- **FR-004**: Imperium MUST load after Core and Royalty.
- **FR-005**: With Core, Royalty and Imperium active, starting a new game and loading a saved one MUST produce no
  errors or warnings from Imperium.
- **FR-006**: With any combination of the other official expansions also active, FR-005 MUST still hold.
- **FR-007**: The mod MUST take its form from the base game and official expansions in `Data/` first, then from
  `ModUpdating.txt`, then from Harmony, each only where the one before gives no form.
- **FR-008**: The mod MUST add no game content in this feature; content belongs to later roadmap entries.

### Key Entities

- **Imperium**: the mod; it holds Mantle and the Empire content in later entries.
- **Royalty**: the official expansion Imperium requires.
- **Other official expansions**: Ideology, Biotech, Anomaly and Odyssey, none of which Imperium requires.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: With Core, Royalty and Imperium active, a new game starts and a save loads with zero errors or warnings
  from Imperium in the game's log.
- **SC-002**: With Royalty off, Imperium shows a missing requirement for Royalty in 100% of attempts, and for no other
  expansion.
- **SC-003**: Across Royalty alone, Royalty with each other expansion, and all expansions together (6 combinations),
  every one loads with zero errors from Imperium.

## Assumptions

- The mod's name in the mod list is Imperium, the name the design uses throughout.
- Text shown in the mod list beyond the name, such as a description or preview image, takes the form the official
  expansions use; settling it belongs to `/speckit-plan`, from `Data/` then `ModUpdating.txt`.
- Whether Harmony is needed is an implementation question for `/speckit-plan`; this feature adds no code that needs
  it unless the plan finds otherwise.
- Testing in the game follows the constitution's testing sources (`Readme.txt` `-quicktest`, then RimBridgeServer with
  GABS); the setup belongs to the plan.
