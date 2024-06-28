import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from mergesort import mergesort

import pytest

def test_sort_empty_list():
    assert mergesort([]) == []

def test_sort_single_element_list():
    assert mergesort([5]) == [5]

def test_sort_sorted_list():
    assert mergesort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_sort_reverse_sorted_list():
    assert mergesort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

def test_merge_empty_lists():
    assert mergesort([]) == []

def test_merge_single_element_lists():
    assert mergesort([3, 7]) == [3, 7]

def test_merge_sorted_lists():
    assert mergesort([1, 3, 5, 2, 4, 6]) == [1, 2, 3, 4, 5, 6]

def test_merge_unsorted_lists():
    assert mergesort([5, 2, 8, 3, 6, 1]) == [1, 2, 3, 5, 6, 8]

def test_mergesort_empty_list():
    assert mergesort([]) == []

def test_mergesort_single_element_list():
    assert mergesort([5]) == [5]

def test_mergesort_sorted_list():
    assert mergesort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_mergesort_reverse_sorted_list():
    assert mergesort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

def test_mergesort_unsorted_list():
    assert mergesort([5, 2, 8, 3, 6, 1]) == [1, 2, 3, 5, 6, 8]