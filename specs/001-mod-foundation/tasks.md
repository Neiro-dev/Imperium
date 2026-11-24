---

description: "Task list for the mod foundation (roadmap R1)"
---

# Tasks: Mod foundation

**Input**: Design documents from `/specs/001-mod-foundation/`

**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: The spec asks for no test code. Each story's Independent Test is a check in the game, listed in
quickstart.md, and the story phases include running it. In-game checks run on the maintainer's computer
(quickstart.md, Prerequisites); the cloud runs only the checks in quickstart.md, Checks in the cloud.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- The repository root is the mod's folder (plan.md, Structure Decision; research.md R-1). R1's only new file is
  `About/About.xml`.

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

No setup tasks: the mod's folder is the repository root, which exists, and R1 adds no build, code or tooling
(research.md R-1, R-9).

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [X] T001 Create `About/About.xml` with the XML declaration of the official `About.xml` files and one `ModMetaData`
  element holding data-model.md `Mod metadata.name`, `Mod metadata.author`, `Mod metadata.packageId` and
  `Mod metadata.supportedVersions` (research.md R-2 to R-5)
- [X] T002 Check `About/About.xml` in the cloud: well-formed XML, and the identifier meets data-model.md
  `Mod metadata.packageId` (quickstart.md, Checks in the cloud, 1 and 2)

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Turn Imperium on with Royalty (Priority: P1) 🎯 MVP

**Goal**: Imperium is listed by its name and loads after Core and Royalty, for a new game and a saved one, with no
errors or warnings from it (spec US1, FR-001, FR-004, FR-005).

**Independent Test**: quickstart.md, Checks in the game, 1 to 3.

### Implementation for User Story 1

- [X] T003 [US1] Add data-model.md `Mod metadata.forceLoadAfter` to `About/About.xml` (research.md R-6)
- [X] T004 [US1] On the maintainer's computer, check that the game honors `forceLoadAfter` from Imperium
  (quickstart.md, Checks in the game, 5); if it does not, replace it in `About/About.xml` with `loadAfter` holding the
  same identifiers, as research.md R-6 gives, and repeat
- [X] T005 [US1] On the maintainer's computer, run quickstart.md, Checks in the game, 1 to 3, against their
  baselines, with `About/About.xml` as left by T004

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - Royalty is required (Priority: P2)

**Goal**: With Royalty off, the game shows that Imperium requires Royalty (spec US2, FR-002).

**Independent Test**: quickstart.md, Checks in the game, 4.

### Implementation for User Story 2

- [X] T006 [US2] Add data-model.md `Mod metadata.modDependencies` to `About/About.xml`, one entry holding
  data-model.md `Royalty dependency.packageId`, `Royalty dependency.displayName`,
  `Royalty dependency.steamWorkshopUrl` and `Royalty dependency.downloadUrl` (research.md R-7)
- [X] T007 [US2] Repeat T002 for the changed `About/About.xml`
- [X] T008 [US2] On the maintainer's computer, run quickstart.md, Checks in the game, 4

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - No other expansion is required (Priority: P3)

**Goal**: Imperium requires nothing but Royalty and loads with any combination of the other official expansions,
after every active one, and can sit directly after them, ahead of every ordinary mod placed after them (spec US3,
FR-003, FR-004, FR-006, FR-011).

**Independent Test**: quickstart.md, Checks in the game, 6, 7 and 10.

### Implementation for User Story 3

- [X] T009 [US3] Check that `About/About.xml` holds no field data-model.md lists as left out in R1, so that Royalty
  is its only requirement (data-model.md, Mod metadata, fields left out; spec FR-003), and that the mod's folder
  holds none of the content folders `Defs`, `Patches`, `Languages`, `Textures`, `Sounds`, `Assemblies`
  (`ModUpdating.txt` lines 96-139), so that R1 adds no content (spec FR-007)
- [X] T010 [US3] On the maintainer's computer, run quickstart.md, Checks in the game, 6 (all 16 combinations) and 7
- [X] T011 [US3] Add to `README.md` the sentence research.md R-6 (Among ordinary mods) gives for Imperium's place in
  the mod list, in the form of the Harmony mod's `README.md` (spec FR-011)
- [X] T012 [US3] Check in the cloud that no load-order field in `About/About.xml` names a package that is not Ludeon's
  (data-model.md `Mod metadata.forceLoadAfter`; spec FR-011) and that `README.md` states Imperium's place
  (quickstart.md, Checks in the cloud, 3)
- [X] T013 [US3] On the maintainer's computer, run quickstart.md, Checks in the game, 10

**Checkpoint**: All user stories should now be independently functional

---

## Phase 6: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [X] T014 On the maintainer's computer, run quickstart.md, Checks in the game, 8 (a save made with a different set
  of mods)
- [X] T015 [P] Check in the cloud that nothing in `About/About.xml` names Ludeon as maker or adds an `ExpansionDef`,
  and that `README.md` holds the EULA's disclaimer (spec FR-008, FR-009; research.md R-8)
- [X] T016 On the maintainer's computer, run quickstart.md, Checks in the game, 9
- [X] T017 Set R1's status to `done` in `ROADMAP.md` once T001 to T016 pass (Spec Kit `docs/how-to/spec-of-specs.md`
  v1.4.3, section Specifying each sub-feature, step 4)

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: none
- **Foundational (Phase 2)**: T001, then T002 - BLOCKS all user stories
- **User Stories (Phase 3+)**: all depend on Phase 2
  - They edit the same file, `About/About.xml`, so their implementation tasks run one after another in priority
    order (P1 → P2 → P3)
- **Polish (Final Phase)**: T014 depends on T005's saved game; T017 depends on every other task

### User Story Dependencies

- **User Story 1 (P1)**: after Phase 2; no dependency on other stories
- **User Story 2 (P2)**: after Phase 2; its check (T008) needs Imperium to load, so it runs after T004 settles the
  load-order field
- **User Story 3 (P3)**: after Phase 2; its checks (T010, T013) need T003, T004 and T006 in place, because they look
  for Imperium after every expansion and no missing requirement; T012 and T013 follow T011

### Within Each User Story

- Edit `About/About.xml`, check it in the cloud, then check it in the game
- Story complete before moving to next priority

### Parallel Opportunities

- T015 only reads `About/About.xml` and `README.md` in the cloud, so it can run alongside any in-game check
- All other tasks edit or test the one file and run in order

---

## Parallel Example: User Story 1

```bash
# User Story 1 has one file and runs in order; T015 can run beside its in-game checks:
Task: "T005 Run quickstart.md, Checks in the game, 1 to 3"
Task: "T015 Check About/About.xml and README.md in the cloud"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 2: Foundational
2. Complete Phase 3: User Story 1
3. **STOP and VALIDATE**: Test User Story 1 independently (quickstart.md 1 to 3 and 5)

### Incremental Delivery

1. Foundational → `About/About.xml` with identity and version
2. User Story 1 → load order, checked in the game (MVP)
3. User Story 2 → the Royalty requirement
4. User Story 3 → all 16 combinations, and the place ahead of ordinary mods
5. Polish → saves with a different mod set, community presentation, roadmap status

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- The file edits (T001, T003, T006, T011) can all be written in the cloud; every in-game check waits for the
  maintainer's computer

- The spec's edge cases for a game version other than 1.7 and for two installed copies are met by T001's
  `supportedVersions` and `packageId`; neither can be produced on the test install, which runs only 1.7 and has no
  Workshop copy of Imperium
- Commit after each task or logical group
