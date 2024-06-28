import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)
sys.setrecursionlimit(15000)

from quicksort import quicksort

def test_empty_list():
    ar = []
    assert quicksort(ar) == []

def test_sorted_list():
    ar = [1, 2, 3, 4, 5]
    assert quicksort(ar) == [1, 2, 3, 4, 5]

def test_reverse_sorted_list():
    ar = [5, 4, 3, 2, 1]
    assert quicksort(ar) == [1, 2, 3, 4, 5]

def test_random_list():
    ar = [3, 7, 2, 9, 1, 5, 4, 6, 8]
    assert quicksort(ar) == [1, 2, 3, 4, 5, 6, 7, 8, 9]

def test_duplicate_elements():
    ar = [3, 2, 3, 1, 2, 1]
    assert quicksort(ar) == [1, 1, 2, 2, 3, 3]

def test_negative_numbers():
    ar = [-5, 0, -3, -1, -2, -4]
    assert quicksort(ar) == [-5, -4, -3, -2, -1, 0]

def test_large_list():
    ar = list(range(10000, 0, -1))
    assert quicksort(ar) == list(range(1, 10001))