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
    assert quicksort(ar) == expected

def test_quicksort_sorted_list():
    ar = [1, 2, 3, 4, 5]
    expected = [1, 2, 3, 4, 5]
    assert quicksort(ar) == expected

def test_quicksort_reverse_sorted_list():
    ar = [5, 4, 3, 2, 1]
    expected = [1, 2, 3, 4, 5]
    assert quicksort(ar) == expected

def test_quicksort_duplicate_elements():
    ar = [4, 2, 1, 3, 2]
    expected = [1, 2, 2, 3, 4]
    assert quicksort(ar) == expected

def test_quicksort_negative_numbers():
    ar = [-3, 0, -5, 2, -1]
    expected = [-5, -3, -1, 0, 2]
    assert quicksort(ar) == expected