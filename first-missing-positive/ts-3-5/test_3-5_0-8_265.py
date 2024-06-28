import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from first_missing_positive import first_missing_positive

def test_first_missing_positive():
    # Test cases for the first_missing_positive function
    
    # Test empty list
    assert first_missing_positive([]) == 1
    
    # Test case where the missing positive is at the start
    assert first_missing_positive([-1, -2, 0, 1, 2, 4]) == 3
    
    # Test case where the missing positive is in the middle
    assert first_missing_positive([3, 4, -1, 1]) == 2
    
    # Test case where all negatives and zeros are removed
    assert first_missing_positive([0, -1, -2, 1, 2, 3]) == 4
    
    # Test case where the missing positive is at the end
    assert first_missing_positive([1, 2, 3, 4, 5]) == 6
    
    # Test case where all numbers are negative
    assert first_missing_positive([-1, -2, -3, -4]) == 1
    
    # Test case where input contains duplicates
    assert first_missing_positive([1, 1, 2, 3, 5]) == 4