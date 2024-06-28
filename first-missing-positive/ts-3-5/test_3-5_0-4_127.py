import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from first_missing_positive import first_missing_positive

def test_first_missing_positive():
    # Test cases for first_missing_positive function
    
    # Test case for empty list
    assert first_missing_positive([]) == 1
    
    # Test case for single element list with negative number
    assert first_missing_positive([-5]) == 1
    
    # Test case for single element list with positive number
    assert first_missing_positive([3]) == 1
    
    # Test case for list with missing positive number at the beginning
    assert first_missing_positive([2, 3, 4, 5]) == 1
    
    # Test case for list with missing positive number in the middle
    assert first_missing_positive([1, 2, 4, 5]) == 3
    
    # Test case for list with missing positive number at the end
    assert first_missing_positive([1, 2, 3, 4]) == 5
    
    # Test case for list with negative numbers
    assert first_missing_positive([-1, -2, -3]) == 1
    
    # Test case for list with duplicates
    assert first_missing_positive([1, 1, 2, 3, 3, 4]) == 5