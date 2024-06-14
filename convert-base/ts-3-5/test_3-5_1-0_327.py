import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from convert_base import convert_base, convert_digit_to_int

def test_convert_base():
    assert convert_base('1010', 2) == 10
    assert convert_base('10', 3) == 3
    assert convert_base('a1', 16) == 161
    assert convert_base('1010', 8) == 520
    assert convert_base('1234', 5) == 194
    assert convert_base('abc', 16) == 2748

def test_convert_digit_to_int():
    assert convert_digit_to_int('0') == 0
    assert convert_digit_to_int('1') == 1
    assert convert_digit_to_int('2') == 2
    assert convert_digit_to_int('3') == 3
    assert convert_digit_to_int('4') == 4
    assert convert_digit_to_int('5') == 5
    assert convert_digit_to_int('6') == 6
    assert convert_digit_to_int('7') == 7
    assert convert_digit_to_int('8') == 8
    assert convert_digit_to_int('9') == 9
    assert convert_digit_to_int('a') == 10
    assert convert_digit_to_int('b') == 11
    assert convert_digit_to_int('c') == 12
    assert convert_digit_to_int('d') == 13
    assert convert_digit_to_int('e') == 14
    assert convert_digit_to_int('f') == 15