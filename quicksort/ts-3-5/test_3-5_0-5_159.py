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
    ar = [3, 2, 5, 1, 4]
    assert quicksort(ar) == [1, 2, 3, 4, 5]

def test_quicksort_duplicate_elements():
    ar = [3, 2, 5, 1, 4, 2, 5]
    assert quicksort(ar) == [1, 2, 2, 3, 4, 5, 5]

def test_quicksort_large_list():
    ar = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    assert quicksort(ar) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def test_quicksort_single_element_list():
    ar = [1]
    assert quicksort(ar) == [1]

def test_quicksort_already_sorted_list():
    ar = [1, 2, 3, 4, 5]
    assert quicksort(ar) == [1, 2, 3, 4, 5]

def test_quicksort_negative_numbers():
    ar = [-5, -2, -4, -1, -3]
    assert quicksort(ar) == [-5, -4, -3, -2, -1]