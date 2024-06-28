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

def test_quicksort_single_element_list():
    assert quicksort([1]) == [1]

def test_quicksort_duplicate_elements():
    assert quicksort([3, 1, 2, 1, 3]) == [1, 1, 2, 3, 3]

def test_quicksort_negative_numbers():
    assert quicksort([-3, 2, -5, 0, 1]) == [-5, -3, 0, 1, 2]

def test_quicksort_large_list():
    assert quicksort([9, 3, 6, 1, 7, 2, 8, 4, 5]) == [1, 2, 3, 4, 5, 6, 7, 8, 9]

def test_quicksort_mixed_data_types():
    with pytest.raises(TypeError):
        quicksort(['a', 2, 'c', 4, 1])
