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
    
def test_mergesort_reverse_list():
    assert mergesort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

def test_mergesort_single_element_list():
    assert mergesort([1]) == [1]

def test_mergesort_duplicate_elements():
    assert mergesort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

def test_mergesort_negative_numbers():
    assert mergesort([-5, -2, -10, -20, -1, -4]) == [-20, -10, -5, -4, -2, -1]

def test_mergesort_large_input():
    assert mergesort(list(range(10000, 0, -1))) == list(range(1, 10001))