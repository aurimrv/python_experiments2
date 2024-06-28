import os
import sys

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)
sys.setrecursionlimit(15000)

import quicksort

def test_quicksort_sorted_list():
    assert quicksort.quicksort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_quicksort_reverse_sorted_list():
    assert quicksort.quicksort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

def test_quicksort_random_list():
    assert quicksort.quicksort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

def test_quicksort_empty_list():
    assert quicksort.quicksort([]) == []

def test_quicksort_single_element_list():
    assert quicksort.quicksort([42]) == [42]

def test_quicksort_duplicate_elements_list():
    assert quicksort.quicksort([9, 6, 7, 6, 9, 7]) == [6, 6, 7, 7, 9, 9]

def test_quicksort_large_list():
    assert quicksort.quicksort([99, 22, 47, 66, 35, 10, 15, 90, 85, 23]) == [10, 15, 22, 23, 35, 47, 66, 85, 90, 99]