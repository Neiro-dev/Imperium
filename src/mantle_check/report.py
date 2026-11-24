"""The report: every problem numbered, each relation's result, the reference pictures, and the closing statement
(spec FR-019, FR-020, FR-022, FR-029)."""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path

FINAL_STATEMENT = (
    "Testing in the game is the final check, and it is still to come: "
    "nothing here is final until it has been tested in the game."
)

Cell = tuple[int, int]
Rect = tuple[int, int, int, int]


@dataclass(frozen=True)
class Problem:
    kind: str
    file: str
    owner: str
    where: str
    message: str
    cell: Rect | None = None

    def sort_key(self):
        cell = self.cell if self.cell is not None else (-1, -1, -1, -1)
        return (self.file, self.owner, self.where, cell, self.kind, self.message)

    def cell_text(self) -> str:
        if self.cell is None:
            return ""
        x1, z1, x2, z2 = self.cell
        if (x1, z1) == (x2, z2):
            return f"({x1}, {z1})"
        return f"({x1}, {z1})-({x2}, {z2})"


@dataclass
class RelationResult:
    file: str
    owner: str
    relation: str
    result: str
    detail: str = ""


@dataclass
class Report:
    problems: list[Problem] = field(default_factory=list)
    relations: list[RelationResult] = field(default_factory=list)
    pictures: list[str] = field(default_factory=list)
    checked: list[str] = field(default_factory=list)

    def numbered(self) -> list[tuple[int, Problem]]:
        unique = sorted(set(self.problems), key=Problem.sort_key)
        return list(enumerate(unique, start=1))

    def text(self) -> str:
        lines = ["Mantle check", ""]
        lines.append("Checked:")
        for name in sorted(set(self.checked)):
            lines.append(f"- {name}")
        lines.append("")
        numbered = self.numbered()
        if numbered:
            lines.append(f"Problems: {len(numbered)}")
            for number, problem in numbered:
                cell = f" at {problem.cell_text()}" if problem.cell is not None else ""
                lines.append(
                    f"{number}. [{problem.kind}] {problem.file}, {problem.owner}, {problem.where}{cell}: "
                    f"{problem.message}"
                )
        else:
            lines.append("Problems: none found.")
        if self.relations:
            lines.append("")
            lines.append("Relations:")
            for result in sorted(self.relations, key=lambda r: (r.file, r.owner, r.relation)):
                detail = f" ({result.detail})" if result.detail else ""
                lines.append(f"- {result.file}, {result.owner}: {result.relation}: {result.result}{detail}")
        if self.pictures:
            lines.append("")
            lines.append("Reference pictures:")
            for line in sorted(self.pictures):
                lines.append(f"- {line}")
        lines.append("")
        lines.append(FINAL_STATEMENT)
        return "\n".join(lines) + "\n"

    def write(self, out_dir: Path) -> str:
        content = self.text()
        out_dir.mkdir(parents=True, exist_ok=True)
        (out_dir / "report.txt").write_text(content, encoding="utf-8", newline="\n")
        return content
