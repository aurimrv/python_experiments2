import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from first_missing_positive import first_missing_positive

def test_first_missing_positive():
    # Test 1: Provided example
    assert first_missing_positive([3, 4, -1, 1]) == 2
    
    # Test 2: All negative numbers
    assert first_missing_positive([-1, -2, -3]) == 1
    
    # Test 3: Random order with missing positive number
    assert first_missing_positive([7, 8, 9, 11, 12]) == 1
    
    # Test 4: No missing positive numbers
    assert first_missing_positive([1, 2, 3, 4, 5]) == 6