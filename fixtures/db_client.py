import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


import pytest
from utils.database import PostresDB


@pytest.fixture(scope='session')
def db_client():
    db = PostresDB()
    yield db
    db.close()

print(sys.path)
