import pytest

from utils.api_client import UserApiClient, UserPostApiClient

@pytest.fixture
def user_api_client():
    yield UserApiClient()

@pytest.fixture
def user_post_api_client():
    yield UserPostApiClient()