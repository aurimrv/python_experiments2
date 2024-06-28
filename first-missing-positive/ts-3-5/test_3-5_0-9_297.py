import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from first_missing_positive import first_missing_positive

def test_first_missing_positive():
    # Testing when the first missing positive is 1
    nums = [3, 4, -1, 1]
    assert first_missing_positive(nums) == 2

    # Testing when the missing positive is in the middle
    nums = [7, 8, 9, 11, 12]
    assert first_missing_positive(nums) == 1

    # Testing when all elements are negative or 0
    nums = [-1, -5, 0, -3, -7]
    assert first_missing_positive(nums) == 1

    # Testing when there are duplicates
    nums = [1, 1, 2, 3, 4]
    assert first_missing_positive(nums) == 5

    # Testing when input list is empty
    nums = []
    assert first_missing_positive(nums) == 1

    # Testing when the list contains only one element being 1
    nums = [1]
    assert first_missing_positive(nums) == 2

    # Testing when the list contains only one element being negative
    nums = [-5]
    assert first_missing_positive(nums) == 1