import os
import sys

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from heapsort import heap_sort, max_heap_sort, custom_heap_sort

def test_heap_sort():
    assert heap_sort([4, 10, 3, 5, 1]) == [1, 3, 4, 5, 10]
    assert heap_sort([1]) == [1]
    assert heap_sort([]) == []

def test_max_heap_sort():
    assert max_heap_sort([4, 10, 3, 5, 1]) == [10, 5, 4, 3, 1]
    assert max_heap_sort([1]) == [1]
    assert max_heap_sort([]) == []

def test_custom_heap_sort():
    assert custom_heap_sort([4, 10, 3, 5, 1]) == [1, 3, 4, 5, 10]
    assert custom_heap_sort([4, 10, 3, 5, 1], sort='max') == [10, 5, 4, 3, 1]
    assert custom_heap_sort([1], sort='max') == [1]
    assert custom_heap_sort([], sort='max') == []