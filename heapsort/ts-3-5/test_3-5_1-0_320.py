import os
import sys

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from heapsort import heap_sort, max_heap_sort, custom_heap_sort

def test_heap_sort():
    # Test case for an empty list
    assert heap_sort([]) == []

    # Test case for a list with one element
    assert heap_sort([5]) == [5]

    # Test case for a list with multiple elements
    assert heap_sort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

def test_max_heap_sort():
    # Test case for an empty list
    assert max_heap_sort([]) == []

    # Test case for a list with one element
    assert max_heap_sort([3]) == [3]

    # Test case for a list with multiple elements
    assert max_heap_sort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == [9, 6, 5, 5, 5, 4, 3, 3, 2, 1, 1]

def test_custom_heap_sort():
    # Test case for an empty list with min sort
    assert custom_heap_sort([], 'min') == []

    # Test case for a list with one element and min sort
    assert custom_heap_sort([0], 'min') == [0]

    # Test case for a list with multiple elements and min sort
    assert custom_heap_sort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5], 'min') == [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

    # Test case for a list with multiple elements and max sort
    assert custom_heap_sort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5], 'max') == [9, 6, 5, 5, 5, 4, 3, 3, 2, 1, 1]