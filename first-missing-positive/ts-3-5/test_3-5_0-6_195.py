import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from first_missing_positive import first_missing_positive

def test_first_missing_positive():
    # Test cases for positive integers
    assert first_missing_positive([1, 2, 0]) == 3
    assert first_missing_positive([3, 4, -1, 1]) == 2
    assert first_missing_positive([7, 8, 9, 11, 12]) == 1

def test_first_missing_positive_duplicates():
    # Test cases for duplicates
    assert first_missing_positive([1, 1, 2, 2]) == 3
    assert first_missing_positive([3, 3, 2, 1]) == 4

def test_first_missing_positive_negative():
    # Test cases with negative integers
    assert first_missing_positive([-1, -2, -3]) == 1
    assert first_missing_positive([-1, -2, 0]) == 1

def test_first_missing_positive_large_input():
    # Test case with large input
    assert first_missing_positive(list(range(1, 10001))) == 10001