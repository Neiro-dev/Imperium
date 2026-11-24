# Contract: reading notes

One notes file per reading chunk, `specs/005-imperium-design-archive/research/<chunk>.md`, written by the reader of that
chunk during Phase 0 (research.md R-3). The archive is written from these notes and checked against the sources they
point to. The notes are in English and keep every name the sources use in their own language.

## What the reader reads

The files of the chunk, at Imperium-old `b218bdcbaf5a9f6253d747399986bfd30cabc243`, every line of the range given.
Paths are relative to the root of Imperium-old.

## Rules

1. Record what the design **is**, in plain declarative sentences: "The Empire's court is not on this planet", not "The
   court MUST NOT be on this planet". A rule, ruling card or session record is restated as the meaning it settles.
2. Record only what the passage says. Add nothing from the base game's Empire or Royalty (hypertech, techno-feudalism,
   titles, peerage and the like), from history, or from your own knowledge, and give no example the passage does not
   give.
3. Every statement ends with its pointer: `` `path` L<first>-<last> ``, the lines that say it.
4. Code and implementation are not sources: Defs, classes, methods, file formats of the mod, build and test results,
   tool behaviour. Keep only the design meaning a passage gives; when a passage is all implementation, class the file so
   and record no statement.
5. Process is not design: how design sessions, dispatch, reviews, storage, backups and tools work. Class such files as
   process; record a statement only for the design meaning found inside them.
6. Facts about the base game or an official expansion (what a definition holds, what the game does) are not Imperium's
   design: record them with the flag `BASEGAME` so they can be checked against `Data/`.
7. Real history (Rome, Byzantium, medieval Europe and the like) is kept only as the concept the passage draws on, with
   the flag `HISTORY`; add no historical detail.
8. Where a passage says what something looks like, record it with the flag `LOOK` and the paths of the images it points
   to, if any.
9. Where the source marks a passage as replaced (an archive of superseded rulings, "已取代", "作废", "改为", a later
   ruling that names the earlier one), give the flag `REPLACES <pointer>` or `REPLACED-BY <pointer>`.
10. Keep ruling ids, dates and the decider the passage names (用户, 设计会话定, and the like) in the pointer line as
    `[R-1028-2127, 用户 10-28]`; they are not part of the statement.
11. A line that the reading tool shows cut short is read in full by another means before it is noted.

## Layout

```markdown
# Reading notes: <chunk>

Files: <n> · Lines read: all

## Files

| File | Lines | Class | What it is | Subjects |
|---|---|---|---|---|
| `Imperium-Knowledge/现行/城/罗马城-墙.md` | 1-120 | design | Current card for the walls of the Roman city | cities |

## Statements

### <subject>

- <statement>. `<path>` L<a>-<b> [flags] [ruling id, decider, date]

## Conflicts inside this chunk

- <point>: <side A> `<pointer>`; <side B> `<pointer>`.

## Open points the sources name

- <point the sources leave undecided, such as an entry of a to-decide list>. `<pointer>`

## Images and data files named

| File | Class | What the sources say it is | Named at |
|---|---|---|---|
```

**Class** is one of: `design` (holds design meaning), `process` (how the old projects worked), `implementation` (about
the mod's code, data or results), `basegame` (about the base game or an expansion), `navigation` (an index or table of
contents generated from other files), `research` (findings gathered to inform design, not a decision), `reference
image`, `data`.

**Subjects** are taken from this list; a statement that fits none goes under `other` with a two-word name:
`imperium` (what Imperium is, its parts, requirements, the end), `world` (the world and setting), `empire` (the Empire,
its people, society, ranks and politics), `military` (forces, weapons, honour guard), `mechanoids`, `core`, `relations`
(envoy, joining, leaving, relations, ill will, purge), `ruins-tech` (ruins, excavations, technology, blueprints,
research), `orders` (orders and quests), `administration` (administrative facilities, regions, regional activities),
`industry` (mechanized industry, production facilities), `water` (hydraulics), `cities` (city building: sites, terrain,
templates, kits, skeletons, walls, gates, streets, buildings, rivers), `cultures` (settlements of cultures other than the
Empire), `mantle` (the framework layer and world generation beyond cities), `art` (appearance, art language, reference
images), `text` (names, game text, interface), `playstyles`, `rhythm`, `expansions` (content tied to an expansion),
`terms` (names in force and names replaced).
