import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from convert_base import convert_base, convert_digit_to_int

import pytest

def test_convert_base():
    assert convert_base('1010', 2) == 10  # Binary to decimal conversion
    assert convert_base('12A', 16) == 298  # Hexadecimal to decimal conversion
    assert convert_base('11', 3) == 4  # Ternary to decimal conversion

def test_convert_digit_to_int():
    assert convert_digit_to_int('A') == 10  # Convert hexadecimal 'A' to integer
    assert convert_digit_to_int('f') == 15  # Convert hexadecimal 'f' to integer
    assert convert_digit_to_int('7') == 7  # Convert decimal '7' to integer