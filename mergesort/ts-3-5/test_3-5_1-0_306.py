import os
import sys
from collections import deque

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from mergesort import mergesort

import pytest

def test_mergesort_empty_list():
    assert mergesort([]) == []

def test_mergesort_single_element():
    assert mergesort([5]) == [5]

def test_mergesort_sorted_list():
    assert mergesort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_mergesort_reverse_sorted_list():
    assert mergesort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

def test_mergesort_random_list():
    assert mergesort([3, 7, 1, 4, 9, 2, 5, 8, 6]) == [1, 2, 3, 4, 5, 6, 7, 8, 9]

def test_mergesort_duplicate_elements():
    assert mergesort([4, 2, 3, 1, 4, 2]) == [1, 2, 2, 3, 4, 4]

def test_mergesort_large_list():
    assert mergesort(list(range(10000, 0, -1))) == list(range(1, 10001))