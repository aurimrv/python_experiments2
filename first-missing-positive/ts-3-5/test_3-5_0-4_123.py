import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from first_missing_positive import first_missing_positive

def test_first_missing_positive():
    # Test cases for the first_missing_positive function
    
    # Test when input list is empty
    assert first_missing_positive([]) == 1
    
    # Test when input list has only negative numbers
    assert first_missing_positive([-1, -5, -10]) == 1
    
    # Test when input list has positive numbers in sequence
    assert first_missing_positive([1, 2, 3, 4, 5]) == 6
    
    # Test when input list has duplicate positive numbers
    assert first_missing_positive([3, 1, 2, 2, 5]) == 4
    
    # Test when input list has missing positive numbers
    assert first_missing_positive([3, 4, -1, 1]) == 2
    
    # Test when input list has large positive numbers
    assert first_missing_positive([100, 200, 300, 400]) == 1