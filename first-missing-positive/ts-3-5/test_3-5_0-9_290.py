import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from first_missing_positive import first_missing_positive

def test_first_missing_positive():
    # Test empty list
    assert first_missing_positive([]) == 1

    # Test list with only negative numbers
    assert first_missing_positive([-5, -1, -3]) == 1

    # Test list with only 1 element
    assert first_missing_positive([3]) == 1

    # Test list with all positive values
    assert first_missing_positive([1, 2, 3, 4, 5]) == 6

    # Test list with duplicates
    assert first_missing_positive([3, 2, 1, 3, 5]) == 4

    # Test list with missing positive numbers
    assert first_missing_positive([1, 3, 4, 2, 7]) == 5

    # Test list with negative numbers and missing positive numbers
    assert first_missing_positive([-3, 0, 2, -1, 4]) == 1

    # Test list with large numbers
    assert first_missing_positive([100, 101, 102, 105]) == 1