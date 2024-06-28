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
    sorted_ar = quicksort(ar)
    assert sorted_ar == []

def test_quicksort_already_sorted():
    ar = [1, 2, 3, 4, 5]
    sorted_ar = quicksort(ar)
    assert sorted_ar == [1, 2, 3, 4, 5]

def test_quicksort_reversed_list():
    ar = [5, 4, 3, 2, 1]
    sorted_ar = quicksort(ar)
    assert sorted_ar == [1, 2, 3, 4, 5]

def test_quicksort_random_list():
    ar = [4, 2, 5, 1, 3]
    sorted_ar = quicksort(ar)
    assert sorted_ar == [1, 2, 3, 4, 5]

def test_quicksort_duplicate_values():
    ar = [3, 1, 2, 3, 2, 1]
    sorted_ar = quicksort(ar)
    assert sorted_ar == [1, 1, 2, 2, 3, 3]