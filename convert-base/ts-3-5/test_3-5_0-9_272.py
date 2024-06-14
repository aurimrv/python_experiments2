import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

import convert_base

def test_convert_base():
    assert convert_base.convert_base('1010', 2) == 10
    assert convert_base.convert_base('a', 16) == 10
    assert convert_base.convert_base('123', 7) == 66

def test_convert_digit_to_int():
    assert convert_base.convert_digit_to_int('a') == 10
    assert convert_base.convert_digit_to_int('f') == 15
    assert convert_base.convert_digit_to_int('3') == 3