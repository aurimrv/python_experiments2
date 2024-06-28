import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from first_missing_positive import first_missing_positive

def test_first_missing_positive():
    # Test cases for the first_missing_positive function

    # Test case 1: Input list contains only negative numbers
    assert first_missing_positive([-1, -5, -3]) == 1

    # Test case 2: Input list contains only positive numbers
    assert first_missing_positive([1, 2, 3, 4]) == 5

    # Test case 3: Input list contains duplicate numbers
    assert first_missing_positive([1, 1, 2, 3, 4]) == 5

    # Test case 4: Input list contains a missing positive number
    assert first_missing_positive([3, 4, -1, 1]) == 2

    # Test case 5: Input list is empty
    assert first_missing_positive([]) == 1

    # Test case 6: Input list with all positive numbers but not sequential
    assert first_missing_positive([7, 8, 9, 1, 2, 3]) == 4

    # Test case 7: Input list with negative numbers and zeros
    assert first_missing_positive([-3, 0, 2, 4, 1]) == 3

    # Test case 8: Input list with large numbers
    assert first_missing_positive([1000, 2000, 5000, 3000]) == 1