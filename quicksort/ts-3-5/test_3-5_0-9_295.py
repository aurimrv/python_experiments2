import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)
sys.setrecursionlimit(15000)

from quicksort import quicksort


def test_quicksort_empty_list():
    result = quicksort([])
    assert result == []


def test_quicksort_sorted_list():
    result = quicksort([1, 2, 3, 4, 5])
    assert result == [1, 2, 3, 4, 5]


def test_quicksort_reverse_sorted_list():
    result = quicksort([5, 4, 3, 2, 1])
    assert result == [1, 2, 3, 4, 5]


def test_quicksort_random_list():
    result = quicksort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])
    assert result == [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]


def test_quicksort_single_element_list():
    result = quicksort([42])
    assert result == [42]


def test_quicksort_duplicate_elements():
    result = quicksort([5, 1, 2, 3, 4, 3, 5, 2, 1])
    assert result == [1, 1, 2, 2, 3, 3, 4, 5, 5]


def test_quicksort_mixed_types():
    result = quicksort(['b', 'a', 'c', 'z', 'm'])
    assert result == ['a', 'b', 'c', 'm', 'z']


def test_quicksort_negative_numbers():
    result = quicksort([5, -3, 2, -1, 0, -2, 4, 1])
    assert result == [-3, -2, -1, 0, 1, 2, 4, 5]