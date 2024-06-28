import sys
import os
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)
sys.setrecursionlimit(15000)

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
    ar = [3, 1, 7, 5, 2, 4, 6]
    assert quicksort(ar) == [1, 2, 3, 4, 5, 6, 7]

def test_quicksort_duplicate_elements():
    ar = [3, 1, 2, 3, 2, 1]
    assert quicksort(ar) == [1, 1, 2, 2, 3, 3]

def test_quicksort_negative_values():
    ar = [-3, -1, -5, 0, -2, -4, -6]
    assert quicksort(ar) == [-6, -5, -4, -3, -2, -1, 0]