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
    assert quicksort([3, 7, 2, 1, 8, 5, 9, 4, 6]) == [1, 2, 3, 4, 5, 6, 7, 8, 9]

def test_quicksort_duplicates():
    assert quicksort([5, 5, 3, 2, 1, 3, 2]) == [1, 2, 2, 3, 3, 5, 5]

def test_quicksort_negative_numbers():
    assert quicksort([-5, 3, 0, -2, 7, -1]) == [-5, -2, -1, 0, 3, 7]

def test_quicksort_mixed():
    assert quicksort([5, -2, 0, -7, 3, 1]) == [-7, -2, 0, 1, 3, 5]