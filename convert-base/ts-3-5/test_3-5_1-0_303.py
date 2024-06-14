import os
import sys

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from convert_base import convert_base, convert_digit_to_int

import pytest

def test_convert_base_valid():
    assert convert_base("10", 2) == 2
    assert convert_base("11", 2) == 3

def test_convert_base_invalid():
    assert convert_base("10", -2) == -1
    assert convert_base("1234", 2) == -1

def test_convert_digit_to_int_valid():
    assert convert_digit_to_int("a") == 10
    assert convert_digit_to_int("B") == 11

def test_convert_digit_to_int_invalid():
    assert convert_digit_to_int("z") == -1
    assert convert_digit_to_int("") == -1