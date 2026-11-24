---

description: "Task list for Mantle as a mod of its own (roadmap R14)"
---

# Tasks: Mantle as a mod of its own

**Input**: Design documents from `/specs/003-mantle-mod/`

**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: The spec asks for no test code. The checks outside the game run first, in the cloud (quickstart.md, Checks
outside the game); each story's Independent Test is a check in the game, listed in quickstart.md, run on the
maintainer's computer (quickstart.md, Prerequisites), which is the final check.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- Paths are relative to the repository root, which holds the two mod folders `Imperium/` and `Mantle/` and the
  repository's own files (plan.md, Structure Decision; contracts/repository-layout.md).
- `RimWorld\` is `D:\Steam\steamapps\common\RimWorld` on the maintainer's computer (research.md R-9).

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: The repository's new layout, which every story uses

- [ ] T001 Move `About/` to `Imperium/About/` and `README.md` to `Imperium/README.md` with `git mv`, both unchanged
  (data-model.md `Repository layout.Imperium/About/About.xml`, `Repository layout.Imperium/README.md`; research.md
  R-1)
- [ ] T002 [P] Copy `LICENSE` to `Imperium/LICENSE` and `Mantle/LICENSE` (data-model.md
  `Repository layout.Imperium/LICENSE`, `Repository layout.Mantle/LICENSE`; research.md R-3)
- [ ] T003 Write the repository's `README.md`: what the repository holds, the two mod folders and that each goes into
  the game's `Mods` folder by its own folder, and the EULA's disclaimer (data-model.md `Repository layout.README.md`;
  research.md R-3)

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Mantle's metadata and the test install, which every story's checks need

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [ ] T004 Create `Mantle/About/About.xml` (data-model.md `Repository layout.Mantle/About/About.xml`) with the byte
  order mark and declaration of the official files and one `ModMetaData` element holding data-model.md `Mantle's metadata.name`, `Mantle's metadata.packageId`,
  `Mantle's metadata.author` and `Mantle's metadata.supportedVersions`, in that order (research.md R-4, R-5)
- [ ] T005 [P] Write `Mantle/README.md` with the EULA's disclaimer (data-model.md `Repository layout.Mantle/README.md`;
  research.md R-8)
- [ ] T006 Run quickstart.md, Checks outside the game, 1, 3 and 5, for T001 to T005
- [ ] T007 On the maintainer's computer, set up the test install as quickstart.md, Prerequisites, gives: move the
  clone from `RimWorld\Mods\Imperium` to `RimWorld\Imperium` and check out the commit under test, change the import
  in `RimWorld\CLAUDE.md` to `@Imperium/.specify/memory/constitution.md`, and copy the clone's `Imperium\` and
  `Mantle\` to `RimWorld\Mods\Imperium` and `RimWorld\Mods\Mantle` (research.md R-9)

**Checkpoint**: Foundation ready - user story implementation can now begin

---

## Phase 3: User Story 1 - Turn Mantle on with the base game alone (Priority: P1) 🎯 MVP

**Goal**: Mantle is listed by its name, apart from Imperium, and loads with Core alone, for a new game and a saved one,
with no missing requirement and no errors or warnings from it (spec US1, FR-001 to FR-003, FR-005).

**Independent Test**: quickstart.md, Checks in the game, 2 and 3.

### Implementation for User Story 1

- [ ] T008 [US1] Check that `Mantle/About/About.xml` holds no field data-model.md lists as left out in R14, so that it
  requires nothing (data-model.md, Mantle's metadata, fields left out; spec FR-003), and that `Mantle/` holds no
  content folder (`ModUpdating.txt` lines 96-151; spec FR-007)
- [ ] T009 [US1] On the maintainer's computer, run quickstart.md, Checks in the game, 2 and 3, against their baselines

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - Mantle with the official expansions and other mods (Priority: P2)

**Goal**: Mantle loads after every active official expansion with any combination of them, and can sit directly after
them, ahead of the mods that depend on it and every ordinary mod (spec US2, FR-004, FR-006, FR-011).

**Independent Test**: quickstart.md, Checks in the game, 4, 5 and 8.

### Implementation for User Story 2

- [ ] T010 [US2] Add data-model.md `Mantle's metadata.forceLoadAfter` to `Mantle/About/About.xml` (research.md R-7)
- [ ] T011 [US2] Add to `Mantle/README.md`, above the disclaimer, the sentence research.md R-7 gives for Mantle's place
  in the mod list (spec FR-011)
