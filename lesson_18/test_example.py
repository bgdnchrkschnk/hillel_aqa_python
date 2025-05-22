import pytest

from lesson_18.class_decorators import say_hello


def deco_precondition(func):
    def wrapper(*args, **kwargs):
        print(f"Testing {func.__name__}...")
        return func(*args, **kwargs)
    return wrapper

def log_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)

        print(f"Test {func.__name__} executed with result: {result}")
        return result
    return wrapper

# def test_data_provider_gen():
#     res = requests.get(url="https://test.com/get_test_data")
#     validate()
#     yield res.json()
#
# def validate_params_decorator(func):
#     def wrapper(*args, **kwargs):
#         # Валідація вхідних параметрів
#         validate(args, kwargs)
#         result = func(*args, **kwargs)
#         return result
#     return wrapper


class TestExample:

    def test_example_negative(self):
        with pytest.raises(ValueError):
            say_hello("Roman")
