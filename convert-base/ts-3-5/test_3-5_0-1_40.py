import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from convert_base import convert_base, convert_digit_to_int

import pytest

def test_convert_base():
    assert convert_base('1010', 2) == 10
    assert convert_base('ff', 16) == 255
    assert convert_base('123', 8) == 83
    assert convert_base('abc', 16) == 2748
    assert convert_base('xyz', 16) == -1
    assert convert_base('123', 2) == -1
    assert convert_base('123', 11) == -1

def test_convert_digit_to_int():
    assert convert_digit_to_int('0') == 0
    assert convert_digit_to_int('9') == 9
    assert convert_digit_to_int('a') == 10
    assert convert_digit_to_int('f') == 15
    assert convert_digit_to_int('g') == -1
    assert convert_digit_to_int('12') == -1