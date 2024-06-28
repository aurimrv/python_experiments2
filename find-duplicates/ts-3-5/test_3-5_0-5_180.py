import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from find_duplicates import duplicates_linear, duplicates_pre_sorted, duplicates_bin_search

# Test cases for duplicates_linear
def test_duplicates_linear_case1():
    arr1 = [1, 2, 3, 4, 5]
    arr2 = [3, 4, 5, 6, 7]
    assert duplicates_linear(arr1, arr2) == [3, 4, 5]

def test_duplicates_linear_case2():
    arr1 = [1, 2, 3]
    arr2 = [4, 5, 6]
    assert duplicates_linear(arr1, arr2) == []

# Test cases for duplicates_pre_sorted
def test_duplicates_pre_sorted_case1():
    arr1 = [1, 2, 3, 4, 5]
    arr2 = [3, 4, 5, 6, 7]
    assert duplicates_pre_sorted(arr1, arr2) == [3, 4, 5]

def test_duplicates_pre_sorted_case2():
    arr1 = [1, 2, 3]
    arr2 = [4, 5, 6]
    assert duplicates_pre_sorted(arr1, arr2) == []

# Test cases for duplicates_bin_search
def test_duplicates_bin_search_case1():
    arr1 = [1, 2, 3, 4, 5]
    arr2 = [3, 4, 5, 6, 7]
    assert duplicates_bin_search(arr1, arr2) == [3, 4, 5]

def test_duplicates_bin_search_case2():
    arr1 = [1, 2, 3]
    arr2 = [4, 5, 6]
    assert duplicates_bin_search(arr1, arr2) == []