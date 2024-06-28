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

def test_first_missing_positive_duplicates():
    nums = [3, 1, 2, 2, 0]
    assert first_missing_positive(nums) == 4

def test_first_missing_positive_negative():
    nums = [3, 1, 2, -1, 0]
    assert first_missing_positive(nums) == 4

def test_first_missing_positive_out_of_bounds():
    nums = [3, 1, 2, 5, 0]
    assert first_missing_positive(nums) == 4

def test_first_missing_positive_random():
    nums = [7, 3, 2, 1, 5, 6, 4]
    assert first_missing_positive(nums) == 8

def test_first_missing_positive_single():
    nums = [1]
    assert first_missing_positive(nums) == 2

def test_first_missing_positive_empty():
    nums = []
    assert first_missing_positive(nums) == 1