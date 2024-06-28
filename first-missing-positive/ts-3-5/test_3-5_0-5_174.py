import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from first_missing_positive import first_missing_positive

def test_first_missing_positive_sorted_list():
    nums = [1, 2, 3, 4, 5]
    assert first_missing_positive(nums) == 6

def test_first_missing_positive_unsorted_list():
    nums = [3, 4, -1, 1]
    assert first_missing_positive(nums) == 2

def test_first_missing_positive_duplicates():
    nums = [1, 2, 2, 1]
    assert first_missing_positive(nums) == 3

def test_first_missing_positive_empty_list():
    nums = []
    assert first_missing_positive(nums) == 1

def test_first_missing_positive_single_element():
    nums = [1]
    assert first_missing_positive(nums) == 2

def test_first_missing_positive_negative_numbers():
    nums = [-1, -2, -3]
    assert first_missing_positive(nums) == 1

def test_first_missing_positive_mixed_numbers():
    nums = [3, -1, 0, 2, 4]
    assert first_missing_positive(nums) == 1

def test_first_missing_positive_large_list():
    nums = list(range(1, 10001))
    assert first_missing_positive(nums) == 10001