import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from find_duplicates import duplicates_linear, duplicates_pre_sorted, duplicates_bin_search

def test_duplicates_linear():
    arr1 = [1, 2, 3, 4, 5]
    arr2 = [3, 4, 5, 6, 7]
    
    # Test case 1: One duplicate
    assert duplicates_linear(arr1, arr2) == [3, 4, 5]
    
    # Test case 2: No duplicates
    assert duplicates_linear([1, 2, 3], [4, 5, 6]) == []
    
    # Test case 3: Empty arrays
    assert duplicates_linear([], []) == []
    
def test_duplicates_pre_sorted():
    arr1 = [1, 2, 3, 4, 5]
    arr2 = [3, 4, 5, 6, 7]
    
    # Test case 1: One duplicate
    assert duplicates_pre_sorted(arr1, arr2) == [3, 4, 5]
    
    # Test case 2: No duplicates
    assert duplicates_pre_sorted([1, 2, 3], [4, 5, 6]) == []
    
    # Test case 3: Empty arrays
    assert duplicates_pre_sorted([], []) == []
    
def test_duplicates_bin_search():
    arr1 = [1, 2, 3, 4, 5]
    arr2 = [3, 4, 5, 6, 7]
    
    # Test case 1: One duplicate
    assert duplicates_bin_search(arr1, arr2) == [3, 4, 5]
    
    # Test case 2: No duplicates
    assert duplicates_bin_search([1, 2, 3], [4, 5, 6]) == []
    
    # Test case 3: Empty arrays
    assert duplicates_bin_search([], []) == []