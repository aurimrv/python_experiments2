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

def test_quicksort_already_sorted():
    ar = [1, 2, 3, 4, 5]
    assert quicksort(ar) == [1, 2, 3, 4, 5]

def test_quicksort_reverse_sorted():
    ar = [5, 4, 3, 2, 1]
    assert quicksort(ar) == [1, 2, 3, 4, 5]

def test_quicksort_duplicate_elements():
    ar = [3, 1, 4, 1, 5]
    assert quicksort(ar) == [1, 1, 3, 4, 5]

def test_quicksort_negative_elements():
    ar = [-5, 10, -3, 0, 8]
    assert quicksort(ar) == [-5, -3, 0, 8, 10]

def test_quicksort_large_list():
    ar = [1000, 2000, 500, 1500, 3000, 2500]
    assert quicksort(ar) == [500, 1000, 1500, 2000, 2500, 3000]