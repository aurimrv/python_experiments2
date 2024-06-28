import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from first_missing_positive import first_missing_positive

def test_first_missing_positive():
    # Test cases for first_missing_positive function
    
    # Test case 1: Input list contains all positive integers
    assert first_missing_positive([1, 2, 3, 4, 5]) == 6

    # Test case 2: Input list contains negative numbers
    assert first_missing_positive([-1, -2, -3, 1, 2, 3]) == 4

    # Test case 3: Input list contains duplicates
    assert first_missing_positive([1, 2, 2, 3, 4, 5]) == 6

    # Test case 4: Input list contains only one element
    assert first_missing_positive([1]) == 2

    # Test case 5: Input list is empty
    assert first_missing_positive([]) == 1

    # Test case 6: Input list contains large numbers
    assert first_missing_positive([1000, 2000, 3000]) == 1