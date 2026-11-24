# Specification Quality Checklist: Mod foundation

**Purpose**: Validate specification completeness and quality before proceeding to planning
**Created**: 2026-11-24
**Feature**: [spec.md](../spec.md)

## Content Quality

- [x] No implementation details (languages, frameworks, APIs)
- [x] Focused on user value and business needs
- [x] Written for non-technical stakeholders
- [x] All mandatory sections completed

## Requirement Completeness

- [x] No [NEEDS CLARIFICATION] markers remain
- [x] Requirements are testable and unambiguous
- [x] Success criteria are measurable
- [x] Success criteria are technology-agnostic (no implementation details)
- [x] All acceptance scenarios are defined
- [x] Edge cases are identified
- [x] Scope is clearly bounded
- [x] Dependencies and assumptions identified

## Feature Readiness

- [x] All functional requirements have clear acceptance criteria
- [x] User scenarios cover primary flows
- [x] Feature meets measurable outcomes defined in Success Criteria
- [x] No implementation details leak into specification

## Notes

- Review of the first draft (PR #8) against the constitution:
  - Principle VI: the requirements, edge cases and assumptions now name their sources in brackets.
  - The first draft's FR-007 restated the constitution's source order as a product requirement. It was removed:
    compliance with the constitution is checked at the plan's Constitution Check (constitution, Governance), and a
    spec describes what the player needs, not how it is built (`/speckit-specify`, Quick Guidelines). Its FR-008 is
    now FR-007.
  - SC-003 covered 6 expansion combinations while FR-006 requires any combination; it now covers all 16.
  - `ROADMAP.md` R1 now links this spec and is in progress, as Spec Kit's roadmap convention asks
    (`docs/how-to/spec-of-specs.md` v1.4.3, sections The roadmap artifact and Linking sub-specs to the roadmap).
- Second review: Imperium measured against the official expansions, not ordinary mods (Imperium-old
  `docs/glossary.md` line 35, Imperium is a remake of Royalty; `docs/setting.md` line 83; constitution, Source
  Register, game content is judged by what the official expansions contain):
  - FR-004 placed Imperium after Core and Royalty only. Each official expansion loads after every one before it
    (`Data/*/About/About.xml`), and Imperium adds content to each other expansion, so it now loads after all of them.
  - FR-002 now records that no official expansion requires another, which is why its form comes from
    `ModUpdating.txt` (Principle III).
  - The assumption that a description and preview image are optional took `ModUpdating.txt` before `Data/`. It now
    takes the official expansions' form (`ExpansionDefs.xml`: label, description, icon, preview images), filled with
    the content it describes in later entries.
  - FR-001, the key entities and the edge cases now compare Imperium with the official expansions.
- Third review, against `EULA.txt` (always followed, constitution, Source Register): FR-008 and SC-004 keep Imperium
  presented as community-created content, never as official or made by Ludeon (EULA lines 57 and 78), and FR-009
  displays the EULA's disclaimer with it (lines 32-34). The testing assumption now cites `Readme.txt` line 58.
- Fourth review, Imperium's place among ordinary mods and the Harmony requirement:
  - FR-004 placed Imperium after the official expansions but said nothing about ordinary mods. Measured against the
    official expansions, Imperium takes the place nearest to theirs, directly after them and ahead of every ordinary
    mod (FR-011, US3 scenario 3, SC-005). The game's load-order fields name single packages and none can place a mod
    ahead of every other (`Data/*/About/About.xml`; `ModUpdating.txt` lines 300-314), so Imperium names no ordinary
    mod and tells players its place, in the form of the Harmony mod's `README.md`, the next source (Principle III).
  - Harmony is not a requirement in R1: a requirement is a mod Imperium needs to function (`ModUpdating.txt` lines
    266-267), and R1 has no code. The Harmony mod loads before Core by its own `loadBefore`, so it needs no
    load-order entry either. The assumption now says so.
  - The clarification on the log no longer names `output_log.txt`, which 1.7.5014 does not write; the plan locates
    the log (research.md R-10).
- Fifth review, from `/speckit-checklist` (checklists/compatibility.md, CHK003, CHK010, CHK011) and in-game check 1:
  the game logs an error for a mod that loads no content, so FR-005's "no errors" could not hold while FR-007 keeps
  R1 without content. FR-005 now expects that one report, which leaves with the first entry that adds content, and
  SC-001, SC-003 and SC-005 count errors and warnings alike, as FR-005 does.
- Bracketed source names in the spec name where each requirement comes from; they do not prescribe a technology.
- No game content in this feature is left to the maintainer: the design settles the requirements, and the mod's
  form is left to `/speckit-plan` from the constitution's sources.
