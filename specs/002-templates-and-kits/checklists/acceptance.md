# Acceptance Checklist: Templates and kits

**Purpose**: Records the maintainer's judgment of each laid-out city, template and reading drawn beside its reference
pictures, one item for each picture (spec FR-029, FR-030, FR-036): what it names, the commit it was drawn from and where
the picture is in the project's files. An item is checked only when the maintainer accepts the comparison, and the
check never reports a match by itself.
**Created**: 2026-11-24
**Feature**: [spec.md](../spec.md), [tasks.md](../tasks.md)

**Review Ownership**: This checklist is reviewer-owned: the maintainer judges each picture by eye and marks an item
`[x]` only when he accepts it. Leave an item unchecked while he has not looked at it or has not accepted it.

## River-bend town

- [ ] CHK001 Does the river-bend town's template (`RiverBendTown`, Imperium's `Templates_Empire.xml`) with the Empire's
  kit, drawn at ab5a33d with `mantle-check`, read as the town of its two reference pictures, the screenshot and the
  render? [SC-007, SC-008, FR-030, FR-031]
  - Note (2026-11-25): the template and kit drawn here are drafts under spec FR-031; they are taken again from the
    river-bend town's new reading once its areas are accepted (tasks T073), and judged again then.
  - Picture: `r13-check/河湾城-ab5a33d/RiverBendTown.side-by-side.png` in the project's files (a preview, `.preview.png`,
    beside it); the check reports no problem.

### The river-bend town's reading from its screenshot, area by area (spec FR-050, FR-053, FR-057, SC-015 to SC-019)

- [ ] CHK002 Does the East Square area of `readings/RiverBendTown.xml`, traced at 51d28fd and drawn at befc9a5 (its
  court opened), reproduce the screenshot
  better than the old sample's same area (sample cells x 276-393, y 196-289), judged in the two pictures of SC-018?
  This is the first look, after tracing (FR-050). [SC-017, SC-018, FR-053, FR-057]
  - Pictures in the project's files: `RiverBendTown.compare-over.png` (the new tracing over the screenshot, beside the
    old sample over the same pixels through the old project's mapping), `RiverBendTown.compare.png` (the new drawing,
    the old sample's same area and the screenshot's area, at one width), `RiverBendTown.side-by-side.png` (the drawing,
    the tracing over the screenshot, the screenshot and the render's same area), `report.txt` (findings of both, road
    ends, plot sizes, shares) and `tracing-pixels.json` (every piece's polygon on the screenshot, R-28).
  - Minutes: tracing began 08:55 UTC and the first picture after tracing was drawn 09:08 UTC, 13 minutes, after ten
    rounds of drawing and looking; pictures the maintainer saw before accepting: none yet (SC-016).
  - Places where the old sample shows a shortfall of FR-057, listed after the new tracing was drawn, in the
    screenshot's pixels (x0,y0,x1,y1), for looking at in the new tracing:
    - S8 (1020,555,1180,680): the long workshop south-east of the square, one long narrow roof with a narrow one
      beside it, is three wide 45° squares in the old sample.
    - S8 and S2 (1070,505,1170,590): the courtyard building east of the fountain, the square's north-east corner and
      the tree are one large 45° square in the old sample.
    - S8 (950,570,1050,660): the 45° house west of the workshop is drawn about half as large again in the old sample.
    - S2 (990,665,1130,717): the four houses south of the main street, with cypresses and gaps between them, are one
      joined block in the old sample.
    - S9 (1000,560,1060,660) and (1060,600,1140,680): shadowed paved ground beside the workshop is garden in the old
      sample.
    - S1 and S3: the old sample's road network is in five pieces and two of its yards touch no house (report,
      findings of the old sample, boxed in the sample's cells on its own drawing).
  - Maintainer's look, 2026-11-25: somewhat better than the old sample, but the buildings are guessed from their roofs
    rather than reproduced as the game's own buildings, and the roads were not read from any road source and do not
    connect on their own. Not accepted; the area is read again by the game's own buildings and road pieces (spec
    FR-058, SC-020; tasks, Handoff of 2026-11-25, evening).
  - Findings of the new reading, places to look again and no condition (SC-019): residence plots over one and a half
    estates (the long roofs and wide yards may be two or more households each), and the east street's north end,
    which a tree crown hides (left as read, marked unsure). Each is left with its region; none was changed to make a
    finding go away.
