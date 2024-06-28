import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from mergesort import mergesort

def test_sort_empty_list():
    assert mergesort([]) == []

def test_sort_single_element_list():
    assert mergesort([1]) == [1]

def test_sort_sorted_list():
    assert mergesort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_sort_reverse_sorted_list():
    assert mergesort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

def test_sort_mixed_positive_negative_numbers():
    assert mergesort([5, -2, 0, 8, -1]) == [-2, -1, 0, 5, 8]

def test_merge_empty_lists():
    assert mergesort([]) == []

def test_merge_single_element_lists():
    assert mergesort([1]) == [1]

def test_merge_sorted_lists():
    assert mergesort([1, 2, 3] + [4, 5, 6]) == [1, 2, 3, 4, 5, 6]

def test_merge_unsorted_lists():
    assert mergesort([6, 2, 1] + [5, 3, 4]) == [1, 2, 3, 4, 5, 6]

def test_merge_negative_numbers_lists():
    assert mergesort([-5, -2, -1] + [-6, -4, -3]) == [-6, -5, -4, -3, -2, -1] 