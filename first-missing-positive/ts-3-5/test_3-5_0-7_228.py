import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from first_missing_positive import first_missing_positive

def test_first_missing_positive():
    # Test cases for empty list
    assert first_missing_positive([]) == 1

    # Test cases for positive integers only
    assert first_missing_positive([3, 4, -1, 1]) == 2
    assert first_missing_positive([1, 2, 0]) == 3

    # Test cases for negative integers only
    assert first_missing_positive([-1, -2, -3]) == 1

    # Test cases for mixed positive and negative integers
    assert first_missing_positive([-1, 2, 3, 4]) == 1
    assert first_missing_positive([-1, -2, 1, 3]) == 2

    # Test cases for duplicate positive integers
    assert first_missing_positive([1, 1, 2, 2]) == 3
    assert first_missing_positive([3, 3, 1, 2]) == 4

    # Test cases for large list of positive integers
    assert first_missing_positive(list(range(1, 1001))) == 1001
    assert first_missing_positive(list(range(-1000, 1001))) == 1001

    # Test cases for large list of negative integers
    assert first_missing_positive(list(range(-1000, 0))) == 1
    assert first_missing_positive(list(range(-1000, -500))) == 1