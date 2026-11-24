# Contract: archive format

The files of `docs/design-archive/` (plan.md, Project Structure; research.md R-1, R-6 to R-8).

## Every section file

```markdown
# <Subject>

<One paragraph saying what this part of the design covers and which other sections it meets.>

## <Topic>

<Prose. Each sentence that states design ends with its pointers, such as
(`Imperium-Knowledge/现行/城/罗马城-墙.md` L12-18; `docs/setting.md` L40). A name the sources give in Chinese
appears as "the outer wall (外墙)" on first use; a term in force in Imperium-old's glossary is used as the glossary
gives it.>

> [!WARNING]
> **Conflict**: <the point>.
> - <side A> (`<path>` L<a>-<b>)
> - <side B> (`<path>` L<a>-<b>)

> [!NOTE]
> **Unverified**: <what the sources leave open here> (<pointer to where the sources say it is open, if they do>).

> [!NOTE]
> **Base game**: <the fact the design rests on>, to be checked against `Data/` (`<path>` L<a>-<b>).

> [!NOTE]
> **Deleted**: <the old line, what it held> (`<path>` L<a>-<b>), deleted by <the newer line or mark, or the
> maintainer's direction> (`<path>` L<a>-<b>).
```

Rules:

1. The body states what the design is. It holds no requirement keywords (MUST, SHOULD, MUST NOT, 必须, 禁止) except
   inside a quotation, and no ruling-card or session-record layout (spec FR-004, SC-003).
2. A sentence without a pointer states no design: it is a heading, a link between sections or this file's opening
   paragraph.
3. Where a source marks a passage as replaced, or a later passage disagrees with an earlier one, the prose gives the
   replacing meaning and adds "(replaces `<pointer>`)" (spec FR-005, FR-009).
4. Looks are given by naming the reference images the sources point to, with their paths; history only as the concept
   the source names (spec FR-008).
5. Nothing the cited passages do not say: no traits of the base game's Empire, no examples of the writer's own (spec
   FR-007).

## README.md

- What the archive is and is not: an account of the design on Imperium-old's default branch at the pinned commit, not a
  source in place of it (spec, Assumptions).
- The pinned commit and how to open a pointer there (research.md R-6).
- The three markings and what each means.
- The list of section files, one line each.

## open-points.md

- Two lists, conflicts and unverified points, each entry linking to the heading of the section where it is, with the
  pointers of its sides.

## coverage.md

- A table of path patterns for the classes research.md R-2 assigns by path, with their reason.
- A table of every file read (the 518 text files and `.github/deprecated-terms.json`), with its class, chunk and the
  sections that use it.
- A table of images and data files with their class and, where a text names them, the pointer that does.
