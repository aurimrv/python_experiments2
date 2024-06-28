import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from first_missing_positive import first_missing_positive

def test_first_missing_positive_example1():
    nums = [1, 2, 0]
    assert first_missing_positive(nums) == 3

def test_first_missing_positive_example2():
    nums = [3, 4, -1, 1]
    assert first_missing_positive(nums) == 2

def test_first_missing_positive_all_positive_integers():
    nums = [1, 2, 3, 4, 5]
    assert first_missing_positive(nums) == 6

def test_first_missing_positive_duplicates_and_out_of_order():
    nums = [3, 1, 2, 2, 5, 4]
    assert first_missing_positive(nums) == 6

def test_first_missing_positive_negative_numbers():
    nums = [-1, -2, -3]
    assert first_missing_positive(nums) == 1

def test_first_missing_positive_large_input():
    nums = list(range(1, 10001))
    assert first_missing_positive(nums) == 10001