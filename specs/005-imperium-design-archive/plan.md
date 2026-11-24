# Implementation Plan: Imperium design archive

**Branch**: `005-imperium-design-archive` | **Date**: 2026-11-24 | **Spec**: [spec.md](spec.md)

**Input**: Feature specification from `specs/005-imperium-design-archive/spec.md`

## Summary

Write an account of all of the design on Imperium-old's default branch at `b218bdc`, as connected English prose by
subject, each statement with a pointer to the passage that says it, conflicts listed and unsettled points marked
unverified, with a record of every file at that commit (spec FR-001 to FR-011). The sources hold about 600 Markdown
files and 8.5 MB of text, mostly Chinese, more than one context holds, so Phase 0 reads them in 32 chunks, one subagent
each, which write reading notes to a fixed contract; the archive is then written subject by subject from the notes and
checked against the sources (research.md R-3 to R-5).

## Technical Context

**Language/Version**: Markdown, in English, keeping the sources' Chinese names (spec, Assumptions; FR-011)

**Primary Dependencies**: Imperium-old at `b218bdcbaf5a9f6253d747399986bfd30cabc243`; Claude Code subagents for the
reading and the writing (research.md R-3, R-5)

**Storage**: files in this repository: the archive in `docs/design-archive/`, the reading notes in
`specs/005-imperium-design-archive/research/` (research.md R-1, R-3)

**Testing**: the checks in [quickstart.md](quickstart.md): every pointer resolves at the pinned commit, every file at
the commit is in the coverage record, no requirement keyword in the body, and a review of at least 30 statements against
their passages (spec SC-001 to SC-004)

**Target Platform**: GitHub, read in the repository and by agents in later slices

**Project Type**: documentation

**Performance Goals**: none

**Constraints**: nothing the sources do not say (spec FR-006, FR-007); code and implementation are not sources (FR-002)

**Scale/Scope**: 2,779 files at the pinned commit; 518 text files read in full, in 32 chunks of at most 300 KB
(research.md R-2, R-3)

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

| Principle | How this plan meets it | Result |
|---|---|---|
| I. One source per topic | The archive's content comes from Imperium-old's default branch, the source of "Imperium's own design". The method comes from the topic each belongs to: the workflow from Spec Kit, the repository files from GitHub Docs, the subagents from code.claude.com (research.md R-1 to R-5) | Pass |
| II. Other sources only cross-check | Commit history, other branches, issues and pull requests of Imperium-old are not read for content; facts about the base game are flagged for `Data/` and not taken as design (contracts/reading-notes.md rules 4 to 6) | Pass |
| III. Sources in order | No topic here lists sources in order except game content, which the archive does not settle; it marks such facts for `Data/` | Pass |
| IV. Asking the maintainer | Nothing is asked: the scope was confirmed by the maintainer, and conflicts and open points are listed for him to decide, not asked one by one (spec, Clarifications) | Pass |
| V. When a source gives no form | Each choice below takes the source's default or its own example (research.md); nothing is added that no source supports. The archive adds no design of its own (FR-006, FR-007) | Pass |
| VI. Every conclusion names its source | Every statement of the archive and the notes carries a pointer (FR-003; contracts/reading-notes.md rule 3); every decision in research.md names its source | Pass |

Re-check after Phase 1: data-model.md, the two contracts and quickstart.md add no source and no rule beyond the spec;
the gate still passes.

## Project Structure

### Documentation (this feature)

```text
specs/005-imperium-design-archive/
├── spec.md
├── plan.md                   # this file
├── research.md               # Phase 0: decisions and the reading log
├── research/                 # Phase 0: the reading notes, C01.md to C32.md
├── data-model.md             # Phase 1
├── quickstart.md             # Phase 1: how the archive is checked
├── contracts/
│   ├── reading-notes.md      # the form of the reading notes
│   └── archive-format.md     # the form of the archive
├── checklists/requirements.md
└── tasks.md                  # Phase 2 (/speckit-tasks)
```

### The archive (repository root)

```text
docs/design-archive/
├── README.md                 # what the archive is, the pinned commit, how to read pointers and markings, the sections
├── <subject>.md              # one file per subject, such as cities.md, empire.md, mechanoids.md
├── open-points.md            # every conflict and unverified point, linked to its section
└── coverage.md               # every file at the pinned commit, its class and the sections that use it
```

**Structure Decision**: the archive is a set of design documents, and Imperium-old keeps its design documents in
`docs/` (Imperium-old `README.md`, Repository layout, row `docs/`); it gets a folder of its own there so that later
design documents of this repository are not mixed with it (research.md R-1).

## Complexity Tracking

No violations.
