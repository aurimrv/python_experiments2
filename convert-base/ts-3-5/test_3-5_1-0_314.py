import sys
import os
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from convert_base import convert_base, convert_digit_to_int

def test_convert_base_valid_input():
    assert convert_base('10', 2) == 2
    assert convert_base('a', 16) == 10
    assert convert_base('1010', 2) == 10

def test_convert_base_invalid_base():
    assert convert_base('10', -2) == -1
    assert convert_base('10', 11) == -1
    assert convert_base('10', 15) == -1

def test_convert_base_invalid_digit():
    assert convert_base('2a', 2) == -1
    assert convert_base('zz', 16) == -1
    assert convert_base('1010', 2) == 10

def test_convert_base_empty_input():
    assert convert_base('', 2) == 0
    assert convert_base('', 16) == 0

def test_convert_digit_to_int_valid_hex():
    assert convert_digit_to_int('0') == 0
    assert convert_digit_to_int('a') == 10
    assert convert_digit_to_int('f') == 15

def test_convert_digit_to_int_invalid_hex():
    assert convert_digit_to_int('g') == -1
    assert convert_digit_to_int('') == -1
    assert convert_digit_to_int('12') == -1