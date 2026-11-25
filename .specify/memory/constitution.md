# Imperium Constitution

## Core Principles

### I. One Source per Topic

Every answer MUST come from the source the Source Register gives for its topic. When no topic fits, the
answer MUST come from the sources the Source Register lists in the question's layer, in the order of their
rows; the maintainer comes last, under Principle IV. What this constitution sets itself is answered by its
text. Nothing outside this constitution and its Source Register is a source.

**Rationale:** A closed list of sources keeps every answer traceable to something anyone can open and
check, instead of to what an AI or an earlier record happened to say.

### II. Other Sources Only Cross-Check

Sources other than those Principle I gives MUST be used only to cross-check an answer reached from a source
it gives.

**Rationale:** Other material may be mistaken or out of date. Used to test answers, it still helps without
deciding anything.

### III. Sources in Order

Where a topic, or a layer under Principle I, lists several sources in order, the next one MUST be used only
when the previous one gives no form.

### IV. Asking the Maintainer

The agent MUST NOT ask the maintainer anything except the broad direction of game content, and that only
where no other source Principle I gives has the answer. Reporting to him, including what a step waits on or
what blocks it, and asking him for an approval or an action that only he can give or take, are not asking
him for an answer.

**Rationale:** The direction of the game is what no source can give. Everything else has a source, and
putting it to him puts his answer where a source belongs.

### V. When a Source Gives No Form

When a source Principle I gives names a default, the agent MUST use it. When it offers options without a
default, the agent MUST use the option the source uses in its own repository or examples. When the sources
Principle I gives offer neither, or it gives none, the agent MUST NOT act on the question, except for game
content, where Principle IV applies. Rules, files and practices that no source supports MUST be removed.

**Rationale:** Choosing where the sources have not chosen is inventing, and an invented rule outlives the
moment it was made for.

### VI. Every Conclusion Names Its Source

Every conclusion, including a judgment, MUST name its source and MUST be reached from that source.

### VII. Imperium's Design Holds by Its Reason

Imperium's own design is game content. A part of it holds while the reason it was set holds against what
the base game and official expansions contain and against the rest of the design; where it is recorded, or
who proposed it, does not make it hold. Where a part is found not to hold, the agent MUST name what defeats
its reason and MUST NOT build on it.

**Rationale:** Imperium is measured against the official expansions. Judging a design by its reason, not
by its record, keeps a mistake from being carried forward because it was written down once.

## Source Register

Three layers: Claude, GitHub and RimWorld. Each topic and its source:

| Layer | Topic | Source |
|-------|-------|--------|
| Claude | How the AI works: sessions, threads, project settings, CLAUDE.md, skills, subagents, hooks | The Anthropic documentation for the product in use: code.claude.com (Claude Code and projects), platform.claude.com (the API), support.claude.com (claude.ai). anthropic.com/engineering only cross-checks |
| GitHub | Development workflow | Spec Kit (`github/spec-kit`) |
| GitHub | Repository files and settings, branches, pull requests, and commit messages | GitHub Docs; choosealicense.com for the license |
| RimWorld | Game content and the released mod | Base game and official expansions in `Data/` → `ModUpdating.txt` → Harmony (`pardeike/HarmonyRimWorld`). Game content is judged by what the official expansions contain. `EULA.txt` is always followed |
| RimWorld | Testing outside the game | The base game and official expansions in `Data/`. Testing outside the game comes before testing in the game and does not replace it: testing in the game is the final check |
| RimWorld | Testing in the game | In order: `Readme.txt` (the `-quicktest` launch option), then RimBridgeServer (`pardeike/RimBridgeServer`) with GABS (`pardeike/GABS`) |
| RimWorld | A title of the Anno series, where game content takes it as a reference | That title's own game files → what its developer has published about that title |

## Development Workflow

Feature artifacts stay in `specs/` as living specs: a feature's `spec.md`, before and after the feature is
delivered, is the agreed intent its feature is built and checked against. When that intent changes, the
artifacts are revised in place, `spec.md` first, and the plan and tasks follow from it.

## Governance

- **Compliance.** Compliance is reviewed at each plan's Constitution Check and at pull request review.
  Work that breaks a principle is changed until it complies; Complexity Tracking does not justify a
  violation of a principle.
- **Amendments.** Amendments go through a pull request that gives the reason for each change and what it
  changes for work already done, which is merged once it is approved.
- **Versioning.** Semantic versioning. MAJOR: backward incompatible governance or principle removals or
  redefinitions. MINOR: a new principle or section, or materially expanded guidance. PATCH: clarifications,
  wording, typo fixes, non-semantic refinements.

**Version**: 3.0.0 | **Ratified**: 2026-11-23 | **Last Amended**: 2026-11-25
