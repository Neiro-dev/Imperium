# Feature Specification: Starting ruins as a decayed town

**Feature Branch**: `claude/project-thread-zww76k`

**Created**: 2026-11-24

**Status**: Draft

**Input**: User description: "Generate the starting ruins as a decayed town, the city-building slice of the design in Neiro-dev/Imperium-old's default branch (docs/core.md "The starting ruins", docs/glossary.md "City building and generation"). When the colony reaches the starting ruins' site, Mantle generates the site's map as a decayed town on the model of a small or middle-sized town of the old empire, different in each game, and players see only a decayed town, not the old empire. Mantle is Imperium's framework layer and city building is its generation of settlements on the map, from their terrain and layout to their walls and buildings. Out of scope for this change: the quest that leads to the ruins, the core and its uses, the ruins disappearing once the core is taken, the envoy, playstyles, other settlement kinds (faction settlements, the medieval, industrial and tribal kits, Roman military posts) and Odyssey's ruins that stay. Compatibility boundaries: Imperium requires Royalty and no other expansion and must be complete with Royalty alone; Mantle runs whether Empire content is on or off; the released mod follows Core and the official DLCs, then ModUpdating.txt, then Harmony. Game content not settled by Imperium-old's default-branch design (its unmerged design-draft PRs are not design) is marked for the maintainer to decide, never chosen by us."

## Sources

Game content in this spec comes only from the maintainer (constitution, Source Register). The maintainer's
design for it is Neiro-dev/Imperium-old's default branch, which settles these points:

- `docs/core.md`, The starting ruins: the starting ruins are near the colony; Mantle generates them, different in each
  game, on the model of a small or middle-sized town of the old empire; players see only a decayed town, not the old
  empire.
- `docs/glossary.md`, City building and generation: city building is Imperium's generation of settlements on the map,
  from their terrain and layout to their walls and buildings. The section's other terms (such as skeleton, template,
  kit, block, district, main street, civic core) name things whose design is not on the default branch.
- `docs/ruins-and-technology.md`, The ruins: the ruins lean toward Old Rome.
- `docs/imperium.md`, Expansions: Imperium requires Royalty and no other expansion, and is complete, Mantle included,
  with Royalty alone.

Everything else about what the town contains is open and marked below for the maintainer.

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Arrive at a decayed town (Priority: P1)

The colony arrives at the site of the starting ruins and finds a map that holds a decayed town: the remains of a small
or middle-sized town, laid out as a town and worn down by time.

**Why this priority**: it is the whole of this change. The quest, the core and the Empire's answer all build on a
place the colony can reach and that reads as a decayed town.

**Independent Test**: open the site of the starting ruins in a game with Imperium and Royalty active; a map
generates without errors and shows the remains of a town.

**Acceptance Scenarios**:

1. **Given** a game with Imperium and Royalty active, **When** the site of the starting ruins is entered, **Then** its
   map generates and holds a decayed town.
2. **Given** the site's map has generated, **When** the player looks over it, **Then** what they see is the remains of
   a town, not an intact settlement and not a scatter of unrelated ruins.

---

### User Story 2 - A different town in each game (Priority: P2)

Each new game gives a different decayed town, so the starting ruins are not the same place every time.

**Why this priority**: the design requires it, and it keeps the first place the colony explores fresh across games,
but a single town already gives a playable site.

**Independent Test**: generate the site in several new games; no two towns are the same.

**Acceptance Scenarios**:

1. **Given** two new games, **When** the site of the starting ruins is generated in each, **Then** the two towns
   differ.
2. **Given** one game, **When** it is saved and loaded after the site has generated, **Then** the town is the one that
   was generated, unchanged by the load.

---

### User Story 3 - Nothing reveals the old empire (Priority: P3)

The player meets the town as a decayed town. Nothing they can see or read on the site names or reveals the old empire.

**Why this priority**: the design requires it, and it keeps the old empire for later play, but it constrains what the
town shows rather than adding something to it.

**Independent Test**: inspect every name, label and description that the site shows; none names the old empire.

**Acceptance Scenarios**:

