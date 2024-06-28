import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from first_missing_positive import first_missing_positive

def test_first_missing_positive():
    assert first_missing_positive([1, 2, 0]) == 3
    assert first_missing_positive([3, 4, -1, 1]) == 2
    assert first_missing_positive([7, 8, 9, 11, 12]) == 1

def test_first_missing_positive_duplicates():
    assert first_missing_positive([1, 1, 3, 4, 2]) == 5
    assert first_missing_positive([1, 1, 1, 1, 1]) == 2

def test_first_missing_positive_negative_values():
    assert first_missing_positive([-1, -2, -3]) == 1
    assert first_missing_positive([-5, 0, 5]) == 1

def test_first_missing_positive_large_input():
    assert first_missing_positive(list(range(1, 1001))) == 1001
    assert first_missing_positive(list(range(1, 1000001))) == 1000001