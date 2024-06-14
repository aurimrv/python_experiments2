import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from complement import complement

def test_complement_zero_input():
    assert complement(0) == 1

def test_complement_positive_number():
    assert complement(5) == 2

def test_complement_power_of_two():
    assert complement(8) == 7

def test_complement_large_number():
    assert complement(123) == 4

def test_complement_negative_number():
    assert complement(-5) == -5

def test_complement_max_int():
    assert complement(2147483647) == 0