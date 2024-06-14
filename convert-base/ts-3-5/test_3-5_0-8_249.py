import pytest
import os
import sys

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from convert_base import convert_base, convert_digit_to_int

def test_convert_base_valid_input():
    assert convert_base("10", 2) == 2
    assert convert_base("ff", 16) == 255
    assert convert_base("1111", 2) == 15

def test_convert_base_invalid_base():
    assert convert_base("10", -1) == -1
    assert convert_base("123", 11) == -1

def test_convert_base_invalid_digit():
    assert convert_base("12g", 16) == -1
    assert convert_base("1z", 36) == -1

def test_convert_digit_to_int_valid_input():
    assert convert_digit_to_int("a") == 10
    assert convert_digit_to_int("f") == 15
    assert convert_digit_to_int("0") == 0

def test_convert_digit_to_int_invalid_input():
    assert convert_digit_to_int("g") == -1
    assert convert_digit_to_int("z") == -1