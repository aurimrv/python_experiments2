import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from first_missing_positive import first_missing_positive

def test_first_missing_positive():
    # Test case for empty list
    assert first_missing_positive([]) == 1

    # Test case for list with negative numbers
    assert first_missing_positive([-1, -2, -3]) == 1

    # Test case for list with positive numbers in sequence
    assert first_missing_positive([1, 2, 3, 4, 5]) == 6

    # Test case for list with missing positive number
    assert first_missing_positive([1, 2, 3, 5]) == 4

    # Test case for list with duplicates
    assert first_missing_positive([1, 2, 2, 3, 3, 4]) == 5

    # Test case for list with large numbers
    assert first_missing_positive([1000, 2000, 3000]) == 1