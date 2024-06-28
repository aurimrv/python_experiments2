import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from first_missing_positive import first_missing_positive

def test_first_missing_positive_sorted_input():
    nums = [1, 2, 3, 4, 5]
    assert first_missing_positive(nums) == 6

def test_first_missing_positive_unsorted_input():
    nums = [3, 4, -1, 1]
    assert first_missing_positive(nums) == 2

def test_first_missing_positive_duplicates():
    nums = [1, 1, 2, 3]
    assert first_missing_positive(nums) == 4

def test_first_missing_positive_negative_values():
    nums = [-1, -2, 0, 3]
    assert first_missing_positive(nums) == 1

def test_first_missing_positive_large_input():
    nums = [1000, 1001, 1002, 1004]
    assert first_missing_positive(nums) == 1

def test_first_missing_positive_empty_input():
    nums = []
    assert first_missing_positive(nums) == 1