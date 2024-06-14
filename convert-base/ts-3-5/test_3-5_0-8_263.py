import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from convert_base import convert_base, convert_digit_to_int

def test_convert_base():
    # Test valid conversion for base 2
    assert convert_base('1010', 2) == 10
    assert convert_base('1111', 2) == 15

    # Test valid conversion for base 10
    assert convert_base('123', 10) == 123
    assert convert_base('987', 10) == 987

    # Test valid conversion for base 16
    assert convert_base('af', 16) == 175
    assert convert_base('1ff', 16) == 511

    # Test for invalid base
    assert convert_base('123', -2) == -1
    assert convert_base('123', 12) == -1

def test_convert_digit_to_int():
    # Test valid hex digit conversion
    assert convert_digit_to_int('a') == 10
    assert convert_digit_to_int('f') == 15

    # Test invalid hex digit conversion
    assert convert_digit_to_int('g') == -1
    assert convert_digit_to_int('z') == -1