import os
import sys
from copy import deepcopy

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from heapsort import heap_sort, max_heap_sort, custom_heap_sort

def test_heap_sort_empty_list():
    lst = []
    assert heap_sort(lst) == []

def test_heap_sort_sorted_list():
    lst = [1, 2, 3, 4, 5]
    assert heap_sort(lst) == [1, 2, 3, 4, 5]

def test_max_heap_sort_empty_list():
    lst = []
    assert max_heap_sort(lst) == []

def test_max_heap_sort_unsorted_list():
    lst = [5, 3, 8, 1, 2]
    assert max_heap_sort(lst) == [8, 5, 3, 2, 1]

def test_custom_heap_sort_empty_list():
    lst = []
    assert custom_heap_sort(lst) == []

def test_custom_heap_sort_sorted_list_min():
    lst = [1, 2, 3, 4, 5]
    assert custom_heap_sort(lst) == [1, 2, 3, 4, 5]

def test_custom_heap_sort_unsorted_list_max():
    lst = [5, 3, 8, 1, 2]
    assert custom_heap_sort(lst, sort='max') == [8, 5, 3, 2, 1]