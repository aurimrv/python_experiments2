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

def test_quicksort_duplicate_elements():
    ar = [3, 2, 1, 4, 3, 4, 2, 1]
    assert quicksort(ar) == [1, 1, 2, 2, 3, 3, 4, 4]

def test_quicksort_mixed_elements():
    ar = [5, 2, 8, 1, 3, 7, 4, 6]
    assert quicksort(ar) == [1, 2, 3, 4, 5, 6, 7, 8]

def test_quicksort_already_sorted_list():
    ar = [1, 2, 3, 4, 5]
    assert quicksort(ar) == [1, 2, 3, 4, 5]

def test_quicksort_single_element_list():
    ar = [1]
    assert quicksort(ar) == [1]

def test_quicksort_large_list():
    ar = [1000, 999, 998, 997, 996, 995, 994, 993, 992, 991]
    assert quicksort(ar) == [991, 992, 993, 994, 995, 996, 997, 998, 999, 1000]