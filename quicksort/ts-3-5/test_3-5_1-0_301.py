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

def test_quicksort_sorted_list():
    ar = [1, 2, 3, 4, 5]
    sorted_ar = quicksort(ar)
    assert sorted_ar == [1, 2, 3, 4, 5]

def test_quicksort_reverse_sorted_list():
    ar = [5, 4, 3, 2, 1]
    sorted_ar = quicksort(ar)
    assert sorted_ar == [1, 2, 3, 4, 5]

def test_quicksort_negative_numbers():
    ar = [5, -3, 0, -1, 2]
    sorted_ar = quicksort(ar)
    assert sorted_ar == [-3, -1, 0, 2, 5]

def test_quicksort_duplicate_values():
    ar = [3, 2, 1, 2, 3]
    sorted_ar = quicksort(ar)
    assert sorted_ar == [1, 2, 2, 3, 3]

def test_quicksort_single_element_list():
    ar = [42]
    sorted_ar = quicksort(ar)
    assert sorted_ar == [42]