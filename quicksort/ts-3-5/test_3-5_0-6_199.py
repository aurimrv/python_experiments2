import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)
sys.setrecursionlimit(15000)

from quicksort import quicksort

def test_quicksort_empty_list():
    assert quicksort([]) == []

def test_quicksort_sorted_list():
    assert quicksort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_quicksort_reverse_sorted_list():
    assert quicksort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

def test_quicksort_random_list():
    assert quicksort([3, 7, 1, 5, 9, 2, 8, 4, 6]) == [1, 2, 3, 4, 5, 6, 7, 8, 9]

def test_quicksort_duplicate_values():
    assert quicksort([3, 7, 1, 5, 9, 2, 8, 5, 4, 6]) == [1, 2, 3, 4, 5, 5, 6, 7, 8, 9]

def test_quicksort_single_element_list():
    assert quicksort([1]) == [1]

def test_quicksort_already_sorted_list():
    assert quicksort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_quicksort_large_list():
    assert quicksort([9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
