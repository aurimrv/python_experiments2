import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from first_missing_positive import first_missing_positive

def test_first_missing_positive():
    # Test cases for the first_missing_positive function
    
    # Test with a simple list
    assert first_missing_positive([1, 2, 0]) == 3
    
    # Test with negative numbers
    assert first_missing_positive([-1, -2, -3]) == 1
    
    # Test with duplicates
    assert first_missing_positive([3, 4, -1, 1]) == 2
    
    # Test with a single positive number
    assert first_missing_positive([7]) == 1
    
    # Test with an empty list
    assert first_missing_positive([]) == 1
    
    # Test with a large list
    assert first_missing_positive([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 11
    
    # Test with a list containing only negative numbers
    assert first_missing_positive([-5, -3, -10, -1, -2]) == 1
    
    # Test with a list containing only positive numbers
    assert first_missing_positive([2, 3, 4, 5, 6, 7]) == 1