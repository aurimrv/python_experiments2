import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from find_duplicates import duplicates_linear, duplicates_pre_sorted, duplicates_bin_search

def test_duplicates_linear():
    # Test case 1: Both arrays have duplicates
    assert duplicates_linear([1, 2, 3, 4, 2, 5], [2, 4, 6, 8, 2, 10]) == [2, 4, 2]

    # Test case 2: No duplicates
    assert duplicates_linear([1, 2, 3, 4], [5, 6, 7, 8]) == []

def test_duplicates_pre_sorted():
    # Test case 1: Both arrays have duplicates
    assert duplicates_pre_sorted([1, 2, 2, 3, 4, 5], [2, 2, 4, 6, 8, 10]) == [2, 2, 4]

    # Test case 2: No duplicates
    assert duplicates_pre_sorted([1, 2, 3, 4], [5, 6, 7, 8]) == []

def test_duplicates_bin_search():
    # Test case 1: Both arrays have duplicates
    assert duplicates_bin_search([1, 2, 3, 4, 5], [2, 4, 6, 8, 10]) == [2, 4]

    # Test case 2: No duplicates
    assert duplicates_bin_search([1, 2, 3, 4], [5, 6, 7, 8]) == []