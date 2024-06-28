import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from first_missing_positive import first_missing_positive

def test_first_missing_positive_empty():
    nums = []
    assert first_missing_positive(nums) == 1

def test_first_missing_positive_single():
    nums = [5]
    assert first_missing_positive(nums) == 1

def test_first_missing_positive_positive_sequence():
    nums = [1, 2, 3, 4, 5]
    assert first_missing_positive(nums) == 6

def test_first_missing_positive_duplicate_values():
    nums = [1, 2, 3, 4, 4, 5]
    assert first_missing_positive(nums) == 6

def test_first_missing_positive_small_gap():
    nums = [1, 2, 3, 5]
    assert first_missing_positive(nums) == 4

def test_first_missing_positive_large_gap():
    nums = [1, 3, 5, 7]
    assert first_missing_positive(nums) == 2

def test_first_missing_positive_negative_values():
    nums = [-1, -2, 1, 2, 3]
    assert first_missing_positive(nums) == 4

def test_first_missing_positive_mixed_values():
    nums = [-1, 0, 1, 2, 4, 5]
    assert first_missing_positive(nums) == 3

def test_first_missing_positive_large_input():
    nums = [1000, 100, 10, 1, 2, 3, 4, 5, 6, 9, 8, 7, 11, 12, 1001]
    assert first_missing_positive(nums) == 13