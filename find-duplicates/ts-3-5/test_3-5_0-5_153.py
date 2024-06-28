import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from find_duplicates import duplicates_linear, duplicates_pre_sorted, duplicates_bin_search

def test_duplicates_linear():
    # Test case where there are duplicates
    assert duplicates_linear([1, 2, 3, 4, 5], [3, 4, 5, 6, 7]) == [3, 4, 5]

    # Test case where there are no duplicates
    assert duplicates_linear([1, 2, 3], [4, 5, 6]) == []

def test_duplicates_pre_sorted():
    # Test case where there are duplicates
    assert duplicates_pre_sorted([1, 2, 3, 4, 5], [3, 4, 5, 6, 7]) == [3, 4, 5]

    # Test case where there are no duplicates
    assert duplicates_pre_sorted([1, 2, 3], [4, 5, 6]) == []

def test_duplicates_bin_search():
    # Test case where there are duplicates
    assert duplicates_bin_search([1, 2, 3, 4, 5], [3, 4, 5, 6, 7]) == [3, 4, 5]

    # Test case where there are no duplicates
    assert duplicates_bin_search([1, 2, 3], [4, 5, 6]) == []