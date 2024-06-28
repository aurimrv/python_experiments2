import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from find_duplicates import duplicates_linear, duplicates_pre_sorted, duplicates_bin_search

# Test cases for duplicates_linear method
def test_duplicates_linear():
    # Test case where both arrays have common elements
    arr1 = [1, 2, 3, 4, 5]
    arr2 = [1, 5, 7, 9]
    expected_output = [1, 5]
    assert duplicates_linear(arr1, arr2) == expected_output

    # Test case where no common elements
    arr1 = [1, 2, 3, 4]
    arr2 = [5, 6, 7, 8]
    expected_output = []
    assert duplicates_linear(arr1, arr2) == expected_output

# Test cases for duplicates_pre_sorted method
def test_duplicates_pre_sorted():
    # Test case where both arrays have common elements
    arr1 = [1, 3, 5, 7, 9]
    arr2 = [2, 3, 5, 8, 9]
    expected_output = [3, 5, 9]
    assert duplicates_pre_sorted(arr1, arr2) == expected_output

    # Test case where one array is empty
    arr1 = []
    arr2 = [1, 2, 3]
    expected_output = []
    assert duplicates_pre_sorted(arr1, arr2) == expected_output

# Test cases for duplicates_bin_search method
def test_duplicates_bin_search():
    # Test case where both arrays have common elements
    arr1 = [1, 4, 6, 8, 10]
    arr2 = [2, 4, 6, 8, 10]
    expected_output = [4, 6, 8, 10]
    assert duplicates_bin_search(arr1, arr2) == expected_output

    # Test case where one array is empty
    arr1 = []
    arr2 = [1, 2, 3]
    expected_output = []
    assert duplicates_bin_search(arr1, arr2) == expected_output