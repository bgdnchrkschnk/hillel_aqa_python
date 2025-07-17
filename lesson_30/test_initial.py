import allure
import logging

import pytest

class TestInitial:

    @pytest.mark.parametrize("input_data, expected_output", [
        ([1, 2, 3], 6),
        ([-1, 0, 1], 0),
        ([10, 20, 30], 60)
    ])
    @allure.title("Testing sum of several numbers {input_data}")
    def test_sum_ref(self, input_data, expected_output):
        logging.info(f"Testing sum of {input_data} expected {expected_output}")
        allure.attach(attachment_type=allure.attachment_type.TEXT, name="Test name", body="Test attachment data")
        with allure.step(f"Calculating sum of {input_data}"):
            actual_result = sum(input_data)
        assert actual_result == expected_output

    @pytest.mark.parametrize("input_string, expected_output", [
        ("hello", "HELLO"),
        ("world", "WORLD")
    ])
    @allure.title("Testing uppercase for string {input_string}")
    def test_uppercase(self, input_string, expected_output):
        logging.info(f"Testing uppercase of {input_string} expected {expected_output}")
        assert input_string.upper() == expected_output

    @allure.title("Testing failed assertion")
    def test_failed(self):
        assert False