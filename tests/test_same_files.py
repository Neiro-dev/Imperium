"""The same inputs give the same files, byte for byte (spec FR-022; quickstart.md step 2)."""

from conftest import FIXTURES

US2 = FIXTURES / "us2"
FILES = [
    US2 / "TestTown.xml",
    US2 / "TestRiverTown.xml",
    US2 / "cities" / "granite-wall-on-marsh.xml",
    FIXTURES / "us3" / "TestPalaceTown.xml",
]


def test_two_runs_give_the_same_files(run_check, make_picture, tmp_path):
    picture = make_picture("plan.png", size=(64, 48))
    references = [f"TestRiverTown:plan={picture}", f"TestPalaceTown:screenshot={picture}"]
    first = run_check(FILES, references=references, out=tmp_path / "first")
    second = run_check(list(reversed(FILES)), references=list(reversed(references)), out=tmp_path / "second")
    names = sorted(p.name for p in first.out.iterdir())
    assert names == sorted(p.name for p in second.out.iterdir())
    assert "report.txt" in names and len(names) > 4
    for name in names:
        assert (first.out / name).read_bytes() == (second.out / name).read_bytes(), name
    assert str(tmp_path) not in first.report
