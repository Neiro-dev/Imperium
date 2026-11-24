# Imperium Constitution

## Core Principles

### I. One Source per Topic

Every answer MUST come from the source the Source Register gives for its topic. Nothing outside
the Source Register is a source.

### II. Other Sources Only Cross-Check

Sources other than the topic's own source MUST be used only to cross-check.

### III. Sources in Order

Where a topic lists several sources in order, the next one MUST be used only when the previous
one gives no form.

### IV. Asking the Maintainer

The agent MUST NOT ask the maintainer about anything other than game content. For game content,
the maintainer is asked only when no source in its chain has the answer, and judges only its broad
direction.

### V. When a Source Gives No Form

When the topic's source names a default, the agent MUST use it. When the source offers options
without a default, the agent MUST use the option the source uses in its own repository or
examples. When the source gives neither, the agent MUST NOT act on the question, except for game
content, where Principle IV applies. Rules, files, and practices that no source supports MUST be
removed.

### VI. Every Conclusion Names Its Source

Every conclusion, including a judgment, MUST name its source and MUST be reached from that
source.

## Source Register

Three layers: Claude, GitHub and RimWorld. Each topic and its source:

| Layer | Topic | Source |
|-------|-------|--------|
| Claude | How the AI works: sessions, threads, project settings, CLAUDE.md, skills, subagents | The Anthropic documentation for the product in use: code.claude.com (Claude Code and projects), platform.claude.com (the API), support.claude.com (claude.ai). anthropic.com/engineering only cross-checks |
| GitHub | Development workflow | Spec Kit (`github/spec-kit`) |
| GitHub | Repository files and settings, branches, pull requests, and commit messages | GitHub Docs; choosealicense.com for the license |
| RimWorld | Game content and the released mod | Base game and official expansions in `Data/` → `ModUpdating.txt` → Harmony (`pardeike/HarmonyRimWorld`). Game content is judged by what the official expansions contain. `EULA.txt` is always followed |
| RimWorld | Testing in the game | In order: `Readme.txt` (the `-quicktest` launch option), then RimBridgeServer (`pardeike/RimBridgeServer`) with GABS (`pardeike/GABS`) |

## Governance

Amendments go through a pull request, which is merged once it is approved.

Versioning follows semantic versioning:

- MAJOR: Backward incompatible governance/principle removals or redefinitions.
- MINOR: New principle/section added or materially expanded guidance.
- PATCH: Clarifications, wording, typo fixes, non-semantic refinements.

Compliance is reviewed at each plan's Constitution Check and at pull request review.

**Version**: 2.0.0 | **Ratified**: 2026-11-23 | **Last Amended**: 2026-11-24
