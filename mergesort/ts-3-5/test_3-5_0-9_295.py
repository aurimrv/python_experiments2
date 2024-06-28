import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from mergesort import mergesort

def test_mergesort_empty_list():
    assert mergesort([]) == []

def test_mergesort_single_element():
    assert mergesort([1]) == [1]

def test_mergesort_already_sorted():
    assert mergesort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_mergesort_reverse_sorted():
    assert mergesort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

def test_mergesort_mixed_elements():
    assert mergesort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

def test_merge_empty_lists():
    assert mergesort([]) == []

def test_merge_one_empty_list():
    assert mergesort([1, 2, 3]) == [1, 2, 3]

def test_merge_both_non_empty_lists():
    assert mergesort([1, 3, 5] + [2, 4, 6]) == [1, 2, 3, 4, 5, 6]

def test_merge_duplicate_elements():
    assert mergesort([1, 2, 3] + [2, 3, 4]) == [1, 2, 2, 3, 3, 4]

def test_sort_empty_list():
    assert mergesort([]) == []

def test_sort_single_element_list():
    assert mergesort([5]) == [5]

def test_sort_already_sorted_list():
    assert mergesort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_sort_reverse_sorted_list():
    assert mergesort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

def test_sort_mixed_elements_list():
    assert mergesort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]