import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from first_missing_positive import first_missing_positive

def test_first_missing_positive():
    # Test cases for the first_missing_positive function
    
    # Test with input list containing only positive integers
    assert first_missing_positive([1, 2, 3, 4, 5]) == 6
    
    # Test with input list containing negative integers
    assert first_missing_positive([-1, -2, -3]) == 1
    
    # Test with input list containing zeros
    assert first_missing_positive([0, 0, 0]) == 1
    
    # Test with input list containing duplicates
    assert first_missing_positive([1, 2, 2]) == 3
    
    # Test with input list containing a mix of positive and negative integers
    assert first_missing_positive([4, -1, 2, 3]) == 1
    
    # Test with input list containing a mix of positive and negative integers and zeros
    assert first_missing_positive([0, 3, 1, -2]) == 2
    
    # Test with empty input list
    assert first_missing_positive([]) == 1
    
    # Test with large input list with missing positive integer
    assert first_missing_positive([9, 8, 7, 6, 5, 4, 3, 2, 1]) == 10