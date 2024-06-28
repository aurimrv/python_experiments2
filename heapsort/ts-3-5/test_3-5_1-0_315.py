import os
import sys

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from heapsort import heap_sort, max_heap_sort, custom_heap_sort

import pytest
from copy import deepcopy

# Tests for heap_sort method
def test_heap_sort_empty_list():
    assert heap_sort([]) == []

def test_heap_sort_sorted_list():
    sorted_list = heap_sort([1, 2, 3, 4, 5])
    assert sorted_list == [1, 2, 3, 4, 5]

def test_heap_sort_reverse_sorted_list():
    reverse_sorted_list = heap_sort([5, 4, 3, 2, 1])
    assert reverse_sorted_list == [1, 2, 3, 4, 5]

# Tests for max_heap_sort method
def test_max_heap_sort_empty_list():
    assert max_heap_sort([]) == []

def test_max_heap_sort_sorted_list():
    sorted_list = max_heap_sort([1, 2, 3, 4, 5])
    assert sorted_list == [5, 4, 3, 2, 1]

def test_max_heap_sort_reverse_sorted_list():
    reverse_sorted_list = max_heap_sort([5, 4, 3, 2, 1])
    assert reverse_sorted_list == [5, 4, 3, 2, 1]

# Tests for custom_heap_sort method
def test_custom_heap_sort_empty_list_min_heap():
    assert custom_heap_sort([], sort='min') == []

def test_custom_heap_sort_sorted_list_max_heap():
    sorted_list = custom_heap_sort([1, 2, 3, 4, 5], sort='max')
    assert sorted_list == [5, 4, 3, 2, 1]

def test_custom_heap_sort_unsorted_list_min_heap():
    unsorted_list = [3, 7, 1, 5, 2]
    sorted_list = custom_heap_sort(unsorted_list, sort='min')
    assert sorted_list == [1, 2, 3, 5, 7]