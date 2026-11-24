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

Every chunk was read in full on 2026-11-24, every line of every file, by one subagent on Sonnet. The last column counts
the statements, conflicts and open points its notes hold. Pointers in the notes were checked to resolve at the pinned
commit; those that named a file by a short name (C06, C16, C19, C22, C28) were written out in full.

| Chunk | Files | Folders | Notes | Statements / conflicts / open points |
|---|---|---|---|---|
| C01 | 26 | `.claude/rules`; `.github`; (root); `Imperium-Knowledge/.claude/agents`; `Imperium-Knowledge/.github/ISSUE_TEMPLATE`; `Imperium-Knowledge/.github`; `Imperium-Knowledge` | [C01.md](research/C01.md) | 313 / 4 / 15 |
| C02 | 1 | `Imperium-Knowledge` | [C02.md](research/C02.md) | 119 / 3 / 13 |
| C03 | 1 | `Imperium-Knowledge/09_地图生成与CBF技术.md lines 1-735` | [C03.md](research/C03.md) | 246 / 10 / 13 |
| C04 | 1 | `Imperium-Knowledge/09_地图生成与CBF技术.md lines 736-978` | [C04.md](research/C04.md) | 180 / 2 / 15 |
| C05 | 4 | `Imperium-Knowledge` | [C05.md](research/C05.md) | 77 / 2 / 15 |
| C06 | 1 | `Imperium-Knowledge/14_来源同步与权威.md lines 1-249` | [C06.md](research/C06.md) | 36 / 3 / 5 |
| C07 | 1 | `Imperium-Knowledge/14_来源同步与权威.md lines 250-394` | [C07.md](research/C07.md) | 13 / 1 / 2 |
| C08 | 23 | `Imperium-Knowledge`; `Imperium-Knowledge/designs/ICF`; `Imperium-Knowledge/designs`; `Imperium-Knowledge/designs/city-plans/blocks/roman/modules`; `Imperium-Knowledge/designs/city-plans/constantinople/data`; `Imperium-Knowledge/designs/city-plans/constantinople`; `Imperium-Knowledge/designs/city-plans/handcity/2026-11-03/住宅`; `Imperium-Knowledge/designs/city-plans/handcity/2026-11-03/整城v3`; `Imperium-Knowledge/designs/city-plans/handcity/2026-11-03`; `Imperium-Knowledge/designs/city-plans/history/塞萨洛尼基/data`; `Imperium-Knowledge/designs/city-plans/history/塞萨洛尼基`; `Imperium-Knowledge/designs/city-plans/history`; `Imperium-Knowledge/designs/city-plans/kit` | [C08.md](research/C08.md) | 188 / 5 / 12 |
| C09 | 29 | `Imperium-Knowledge/designs/city-plans/kit`; `Imperium-Knowledge/designs/city-plans/rome/data`; `Imperium-Knowledge/designs/city-plans/templates`; `Imperium-Knowledge/designs/city-plans`; `Imperium-Knowledge/designs/city-plans/量城`; `Imperium-Knowledge/designs/instructions` | [C09.md](research/C09.md) | 195 / 5 / 13 |
| C10 | 13 | `Imperium-Knowledge/designs/instructions`; `Imperium-Knowledge/designs/medieval-cards`; `Imperium-Knowledge/designs/reviews`; `Imperium-Knowledge/designs/roman-cards` | [C10.md](research/C10.md) | 167 / 8 / 9 |
| C11 | 5 | `Imperium-Knowledge/designs/roman-cards`; `Imperium-Knowledge/designs/tools`; `Imperium-Knowledge/designs/tools/city` | [C11.md](research/C11.md) | 83 / 2 / 7 |
| C12 | 11 | `Imperium-Knowledge/designs/tools/city`; `Imperium-Knowledge/designs/tools/city/说明` | [C12.md](research/C12.md) | 68 / 4 / 9 |
| C13 | 26 | `Imperium-Knowledge/designs/tools/city/说明`; `Imperium-Knowledge/designs/tools/plugins/imperium`; `Imperium-Knowledge/designs/tools/plugins/imperium/agents`; `Imperium-Knowledge/designs/tools/prompts`; `Imperium-Knowledge/designs/tools` | [C13.md](research/C13.md) | 85 / 5 / 4 |
| C14 | 23 | `Imperium-Knowledge/designs/tools`; `Imperium-Knowledge/designs/做法史` | [C14.md](research/C14.md) | 85 / 2 / 12 |
| C15 | 18 | `Imperium-Knowledge/designs/做法史`; `Imperium-Knowledge/designs`; `Imperium-Knowledge/designs/待用` | [C15.md](research/C15.md) | 226 / 8 / 14 |
| C16 | 12 | `Imperium-Knowledge/designs/待用`; `Imperium-Knowledge/designs/整理`; `Imperium-Knowledge/designs/整理/回报` | [C16.md](research/C16.md) | 149 / 7 / 13 |
| C17 | 14 | `Imperium-Knowledge/designs/整理`; `Imperium-Knowledge/designs/派活` | [C17.md](research/C17.md) | 60 / 2 / 10 |
| C18 | 37 | `Imperium-Knowledge/designs/派活`; `Imperium-Knowledge/designs/研究`; `Imperium-Knowledge/designs/研究/原版数据`; `Imperium-Knowledge/designs/研究/参照模组`; `Imperium-Knowledge/designs/研究/城` | [C18.md](research/C18.md) | 135 / 6 / 13 |
| C19 | 17 | `Imperium-Knowledge/designs/研究/城`; `Imperium-Knowledge/designs/研究/城/纪元资料`; `Imperium-Knowledge/designs/研究`; `Imperium-Knowledge/designs/研究/帝国`; `Imperium-Knowledge/designs/研究/机械` | [C19.md](research/C19.md) | 116 / 7 / 13 |
| C20 | 17 | `Imperium-Knowledge/designs/研究/机械`; `Imperium-Knowledge/designs/研究/美术`; `Imperium-Knowledge/designs`; `Imperium-Knowledge/designs/美术`; `Imperium-Knowledge/designs/聚落设计图`; `Imperium-Knowledge/synced`; `Imperium-Knowledge/现行/城` | [C20.md](research/C20.md) | 250 / 9 / 15 |
| C21 | 20 | `Imperium-Knowledge/现行/城`; `Imperium-Knowledge/现行/机械体`; `Imperium-Knowledge/现行/流程` | [C21.md](research/C21.md) | 265 / 1 / 11 |
| C22 | 32 | `Imperium-Knowledge/现行`; `Imperium-Knowledge/目录` | [C22.md](research/C22.md) | 114 / 1 / 10 |
| C23 | 27 | `Imperium-Knowledge/裁定归档`; (root); `RimWorld-Imperium/.claude/agents`; `RimWorld-Imperium`; `RimWorld-Imperium/docs/claude`; `RimWorld-Imperium/docs`; `RimWorld-Imperium/tools/TestHarness17/Cli`; `RimWorld-Imperium/tools/TestHarness17`; `RimWorld-Imperium/tools/sync`; `docs` | [C23.md](research/C23.md) | 377 / 6 / 11 |
| C24 | 4 | `docs` | [C24.md](research/C24.md) | 69 / 1 / 5 |
| C25 | 31 | `Imperium-Knowledge/designs/回报` | [C25.md](research/C25.md) | 41 / 3 / 10 |
| C26 | 24 | `Imperium-Knowledge/designs/回报`; `Imperium-Knowledge/designs/回报/tidy文档`; `Imperium-Knowledge/designs/回报/参照只取继承`; `Imperium-Knowledge/designs/回报/基准改外缘`; `Imperium-Knowledge/designs/回报/基准改门`; `Imperium-Knowledge/designs/回报/复刻-Anno117真实尺度` | [C26.md](research/C26.md) | 51 / 3 / 13 |
| C27 | 6 | `Imperium-Knowledge/designs/回报` | [C27.md](research/C27.md) | 34 / 3 / 7 |
| C28 | 15 | `Imperium-Knowledge/designs/回报`; `Imperium-Knowledge/designs/回报/斜卡试做`; `Imperium-Knowledge/designs/回报/斜街错开摆卡`; `Imperium-Knowledge/designs/回报/纪元城分区`; `Imperium-Knowledge/designs/回报/纪元城放法`; `Imperium-Knowledge/designs/回报/纪元城读房型`; `Imperium-Knowledge/designs/回报/规矩落地与流程工具` | [C28.md](research/C28.md) | 22 / 0 / 6 |
| C29 | 14 | `Imperium-Knowledge/designs/回报/规矩落地与流程工具`; `Imperium-Knowledge/designs/回报`; `Imperium-Knowledge/designs/回报/试做-城区清障`; `Imperium-Knowledge/designs/回报/试做-外形顺路临水` | [C29.md](research/C29.md) | 11 / 1 / 6 |
| C30 | 7 | `Imperium-Knowledge/designs/回报` | [C30.md](research/C30.md) | 37 / 1 / 10 |
| C31 | 29 | `Imperium-Knowledge/designs/回报` | [C31.md](research/C31.md) | 38 / 3 / 9 |
| C32 | 31 | `Imperium-Knowledge/designs/回报`; `Imperium-Knowledge/designs/回报/配套表` | [C32.md](research/C32.md) | 53 / 6 / 11 |
