from leapyear import *


def test_leapyear_good():
    assert func(2000) == 1


def test_leapyear_bad():
    assert func(1999) == 2