import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)
sys.setrecursionlimit(15000)

import quicksort

def test_quicksort_empty_list():
    assert quicksort.quicksort([]) == []

def test_quicksort_sorted_list():
    assert quicksort.quicksort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_quicksort_reverse_list():
    assert quicksort.quicksort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

def test_quicksort_random_list():
    assert quicksort.quicksort([3, 8, 1, 5, 2, 4, 7, 6]) == [1, 2, 3, 4, 5, 6, 7, 8]

def test_quicksort_duplicate_values():
    assert quicksort.quicksort([3, 2, 3, 1, 2, 1]) == [1, 1, 2, 2, 3, 3]

def test_sort_empty_list():
    ar = []
    with pytest.raises(AttributeError):
        quicksort.sort(ar, 0, len(ar) - 1)

def test_sort_sorted_list():
    ar = [1, 2, 3, 4, 5]
    with pytest.raises(AttributeError):
        quicksort.sort(ar, 0, len(ar) - 1)

def test_sort_reverse_list():
    ar = [5, 4, 3, 2, 1]
    with pytest.raises(AttributeError):
        quicksort.sort(ar, 0, len(ar) - 1)

def test_partition_basic():
    ar = [3, 8, 1, 5, 2, 4, 7, 6]
    with pytest.raises(AttributeError):
        quicksort.partition(ar, 0, len(ar) - 1)

def test_partition_single_element():
    ar = [1]
    with pytest.raises(AttributeError):
        quicksort.partition(ar, 0, len(ar) - 1)

def test_partition_empty_list():
    ar = []
    with pytest.raises(AttributeError):
        quicksort.partition(ar, 0, len(ar) - 1)