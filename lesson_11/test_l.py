from lesson_11.logging_all import logger

import pytest

def sum(a, b):
    return a + b

def test_sum():
    a = 2
    b = 3
    logger.info(f"Testing of sum function.\nfirst argument: {a}\nsecond argument: {b}")
    if not sum(a,b) != 5:
        logger.error(f"sum of {sum(2,3)} is not equal to 5")
        raise AssertionError