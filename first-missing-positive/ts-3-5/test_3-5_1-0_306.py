import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from first_missing_positive import first_missing_positive

def test_first_missing_positive_empty_list():
    nums = []
    assert first_missing_positive(nums) == 1

def test_first_missing_positive_single_positive():
    nums = [1]
    assert first_missing_positive(nums) == 2

def test_first_missing_positive_sequence_with_gaps():
    nums = [3, 4, -1, 1]
    assert first_missing_positive(nums) == 2

def test_first_missing_positive_all_negative():
    nums = [-5, -1, -8]
    assert first_missing_positive(nums) == 1

def test_first_missing_positive_duplicates_and_out_of_order():
    nums = [7, 8, 9, 9, 6, 1, 4, 3, 2]
    assert first_missing_positive(nums) == 5

def test_first_missing_positive_all_positives_in_sequence():
    nums = [1, 2, 3, 4, 5]
    assert first_missing_positive(nums) == 6

def test_first_missing_positive_all_positives_not_in_sequence():
    nums = [5, 4, 3, 2, 1]
    assert first_missing_positive(nums) == 6
