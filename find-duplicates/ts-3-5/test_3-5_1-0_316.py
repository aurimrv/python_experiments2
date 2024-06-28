import os
import sys
module_path = os.path.dirname(os.path.abspath(__file__))
project_path = os.path.abspath(os.path.join(module_path, '..'))
sys.path.append(project_path)

from find_duplicates import duplicates_linear, duplicates_pre_sorted, duplicates_bin_search

def test_duplicates_linear():
    # Test case with duplicates
    assert duplicates_linear([1, 2, 3, 4, 5], [3, 4, 5, 6, 7]) == [3, 4, 5]

    # Test case with no duplicates
    assert duplicates_linear([1, 2, 3], [4, 5, 6]) == []

def test_duplicates_pre_sorted():
    # Test case with duplicates
    assert duplicates_pre_sorted([1, 2, 3, 4, 5], [3, 4, 5, 6, 7]) == [3, 4, 5]

    # Test case with no duplicates
    assert duplicates_pre_sorted([1, 2, 3], [4, 5, 6]) == []

def test_duplicates_bin_search():
    # Test case with duplicates
    assert duplicates_bin_search([1, 2, 3, 4, 5], [3, 4, 5, 6, 7]) == [3, 4, 5]

    # Test case with no duplicates
    assert duplicates_bin_search([1, 2, 3], [4, 5, 6]) == []