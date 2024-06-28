import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from first_missing_positive import first_missing_positive

def test_first_missing_positive_sorted():
    nums = [1, 2, 3, 4, 6]
    assert first_missing_positive(nums) == 5

def test_first_missing_positive_unsorted():
    nums = [3, 4, -1, 1]
    assert first_missing_positive(nums) == 2

def test_first_missing_positive_duplicates():
    nums = [1, 1, 2, 3]
    assert first_missing_positive(nums) == 4

def test_first_missing_positive_negative_values():
    nums = [-1, -2, -3]
    assert first_missing_positive(nums) == 1

def test_first_missing_positive_large_numbers():
    nums = [1000, 1002, 1005, 1001]
    assert first_missing_positive(nums) == 1