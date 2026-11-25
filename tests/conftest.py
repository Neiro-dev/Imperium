"""Shared test setup: the game's Data/ folder and small reference pictures."""

import os
import re
from dataclasses import dataclass
from pathlib import Path

import pytest
from PIL import Image

from mantle_check import cli

FIXTURES = Path(__file__).parent / "fixtures"
MODS = FIXTURES / "mods"
NO_EXPANSION = MODS / "NoExpansion"
NEEDS_ROYALTY = MODS / "NeedsRoyalty"


@pytest.fixture(scope="session")
def data_dir() -> Path:
    value = os.environ.get("RIMWORLD_DATA_DIR")
    if not value:
        pytest.fail("Set RIMWORLD_DATA_DIR to the Data folder of RimWorld 1.7.5014.")
    return Path(value)


@pytest.fixture
def make_picture(tmp_path):
    """Writes a small reference picture into the test's temporary folder and gives its path."""

    def make(name: str = "reference.png", size=(40, 30), colour=(90, 120, 60)) -> Path:
        path = tmp_path / "pictures" / name
        path.parent.mkdir(parents=True, exist_ok=True)
        Image.new("RGB", size, colour).save(path)
        return path

    return make


PROBLEM_LINE = re.compile(
    r"^(?P<number>\d+)\. \[(?P<kind>[^\]]+)\] (?P<file>[^,]+), (?P<owner>[^,]+), (?P<where>.+?)"
    r"(?: at (?P<cell>\(\d+, \d+\)(?:-\(\d+, \d+\))?))?: (?P<message>.*)$"
)


FINDING_LINE = re.compile(
    r"^(?P<number>L\d+)\. \[(?P<kind>[^\]]+)\] (?P<file>[^,]+), (?P<owner>.+?), (?P<where>(?:parts|household|plots|the road network)[^:]*?)"
    r"(?: at (?P<cell>\(\d+, \d+\)(?:-\(\d+, \d+\))?))?: (?P<message>.*)$"
)


@dataclass
class CheckResult:
    status: int
    report: str
    out: Path

    @property
    def problems(self) -> list[dict]:
        found = []
        for line in self.report.splitlines():
            match = PROBLEM_LINE.match(line)
            if match:
                found.append(match.groupdict())
        return found

    def kinds(self) -> list[str]:
        return [p["kind"] for p in self.problems]

    @property
    def findings(self) -> list[dict]:
        found = []
        for line in self.report.splitlines():
            match = FINDING_LINE.match(line)
            if match:
                found.append(match.groupdict())
        return found


@pytest.fixture
def run_check(data_dir, tmp_path, capsys):
    """Runs the check as the command does, in the test's own output folder, and gives the exit status and report."""

    def run(files, mods=(), references=(), out: Path | None = None, **options) -> CheckResult:
        out = out or tmp_path / "out"
        status = cli.run([Path(f) for f in files], data_dir, out, [Path(m) for m in mods], list(references), **options)
        captured = capsys.readouterr()
        report_file = out / "report.txt"
        result = CheckResult(status, captured.out + captured.err, out)
        if status != 2:
            assert report_file.read_text(encoding="utf-8") == captured.out
            header = re.search(r"^Problems: (\d+)$", captured.out, re.MULTILINE)
            assert len(result.problems) == (int(header.group(1)) if header else 0), captured.out
        return result

    return run
