import unittest
from leapyear import *
import pytest


def test_leapyear_good():
    assert func(2000) == 1


def test_leapyear_bad():
    assert func(1999) == 2


class TestCase(unittest.TestCase):
    def test_pos(self):
        self.assertEqual(func(2000), 1)

    def test_neg(self):
        self.assertEqual(func(1999), 2)


if __name__ == "__main__":
    unittest.main()