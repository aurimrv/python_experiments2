import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from convert_base import convert_base, convert_digit_to_int

def test_convert_base():
    assert convert_base("1010", 2) == 10
    assert convert_base("A1", 16) == 161
    assert convert_base("123", 8) == 83
    assert convert_base("12", 5) == 7
    assert convert_base("101010", 2) == 42

def test_convert_digit_to_int():
    assert convert_digit_to_int("0") == 0
    assert convert_digit_to_int("5") == 5
    assert convert_digit_to_int("A") == 10
    assert convert_digit_to_int("F") == 15
    assert convert_digit_to_int("a") == 10
    assert convert_digit_to_int("f") == 15