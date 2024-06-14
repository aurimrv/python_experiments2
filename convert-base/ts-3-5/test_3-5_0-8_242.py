import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from convert_base import convert_base, convert_digit_to_int

@pytest.mark.parametrize("val, base, expected", [
    ("10", 2, 2),
    ("10", 16, 16),
    ("a", 16, 10),
    ("101", 2, 5),
    ("10a", 16, 266),
])
def test_convert_base(val, base, expected):
    assert convert_base(val, base) == expected

@pytest.mark.parametrize("char, expected", [
    ("0", 0),
    ("a", 10),
    ("f", 15),
])
def test_convert_digit_to_int(char, expected):
    assert convert_digit_to_int(char) == expected

@pytest.mark.parametrize("val, base", [
    ("10", 0),  # negative base
    ("10", -1),  # negative base
    ("10", 11),  # invalid base
    ("10", 15),  # invalid base
    ("g", 16),  # invalid digit for base 16
    ("10a", 2),  # invalid digit for base 2
])
def test_convert_base_invalid(val, base):
    assert convert_base(val, base) == -1

@pytest.mark.parametrize("char", [
    "",  # empty string
    "ab",  # multiple characters
    "g",  # invalid character
])
def test_convert_digit_to_int_invalid(char):
    assert convert_digit_to_int(char) == -1