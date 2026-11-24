---

description: "Task list for the constitution enforced by hooks"
---

# Tasks: The constitution enforced by hooks

**Input**: Design documents from `/specs/004-constitution-hooks/`

**Prerequisites**: plan.md, spec.md, research.md, data-model.md, contracts/

**Tests**: The spec asks for no test code. The checks are the runs in quickstart.md: in the cloud first, then a thread
on the maintainer's computer, which is the final check.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2)

## Path Conventions

- Paths are relative to the repository root.

---

## Phase 1: Setup

- [X] T001 Create `.claude/settings.json` with an empty `hooks` object (contracts/hooks-settings.md; research R-1)

---

## Phase 2: User Story 1 - A message to the maintainer that breaks the constitution does not reach him (P1) MVP

**Goal**: a `PreToolUse` agent hook judges each message or question to the maintainer against the constitution.

**Independent Test**: quickstart.md checks 1 and 3.

- [X] T002 [US1] Add `hooks.PreToolUse` to `.claude/settings.json`: matcher
  `mcp__.*__(post_message|request_decision)|^AskUserQuestion$` (research R-5) and one `agent` handler whose prompt
  holds `$ARGUMENTS`, points to `.specify/memory/constitution.md` at the repository root and to `transcript_path`,
  judges `tool_input`, and asks for the answer in data-model.md's form, with no rule of the constitution in it
  (research R-4, R-6, R-7)
- [X] T003 [US1] Run quickstart.md checks 1 and 3

---

## Phase 3: User Story 2 - A final answer that breaks the constitution is sent back for correction (P2)

**Goal**: a `Stop` agent hook judges Claude's final response the same way.

**Independent Test**: quickstart.md check 2.

- [X] T004 [US2] Add `hooks.Stop` to `.claude/settings.json`: no matcher, one `agent` handler like T002's that judges
  `last_assistant_message` and passes a response with no answer, conclusion or question (research R-3, R-7)
- [X] T005 [US2] Run quickstart.md check 2

---

## Phase 4: Polish

- [X] T006 Run quickstart.md check 4 (SC-004)
- [ ] T007 Final check: quickstart.md check 5, in a thread on the maintainer's computer, after the maintainer's steps
  in quickstart.md

## Dependencies

- T001 before T002 and T004; T002 before T003; T004 before T005; T003 and T005 before T006; the merge and the
  maintainer's steps before T007.
