import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from mergesort import mergesort

def test_mergesort_empty_list():
    assert mergesort([]) == []

def test_mergesort_single_element_list():
    assert mergesort([5]) == [5]

def test_mergesort_sorted_list():
    assert mergesort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_mergesort_reverse_sorted_list():
    assert mergesort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

def test_mergesort_random_list():
    assert mergesort([3, 7, 2, 10, 1]) == [1, 2, 3, 7, 10]

def test_mergesort_duplicate_elements_list():
    assert mergesort([4, 2, 3, 1, 4, 2]) == [1, 2, 2, 3, 4, 4]

def test_mergesort_already_sorted_list():
    assert mergesort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_mergesort_large_list():
    assert mergesort([1000, 345, 87, 2, 976, 432, 56, 876, 21]) == [2, 21, 56, 87, 345, 432, 876, 976, 1000]