from .fixtures.db_client import *
from .fixtures.api_client import *
from fixtures.logging_tests import *


@pytest.fixture(autouse=True)
def test_log():
    print("CONFTEST.PY")
    yield

