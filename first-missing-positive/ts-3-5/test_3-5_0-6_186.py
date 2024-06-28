import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from first_missing_positive import first_missing_positive

def test_first_missing_positive():
    # Test cases for the first_missing_positive function
    
    # Test case for empty list
    assert first_missing_positive([]) == 1

    # Test case with positive integers in sequential order
    assert first_missing_positive([1, 2, 3, 4, 5]) == 6

    # Test case with negative numbers
    assert first_missing_positive([-1, -2, -3, 1, 2, 3]) == 4

    # Test case with duplicate numbers
    assert first_missing_positive([1, 1, 2, 3]) == 4

    # Test case with missing positive integer in the middle
    assert first_missing_positive([1, 2, 4, 5]) == 3

    # Test case with missing positive integer at the beginning
    assert first_missing_positive([3, 4, 5]) == 1

    # Test case with missing positive integer at the end
    assert first_missing_positive([1, 2, 3, 4]) == 5

    # Test case with large numbers
    assert first_missing_positive([1000, 2000, 3000]) == 1