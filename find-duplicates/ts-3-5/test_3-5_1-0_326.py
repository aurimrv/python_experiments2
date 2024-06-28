import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from find_duplicates import duplicates_linear, duplicates_pre_sorted, duplicates_bin_search

def test_duplicates_linear_empty_arrays():
    arr1 = []
    arr2 = []
    assert duplicates_linear(arr1, arr2) == []

def test_duplicates_linear_no_duplicates():
    arr1 = [1, 2, 3]
    arr2 = [4, 5, 6]
    assert duplicates_linear(arr1, arr2) == []

def test_duplicates_linear_with_duplicates():
    arr1 = [1, 2, 3, 4]
    arr2 = [3, 4, 5, 6]
    assert duplicates_linear(arr1, arr2) == [3, 4]

def test_duplicates_pre_sorted_empty_arrays():
    arr1 = []
    arr2 = []
    assert duplicates_pre_sorted(arr1, arr2) == []

def test_duplicates_pre_sorted_no_duplicates():
    arr1 = [1, 2, 3]
    arr2 = [3, 4, 5]
    assert duplicates_pre_sorted(arr1, arr2) == [3]

def test_duplicates_pre_sorted_with_duplicates():
    arr1 = [1, 2, 3, 4]
    arr2 = [3, 4, 5, 6]
    assert duplicates_pre_sorted(arr1, arr2) == [3, 4]

def test_duplicates_bin_search_empty_arrays():
    arr1 = []
    arr2 = []
    assert duplicates_bin_search(arr1, arr2) == []

def test_duplicates_bin_search_no_duplicates():
    arr1 = [1, 2, 3]
    arr2 = [4, 5, 6]
    assert duplicates_bin_search(arr1, arr2) == []

def test_duplicates_bin_search_with_duplicates():
    arr1 = [1, 2, 3, 4]
    arr2 = [3, 4, 5, 6]
    assert duplicates_bin_search(arr1, arr2) == [3, 4]