import os
import logging

import pytest
logging.basicConfig(
    filename='basic_logs.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def divide(x, y):
    return x / y

@pytest.mark.smoke
class TestExamples:

    BASE_URL = "http://example.com"

    def setup_class(self):
        logging.info("Setting up the class")
        print("precondition setup")

    def test_sum_positive(self):
        print("HELLO I AM PRINT")
        logging.info("testing logger")
        assert 1 + 2 == 3
        # assert_that(1+1).is_equal_to(3)

    # @pytest.mark.parametrize("a, b, expected", [
    #     (1, 2, 3),
    #     (5, 5, 10),
    #     (10, -2, 8)
    # ])
    # def test_addition(self, a, b, expected):
    #     assert a + b == expected
    #
    #
    def test_zero_division_negative(self):
        with pytest.raises(ZeroDivisionError):
            divide(10, 0)

    @pytest.mark.xfail
    def test_multiply(self):
        assert 3 * 3 == 10

    @pytest.mark.skip(reason="need to bugfix BOF-75")
    def test_subtract(self):
        assert 5 - 2 == 3
    #
    # @pytest.fixture
    # def sample_list(self):
    #     return [1, 2, 3]
    #
    # def test_list_length(self, sample_list):
    #     assert len(sample_list) == 3
    #
    # def test_list_sum(self, sample_list):
    #     assert sum(sample_list) == 6
    #
    # @pytest.mark.skip(reason="Функціонал ще не реалізований")
    # def test_skipped(self):
    #     assert 1 == 1

def define_env(env):
    return True if env == "prod" else False

    import sys

    @pytest.mark.skipif(env == "prod", reason="Не підтримується на Windows")
    def test_not_on_windows(self):
        assert True
    #
    # @pytest.mark.xfail(reason="Відомий баг #123")
    # def test_known_bug(self):
    #     assert 2 + 2 == 5

    # @pytest.mark.parametrize("status", ["ok", "error", "unknown"])
    # def test_status_handler(self, status):
    #     if status not in ("ok", "error"):
    #        pytest.fail(f"Невідомий статус: {status}")

