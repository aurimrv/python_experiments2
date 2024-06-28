import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from first_missing_positive import first_missing_positive

def test_first_missing_positive_case1():
    nums = [1, 2, 0]
    assert first_missing_positive(nums) == 3

def test_first_missing_positive_case2():
    nums = [3, 4, -1, 1]
    assert first_missing_positive(nums) == 2

def test_first_missing_positive_case3():
    nums = [7, 8, 9, 11, 12]
    assert first_missing_positive(nums) == 1

def test_first_missing_positive_case4():
    nums = [1, 1, 1, 1]
    assert first_missing_positive(nums) == 2

def test_first_missing_positive_case5():
    nums = [2, 2, 2, 2]
    assert first_missing_positive(nums) == 1

def test_first_missing_positive_case6():
    nums = [0, 0, 0, 0]
    assert first_missing_positive(nums) == 1

def test_first_missing_positive_case7():
    nums = [1, 2, 3, 4, 5]
    assert first_missing_positive(nums) == 6

def test_first_missing_positive_case8():
    nums = [5, 4, 3, 2, 1]
    assert first_missing_positive(nums) == 6