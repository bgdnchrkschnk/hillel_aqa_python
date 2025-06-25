import logging
import random

import pytest
logging.basicConfig(level=logging.INFO)


@pytest.fixture(scope="function")
def logging_tests(request) -> None: # default (scope='function')
    logging.info(f"\nTest {request.node.name} execution started..")
    yield
    logging.info(f"Test {request.node.name} execution ended..")

@pytest.fixture(scope="session")
def random_number() -> int:
    number = random.randint(1, 100)
    logging.info(f"Random number: {number}")
    yield number


# @pytest.fixture(scope="session", autouse=True)
# def set_env():
#     db_client = DatabaseClient()
#     db_client.mutation(f"UPDATE users SET status = 'test' WHERE user_id = 5")
#     yield
#     db_client.mutation(f"UPDATE users SET status = 'active' WHERE user_id = 5")


@pytest.fixture(scope="function", params=["Anatoliy", "Eduardo", "Tanisha"])
def name():
    # logging.info(f"Ex: {request.node.name}")
    param_value = request.param
    yield param_value


### scopes
# function = for each test function
# class = for each test class
# module = for each module
# session = for each session