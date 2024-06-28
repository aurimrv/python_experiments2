import os
import sys
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

def test_mergesort_reverse_list():
    assert mergesort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

def test_mergesort_mixed_list():
    assert mergesort([3, 1, 4, 1, 5, 9, 2, 6, 5]) == [1, 1, 2, 3, 4, 5, 5, 6, 9]

def test_mergesort_duplicates():
    assert mergesort([3, 1, 4, 1, 5, 3, 2, 6, 5]) == [1, 1, 2, 3, 3, 4, 5, 5, 6]

def test_mergesort_large_list():
    assert mergesort([9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]