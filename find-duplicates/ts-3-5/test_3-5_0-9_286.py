import os
import sys
project_dir = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
sys.path.append(project_dir)

from find_duplicates import duplicates_linear, duplicates_pre_sorted, duplicates_bin_search
from binary_search import binary_search

# Test cases for duplicates_linear function
def test_duplicates_linear():
    arr1 = [1, 2, 3, 4, 5]
    arr2 = [3, 4, 5, 6, 7]
    assert duplicates_linear(arr1, arr2) == [3, 4, 5]

    arr1 = [1, 2, 3]
    arr2 = [4, 5, 6]
    assert duplicates_linear(arr1, arr2) == []

# Test cases for duplicates_pre_sorted function
def test_duplicates_pre_sorted():
    arr1 = [1, 2, 3, 4, 5]
    arr2 = [3, 4, 5, 6, 7]
    assert duplicates_pre_sorted(arr1, arr2) == [3, 4, 5]

    arr1 = [1, 2, 3]
    arr2 = [4, 5, 6]
    assert duplicates_pre_sorted(arr1, arr2) == []

# Test cases for duplicates_bin_search function
def test_duplicates_bin_search():
    arr1 = [1, 2, 3, 4, 5]
    arr2 = [3, 4, 5, 6, 7]
    assert duplicates_bin_search(arr1, arr2) == [3, 4, 5]

    arr1 = [1, 2, 3]
    arr2 = [4, 5, 6]
    assert duplicates_bin_search(arr1, arr2) == []