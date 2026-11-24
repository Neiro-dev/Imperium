# Imperium Constitution

## Core Principles

### I. One Fixed Source per Topic

Every answer MUST come from the fixed source for its topic in the Source Register. Each topic
has one source. For the released mod, that one source is the ordered sequence in
Principle III.

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

Questions other than game content MUST NOT be put to the maintainer. Rules, files, and practices
that no fixed source supports MUST be removed. When no fixed source settles such a question, the
agent MUST NOT act on it.

### VI. Every Conclusion Names Its Source

Every conclusion, including a judgment, MUST name its source and MUST be reached from that
source.

## Source Register

Each topic and its one fixed source:

| Topic | Fixed source |
|-------|--------------|
| Game content | The maintainer; decisions in force are the design documents on the default branch of `Neiro-dev/Imperium-old` |
| The released mod | The Principle III sequence: Core and the official DLCs, then `ModUpdating.txt`, then Harmony |
| Development process | Spec Kit |
| The agent and the files it reads | Claude's official documentation |
| Repository | GitHub Docs |
| Commit messages | Conventional Commits 1.0.0 |

## Governance

Amendments go through a pull request, which is merged once it is approved.

Versioning follows semantic versioning:

- MAJOR: Backward incompatible governance/principle removals or redefinitions.
- MINOR: New principle/section added or materially expanded guidance.
- PATCH: Clarifications, wording, typo fixes, non-semantic refinements.

Compliance is reviewed at each plan's Constitution Check and at pull request review.

**Version**: 2.0.0 | **Ratified**: 2026-11-23 | **Last Amended**: 2026-11-24
