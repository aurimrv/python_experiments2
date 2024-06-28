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
    assert quicksort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

def test_quicksort_duplicate_elements():
    assert quicksort([5, 2, 1, 5, 3, 2, 4, 4]) == [1, 2, 2, 3, 4, 4, 5, 5]

def test_quicksort_negative_numbers():
    assert quicksort([-5, -2, -8, -1, -3]) == [-8, -5, -3, -2, -1]

def test_quicksort_mixed_numbers():
    assert quicksort([5, -2, 0, 10, -3, 8, -1]) == [-3, -2, -1, 0, 5, 8, 10]