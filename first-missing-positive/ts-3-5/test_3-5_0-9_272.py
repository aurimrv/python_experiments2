import sys
import os
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from first_missing_positive import first_missing_positive

import pytest

def test_first_missing_positive_sorted_list():
    nums = [1, 2, 3, 4]
    assert first_missing_positive(nums) == 5

def test_first_missing_positive_unsorted_list():
    nums = [3, 4, -1, 1]
    assert first_missing_positive(nums) == 2

def test_first_missing_positive_with_duplicates():
    nums = [1, 2, 2, 4]
    assert first_missing_positive(nums) == 3

def test_first_missing_positive_negative_values():
    nums = [-1, -2, -3]
    assert first_missing_positive(nums) == 1

def test_first_missing_positive_with_zero():
    nums = [0, 2, 3, 4]
    assert first_missing_positive(nums) == 1

def test_first_missing_positive_single_element_list():
    nums = [5]
    assert first_missing_positive(nums) == 1

def test_first_missing_positive_empty_list():
    nums = []
    assert first_missing_positive(nums) == 1