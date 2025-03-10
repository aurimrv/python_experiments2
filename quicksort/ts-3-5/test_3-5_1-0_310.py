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

def test_quicksort_reversed_list():
    ar = [5, 4, 3, 2, 1]
    assert quicksort(ar) == [1, 2, 3, 4, 5]

def test_quicksort_duplicate_elements():
    ar = [3, 2, 5, 2, 1]
    assert quicksort(ar) == [1, 2, 2, 3, 5]

def test_quicksort_negative_elements():
    ar = [-5, 0, -3, -1, -4]
    assert quicksort(ar) == [-5, -4, -3, -1, 0]

def test_quicksort_large_list():
    ar = [100, 23, 45, 78, 12, 56, 89, 34, 67, 90]
    assert quicksort(ar) == [12, 23, 34, 45, 56, 67, 78, 89, 90, 100]