import os
import sys

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from find_duplicates import duplicates_linear, duplicates_pre_sorted, duplicates_bin_search

arr1 = [2, 4, 6, 8, 10]
arr2 = [1, 3, 5, 7, 9, 2, 6]

def test_duplicates_linear():
    assert duplicates_linear([1, 2, 3], [2, 4, 6]) == [2]
    assert duplicates_linear([1, 2, 3], [4, 5, 6]) == []
    assert duplicates_linear([1, 2, 3], [1, 2, 3]) == [1, 2, 3]

def test_duplicates_pre_sorted():
    assert duplicates_pre_sorted([1, 2, 3, 5], [2, 4, 6]) == [2]
    assert duplicates_pre_sorted([1, 2, 3], [4, 5, 6]) == []
    assert duplicates_pre_sorted([2, 3, 4, 5], [1, 2, 3, 4]) == [2, 3, 4]

def test_duplicates_bin_search():
    assert duplicates_bin_search([1, 2, 3], [2, 4, 6]) == [2]
    assert duplicates_bin_search([1, 2, 3], [4, 5, 6]) == []
    assert duplicates_bin_search([7, 8, 9], [5, 6, 9]) == [9]