import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from find_duplicates import duplicates_linear, duplicates_pre_sorted, duplicates_bin_search
from binary_search import binary_search

def test_duplicates_linear():
    arr1 = [1, 2, 3, 4, 5]
    arr2 = [3, 4, 5, 6, 7]
    assert duplicates_linear(arr1, arr2) == [3, 4, 5]

    arr1 = [10, 20, 30, 40, 50]
    arr2 = [5, 10, 15, 20, 25, 30]
    assert duplicates_linear(arr1, arr2) == [10, 20, 30]

def test_duplicates_pre_sorted():
    arr1 = [2, 3, 4, 5, 6]
    arr2 = [4, 5, 6, 7]
    assert duplicates_pre_sorted(arr1, arr2) == [4, 5, 6]

    arr1 = [10, 20, 30]
    arr2 = [30, 40, 50]
    assert duplicates_pre_sorted(arr1, arr2) == [30]

def test_duplicates_bin_search():
    arr1 = [1, 3, 5, 7, 9]
    arr2 = [2, 4, 6, 8, 10]
    assert duplicates_bin_search(arr1, arr2) == []

    arr1 = [2, 4, 6, 8]
    arr2 = [3, 6, 9, 12]
    assert duplicates_bin_search(arr1, arr2) == [6]