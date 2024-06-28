import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)
sys.setrecursionlimit(1500)

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

def test_quicksort_random_list():
    ar = [4, 2, 1, 5, 3]
    assert quicksort(ar) == [1, 2, 3, 4, 5]

def test_quicksort_duplicate_elements():
    ar = [4, 2, 1, 5, 3, 2, 4]
    assert quicksort(ar) == [1, 2, 2, 3, 4, 4, 5]

def test_quicksort_large_list():
    ar = [1000, 2000, 500, 4000, 300, 700, 800, 900, 600, 100, 3000]
    assert quicksort(ar) == [100, 300, 500, 600, 700, 800, 900, 1000, 2000, 3000, 4000]