import os
import sys
from collections import deque

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

def test_mergesort_single_element_list():
    assert mergesort([1]) == [1]

def test_mergesort_duplicate_elements_list():
    assert mergesort([3, 2, 3, 1, 2]) == [1, 2, 2, 3, 3]

def test_mergesort_negative_elements_list():
    assert mergesort([-3, -2, -5, -1, -4]) == [-5, -4, -3, -2, -1]

def test_mergesort_mixed_elements_list():
    assert mergesort([0, -1, 5, -3, 2]) == [-3, -1, 0, 2, 5]