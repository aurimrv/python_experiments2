import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from find_duplicates import duplicates_linear, duplicates_pre_sorted, duplicates_bin_search
from binary_search import binary_search

def test_duplicates_linear():
    # Test case where duplicates exist
    assert duplicates_linear([1, 2, 3, 4], [3, 4, 5, 6]) == [3, 4]

    # Test case where no duplicates exist
    assert duplicates_linear([1, 2, 3, 4], [5, 6, 7, 8]) == []

def test_duplicates_pre_sorted():
    # Test case where duplicates exist
    assert duplicates_pre_sorted([1, 2, 3, 4], [3, 4, 5, 6]) == [3, 4]

    # Test case where no duplicates exist
    assert duplicates_pre_sorted([1, 2, 3, 4], [5, 6, 7, 8]) == []

def test_duplicates_bin_search():
    # Test case where duplicates exist
    assert duplicates_bin_search([1, 2, 3, 4], [3, 4, 5, 6]) == [3, 4]

    # Test case where no duplicates exist
    assert duplicates_bin_search([1, 2, 3, 4], [5, 6, 7, 8]) == []