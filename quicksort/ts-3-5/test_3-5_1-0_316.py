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

def test_quicksort_random_list():
    ar = [5, 2, 3, 1, 4]
    assert quicksort(ar) == [1, 2, 3, 4, 5]

def test_quicksort_duplicates():
    ar = [4, 2, 3, 1, 4]
    assert quicksort(ar) == [1, 2, 3, 4, 4]

def test_quicksort_negative_values():
    ar = [-4, 2, -3, 1, 0]
    assert quicksort(ar) == [-4, -3, 0, 1, 2]

def test_quicksort_large_list():
    ar = list(range(100, 0, -1))
    assert quicksort(ar) == list(range(1, 101))