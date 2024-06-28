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

    # Test cases for single element list
    assert first_missing_positive([0]) == 1
    assert first_missing_positive([1]) == 2

    # Test cases for multiple element list
    assert first_missing_positive([1, 2, 3]) == 4
    assert first_missing_positive([3, 4, -1, 1]) == 2
    assert first_missing_positive([7, 8, 9, 11, 12]) == 1
    assert first_missing_positive([1, 2, 0]) == 3
    assert first_missing_positive([2, 3, 4, 5]) == 1