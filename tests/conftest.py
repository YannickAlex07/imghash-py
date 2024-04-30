from collections.abc import Callable
from os.path import dirname
from pathlib import Path

import pytest

ResourceFunc = Callable[[str], Path]


@pytest.fixture()
def resource() -> ResourceFunc:
    def _resource(name: str) -> Path:
        data_dir = Path(dirname(__file__)) / "data"
        return data_dir / name

    return _resource
