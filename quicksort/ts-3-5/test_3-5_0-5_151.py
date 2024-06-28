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

def test_quicksort_single_element_list():
    ar = [5]
    assert quicksort(ar) == [5]

def test_quicksort_sorted_list():
    ar = [1, 2, 3, 4, 5]
    assert quicksort(ar) == [1, 2, 3, 4, 5]

def test_quicksort_reverse_sorted_list():
    ar = [5, 4, 3, 2, 1]
    assert quicksort(ar) == [1, 2, 3, 4, 5]

def test_quicksort_random_list():
    ar = [3, 7, 2, 1, 9, 4, 6, 8, 5]
    assert quicksort(ar) == [1, 2, 3, 4, 5, 6, 7, 8, 9]

def test_quicksort_duplicate_elements():
    ar = [5, 2, 7, 5, 3, 2, 8, 5]
    assert quicksort(ar) == [2, 2, 3, 5, 5, 5, 7, 8]

def test_quicksort_negative_elements():
    ar = [-5, 2, -7, 0, 3, -2, 8, -1]
    assert quicksort(ar) == [-7, -5, -2, -1, 0, 2, 3, 8]