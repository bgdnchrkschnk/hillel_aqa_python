import pytest


class DecoratorUpper:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        result = self.func(*args, **kwargs)
        return result.upper()

# --------------------------------

def deco_upper(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper

# -------------------------------------------------------

def deco_upper_and_mul_len_10_max(max_len: int, repeat: int = 1):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if len(result) > max_len:
                raise ValueError("limit is 10")
            return result.upper() * repeat
        return wrapper
    return decorator


class DecoratorUpperMultipleLenMax:
    def __init__(self, max_len: int, repeat: int = 1):
        self.max_len = max_len
        self.repeat = repeat

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if len(result) > self.max_len:
                raise ValueError("limit is 10")
            return result.upper() * self.repeat
        return wrapper


# @deco_upper_and_mul_len_10_max(max_len=100, repeat=3)
@DecoratorUpperMultipleLenMax(max_len=100, repeat=3)
def say_hello(name) -> str:
    return f"Hello World! My name is {name}"

class TestExample:

    def test_example_negative(self):
        with pytest.raises(ValueError):
            say_hello("Roman")

    def test_example_positive(self):
        test_name: str = "Stepan"
        repeat_param: int = 3
        expected_result: str = f"Hello World! My name is {test_name}".upper() * repeat_param
        assert say_hello(test_name) == expected_result
