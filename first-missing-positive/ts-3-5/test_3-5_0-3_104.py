import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from first_missing_positive import first_missing_positive

def test_first_missing_positive_basic():
    nums = [1, 2, 0]
    assert first_missing_positive(nums) == 3

def test_first_missing_positive_duplicates():
    nums = [3, 4, -1, 1, 1]
    assert first_missing_positive(nums) == 2

def test_first_missing_positive_negative_values():
    nums = [7, 8, -1, 9, 2, 1, 3, 4, 5]
    assert first_missing_positive(nums) == 6

def test_first_missing_positive_empty_list():
    nums = []
    assert first_missing_positive(nums) == 1

def test_first_missing_positive_large_input():
    nums = [1000, 1001, 1002, 1004]
    assert first_missing_positive(nums) == 1

def test_first_missing_positive_all_negative():
    nums = [-5, -3, -1, -2, -4]
    assert first_missing_positive(nums) == 1