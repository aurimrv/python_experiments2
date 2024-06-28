import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from first_missing_positive import first_missing_positive

def test_first_missing_positive():
    # Test cases for first_missing_positive method
    assert first_missing_positive([1, 2, 0]) == 3
    assert first_missing_positive([3, 4, -1, 1]) == 2

def test_start_equals_end():
    # Test cases when start equals end
    assert first_missing_positive([1]) == 2
    assert first_missing_positive([2]) == 1

def test_negative_numbers():
    # Test cases with negative numbers
    assert first_missing_positive([-1, -2, -3]) == 1
    assert first_missing_positive([-3, -5, 4]) == 1

def test_duplicates():
    # Test cases with duplicates
    assert first_missing_positive([3, 3, 3]) == 1
    assert first_missing_positive([1, 1, 2, 2, 3, 3]) == 4