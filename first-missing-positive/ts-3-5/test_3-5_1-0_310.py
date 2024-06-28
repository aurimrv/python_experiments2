import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from first_missing_positive import first_missing_positive

def test_first_missing_positive_sorted_list():
    nums = [1, 2, 3, 4, 5]
    assert first_missing_positive(nums) == 6

def test_first_missing_positive_unsorted_list():
    nums = [3, 4, -1, 1, -2, 6, 5]
    assert first_missing_positive(nums) == 2

def test_first_missing_positive_duplicate_values():
    nums = [3, 4, 4, 1, -2, 6, 5]
    assert first_missing_positive(nums) == 2

def test_first_missing_positive_all_negative_values():
    nums = [-3, -5, -1, -2, -4]
    assert first_missing_positive(nums) == 1

def test_first_missing_positive_empty_list():
    nums = []
    assert first_missing_positive(nums) == 1