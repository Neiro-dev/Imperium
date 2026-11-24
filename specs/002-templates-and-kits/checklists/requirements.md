# Specification Quality Checklist: Templates and kits

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

- Game names such as `Data/`, terrain, natural rock, roof and the `x` and `z` coordinates are the domain's own words
  [Data], not implementation choices; how the forms are written and the pictures' look and file format are left to
  `/speckit-plan`.
- Where template layouts come from, what is fixed and what is left to generation beyond the parts the design names,
  how a template is accepted, and how templates and kits are taken from a reference's reading follow the maintainer's
  broad direction ([Direction]; Purpose; FR-005, FR-010, FR-029 to FR-037), since the design leaves them open
  (constitution, Principle IV). The tribal culture's kit and template for the alpha, and the Empire's kit and the
  river-bend town's template for Imperium, follow the roadmap (R13, R14, R15).
- No marker remains. `/speckit-clarify` settled three questions (spec, Clarifications): how a laid-out city is judged
  to match its reference and whether one template serves several cultures, both answered by the maintainer as game
  content (constitution, Principle IV), and how the river-bend town fits a 350×350 map, settled from the sources. The
  spec was then reconciled with the roadmap's new R13, R14 and R15 (Spec Kit, spec-of-specs), and three more answers
  came from the maintainer's direction: what a kit's groups and fill hold, where the tribal culture's reference comes
  from, and that a calibrated template ships as it stands. Which Albion city is the tribal reference is his choice
  among candidates (FR-037); it gates the tribal reading, kit and template, not the forms or the check.
