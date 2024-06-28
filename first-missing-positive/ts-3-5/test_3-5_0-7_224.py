import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from first_missing_positive import first_missing_positive

def test_first_missing_positive_example1():
    nums = [3, 4, -1, 1]
    assert first_missing_positive(nums) == 2

def test_first_missing_positive_example2():
    nums = [1, 2, 0]
    assert first_missing_positive(nums) == 3

def test_first_missing_positive_sorted_input():
    nums = [1, 2, 3, 4]
    assert first_missing_positive(nums) == 5

def test_first_missing_positive_duplicates():
    nums = [3, 4, 3, 1]
    assert first_missing_positive(nums) == 2

def test_first_missing_positive_negative_values():
    nums = [-1, -2, -3]
    assert first_missing_positive(nums) == 1

def test_first_missing_positive_single_element():
    nums = [5]
    assert first_missing_positive(nums) == 1

def test_first_missing_positive_empty_list():
    nums = []
    assert first_missing_positive(nums) == 1