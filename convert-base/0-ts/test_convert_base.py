import pytest
from convert_base import convert_base, convert_digit_to_int

def test_convert_digit_valid():
    for i in range(10):
        assert i == convert_digit_to_int(str(i))
    for c, v in [("a", 10), ("b", 11), ("c", 12), ("d", 13), ("e", 14), ("f", 15)]:
        assert v == convert_digit_to_int(c)
    for c in "ghijklmnopqrstuvwxyz":
        assert -1 == convert_digit_to_int(c)


def test_convert_base_2():
    assert 5 == convert_base("101", 2)
    assert 11 == convert_base("1011", 2)


def test_convert_base_10():
    assert 20 == convert_base("20", 10)
    assert 135 == convert_base("135", 10)
    assert 7 == convert_base("7", 10)


def test_convert_base_16():
    assert int("4e", 16) == convert_base("4e", 16)


def test_convert_base_outside_range():
    assert -1 == convert_base("63", 4)


def test_convert_base_invalid_base():
    assert -1 == convert_base("101", -3)
    assert -1 == convert_base("101", 12)

