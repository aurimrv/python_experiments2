import os
import sys
import pytest
from collections import deque

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from mergesort import mergesort

def test_mergesort_empty_list():
    assert mergesort([]) == []

def test_mergesort_single_element():
    assert mergesort([5]) == [5]

def test_mergesort_sorted_list():
    assert mergesort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_mergesort_reverse_sorted_list():
    assert mergesort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

def test_mergesort_random_list():
    assert mergesort([3, 1, 7, 2, 4, 6, 5]) == [1, 2, 3, 4, 5, 6, 7]

def test_mergesort_duplicate_elements():
    assert mergesort([2, 1, 3, 2, 3, 1]) == [1, 1, 2, 2, 3, 3]

def test_mergesort_with_negative_numbers():
    assert mergesort([-3, 5, -2, 0, 7, -1]) == [-3, -2, -1, 0, 5, 7]