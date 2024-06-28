import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)
sys.setrecursionlimit(15000)
import quicksort

def test_quicksort_empty_list():
    ar = []
    assert quicksort.quicksort(ar) == []

def test_quicksort_sorted_list():
    ar = [1, 2, 3, 4, 5]
    assert quicksort.quicksort(ar) == [1, 2, 3, 4, 5]

def test_quicksort_reverse_sorted_list():
    ar = [5, 4, 3, 2, 1]
    assert quicksort.quicksort(ar) == [1, 2, 3, 4, 5]

def test_quicksort_mixed_list():
    ar = [2, 9, 1, 6, 4]
    assert quicksort.quicksort(ar) == [1, 2, 4, 6, 9]

def test_quicksort_duplicate_elements():
    ar = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
    assert quicksort.quicksort(ar) == [1, 1, 2, 3, 3, 4, 5, 5, 6, 9]

def test_quicksort_single_element_list():
    ar = [7]
    assert quicksort.quicksort(ar) == [7]

def test_quicksort_already_sorted_list():
    ar = [1, 2, 3, 4, 5]
    assert quicksort.quicksort(ar) == [1, 2, 3, 4, 5]

def test_quicksort_large_list():
    ar = [1000, 2000, 500, 1500, 3000, 2500]
    assert quicksort.quicksort(ar) == [500, 1000, 1500, 2000, 2500, 3000]