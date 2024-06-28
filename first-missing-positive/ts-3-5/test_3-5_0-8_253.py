import os
import sys

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from first_missing_positive import first_missing_positive

def test_first_missing_positive():
    # Test cases for the first_missing_positive function
    
    # Test case for a basic scenario
    assert first_missing_positive([3, 4, -1, 1]) == 2

    # Test case for all negative numbers
    assert first_missing_positive([-1, -2, -3]) == 1

    # Test case for all positive numbers in order
    assert first_missing_positive([1, 2, 3, 4]) == 5

    # Test case for duplicates
    assert first_missing_positive([1, 1, 2, 3, 4]) == 5

    # Test case for empty list
    assert first_missing_positive([]) == 1

    # Test case for large numbers
    assert first_missing_positive([1000000, 2000000, 3000000, 4000000]) == 1

    # Test case with a mix of positive and negative numbers
    assert first_missing_positive([-1, 1, 3, -2]) == 2