import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

import first_missing_positive

def test_first_missing_positive_empty_list():
    nums = []
    assert first_missing_positive.first_missing_positive(nums) == 1

def test_first_missing_positive_single_element_list():
    nums = [5]
    assert first_missing_positive.first_missing_positive(nums) == 1

def test_first_missing_positive_positive_integers():
    nums = [1, 2, 3, 4]
    assert first_missing_positive.first_missing_positive(nums) == 5

def test_first_missing_positive_negative_integer():
    nums = [-1, 2, 3, 4]
    assert first_missing_positive.first_missing_positive(nums) == 1

def test_first_missing_positive_duplicates():
    nums = [1, 1, 3, 4]
    assert first_missing_positive.first_missing_positive(nums) == 2

def test_first_missing_positive_mixed_integers():
    nums = [0, 2, 3, 4]
    assert first_missing_positive.first_missing_positive(nums) == 1

def test_first_missing_positive_large_list():
    nums = list(range(1, 10001))
    assert first_missing_positive.first_missing_positive(nums) == 10001