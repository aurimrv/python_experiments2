import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from first_missing_positive import first_missing_positive

def test_first_missing_positive():
    # Test cases for the first_missing_positive function
    
    # Test case with positive integers in order
    assert first_missing_positive([1, 2, 3, 4, 5]) == 6
    
    # Test case with negative integers
    assert first_missing_positive([-1, -2, -3, -4]) == 1
    
    # Test case with duplicates
    assert first_missing_positive([1, 1, 2, 2, 3, 3]) == 4
    
    # Test case with missing positive integer
    assert first_missing_positive([1, 2, 3, 5]) == 4
    
    # Test case with large list of positive integers
    assert first_missing_positive([7, 8, 9, 11, 12, 15]) == 1

    # Test case with empty list
    assert first_missing_positive([]) == 1