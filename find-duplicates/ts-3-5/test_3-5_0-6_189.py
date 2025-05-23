import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from find_duplicates import duplicates_linear, duplicates_pre_sorted, duplicates_bin_search

# Test cases for duplicates_linear method
def test_duplicates_linear():
    arr1 = [1, 2, 3, 4, 5]
    arr2 = [2, 4, 6, 8, 10]
    assert duplicates_linear(arr1, arr2) == [2, 4]

    arr1 = [1, 2, 3, 4, 5]
    arr2 = [6, 7, 8, 9, 10]
    assert duplicates_linear(arr1, arr2) == []

# Test cases for duplicates_pre_sorted method
def test_duplicates_pre_sorted():
    arr1 = [1, 2, 3, 4, 5]
    arr2 = [2, 4, 6, 8, 10]
    assert duplicates_pre_sorted(arr1, arr2) == [2, 4]

    arr1 = [1, 2, 3, 4, 5]
    arr2 = [6, 7, 8, 9, 10]
    assert duplicates_pre_sorted(arr1, arr2) == []

# Test cases for duplicates_bin_search method
def test_duplicates_bin_search():
    arr1 = [1, 2, 3, 4, 5]
    arr2 = [2, 4, 6, 8, 10]
    assert duplicates_bin_search(arr1, arr2) == [2, 4]

    arr1 = [1, 2, 3, 4, 5]
    arr2 = [6, 7, 8, 9, 10]
    assert duplicates_bin_search(arr1, arr2) == []