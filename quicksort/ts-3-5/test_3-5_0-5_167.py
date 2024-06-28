import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)
sys.setrecursionlimit(1500)

from quicksort import quicksort

def test_quicksort_empty_list():
    ar = []
    assert quicksort(ar) == []

def test_quicksort_sorted_list():
    ar = [1, 2, 3, 4, 5]
    assert quicksort(ar) == [1, 2, 3, 4, 5]

def test_quicksort_reverse_sorted_list():
    ar = [5, 4, 3, 2, 1]
    assert quicksort(ar) == [1, 2, 3, 4, 5]

def test_quicksort_random_list():
    ar = [3, 7, 1, 9, 4, 2, 6, 5, 8]
    assert quicksort(ar) == [1, 2, 3, 4, 5, 6, 7, 8, 9]

def test_quicksort_duplicate_values():
    ar = [2, 1, 3, 2, 1, 3]
    assert quicksort(ar) == [1, 1, 2, 2, 3, 3]

def test_quicksort_single_element_list():
    ar = [1]
    assert quicksort(ar) == [1]

def test_quicksort_already_sorted_list():
    ar = [1, 2, 3, 4, 5]
    assert quicksort(ar) == [1, 2, 3, 4, 5]

def test_quicksort_large_list():
    ar = [100, 20, 40, 10, 50, 30, 90, 80, 60, 70]
    assert quicksort(ar) == [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]