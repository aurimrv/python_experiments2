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
    quicksort(ar)
    assert ar == []

def test_quicksort_sorted_list():
    ar = [1, 2, 3, 4, 5]
    quicksort(ar)
    assert ar == [1, 2, 3, 4, 5]

def test_quicksort_reverse_list():
    ar = [5, 4, 3, 2, 1]
    quicksort(ar)
    assert ar == [1, 2, 3, 4, 5]

def test_quicksort_random_list():
    ar = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    quicksort(ar)
    assert ar == [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

def test_quicksort_single_element_list():
    ar = [1]
    quicksort(ar)
    assert ar == [1]

def test_quicksort_duplicate_elements():
    ar = [4, 2, 1, 3, 2, 1, 4, 3]
    quicksort(ar)
    assert ar == [1, 1, 2, 2, 3, 3, 4, 4]