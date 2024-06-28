import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from mergesort import mergesort

def test_mergesort_empty_list():
    assert mergesort([]) == []

def test_mergesort_sorted_list():
    assert mergesort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_mergesort_reverse_sorted_list():
    assert mergesort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

def test_mergesort_random_list():
    assert mergesort([3, 1, 5, 2, 4]) == [1, 2, 3, 4, 5]

def test_mergesort_duplicate_values():
    assert mergesort([3, 1, 5, 2, 3, 4]) == [1, 2, 3, 3, 4, 5]

def test_mergesort_single_element_list():
    assert mergesort([1]) == [1]

def test_mergesort_large_list():
    assert mergesort([9, 3, 6, 1, 4, 8, 2, 5, 7]) == [1, 2, 3, 4, 5, 6, 7, 8, 9]