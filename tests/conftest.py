"""Shared test setup: the game's Data/ folder and small reference pictures."""

import os
from pathlib import Path

import pytest
from PIL import Image

FIXTURES = Path(__file__).parent / "fixtures"


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
