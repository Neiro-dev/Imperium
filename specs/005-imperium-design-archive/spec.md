# Feature Specification: Imperium design archive

**Feature Branch**: `005-imperium-design-archive`

**Created**: 2026-11-24

**Status**: Draft

**Input**: Parent roadmap: `ROADMAP.md` → entry **R17**. Description: "An archive of Imperium's design, written from the
meaning of the design on the default branch of Neiro-dev/Imperium-old, which now holds Imperium-Knowledge/ and
RimWorld-Imperium/ as they were (Imperium-old PR #291). The old content is right but was written in the wrong form: MUST
rules, ruling cards and session records. The archive writes the meaning behind them as a coherent setting, not as copied
rules. Conflicts are listed as they are, not decided; what the sources cannot settle is marked unverified. The base
game's Empire (hypertech, techno-feudalism, titles, peerage and the like) is not used to fill gaps, and the archive
gives no examples of its own. History is only a reference for concepts; concrete appearance follows the reference
images. Code and implementation are not sources; commit history, other branches, issues and pull requests only
cross-check."

## Why

Agents working on the rebuild have no reliable picture of what Imperium is; later features need one to start from (the
maintainer's decision). Spec Kit advises against making "document the entire existing system" a first feature "unless
that inventory is itself the intended deliverable" (`github/spec-kit`, `docs/how-to/existing-projects.md`, lines 62-64).
Here it is the deliverable.

The design is on Imperium-old's default branch (constitution, Source Register, "Imperium's own design"), at
`b218bdcbaf5a9f6253d747399986bfd30cabc243` (2026-11-24, PR #291). It is spread over three bodies of text: `docs/` at the
root, `Imperium-Knowledge/` and `RimWorld-Imperium/`, which PR #291 merged in unchanged and unreconciled, with
"content that contradicts across the three repositories ... left as it is" (PR #291 description).

## Scope

The archive covers all of the design on that branch, not the Empire alone: the Empire, Mantle and the settlements of
the other cultures it lays out, and every other part the branch designs. The Source Register's topic is Imperium's own
design on that branch, and it retires Imperium-old "once the rebuild covers all of it" (constitution, Source
Register, "Imperium's own design"); Imperium-old's glossary makes Mantle part of Imperium ("The framework layer of
Imperium's code", `docs/glossary.md`, line 221) and city building Imperium's generation of settlements, with kits for
Roman, medieval, industrial and tribal settlements (lines 173 and 184). The maintainer confirmed this scope.

## Clarifications

### Session 2026-11-24

- Q: Does the archive cover only the Empire, or all of the design on Imperium-old's default branch? → A: All of it,
  as Scope states (constitution, Source Register, "Imperium's own design", its retirement sentence; confirmed by the
  maintainer).
- Q: Where a passage states a fact about the base game or an expansion, is it part of the archive's design? → A: No;
  its source is `Data/`. The archive keeps the design point and marks the fact as a claim to check (constitution,
  Source Register, "Game content and the released mod"). Answered from the source, not asked.
- Q: Which name does the archive use where the sources use several for one thing? → A: The term in force in
  Imperium-old's glossary, with the others beside it on first use (`docs/glossary.md`, lines 3-4). Answered from the
  source, not asked.

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Learn what a part of Imperium is, and where the old repository says it (Priority: P1)

An agent starting a later slice of the rebuild, or the maintainer, opens the archive at a subject, such as the Empire,
the core or the Empire's cities, and reads what the design means there, as connected prose. Every statement leads back
to the passage of Imperium-old that says it, so the reader can check it in the source.

**Why this priority**: this is the reason for the archive; without it, each slice has to read the whole old repository
again.

**Independent Test**: take any subject the roadmap names (for example R3, the Empire faction) and read its part of the
archive; every statement names a file and place at the pinned commit, and opening it shows a passage that says the
same.

**Acceptance Scenarios**:

1. **Given** the archive, **When** a reader looks up a subject that the old repository designs, **Then** they find it
   described, with a source pointer for each statement.
2. **Given** a statement in the archive, **When** the reader opens its pointer, **Then** the passage at the pinned
   commit says what the statement says.

---

### User Story 2 - See conflicts and gaps instead of decisions made for the maintainer (Priority: P1)

Where the old repository says two things about one subject, the archive shows both, each with its source, and does not
pick one. Where the meaning cannot be worked out from the sources, the archive marks it unverified and leaves it
unfilled.

**Why this priority**: an archive that settles conflicts or fills gaps silently would put the agent's guesses in place
of the maintainer's design; the maintainer decides these (constitution, Principle IV).

**Independent Test**: for each conflict listed in the archive, open both pointers; they disagree, and the archive states
neither side as the design. For each place marked unverified, no source passage settles it.

**Acceptance Scenarios**:

1. **Given** two passages that disagree, **When** the archive covers that subject, **Then** both are stated side by side
   with their sources, under a conflict marking, and neither is presented as the design.
2. **Given** a subject the sources leave open, **When** the archive reaches it, **Then** it is marked unverified, and
   nothing from the base game's Empire, from history or from the writer's own examples is put in its place.

---

### User Story 3 - Read the design as a setting, not as rules (Priority: P2)

The maintainer reads a part of the archive and finds a coherent account of the world and of how the mod's parts fit,
not a list of MUST rules, ruling cards or session records.

**Why this priority**: the maintainer judges the old content right but its form wrong; the archive is valuable only if
it changes the form without changing the meaning.

**Independent Test**: read any section; it is prose that describes what things are and how they relate, and holds no
requirement keywords, ruling numbers as text, or session narration outside source pointers.

**Acceptance Scenarios**:

1. **Given** a source passage written as a rule ("X MUST be Y"), **When** the archive covers it, **Then** it says what
   the design is (X is Y) and cites the rule as its source.
2. **Given** a ruling card or session record, **When** the archive covers it, **Then** only the design meaning it
   settles appears, and the card or record is the source pointer.

---

### User Story 4 - Know that nothing was skipped (Priority: P3)

A reader can see, for every part of the pinned commit, whether it was read as a source of design meaning and where its
meaning went, or why it is not a source.

**Why this priority**: the archive is relied on only if its coverage is known.

**Independent Test**: pick any file at the pinned commit; the coverage record lists it, or the folder or pattern that
holds it, with its class and, for a design source, the archive sections that use it.

**Acceptance Scenarios**:

1. **Given** any file at the pinned commit, **When** the reader looks it up in the coverage record, **Then** it is
   classed as a design source, a reference image, or not a source (code, implementation, tool, process), with a reason.

---

### Edge Cases

- A source marks one of its own passages as replaced, such as a ruling moved to Imperium-Knowledge's archive of
  superseded rulings (`Imperium-Knowledge/README.md`, line 74): the archive gives the meaning that replaces it and
  names the replaced passage beside it. Where nothing in the sources says which of two passages holds, they are a
  conflict.
- The three bodies of text disagree: none ranks above another unless a source passage says so; the disagreement is
  listed as a conflict.
- A passage mixes design and implementation, such as a design document that names Defs or code: only the design meaning
  is taken; the implementation is not a source.
- A passage refers to the base game's Empire or Royalty: what it says Imperium is or is not is design meaning; the base
  game's own traits are not added beyond what the passage says.
- A passage uses real history, such as Rome: the archive keeps it as the concept the passage draws on and adds no
  historical detail the passage does not give.
- Appearance: where a source describes how something looks, the archive names the reference images that source points
  to; where it points to none, the look is marked unverified.
- An unmerged draft, an issue, a pull request or a commit message says something the default branch does not: it is
  not design (constitution, Principle II; `ROADMAP.md`, lines 13-14), and the archive uses it only to cross-check.
- A passage states a fact about the base game or an official expansion, such as what one of its definitions holds:
  that fact is not Imperium's design, and its source is `Data/` (constitution, Source Register, "Game content and the
  released mod"). The archive gives the design point that rests on it and marks the fact as the old repository's
  claim, to be checked against `Data/`.
- Imperium-old's default branch moves after the pinned commit: the archive stays at the pinned commit and says so.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: The archive MUST describe all of the design on the default branch of Neiro-dev/Imperium-old as that
  branch means it at the pinned commit, across all three bodies of text and the reference images, as Scope states
  (constitution, Source Register, "Imperium's own design").
- **FR-002**: Code and implementation MUST NOT be a source of the archive; commit history, other branches, issues and
  pull requests MUST be used only to cross-check (constitution, Source Register and Principle II).
- **FR-003**: Every statement of the archive MUST name the passage it comes from, as a file at the pinned commit and a
  place in it (constitution, Principle VI).
- **FR-004**: The archive MUST be written as connected prose organized by subject, stating what things are and how they
  relate, not as MUST rules, ruling cards or session records; ruling numbers and dates appear only inside source
  pointers.
- **FR-005**: Where passages conflict, the archive MUST state each side with its source under a conflict marking and
  MUST NOT choose between them.
- **FR-006**: Where the sources do not settle a point the archive reaches, it MUST mark the point unverified and leave it
  unfilled.
- **FR-007**: The archive MUST NOT fill a gap with traits of the base game's Empire, such as hypertech,
  techno-feudalism, titles or peerage, and MUST NOT give examples that no source gives.
- **FR-008**: Real history MUST appear only as the concept a source draws on; concrete appearance MUST be given by
  pointing to the reference images the sources name.
- **FR-009**: Where a source itself marks a passage as replaced, the archive MUST give the replacing meaning and name
  the replaced passage beside it.
- **FR-010**: A coverage record MUST class every file at the pinned commit as a design source, a reference image or not
  a source, with the reason, and MUST name, for each design source, the archive sections that use it.
- **FR-011**: The archive MUST keep the sources' own names for things; where it translates a name, it MUST give the
  original beside it on first use. Where Imperium-old's glossary names the term in force for a thing, the archive MUST
  use it and give the other names the sources use beside it on first use (`docs/glossary.md`, lines 3-4).

### Key Entities

- **Archive section**: the account of one subject of the design, in prose, with source pointers, conflict markings and
  unverified markings.
- **Source pointer**: a file path at the pinned commit and a place in it (lines or heading).
- **Conflict**: two or more passages that say different things about one point, each with its pointer.
- **Unverified point**: a point the archive reaches that no passage settles.
- **Coverage record**: every file or file pattern at the pinned commit, with its class, reason and the sections that use
  it.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Every statement in the archive carries a source pointer, and a review of at least 30 statements picked
  across all sections finds each pointer's passage saying what the statement says.
- **SC-002**: Every file at the pinned commit is accounted for in the coverage record; none is left out.
- **SC-003**: Outside quotations in source pointers, the archive body holds no requirement keywords (MUST, SHOULD, 必须)
  and no ruling-card or session-record layout.
- **SC-004**: Every conflict found while reading the sources appears in the archive with each side's pointer, and the
  archive resolves none of them.
- **SC-005**: For each slice in `ROADMAP.md` (R1 to R16), the archive has a section that covers the design its intent
  names, or marks it unverified.
- **SC-006**: No trait of the base game's Empire appears in the archive unless a cited passage states it of Imperium.

## Assumptions

- The pinned commit is `b218bdcbaf5a9f6253d747399986bfd30cabc243`, the head of Imperium-old's `main` on 2026-11-24
  after PR #291. Its three bodies of text have the same standing as sources.
- The archive is English, as this repository's files are and as Imperium-old's own design documents in `docs/` are
  (Imperium-old `CONTRIBUTING.md`, lines 121-124); FR-011 keeps the Chinese names.
- The archive is a reading aid, not a source: the constitution's source for Imperium's design stays Imperium-old, and
  later slices cite its passages, which the archive names.
- Mantle's design is part of Imperium's design: Imperium-old's glossary calls Mantle "the framework layer of
  Imperium's code" (`docs/glossary.md`, line 221).
- Process and tooling of the old repositories (how design sessions, dispatch, reviews and tools worked) is not
  Imperium's design; it is read and classed in the coverage record, and only design meaning found inside it is taken.
