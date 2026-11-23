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

### IV. The Maintainer Settles Open Questions

When no source settles a question, the agent MUST ask the maintainer and MUST act only after
the maintainer decides.

## Source Register

Each topic and its one fixed source:

| Topic | Fixed source |
|-------|--------------|
| Game content | The maintainer |
| The released mod | Core and the official DLCs, then `ModUpdating.txt`, then Harmony (Principle III) |
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

**Version**: 1.0.0 | **Ratified**: 2026-11-23 | **Last Amended**: 2026-11-23
