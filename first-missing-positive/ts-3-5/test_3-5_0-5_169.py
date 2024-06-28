import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from first_missing_positive import first_missing_positive

def test_first_missing_positive():
    # Test cases for the first_missing_positive function
    
    # Test case with positive integers in ascending order
    assert first_missing_positive([1, 2, 3, 4, 5]) == 6
    
    # Test case with negative integers
    assert first_missing_positive([-1, -2, -3]) == 1
    
    # Test case with positive integers in random order
    assert first_missing_positive([3, 4, -1, 1]) == 2
    
    # Test case with duplicates
    assert first_missing_positive([1, 1, 2, 3, 4]) == 5
    
    # Test case with empty list
    assert first_missing_positive([]) == 1
    
    # Test case with large positive integers
    assert first_missing_positive([1000, 1001, 1002]) == 1
    
    # Test case with large negative integers
    assert first_missing_positive([-100, -99, -98]) == 1