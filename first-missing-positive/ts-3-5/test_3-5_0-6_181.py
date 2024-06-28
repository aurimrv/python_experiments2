import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from first_missing_positive import first_missing_positive

def test_first_missing_positive():
    # Test cases for first_missing_positive function
    
    # Test case where the missing positive integer is 1
    assert first_missing_positive([3, 4, -1, 1]) == 2
    
    # Test case where the missing positive integer is 2
    assert first_missing_positive([1, 3, 4, 5]) == 2
    
    # Test case where the missing positive integer is 3
    assert first_missing_positive([1, 2, 4, 5]) == 3
    
    # Test case where the missing positive integer is 4
    assert first_missing_positive([1, 2, 3, 5]) == 4
    
    # Test case where the missing positive integer is 5
    assert first_missing_positive([1, 2, 3, 4]) == 5
    
    # Test case with negative numbers
    assert first_missing_positive([-1, -2, 0, 1]) == 2
    
    # Test case with duplicates
    assert first_missing_positive([1, 1, 2, 2]) == 3
    
    # Test case with only negative numbers
    assert first_missing_positive([-1, -2, -3, -4]) == 1