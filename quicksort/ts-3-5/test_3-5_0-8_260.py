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

def test_quicksort_random_list():
    ar = [4, 2, 5, 1, 3]
    sorted_ar = quicksort(ar)
    assert sorted_ar == [1, 2, 3, 4, 5]

def test_quicksort_duplicate_elements():
    ar = [3, 2, 1, 2, 4, 3]
    sorted_ar = quicksort(ar)
    assert sorted_ar == [1, 2, 2, 3, 3, 4]

def test_quicksort_single_element_list():
    ar = [1]
    sorted_ar = quicksort(ar)
    assert sorted_ar == [1]