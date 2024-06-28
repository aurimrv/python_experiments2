import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)
sys.setrecursionlimit(15000)

from quicksort import quicksort

def test_quicksort_empty_list():
    ar = []
    assert quicksort(ar) == []

def test_quicksort_already_sorted_list():
    ar = [1, 2, 3, 4, 5]
    assert quicksort(ar) == [1, 2, 3, 4, 5]

def test_quicksort_reverse_sorted_list():
    ar = [5, 4, 3, 2, 1]
    assert quicksort(ar) == [1, 2, 3, 4, 5]

def test_quicksort_single_element_list():
    ar = [7]
    assert quicksort(ar) == [7]

def test_quicksort_duplicate_elements():
    ar = [2, 1, 4, 2, 3, 1]
    assert quicksort(ar) == [1, 1, 2, 2, 3, 4]

def test_quicksort_mixed_positive_negative_elements():
    ar = [-2, 4, -1, 0, 3, -3]
    assert quicksort(ar) == [-3, -2, -1, 0, 3, 4]