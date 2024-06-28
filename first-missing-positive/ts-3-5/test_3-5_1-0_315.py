import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from first_missing_positive import first_missing_positive

def test_sorted_array():
    nums = [1, 2, 3, 4]
    assert first_missing_positive(nums) == 5

def test_unsorted_array():
    nums = [3, 4, -1, 1]
    assert first_missing_positive(nums) == 2

def test_negative_numbers():
    nums = [-1, -2, -3]
    assert first_missing_positive(nums) == 1

def test_duplicates():
    nums = [1, 1, 1, 1]
    assert first_missing_positive(nums) == 2

def test_mixed_array():
    nums = [7, 8, 9, 1, 2, 3, 5]
    assert first_missing_positive(nums) == 4

def test_large_array():
    nums = [1000] * 1000
    assert first_missing_positive(nums) == 1