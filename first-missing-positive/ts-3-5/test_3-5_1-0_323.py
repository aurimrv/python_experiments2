import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from first_missing_positive import first_missing_positive

def test_first_missing_positive_1():
    nums = [1, 2, 0]
    assert first_missing_positive(nums) == 3

def test_first_missing_positive_2():
    nums = [3, 4, -1, 1]
    assert first_missing_positive(nums) == 2

def test_first_missing_positive_3():
    nums = [7, 8, 9, 11, 12]
    assert first_missing_positive(nums) == 1

def test_first_missing_positive_4():
    nums = [2, 2, 3, 3, 7, 1]
    assert first_missing_positive(nums) == 4

def test_first_missing_positive_5():
    nums = [1, 2, 3, 4, 5]
    assert first_missing_positive(nums) == 6