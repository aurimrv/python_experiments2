import os
import sys

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from heapsort import heap_sort, max_heap_sort, custom_heap_sort

def test_heap_sort():
    lst = [4, 1, 3, 9, 7]
    assert heap_sort(lst) == [1, 3, 4, 7, 9]

    lst = [1, 5, 2, 8, 6]
    assert heap_sort(lst) == [1, 2, 5, 6, 8]

def test_max_heap_sort():
    lst = [4, 1, 3, 9, 7]
    assert max_heap_sort(lst) == [9, 7, 4, 3, 1]

    lst = [1, 5, 2, 8, 6]
    assert max_heap_sort(lst) == [8, 6, 5, 2, 1]

def test_custom_heap_sort_min():
    lst = [4, 1, 3, 9, 7]
    assert custom_heap_sort(lst, 'min') == [1, 3, 4, 7, 9]

    lst = [1, 5, 2, 8, 6]
    assert custom_heap_sort(lst, 'min') == [1, 2, 5, 6, 8]

def test_custom_heap_sort_max():
    lst = [4, 1, 3, 9, 7]
    assert custom_heap_sort(lst, 'max') == [9, 7, 4, 3, 1]

    lst = [1, 5, 2, 8, 6]
    assert custom_heap_sort(lst, 'max') == [8, 6, 5, 2, 1]