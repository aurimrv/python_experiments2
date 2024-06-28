import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)
from first_missing_positive import first_missing_positive

def test_first_missing_positive():
    assert first_missing_positive([1, 2, 0]) == 3

def test_first_missing_positive_duplicates():
    assert first_missing_positive([3, 4, -1, 1]) == 2

def test_first_missing_positive_negative_values():
    assert first_missing_positive([-1, -2, -3]) == 1

def test_first_missing_positive_large_array():
    assert first_missing_positive([7, 8, 9, 11, 12]) == 1

def test_first_missing_positive_empty_array():
    assert first_missing_positive([]) == 1

def test_first_missing_positive_single_element():
    assert first_missing_positive([1]) == 2