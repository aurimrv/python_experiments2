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
    result = quicksort(ar)
    assert result == []

def test_quicksort_sorted_list():
    ar = [1, 2, 3, 4, 5]
    result = quicksort(ar)
    assert result == [1, 2, 3, 4, 5]

def test_quicksort_reverse_sorted_list():
    ar = [5, 4, 3, 2, 1]
    result = quicksort(ar)
    assert result == [1, 2, 3, 4, 5]

def test_quicksort_random_list():
    ar = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    result = quicksort(ar)
    assert result == [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

def test_quicksort_single_element_list():
    ar = [7]
    result = quicksort(ar)
    assert result == [7]

def test_quicksort_duplicate_elements_list():
    ar = [5, 9, 2, 4, 9, 2, 1, 8, 3]
    result = quicksort(ar)
    assert result == [1, 2, 2, 3, 4, 5, 8, 9, 9]