# Implementation Plan: The constitution enforced by hooks

**Branch**: `claude/project-thread-mjdz9x` | **Date**: 2026-11-24 | **Spec**: [spec.md](spec.md)

**Input**: Feature specification from `/specs/004-constitution-hooks/spec.md`

## Summary

Two Claude Code hooks in the repository's `.claude/settings.json` judge what Claude is about to tell the maintainer
against the constitution's current text: a `PreToolUse` hook on the tools that send him a message or a question, and a
`Stop` hook on Claude's final response. Each is an `agent` hook whose instructions say where the constitution and the
session's record are and how to answer, and state none of its rules (research R-1 to R-7). The hooks run wherever
Claude Code reads the repository's settings, which includes a project thread on the maintainer's computer started in
his clone and excludes a project's cloud threads and the project conversation (research R-2).

## Technical Context

**Language/Version**: JSON (Claude Code settings file)

**Primary Dependencies**: Claude Code hooks, `agent` type (code.claude.com/docs/en/hooks.md)

**Storage**: N/A

**Testing**: `claude -p` in a copy of the repository, with a stand-in MCP server for the messaging tool
(quickstart.md); then a project thread on the maintainer's computer, which is the final check

**Target Platform**: Claude Code sessions started in the repository root: the maintainer's Windows computer through
Remote Control, and sessions outside a project

**Project Type**: repository configuration

**Performance Goals**: none set by a source; the checks took 7 to 12 seconds each in quickstart.md with the default
60-second timeout (research R-6)

**Constraints**: the configuration restates no rule of the constitution (spec FR-004)

**Scale/Scope**: one file, two hook handlers

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

| Principle | Check | Result |
|-----------|-------|--------|
| I. One Source per Topic | How hooks work comes from the Claude Code docs (Source Register, Claude layer); the repository file from GitHub Docs and Spec Kit (GitHub layer). | Pass (research R-1 to R-7) |
| II. Other Sources Only Cross-Check | The test runs in this thread's container only confirm what the docs say; no decision rests on them alone. | Pass |
| III. Sources in Order | No topic here lists several sources in order. | N/A |
| IV. Asking the Maintainer | Nothing is asked of him. What only he can do on his computer and in the project's settings is listed in quickstart.md, Maintainer's steps, as steps, not questions. | Pass |
| V. When a Source Gives No Form | Defaults used for timeout and model (R-6); the agent type follows the docs' rule for judgment against the codebase (R-4); ways with no supporting source are not used (R-2). | Pass |
| VI. Every Conclusion Names Its Source | Each decision in research.md names its page and line. | Pass |

Re-check after Phase 1: unchanged; the contract and quickstart add no decision without a source.

## Project Structure

### Documentation (this feature)

```text
specs/004-constitution-hooks/
├── plan.md
├── research.md
├── data-model.md
├── quickstart.md
├── contracts/
│   └── hooks-settings.md
├── checklists/
│   └── requirements.md
└── tasks.md
```

### Source Code (repository root)

```text
.claude/
├── settings.json        # new: the two hooks
└── skills/              # unchanged: Spec Kit's skills
```

**Structure Decision**: one file at the repository root, since it serves the repository and not a mod
(`specs/003-mantle-mod/contracts/repository-layout.md`, Stable, fourth entry), at the path the docs give for shared
project settings (research R-1).

## Complexity Tracking

No violations.
