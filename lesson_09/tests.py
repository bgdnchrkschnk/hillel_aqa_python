# import unittest
# from lesson_09.func import * - краще так не робити
from lesson_09.func import add, sub
from unittest import TestCase
import unittest


# from importlib.machinery import SourceFileLoader
# module_name = 'add_function'
# math_module = SourceFileLoader(module_name, '/Users/milanstar/PycharmProjects/hillel_aqa_python/lesson_09/func.py').load_module()
# result = math_module.add(2, 3)


class Tests(TestCase):

    def test_1(self):
        pass

    def test_2(self):
        pass

    def test_3(self):
        pass


if __name__ == '__main__':
    unittest.main()