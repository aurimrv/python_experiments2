import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from first_missing_positive import first_missing_positive

def test_first_missing_positive_sorted_input():
    nums = [1, 2, 3, 4]
    assert first_missing_positive(nums) == 5

def test_first_missing_positive_unsorted_input():
    nums = [3, 4, -1, 1]
    assert first_missing_positive(nums) == 2

def test_first_missing_positive_with_duplicates():
    nums = [1, 2, 2, 3]
    assert first_missing_positive(nums) == 4

def test_first_missing_positive_with_negative_numbers():
    nums = [-1, -2, -3]
    assert first_missing_positive(nums) == 1

def test_first_missing_positive_with_large_numbers():
    nums = [1000, 1001, 1002]
    assert first_missing_positive(nums) == 1