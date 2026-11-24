---

description: "Task list for the Imperium design archive"
---

# Tasks: Imperium design archive

**Input**: Design documents from `specs/005-imperium-design-archive/`

**Prerequisites**: plan.md, spec.md, research.md and its notes in `research/`, data-model.md, contracts/

**Tests**: The spec asks for no test code. The checks are the commands and reviews in quickstart.md.

**Organization**: Tasks are grouped by user story. User Story 1 and User Story 2 are both P1 and are built together:
each section is written with its conflicts and unverified points in it (contracts/archive-format.md).

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (US1 to US4)

## Path Conventions

- Paths are relative to the repository root. `research/` is `specs/005-imperium-design-archive/research/`.

---

## Phase 1: Setup

- [X] T001 Fill the reading log in `specs/005-imperium-design-archive/research.md` from the 32 notes files: files,
  contents, notes file and status of each chunk (research.md R-3)
- [X] T002 Create `docs/design-archive/` with `README.md` holding what the archive is, the pinned commit, how to open a
  pointer and the three markings (contracts/archive-format.md, README.md; research.md R-6, R-7)

---

## Phase 2: Foundational (blocks every section)

- [X] T003 Gather the statements of all 32 notes by subject into one extract per section, keeping each statement and
  its pointers unchanged; split `cities` into the topics of the sections below by having each statement assigned to one
  topic (research.md R-5; data-model.md, Reading notes)
- [X] T004 Gather the conflicts and open points of all 32 notes into the same extracts, by subject (data-model.md,
  Reading notes)

**Checkpoint**: one extract per section; every statement of the notes is in exactly one extract.

---

## Phase 3: User Stories 1 and 2 - The design, with its conflicts and gaps (Priority: P1) MVP

**Goal**: a reader finds what each part of the design is, with a pointer for every statement, and sees conflicts and
unsettled points as they are.

**Independent Test**: quickstart.md checks 1, 4 and 6 for the sections written, and check 7.

### City building first (R13 waits for it)

- [X] T005 [P] [US1] Write `docs/design-archive/cities.md`: what city building is, its scale and references, the
  Roman city's eras and the order in which a city is made
- [X] T006 [P] [US1] Write `docs/design-archive/cities-siting.md`: terrain, landforms and where cities stand
- [X] T007 [P] [US1] Write `docs/design-archive/cities-walls.md`: walls, towers, gates, water gates and moats, and what
  they are made of
- [X] T008 [P] [US1] Write `docs/design-archive/cities-inside.md`: the core, the palace district, streets, housing,
  groups, buildings and their materials
- [X] T009 [P] [US1] Write `docs/design-archive/cities-outside.md`: the land outside the walls, and rivers and water in
  the city
- [X] T010 [P] [US1] Write `docs/design-archive/cities-forms.md`: templates, kits, skeletons, spec cards and the city
  grammar, as design and not as file formats
- [X] T011 [US2] Find the conflicts between the six city sections and record each in both places
  (contracts/archive-format.md)

### The rest of the design

- [ ] T012 [P] [US1] Write `docs/design-archive/cultures.md`: settlements of the cultures other than the Empire
- [ ] T013 [P] [US1] Write `docs/design-archive/mantle.md`: the framework layer and the world it generates
- [ ] T014 [P] [US1] Write `docs/design-archive/mechanoids.md`
- [ ] T015 [P] [US1] Write `docs/design-archive/empire.md` and `docs/design-archive/military.md`
- [ ] T016 [P] [US1] Write `docs/design-archive/imperium.md` and `docs/design-archive/world.md`: what Imperium is, its
  parts, requirements, playstyles, expansions, rhythm and end; the world it is set in
- [ ] T017 [P] [US1] Write `docs/design-archive/core.md`, `docs/design-archive/relations.md` and
  `docs/design-archive/orders.md`
- [ ] T018 [P] [US1] Write `docs/design-archive/ruins-and-technology.md`
- [ ] T019 [P] [US1] Write `docs/design-archive/administration.md`, `docs/design-archive/industry.md` and
  `docs/design-archive/water.md`
- [ ] T020 [P] [US1] Write `docs/design-archive/art.md`, with the reference images the sources name
- [ ] T021 [P] [US1] Write `docs/design-archive/text.md` and `docs/design-archive/terms.md`
- [ ] T022 [US2] Find the conflicts between sections written by different tasks and record each in both places
- [ ] T023 [US2] Write `docs/design-archive/open-points.md` from every Conflict and Unverified alert in the sections
  (data-model.md, Open-points index)
- [ ] T024 [US1] Run quickstart.md checks 1, 4, 5 and 6 and correct what they find

**Checkpoint**: every subject of the notes has its section; every pointer resolves; 30 sampled statements match their
passages.

---

## Phase 4: User Story 3 - A setting, not rules (Priority: P2)

**Goal**: the sections read as connected prose.

**Independent Test**: quickstart.md check 3; reading any section shows no rule list, ruling card or session record.

- [ ] T025 [US3] Run quickstart.md checks 3 and 8 on `docs/design-archive/` and rewrite every passage they find
- [ ] T026 [US3] Read each section once through for rule lists and session narration and rewrite them as prose

---

## Phase 5: User Story 4 - Nothing skipped (Priority: P3)

**Goal**: every file at the pinned commit is accounted for.

**Independent Test**: quickstart.md check 2.

- [ ] T027 [US4] Write `docs/design-archive/coverage.md` from the path classes of research.md R-2, the Files tables of
  the 32 notes and their images and data tables, with the sections that use each file (data-model.md, Coverage record)
- [ ] T028 [US4] Run quickstart.md check 2 and add what it finds missing

---

## Phase 6: Polish

- [ ] T029 Finish `docs/design-archive/README.md` with the list of sections
- [ ] T030 Run quickstart.md check 7 and record which section covers each roadmap slice in the pull request
- [ ] T031 Set R17 to done in `ROADMAP.md`

---

## Dependencies & Execution Order

- T001 and T002 have no dependencies. T003 and T004 need the 32 notes and block every section.
- T005 to T010 run in parallel; T011 needs them. They are delivered first, in a pull request of their own, since R13
  waits for the design of the Empire's walls and gates (`ROADMAP.md`).
- T012 to T021 run in parallel after T003 and T004; T022 and T023 need all sections; T024 needs T023.
- Phases 4 and 5 need Phase 3; T027 needs only the notes and can run beside Phase 3.

## Implementation Strategy

1. Merge the spec, plan, research and tasks (this pull request).
2. Phases 1 and 2, then the city sections T005 to T011, in a pull request; R13 can use them once merged.
3. The other sections, the open points, the style pass, the coverage record and the polish, in a final pull request.

## Who does each task

T003 assigns statements to topics: a subagent on Haiku per notes file, since sorting statements into a fixed list is a
simple task (code.claude.com/docs/en/costs.md, line 278). T005 to T021 are each written by a subagent on Opus, since
joining statements from 32 notes, finding conflicts between them and keeping every pointer is multi-step reasoning
(same line; research.md R-5). The checks and the review in T024 to T030 are done in this session.
