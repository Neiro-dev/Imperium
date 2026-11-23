# Imperium Constitution

## Core Principles

### I. One Fixed Source per Topic

Every answer, decision, or piece of work MUST come from the single source fixed for its
topic in the Source Register. Each topic has exactly one source. A question is first
assigned to its topic; the answer is then taken from that topic's source and from no other.

Rationale: a fixed source makes every decision traceable and stops two sources from giving
two competing answers.

### II. Other Sources Only Cross-Check

Sources other than the topic's fixed source MAY be consulted only to cross-check an answer
already taken from the fixed source. They MUST NOT supply, override, or extend that answer.
If a cross-check disagrees with the fixed source, the fixed source stands; if that leaves
the question unsettled, Principle IV applies.

Rationale: cross-checking catches mistakes without turning secondary material into a second
authority.

### III. Released Mod Source Order

For the released mod, sources are used in this strict order:

1. RimWorld Core and the official DLCs.
2. `ModUpdating.txt`.
3. Harmony.

A lower level MUST be used only when every level above it gives no form for what is needed.
Work MUST NOT move to `ModUpdating.txt` while Core or an official DLC gives a form, and MUST
NOT use Harmony while Core, the official DLCs, or `ModUpdating.txt` gives a form.

Rationale: staying with the forms the game itself provides keeps the mod closest to the game
and least likely to break, and reserves Harmony for what the game offers no form for.

### IV. The Maintainer Settles Open Questions

When no source settles a question, the agent MUST ask the maintainer and MUST NOT act on
that question until the maintainer has decided. A guess, a default, or an answer from a
non-fixed source MUST NOT stand in for that decision.

Rationale: the maintainer owns the project; unsettled questions are the maintainer's to
decide, not the agent's.

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

A topic not in this table has no fixed source; questions on it fall under Principle IV until
the maintainer adds the topic through an amendment.

## Decision Workflow

1. Assign the question to a topic in the Source Register.
2. Take the answer from that topic's fixed source; for the released mod, follow the order in
   Principle III.
3. Optionally cross-check against other sources (Principle II).
4. If no source settles the question, ask the maintainer and wait for the decision
   (Principle IV).
5. Every commit message MUST follow Conventional Commits 1.0.0.

## Governance

This constitution takes precedence over every other practice in the project. Only the
maintainer can amend it; an amendment takes effect once the maintainer has approved it and
the updated file is committed.

Versioning follows semantic versioning:

- MAJOR: a principle or Source Register entry is removed or redefined incompatibly.
- MINOR: a principle, section, or Source Register topic is added, or guidance materially
  expanded.
- PATCH: clarifications and wording fixes that do not change meaning.

Compliance is reviewed at each plan's Constitution Check and at every pull request review:
each decision MUST be traceable to its topic's fixed source or to a maintainer decision.

**Version**: 1.0.0 | **Ratified**: 2026-11-23 | **Last Amended**: 2026-11-23
