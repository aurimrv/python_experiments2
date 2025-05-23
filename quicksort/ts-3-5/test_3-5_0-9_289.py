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

def test_quicksort_duplicate_values_list():
    ar = [3, 5, 2, 5, 1, 3]
    assert quicksort(ar) == [1, 2, 3, 3, 5, 5]

def test_quicksort_negative_values_list():
    ar = [-3, 5, -2, 0, -1]
    assert quicksort(ar) == [-3, -2, -1, 0, 5]

def test_quicksort_mixed_values_list():
    ar = [2.5, -1, 0, 3.5, -0.5]
    assert quicksort(ar) == [-1, -0.5, 0, 2.5, 3.5]