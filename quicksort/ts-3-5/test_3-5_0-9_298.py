import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)
sys.setrecursionlimit(15000)

from quicksort import quicksort

def test_quicksort_empty_list():
    assert quicksort([]) == []

def test_quicksort_sorted_list():
    assert quicksort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_quicksort_reverse_sorted_list():
    assert quicksort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

def test_quicksort_random_list():
    assert quicksort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

def test_quicksort_single_element_list():
    assert quicksort([42]) == [42]

def test_quicksort_duplicate_elements():
    assert quicksort([4, 2, 5, 2, 1, 5]) == [1, 2, 2, 4, 5, 5]

def test_quicksort_already_sorted():
    assert quicksort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_quicksort_negative_numbers():
    assert quicksort([-4, -2, 5, 0, -1, 3, -5]) == [-5, -4, -2, -1, 0, 3, 5]

def test_quicksort_mixed_types():
    with pytest.raises(TypeError):
        quicksort([1, 'a', 3, 4, 5])

def test_quicksort_large_list():
    assert quicksort([i for i in range(10000, 0, -1)]) == [i for i in range(1, 10001)]