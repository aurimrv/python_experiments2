import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)
sys.setrecursionlimit(15000)

import quicksort

import pytest

def test_quicksort_empty_list():
    ar = []
    result = quicksort.quicksort(ar)
    assert result == []

def test_quicksort_sorted_list():
    ar = [1, 2, 3, 4, 5]
    result = quicksort.quicksort(ar)
    assert result == [1, 2, 3, 4, 5]

def test_quicksort_reverse_sorted_list():
    ar = [5, 4, 3, 2, 1]
    result = quicksort.quicksort(ar)
    assert result == [1, 2, 3, 4, 5]

def test_quicksort_duplicate_elements():
    ar = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
    result = quicksort.quicksort(ar)
    assert result == [1, 1, 2, 3, 3, 4, 5, 5, 6, 9]

def test_quicksort_negative_numbers():
    ar = [-5, -1, -3, -2, -4]
    result = quicksort.quicksort(ar)
    assert result == [-5, -4, -3, -2, -1]

def test_quicksort_mixed_elements():
    ar = [-2, 3, 0, -1, 5]
    result = quicksort.quicksort(ar)
    assert result == [-2, -1, 0, 3, 5]