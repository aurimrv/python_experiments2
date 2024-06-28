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

def test_first_missing_positive_duplicates():
    nums = [1, 1, 1, 1]
    assert first_missing_positive(nums) == 2

def test_first_missing_positive_negative():
    nums = [4, 5, -2, 0, 1]
    assert first_missing_positive(nums) == 2

def test_first_missing_positive_out_of_bounds():
    nums = [3, 6, 7, 8, 9]
    assert first_missing_positive(nums) == 1

def test_first_missing_positive_empty():
    nums = []
    assert first_missing_positive(nums) == 1