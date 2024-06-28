import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from first_missing_positive import first_missing_positive

def test_first_missing_positive_sorted_array():
    nums = [1, 2, 3, 4, 5, 6]
    assert first_missing_positive(nums) == 7

def test_first_missing_positive_unsorted_array():
    nums = [3, 4, -1, 1]
    assert first_missing_positive(nums) == 2

def test_first_missing_positive_duplicate_elements():
    nums = [1, 1, 1]
    assert first_missing_positive(nums) == 2

def test_first_missing_positive_single_element():
    nums = [2]
    assert first_missing_positive(nums) == 1

def test_first_missing_positive_negative_elements():
    nums = [-1, -2, -3]
    assert first_missing_positive(nums) == 1

def test_first_missing_positive_mixed_elements():
    nums = [1, 2, -1, -3]
    assert first_missing_positive(nums) == 3