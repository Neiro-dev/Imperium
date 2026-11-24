# Imperium Constitution

## Core Principles

### I. One Fixed Source per Topic

Every answer MUST come from the fixed source for its topic in the Source Register. Each topic
has one source.

### II. Other Sources Only Cross-Check

Sources other than the topic's fixed source MUST be used only to cross-check.

### III. Released Mod Source Order

For the released mod, sources are used in this order:

1. Core and the official DLCs.
2. `ModUpdating.txt`.
3. Harmony.

The next level MUST be used only when the previous one gives no form.

### IV. The Maintainer Settles Open Game-Content Questions

When no source settles a game-content question, the agent MUST ask the maintainer and MUST act
only after the maintainer decides.

### V. The Project Logic Settles Everything Else

The project logic is this constitution and the fixed sources in its Source Register. Every
development question other than game content MUST be settled from the project logic, not by
asking the maintainer. Rules, files, and practices that the project logic does not support MUST
be removed.

### VI. Every Conclusion Names Its Source

Every conclusion, including a judgment, MUST name its source and MUST be reached from that
source. When the source allows the agent to judge, the agent MUST judge without asking.

### VII. The Maintainer's Words Are Not Recorded

The maintainer's own words MUST NOT be saved or quoted in any file, list, memory, or message to
another session. Only a cleaned-up, unambiguous statement of their meaning MAY be written.

## Source Register

Each topic and its one fixed source:

| Topic | Fixed source |
|-------|--------------|
| Game content | The maintainer (recorded decisions: see Game Content Records) |
| The released mod | Core and the official DLCs, then `ModUpdating.txt`, then Harmony (Principle III) |
| Development process | Spec Kit |
| The agent and the files it reads | Claude's official documentation |
| Repository | GitHub Docs |
| Commit messages | Conventional Commits 1.0.0 |

## Game Content Records

The maintainer's recorded game-content decisions are the design on the default branch of
`Neiro-dev/Imperium-old`.

- That design supersedes `Neiro-dev/Imperium-Knowledge` and `Neiro-dev/RimWorld-Imperium` (the
  old repositories). The old repositories MUST be used only to see how something was implemented
  before.
- Old-repository content on a topic that Imperium-old deleted is void.
- Old-repository content on a topic that Imperium-old never addressed is a gap: it is neither
  void nor decided, and the maintainer settles it (Principle IV).
- Lists derived from these repositories MUST NOT decide game content.
- Imperium-old's unmerged design-draft pull requests are undecided. They MUST NOT be treated as
  its design, and MUST be handled only when a feature needs them, through the development
  process.

## Governance

Amendments go through a pull request, which is merged once it is approved.

Versioning follows semantic versioning:

- MAJOR: Backward incompatible governance/principle removals or redefinitions.
- MINOR: New principle/section added or materially expanded guidance.
- PATCH: Clarifications, wording, typo fixes, non-semantic refinements.

Compliance is reviewed at each plan's Constitution Check and at pull request review.

**Version**: 2.0.0 | **Ratified**: 2026-11-23 | **Last Amended**: 2026-11-24