- [ ] T012 [US2] Run quickstart.md, Checks outside the game, 2 and 4, and copy the changed `Mantle\` to
  `RimWorld\Mods\Mantle` again
- [ ] T013 [US2] On the maintainer's computer, run quickstart.md, Checks in the game, 4 (all 32 combinations), 5 and 8

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Each mod from its own folder (Priority: P3)

**Goal**: Each mod loads from its own folder, Imperium as R1 set it, and both together (spec US3, FR-012 to FR-016).

**Independent Test**: quickstart.md, Checks in the game, 1, 9 and 10.

### Implementation for User Story 3

- [ ] T014 [US3] On the maintainer's computer, run quickstart.md, Checks in the game, 1, 9 and 10

**Checkpoint**: All user stories should now be independently functional

---

## Phase 6: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [ ] T015 On the maintainer's computer, run quickstart.md, Checks in the game, 6 (a save made with a different set of
  mods) and 7 (community content)
- [ ] T016 [P] Note in `specs/001-mod-foundation/research.md`, R-1 and R-10, that R14 moves Imperium's mod folder to
  `Imperium/` and the clone out of `Mods` (research.md R-1, Effect on R1)
- [ ] T017 Set R14's status to `done` in `ROADMAP.md` once T001 to T016 pass (Spec Kit `docs/how-to/spec-of-specs.md`
  v1.4.3, section Specifying each sub-feature, step 4)

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: T001, then T003; T002 alongside
- **Foundational (Phase 2)**: after Phase 1; T004, then T006; T005 alongside T004; T007 after T006 - BLOCKS all user
  stories' checks in the game
- **User Stories (Phase 3+)**: all depend on Phase 2
  - US2 edits `Mantle/About/About.xml` and `Mantle/README.md` after US1's checks, so the stories run in priority
    order (P1 → P2 → P3)
- **Polish (Final Phase)**: T015 depends on T009's saved game; T017 depends on every other task

### User Story Dependencies

- **User Story 1 (P1)**: after Phase 2; no dependency on other stories
- **User Story 2 (P2)**: after Phase 2; its checks need T010, because they look for Mantle after every expansion
- **User Story 3 (P3)**: after Phase 2; check 10 places Mantle before and after Imperium, so it runs after T010 has
  placed Mantle after the expansions

### Within Each User Story

- Edit the files, check them outside the game, copy the changed mod folder into `RimWorld\Mods`, then check in the
  game
- Story complete before moving to next priority

### Parallel Opportunities

- T002 and T005 write files no other task in their phase writes
- T016 edits only R1's research and can run alongside any check in the game

---

## Parallel Example: Setup and Foundational

```bash
# Files that no other task in the phase writes:
Task: "T002 Copy LICENSE to Imperium/LICENSE and Mantle/LICENSE"
Task: "T005 Write Mantle/README.md with the EULA's disclaimer"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup and Phase 2: Foundational
2. Complete Phase 3: User Story 1
3. **STOP and VALIDATE**: Test User Story 1 independently (quickstart.md, Checks in the game, 2 and 3)

### Incremental Delivery

1. Setup → the two mod folders and the repository's README
2. Foundational → Mantle's identity and version, and the test install
3. User Story 1 → Mantle with the base game alone (MVP)
4. User Story 2 → load order, all 32 combinations, the place ahead of ordinary mods
5. User Story 3 → Imperium from its own folder, and both mods together
6. Polish → saves with a different mod set, community presentation, R1's note, roadmap status

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- The file edits (T001 to T005, T010, T011, T016) and the checks outside the game run in the cloud; every check in the
  game waits for the maintainer's computer
- The spec's edge cases for a game version other than 1.7 and for two installed copies are met by T004's
  `supportedVersions` and `packageId`; neither can be produced on the test install, which runs only 1.7 and has no
  Workshop copy of Mantle
- R13's paths follow contracts/repository-layout.md once this feature is merged (spec, Assumptions)
- Commit after each task or logical group
