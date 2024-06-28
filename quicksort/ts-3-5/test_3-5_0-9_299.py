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

def test_quicksort_single_element_list():
    ar = [5]
    assert quicksort(ar) == [5]

def test_quicksort_sorted_list():
    ar = [1, 2, 3, 4, 5]
    assert quicksort(ar) == [1, 2, 3, 4, 5]

def test_quicksort_reverse_sorted_list():
    ar = [5, 4, 3, 2, 1]
    assert quicksort(ar) == [1, 2, 3, 4, 5]

def test_quicksort_mixed_values():
    ar = [3, 5, 1, 4, 2]
    assert quicksort(ar) == [1, 2, 3, 4, 5]

def test_quicksort_duplicate_values():
    ar = [3, 2, 3, 1, 2]
    assert quicksort(ar) == [1, 2, 2, 3, 3]

def test_quicksort_large_list():
    ar = [10, 5, 7, 2, 8, 9, 1, 3, 6, 4]
    assert quicksort(ar) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]