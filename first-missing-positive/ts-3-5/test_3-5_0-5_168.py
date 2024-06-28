import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from first_missing_positive import first_missing_positive

def test_first_missing_positive():
    # Test cases for first_missing_positive function

    # Test case for an empty list
    assert first_missing_positive([]) == 1

    # Test case for a list with only negative numbers
    assert first_missing_positive([-1, -5, -3]) == 1

    # Test case for a list with all positive numbers in order
    assert first_missing_positive([1, 2, 3, 4, 5]) == 6

    # Test case for a list with missing positive numbers
    assert first_missing_positive([3, 4, -1, 1]) == 2

    # Test case for a list with duplicates
    assert first_missing_positive([1, 1, 2, 3]) == 4

    # Test case for a list with large numbers
    assert first_missing_positive([1000, 1001, 1002]) == 1