1. **Given** the site's map has generated, **When** the player inspects anything on it, **Then** no name, label or
   description names or reveals the old empire.

---

### Edge Cases

- The site's world tile has terrain that leaves little room for a town, such as mountains or water over much of the
  map: the site still generates a town that fits on the map, or the site is not placed there.
- Only Royalty is active besides Core: the town generates complete, with nothing missing.
- Biotech, Ideology, Anomaly or Odyssey are also active: the town still generates, and nothing from them breaks it.
- The game is saved and loaded on the site: the town is unchanged.
- Another mod that changes map generation is active: the town still generates.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: Mantle MUST generate the map of the starting ruins' site as a decayed town.
- **FR-002**: The town MUST be on the model of a small or middle-sized town of the old empire, and MUST lean toward
  Old Rome.
- **FR-003**: The town MUST have these parts: [NEEDS CLARIFICATION: which parts a small or middle-sized town of the old
  empire has at the starting ruins, such as walls and gates, a main street, a square or civic core, blocks of houses,
  public buildings; the default branch names these terms but does not say which a town has]
- **FR-004**: The town's size MUST be [NEEDS CLARIFICATION: whether each game picks small or middle-sized, or one of
  them always, and how large each is on the map]
- **FR-005**: Besides its buildings, the site MUST hold [NEEDS CLARIFICATION: what the site holds besides the remains
  of the town, such as guards, enemies, items or nothing, apart from the core, which a later change adds]
- **FR-006**: The town MUST differ from one game to the next.
- **FR-007**: Once generated, the town MUST stay as it is across saving and loading.
- **FR-008**: No name, label or description that players see on the site MUST name or reveal the old empire.
- **FR-009**: The town MUST generate completely with Core and Royalty alone, and MUST still generate when any other
  official expansion is also active.
- **FR-010**: The released mod MUST take its form from Core and the official expansions first, then from
  `ModUpdating.txt`, then from Harmony, each only where the one before gives no form.
- **FR-011**: The town MUST fit the site's terrain, and MUST NOT leave buildings over water or inside mountains in a
  way that cannot be entered.

### Key Entities

- **Starting ruins**: the place near the colony that holds the core; in this change, the site whose map is a decayed
  town.
- **Decayed town**: the remains of a small or middle-sized town of the old empire, laid out as a town and worn down by
  time; what players see of the starting ruins.
- **Old empire**: the empire before the silence, whose towns the starting ruins are modeled on and which players do not
  see on the site.
- **Mantle**: Imperium's framework layer, which generates the town.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: In 20 new games, the site of the starting ruins generates a decayed town every time, with no errors in
  the game's log.
- **SC-002**: Across those 20 games, no two towns are the same.
- **SC-003**: A tester shown the generated map identifies it as the remains of a town in every one of those games.
- **SC-004**: Inspecting everything on the site turns up no text that names the old empire.
- **SC-005**: The same checks pass with Core and Royalty alone and with every official expansion active.
- **SC-006**: Generating the site takes no longer than the base game takes to generate a site map of the same size.

## Assumptions

- The quest that leads to the ruins, the core, the ruins disappearing once the core is taken, the envoy and the
  playstyles are later changes. Until the quest exists, testers reach the site through a development-only way of
  opening it, which players never see.
- Other settlement kinds that city building covers (faction settlements, the medieval, industrial and tribal kits,
  Roman military posts) and Odyssey's ruins that stay are later changes.
- Imperium-old's unmerged design-draft pull requests are not design and are not used here.
- The repository holds no mod yet, so this change also makes the mod's first loadable form, as far as the town needs.
- Open game content beyond the three markers above, for the maintainer to decide at `/speckit-clarify`, not chosen
  here:
  - How the town is made different in each game, for example whether it follows designed site templates that are
    mirrored, turned or stretched, or is laid out anew each time.
  - How decayed the town is: how much of its walls, roofs and floors stands.
  - Whether its look changes with the region, as the default branch's arid and temperate looks do for imperial cities.
  - Which terrain the site prefers or needs, such as a river or a defensible height.
