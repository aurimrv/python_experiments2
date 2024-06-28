import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from first_missing_positive import first_missing_positive

def test_first_missing_positive():
    # Test cases for first_missing_positive function
    
    # Test empty list
    assert first_missing_positive([]) == 1

    # Test list with positive integers in order
    assert first_missing_positive([1, 2, 3, 4, 5]) == 6

    # Test list with negative numbers
    assert first_missing_positive([-1, -2, -3, -4]) == 1

    # Test list with duplicates
    assert first_missing_positive([1, 1, 2, 2, 3, 3]) == 4

    # Test list with out of order positive integers
    assert first_missing_positive([3, 4, 2, 1]) == 5

    # Test list with out of order positive and negative integers
    assert first_missing_positive([-1, 3, -2, 1]) == 2

    # Test list with missing positive integer
    assert first_missing_positive([1, 2, 3, 5, 6]) == 4

    # Test list with only one element
    assert first_missing_positive([1]) == 2

    # Test list with large positive integers
    assert first_missing_positive([1000, 2000, 3000]) == 1