import sys
import os

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)
sys.setrecursionlimit(15000)

from quicksort import quicksort

def test_sort_empty_list():
    assert quicksort([]) == []

def test_sort_single_element_list():
    assert quicksort([1]) == [1]

def test_sort_ordered_list():
    assert quicksort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_sort_reversed_list():
    assert quicksort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

def test_sort_random_list():
    assert quicksort([3, 5, 1, 4, 2]) == [1, 2, 3, 4, 5]

def test_sort_duplicate_elements():
    assert quicksort([3, 5, 1, 5, 2]) == [1, 2, 3, 5, 5]

def test_sort_negative_numbers():
    assert quicksort([-3, -5, -1, -4, -2]) == [-5, -4, -3, -2, -1]

def test_sort_mixed_positive_negative():
    assert quicksort([-3, 5, 1, -4, 2]) == [-4, -3, 1, 2, 5]

def test_sort_large_list():
    assert quicksort([9, 8, 7, 6, 5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5, 6, 7, 8, 9]