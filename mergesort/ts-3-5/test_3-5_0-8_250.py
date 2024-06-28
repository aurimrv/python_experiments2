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
    assert mergesort([3, 7, 1, 9, 2]) == [1, 2, 3, 7, 9]

def test_mergesort_single_element():
    assert mergesort([9]) == [9]

def test_mergesort_duplicates():
    assert mergesort([3, 2, 3, 1, 1]) == [1, 1, 2, 3, 3]

def test_mergesort_large_list():
    assert mergesort([100, 3, 45, 67, 23, 89, 12, 34, 56]) == [3, 12, 23, 34, 45, 56, 67, 89, 100]