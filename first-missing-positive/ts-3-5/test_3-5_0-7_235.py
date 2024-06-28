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
    
    # Test case for single element list with 1
    assert first_missing_positive([1]) == 2
    
    # Test case for single element list with 2
    assert first_missing_positive([2]) == 1
    
    # Test case for positive consecutive integers
    assert first_missing_positive([1, 2, 3, 4, 5]) == 6
    
    # Test case for negative integers
    assert first_missing_positive([-1, -2, -3]) == 1
    
    # Test case for mix of negative and positive integers
    assert first_missing_positive([-1, 1, 3, 4, 5]) == 2
    
    # Test case for duplicate integers
    assert first_missing_positive([1, 1, 2, 3, 4]) == 5
    
    # Test case for large list of integers
    assert first_missing_positive([7, 8, 9, 11, 12, 13]) == 1