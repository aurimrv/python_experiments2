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

def test_quicksort_sorted_list():
    ar = [1, 2, 3, 4, 5]
    assert quicksort(ar) == [1, 2, 3, 4, 5]

def test_quicksort_reverse_sorted_list():
    ar = [5, 4, 3, 2, 1]
    assert quicksort(ar) == [1, 2, 3, 4, 5]

def test_quicksort_duplicate_values():
    ar = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
    assert quicksort(ar) == [1, 1, 2, 3, 3, 4, 5, 5, 6, 9]

def test_quicksort_negative_values():
    ar = [-5, -3, -1, -7, -2]
    assert quicksort(ar) == [-7, -5, -3, -2, -1]

def test_quicksort_mixed_values():
    ar = [5, -3, 0, 2, -1, 8, -2]
    assert quicksort(ar) == [-3, -2, -1, 0, 2, 5, 8]

def test_quicksort_large_list():
    ar = [i for i in range(1000, 0, -1)]
    assert quicksort(ar) == [i for i in range(1, 1001)]