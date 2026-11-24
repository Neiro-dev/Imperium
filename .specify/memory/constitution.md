# Imperium Constitution

## Core Principles

### I. Sources by Topic, Then by Layer

Every answer MUST come from the Source Register, first by topic, then by layer:

- When a topic fits the question, the answer MUST come from the source the register gives for
  that topic.
- When no topic fits, the agent MUST decide which of the three layers (Claude, GitHub or
  RimWorld) the question belongs to, and the answer MUST come from that layer's sources. A layer's
  sources are only those the register already lists in that layer's rows, used in the order the
  register lists them: row by row, and within a row in that row's own order. Each source keeps the
  limits its row sets: a source that only cross-checks stays a cross-check, `EULA.txt` is always
  followed, and a source given for one matter, such as choosealicense.com for the license, answers
  only that matter. The maintainer's broad direction is not one of a layer's sources; only
  Principle IV says when he is asked.
- A question that fits no topic but fits a layer MUST NOT be treated as having no source, and MUST
  NOT be left unanswered or left as it is for want of a topic.

Nothing outside the Source Register is a source, and belonging to a layer does not make one.

### II. Other Sources Only Cross-Check

Sources other than the question's own sources (Principle I: its topic's source or, when no topic
fits, its layer's sources) MUST be used only to cross-check.

### III. Sources in Order

Where a topic lists several sources in order, and where a question is answered from its layer's
sources (Principle I), the next source MUST be used only when the previous one gives no form.

### IV. Asking the Maintainer

The agent MUST NOT ask the maintainer about anything other than game content. For game content,
the maintainer is asked only when no source in its chain, or for a question that fits no topic no
source of its layer (Principle I), has the answer, and judges only its broad direction.

### V. When a Source Gives No Form

When the topic's source names a default, the agent MUST use it. When the source offers options
without a default, the agent MUST use the option the source uses in its own repository or
examples. For a question that fits no topic, the same holds for each of its layer's sources in
order (Principle I). When the sources give neither, the agent MUST NOT act on the question, except
for game content, where Principle IV applies. For a question that fits no topic, this applies only
once every source of its layer gives neither, or when no layer fits the question either. Rules,
files, and practices that no source supports MUST be removed.

### VI. Every Conclusion Names Its Source

Every conclusion, including a judgment, MUST name its source and MUST be reached from that
source. It MUST also show the path that reached the source, in this order, and stop at the step
where a source gave the answer:

1. The topic: which topic fits, or that none does.
2. The layer, when no topic fits: which layer, and which of its sources were tried, in order.
3. Principle V or, for game content, Principle IV, when no source gives a form.

The path MUST NOT skip a step.

## Source Register

Three layers: Claude, GitHub and RimWorld. Each topic and its source:

| Layer | Topic | Source |
|-------|-------|--------|
| Claude | How the AI works: sessions, threads, project settings, CLAUDE.md, skills, subagents | The Anthropic documentation for the product in use: code.claude.com (Claude Code and projects), platform.claude.com (the API), support.claude.com (claude.ai). anthropic.com/engineering only cross-checks |
| GitHub | Development workflow | Spec Kit (`github/spec-kit`) |
| GitHub | Repository files and settings, branches, pull requests, and commit messages | GitHub Docs; choosealicense.com for the license |
| RimWorld | Imperium's own design | While the rebuild runs: the meaning of the design on the default branch of `Neiro-dev/Imperium-old`, not its code or implementation. Imperium-old is retired once the rebuild covers all of it. Design beyond it: the maintainer's broad direction (Principle IV) |
| RimWorld | Game content and the released mod | Base game and official expansions in `Data/` → `ModUpdating.txt` → Harmony (`pardeike/HarmonyRimWorld`). Game content is judged by what the official expansions contain. `EULA.txt` is always followed |
| RimWorld | Testing outside the game | The base game and official expansions in `Data/`. Testing outside the game comes before testing in the game and does not replace it: testing in the game is the final check |
| RimWorld | Testing in the game | In order: `Readme.txt` (the `-quicktest` launch option), then RimBridgeServer (`pardeike/RimBridgeServer`) with GABS (`pardeike/GABS`) |

## Governance

Amendments go through a pull request, which is merged once it is approved.

Versioning follows semantic versioning:

- MAJOR: Backward incompatible governance/principle removals or redefinitions.
- MINOR: New principle/section added or materially expanded guidance.
- PATCH: Clarifications, wording, typo fixes, non-semantic refinements.

Compliance is reviewed at each plan's Constitution Check and at pull request review.

**Version**: 2.2.0 | **Ratified**: 2026-11-23 | **Last Amended**: 2026-11-24
