import pytest


@pytest.fixture(autouse=True)
def test_log():
    print("CONFTEST.PY testing directory")
    yield