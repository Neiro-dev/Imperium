"""The command refuses to run, with exit status 2, where nothing can be checked (contracts/check-command.md, Exit
status; spec, Edge Cases)."""

from pathlib import Path

from mantle_check import cli

from conftest import NO_EXPANSION

TEMPLATE = NO_EXPANSION / "Defs/TemplateDefs/TestHillfort.xml"


def refused(capsys, out: Path, status: int) -> str:
    captured = capsys.readouterr()
    assert status == 2
    assert captured.out == ""
    assert "Nothing is reported as passing." in captured.err
    assert not (out / "report.txt").exists()
    return captured.err


def test_missing_data_folder(tmp_path, capsys):
    out = tmp_path / "out"
    status = cli.run([TEMPLATE], tmp_path / "no-such-Data", out, [NO_EXPANSION], [])
    assert "Data/ not found" in refused(capsys, out, status)


def test_data_of_another_version(tmp_path, capsys):
    game = tmp_path / "RimWorld"
    (game / "Data").mkdir(parents=True)
    (game / "Version.txt").write_text("1.6.4633 rev1261\n", encoding="utf-8")
    out = tmp_path / "out"
    status = cli.run([TEMPLATE], game / "Data", out, [NO_EXPANSION], [])
    assert "not 1.7" in refused(capsys, out, status)


def test_mod_folder_without_about(data_dir, tmp_path, capsys):
    folder = tmp_path / "NotAMod"
    folder.mkdir()
    out = tmp_path / "out"
    status = cli.run([TEMPLATE], data_dir, out, [folder], [])
    assert "has no About/About.xml" in refused(capsys, out, status)


def test_output_folder_inside_a_repository(data_dir, tmp_path, capsys):
    repository = tmp_path / "repository"
    (repository / ".git").mkdir(parents=True)
    out = repository / "out"
    status = cli.run([TEMPLATE], data_dir, out, [NO_EXPANSION], [])
    assert "inside a repository" in refused(capsys, out, status)
    assert not out.exists()


def test_file_that_is_not_xml(data_dir, tmp_path, capsys):
    broken = tmp_path / "broken.xml"
    broken.write_text("<Defs><Mantle.TemplateDef>", encoding="utf-8")
    out = tmp_path / "out"
    status = cli.run([broken], data_dir, out, [NO_EXPANSION], [])
    assert "is not XML" in refused(capsys, out, status)
