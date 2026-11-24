# Imperium design archive

This archive gives an account of the design on Imperium-old's default branch, as connected prose by subject, with a
pointer for every statement to the passage that says it. It covers all of that design: the Empire, Mantle, the
settlements of the other cultures and every other part the branch designs (`specs/005-imperium-design-archive/spec.md`,
Scope).

The archive is a reading aid, not a source. The constitution's source for Imperium's own design stays Imperium-old
(`.specify/memory/constitution.md`, Source Register); work that relies on a statement here cites the passage its
pointer names.

## The pinned commit

Every pointer refers to Imperium-old at `b218bdcbaf5a9f6253d747399986bfd30cabc243` (2026-11-24, after Imperium-old
pull request #291). At that commit the design lies in three bodies of text: `docs/` at the root, and
`Imperium-Knowledge/` and `RimWorld-Imperium/`, which PR #291 merged in unchanged and unreconciled. None ranks above
another unless a passage says so.

## Reading a pointer

A pointer is a path relative to Imperium-old's root and the lines that say the statement, such as
(`Imperium-Knowledge/现行/城/罗马城-墙.md` L12-18). A ruling id the passage gives may follow it. To open a pointer at
the pinned commit:

```text
https://github.com/Neiro-dev/Imperium-old/blob/b218bdcbaf5a9f6253d747399986bfd30cabc243/<path>?plain=1#L12-L18
```

## Markings

> [!WARNING]
> **Conflict**: two or more passages of the same date, or of no date, say different things about one point, and no
> passage says which holds. Each side is given with its pointers, and the prose states neither.

> [!NOTE]
> **Unverified**: the sources leave the point open, or hold only a proposal that was not decided. Nothing has been put
> in its place.

> [!NOTE]
> **Base game**: a fact about the base game or an official expansion that a design point rests on. It is the old
> repository's claim, to be checked against `Data/`.

> [!NOTE]
> **Deleted**: an old line of the design that a newer setting removed with everything on it, such as the hydraulics
> axis (水利, the imperial aqueducts). It is named once, with pointers to it and to what deleted it, and its details are
> not listed as conflicts or open points.

Where passages disagree and carry different dates, the later one is the design, as the maintainer directed on
2026-11-24; for looks the latest holds. Imperium-old's root `docs/` files (2026-11-16 to 2026-11-21) are later than
everything in `Imperium-Knowledge/` (to 2026-11-15) and `RimWorld-Imperium/` (to 2026-11-11). The prose gives the
meaning that holds and names the earlier passage as "(replaces ...)", as it does where a source itself marks a passage
replaced. Every conflict and unverified point is also listed in [open-points.md](open-points.md).

## Sections

City building:

- [cities.md](cities.md): city building as a whole, its scale and references, the eras of the Roman city, its
  principles and the order in which a city is made
- [cities-siting.md](cities-siting.md): terrain, landforms and where cities stand
- [cities-walls.md](cities-walls.md): walls, towers, gates and moats, and what they are made of
- [cities-inside.md](cities-inside.md): the core, the palace district, streets, housing, groups and buildings
- [cities-outside.md](cities-outside.md): the land outside the walls, and rivers, banks, bridges and harbours
- [cities-forms.md](cities-forms.md): templates, kits, skeletons, spec cards and the city grammar

Imperium and the Empire:

- [imperium.md](imperium.md): what Imperium is, its parts, requirements, playstyles, expansions, rhythm and end
- [world.md](world.md): the world Imperium is set in
- [empire.md](empire.md): the Empire, its people, ranks and politics
- [military.md](military.md): forces and weapons
- [mechanoids.md](mechanoids.md): the imperial mechanoids
- [core.md](core.md): the core
- [relations.md](relations.md): contact and relations with the Empire
- [orders.md](orders.md): orders and quests
- [ruins-and-technology.md](ruins-and-technology.md): ruins, excavations and technology
- [administration.md](administration.md): administration and regions
- [industry.md](industry.md): mechanized industry
- [water.md](water.md): the hydraulics axis, deleted

Beyond the Empire, and across the design:

- [cultures.md](cultures.md): settlements of the other cultures
- [mantle.md](mantle.md): Mantle, the framework layer, and the world it generates
- [art.md](art.md): appearance and the reference images
- [text.md](text.md): game text and naming
- [terms.md](terms.md): the terms in force and the names they replaced

Indexes:

- [open-points.md](open-points.md): every conflict and unverified point, with a link to where it stands
- [coverage.md](coverage.md): every file at the pinned commit, its class and the sections that cite it
