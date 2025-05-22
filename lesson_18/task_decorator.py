import pytest


def decorator_zero_division_check(func):
    def wrapper(*args, **kwargs):
        for key, value in kwargs.items():
            if key == "b" and value == 0:
                raise ValueError("Don't divide by zero. Not supported")
        return func(*args, **kwargs)
    return wrapper


        # try:
        #     return func(*args, **kwargs)
        # except ZeroDivisionError:

@decorator_zero_division_check
def div(a: int | float, b: int | float) -> int | float:
    return a / b


div(a=1,b=0)


# class TestDivCheck:

    # @pytest.mark.parametrize("a, b", [
    #     (1, 2), (5, 9), (10, 3)
    # ])
    # def test_div_positive_scenario(self, a, b):
    #     expected = a / b
    #     assert div(a, b) == expected

    # @pytest.mark.parametrize("a, b", [
    #     (0,0), (2,0), (18,0)
    # ])
    # def test_div_negative_scenario(self):
    #     with pytest.raises(ValueError):
    #        div(a=5, b=0)
