# Research: Imperium design archive

Phase 0 of [plan.md](plan.md). The decisions come first, each with its source; the reading log follows. The reading
itself is in [research/](research/), one notes file per chunk.

## R-1 Where the archive lives

**Decision**: `docs/design-archive/`, one Markdown file per subject, with `README.md`, `open-points.md` and
`coverage.md`.

**Source**: Imperium-old keeps its design documents in `docs/` (Imperium-old `README.md`, line 84). The archive is a
set of design documents, so it goes under `docs/`, in a folder of its own so that later design documents of this
repository are not mixed with it.

## R-2 What is read and what is classed by its path

**Decision**: every file at the pinned commit is classed (spec FR-010). Text files (`.md`, `.txt`) are read in full,
518 of them, with `.github/deprecated-terms.json`, which names replaced terms. The rest are classed by their path
without being read for design:

| Class | Paths | Why |
|---|---|---|
| code | `Source/`, `Tests/`, `RimWorld-Imperium/Source/`, `RimWorld-Imperium/tools/` except its text files, `RimWorld-Imperium/docs/claude/代码地图.md` (a map of the code), the knowledge base tools' library and test fixtures (`Imperium-Knowledge/designs/tools/ledgerlib/`, `.../tools/fixtures/`), and every `.cs`, `.py`, `.ps1`, `.psm1`, `.sh`, `.csproj`, `.slnx`, `.props`, `.patch`, `.toml`, `.dll` | Code is not a source (constitution, Source Register, "Imperium's own design") |
| implementation | `About/`, and `RimWorld-Imperium/` `About/`, `Assemblies/`, `ArtSource/`, `CityPlans/`, `Compatibility/`, `Defs/`, `Landforms/`, `Languages/`, `LoadFolders.xml`, `Patches/`, `Textures/`, `ThirdParty/` | Implementation is not a source (same row) |
| configuration | `.claude/settings.json`, `.claude/skills/`, `.specify/`, `.github/` except its Markdown and `deprecated-terms.json`, `.editorconfig`, `.gitattributes`, `.gitignore`, `global.json`, and the knowledge base's `.vale/`, lint, hook and manifest files | Repository setup, not design |
| base game | `RimWorld-Imperium/upstream/` | A copy of base-game files (`RimWorld-Imperium/upstream/README.md`, lines 3-10); the source for game content is `Data/` (constitution, Source Register, "Game content and the released mod") |

Images (418) and data files (326) are classed from what the texts say of them (contracts/reading-notes.md, "Images and
data files named"), and the rest by their folder in `coverage.md`.

**Source**: the constitution's Source Register for code and implementation; Imperium-Knowledge's own description of its
folders (`Imperium-Knowledge/README.md`, lines 72-75 and 61) for which of its files are working material, reports and
tools.

## R-3 How the reading is split

**Decision**: the 518 text files are packed in path order into 32 chunks of at most 300 KB; the three files larger than
that, `08_机械体设计.md`, `09_地图生成与CBF技术.md` and `14_来源同步与权威.md`, are split by line ranges. The Code
reports in `Imperium-Knowledge/designs/回报/` form chunks of their own (C25 to C32). Each chunk is read in full by one
subagent on Sonnet, which writes its notes to the contract in [contracts/reading-notes.md](contracts/reading-notes.md).
One chunk is read first as a pilot, and its notes are checked against the sources before the rest are started.

**Source**: "Delegate verbose operations to subagents ... so the verbose output stays in the subagent's context while
only a summary returns" (code.claude.com/docs/en/costs.md, lines 355-357); "Isolate high-volume operations" and "Run
parallel research" (sub-agents.md, lines 1035-1051). The model: "Sonnet handles most coding tasks well and costs less
than Opus. Reserve Opus for complex architectural decisions or multi-step reasoning ... For simple subagent tasks,
specify `model: haiku`" (costs.md, line 278). Reading a chunk and restating what it says is neither a simple task nor
multi-step reasoning across the design, so the readers run on Sonnet. 300 KB keeps a chunk of mostly Chinese text, the
reading tool's line numbers and the notes inside one subagent's context.

## R-4 The form of the notes

**Decision**: [contracts/reading-notes.md](contracts/reading-notes.md). Statements say what the design is, each with
its line pointer; rules, ruling cards and session records are restated as the meaning they settle; facts about the base
game, history, looks and replacements are flagged; conflicts and open points are listed, not decided. The subjects are
the sources' own division of the design: the files of Imperium-old's `docs/` and the chapters of Imperium-Knowledge
(`01` to `16`, `现行/城`, `现行/机械体`).

**Source**: spec FR-003 to FR-009 and the maintainer's direction recorded in its Input.

## R-5 How the archive is written from the notes

**Decision**: one subject at a time. For each subject, the statements of every chunk under that subject, with the
conflicts and open points that touch it, are gathered and written as connected prose; a statement keeps its pointers,
and statements from different chunks that disagree become a conflict. Each subject is written by one subagent on Opus,
since joining statements from 32 notes files, finding the conflicts between them and keeping every pointer is
multi-step reasoning (costs.md, line 278), and each file it writes is checked as quickstart.md describes. `cities`
comes first, since R13 waits for the design of the Empire's walls and gates (`ROADMAP.md`, R13).

**Source**: costs.md, line 278; sub-agents.md, lines 1043-1051; spec-of-specs, The roadmap pass, step 4 (prerequisites
first).

## R-6 The form of a source pointer

**Decision**: the path relative to Imperium-old's root and the lines, `` (`Imperium-Knowledge/现行/城/罗马城-墙.md`
L12-18) ``. The archive's README says how to open one at the pinned commit:
`https://github.com/Neiro-dev/Imperium-old/blob/b218bdcbaf5a9f6253d747399986bfd30cabc243/<path>?plain=1#L12-L18`.

**Source**: GitHub Docs, "Getting permanent links to files" (a commit ID in the URL "will permanently link to the exact
version of the file in that commit") and "Creating a permanent link to a code snippet" (for a Markdown file, append
`?plain=1#L` and the line numbers).

## R-7 How conflicts and unverified points are marked

**Decision**: with GitHub's alert syntax, so they stand out where they are read: `> [!WARNING]` headed **Conflict**,
giving each side with its pointer; `> [!NOTE]` headed **Unverified**, saying what the sources leave open; `> [!NOTE]`
headed **Base game**, for a fact to check against `Data/`. `open-points.md` lists every one with a link to its place.

**Source**: GitHub Docs, "Basic writing and formatting syntax", Alerts.

## R-8 Language

**Decision**: English, with the sources' names kept beside their English renderings on first use, and the glossary's
terms in force (spec FR-011, Clarifications).

**Source**: Imperium-old `CONTRIBUTING.md`, lines 121-124; `docs/glossary.md`, lines 3-4.

## Reading log

| Chunk | Files | Contents | Notes | Status |
|---|---|---|---|---|
