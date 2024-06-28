import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from first_missing_positive import first_missing_positive

def test_first_missing_positive_basic():
    nums = [3, 4, -1, 1]
    assert first_missing_positive(nums) == 2

def test_first_missing_positive_duplicate():
    nums = [1, 1, 2, 3]
    assert first_missing_positive(nums) == 4

def test_first_missing_positive_all_positive():
    nums = [1, 2, 3, 4]
    assert first_missing_positive(nums) == 5

def test_first_missing_positive_negative_in_array():
    nums = [1, 2, -3, -4]
    assert first_missing_positive(nums) == 3

def test_first_missing_positive_empty_array():
    nums = []
    assert first_missing_positive(nums) == 1