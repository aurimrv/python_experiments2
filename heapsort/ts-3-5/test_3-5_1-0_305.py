from copy import deepcopy
from heapq import heapify, heappop
import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

import heapsort

def test_heap_sort():
    assert heapsort.heap_sort([]) == []
    assert heapsort.heap_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert heapsort.heap_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

def test_max_heap_sort():
    assert heapsort.max_heap_sort([]) == []
    assert heapsort.max_heap_sort([5, 4, 3, 2, 1]) == [5, 4, 3, 2, 1]
    assert heapsort.max_heap_sort([1, 2, 3, 4, 5]) == [5, 4, 3, 2, 1]

def test_custom_heap_sort():
    assert heapsort.custom_heap_sort([], sort='min') == []
    assert heapsort.custom_heap_sort([1, 2, 3, 4, 5], sort='min') == [1, 2, 3, 4, 5]
    assert heapsort.custom_heap_sort([5, 4, 3, 2, 1], sort='max') == [5, 4, 3, 2, 1]