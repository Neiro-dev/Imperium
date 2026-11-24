# Data model: Imperium design archive

The entities of spec.md, Key Entities, as files and parts of files. Their forms are in
[contracts/archive-format.md](contracts/archive-format.md) and [contracts/reading-notes.md](contracts/reading-notes.md).

## Source pointer

- **Path**: relative to Imperium-old's root, at `b218bdcbaf5a9f6253d747399986bfd30cabc243`.
- **Lines**: first and last line that say the statement (`L12-18`, or `L12` for one line).
- **Ruling** (optional): the ruling id, decider and date the passage gives, such as `R-1028-2127, 用户 10-28`.
- Valid when the path exists at the pinned commit and the lines are within the file (quickstart.md, check 1).

## Reading notes (one per chunk)

- **Chunk**: `C01` to `C32`, with the files and line ranges it covers (research.md, Reading log).
- **File rows**: each file of the chunk, the lines read, its class and its subjects.
- **Statements**: grouped by subject, each with one or more pointers and flags (`BASEGAME`, `HISTORY`, `LOOK`,
  `REPLACES`, `REPLACED-BY`).
- **Conflicts**, **open points**, and **images and data files named**.

## Archive section (one file per subject)

- **Subject**: one of the subjects of the notes contract that has statements, or one the notes name under `other`.
- **Prose**: paragraphs under headings; each sentence that states design ends with its pointers.
- **Conflicts**: two or more sides, each with its pointers; never resolved.
- **Unverified points**: what the section reaches and no passage settles, including the open points the sources list.
- **Base-game facts**: the design point that rests on a fact about the base game, with the fact to check against
  `Data/`.
- **Replaced meaning**: where a source marks a passage replaced, the replacing meaning in the prose and the replaced
  passage named beside it.

## Open-points index

- One entry per conflict and per unverified point of every section: the point, the section and heading it is under.

## Coverage record

- One row per file or path pattern at the pinned commit: **path**, **class** (design, research, process,
  implementation, code, configuration, base game, navigation, reference image, data), **reason**, **chunk** (for files
  read) and **sections** (for files the archive uses).
- Complete when every path of `git ls-tree -r` at the pinned commit matches exactly one row (quickstart.md, check 2).

## Relationships

- A statement in a section has one or more pointers; a pointer names one file of the coverage record.
- A conflict has two or more sides; each side has its own pointers.
- Every conflict and unverified point of a section has one entry in the open-points index.
