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
    expected = []
    quicksort(ar)
    assert ar == expected

def test_quicksort_sorted_list():
    ar = [1, 2, 3, 4, 5]
    expected = [1, 2, 3, 4, 5]
    quicksort(ar)
    assert ar == expected

def test_quicksort_reverse_sorted_list():
    ar = [5, 4, 3, 2, 1]
    expected = [1, 2, 3, 4, 5]
    quicksort(ar)
    assert ar == expected

def test_quicksort_random_list():
    ar = [3, 1, 4, 1, 5, 9, 2, 6]
    expected = [1, 1, 2, 3, 4, 5, 6, 9]
    quicksort(ar)
    assert ar == expected

def test_quicksort_duplicate_values():
    ar = [3, 1, 4, 1, 5, 9, 2, 6, 2]
    expected = [1, 1, 2, 2, 3, 4, 5, 6, 9]
    quicksort(ar)
    assert ar == expected