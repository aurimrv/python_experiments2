import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from first_missing_positive import first_missing_positive

def test_first_missing_positive():
    # Test cases for first_missing_positive function

    # Test case for empty list
    assert first_missing_positive([]) == 1

    # Test case for list with negative numbers
    assert first_missing_positive([-1, -2, -3]) == 1

    # Test case for list with positive numbers in sequence
    assert first_missing_positive([1, 2, 3, 4, 5]) == 6

    # Test case for list with positive numbers out of order
    assert first_missing_positive([3, 4, -1, 1]) == 2

    # Test case for list with duplicates
    assert first_missing_positive([1, 1, 2, 2, 3, 3]) == 4

    # Test case for list with large numbers
    assert first_missing_positive([1000, 1001, 1002]) == 1