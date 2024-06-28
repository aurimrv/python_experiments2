import os
import sys

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from heapsort import heap_sort, max_heap_sort, custom_heap_sort

def test_heap_sort():
    assert heap_sort([4, 2, 1, 5, 3]) == [1, 2, 3, 4, 5]
    assert heap_sort([10, 5, 8, 3, 1]) == [1, 3, 5, 8, 10]

def test_max_heap_sort():
    assert max_heap_sort([4, 2, 1, 5, 3]) == [5, 4, 3, 2, 1]
    assert max_heap_sort([10, 5, 8, 3, 1]) == [10, 8, 5, 3, 1]

def test_custom_heap_sort_min():
    assert custom_heap_sort([4, 2, 1, 5, 3], 'min') == [1, 2, 3, 4, 5]
    assert custom_heap_sort([10, 5, 8, 3, 1], 'min') == [1, 3, 5, 8, 10]

def test_custom_heap_sort_max():
    assert custom_heap_sort([4, 2, 1, 5, 3], 'max') == [5, 4, 3, 2, 1]
    assert custom_heap_sort([10, 5, 8, 3, 1], 'max') == [10, 8, 5, 3, 1]