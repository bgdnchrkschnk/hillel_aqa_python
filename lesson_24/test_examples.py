import pytest

def add(a, b):
    return a + b

class TestExamples:

    def test_example1(self, name):
        assert name == "Anatoliy"

    @pytest.mark.parametrize("some_letter", [
        "a", "A", "b", "B"
    ])
    def test_example2(self, some_letter):
        assert some_letter.isupper()

    @pytest.mark.parametrize("x, y, expected_result", [
        (1, 2, 3),
        (5, 5, 10),
        (10, -5, 5),
        (0, 0, 0)
    ])
    def test_addition(self, x, y, expected_result):
        assert add(x, y) == expected_result


@pytest.mark.usefixtures("logging_tests")
class TestExamples2:

    def test_example2(self, random_number):
        print(random_number)
        assert random_number % 2 == 0, random_number

    def test_example3(self, random_number):
        print(random_number)
        assert random_number % 2 == 0, random_number

