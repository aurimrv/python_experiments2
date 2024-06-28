import os
import sys
from collections import deque

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

import mergesort

def test_sort_empty_list():
    assert mergesort.mergesort([]) == []

def test_sort_single_element_list():
    assert mergesort.mergesort([5]) == [5]

def test_sort_sorted_list():
    assert mergesort.mergesort([1, 2, 3, 4]) == [1, 2, 3, 4]

def test_sort_reversed_list():
    assert mergesort.mergesort([4, 3, 2, 1]) == [1, 2, 3, 4]

def test_sort_random_list():
    assert mergesort.mergesort([7, 3, 9, 2, 5, 1]) == [1, 2, 3, 5, 7, 9]

def test_merge_empty_lists():
    assert mergesort.mergesort([]) == []

def test_merge_one_empty_list():
    assert mergesort.mergesort([1, 3, 5]) == [1, 3, 5]

def test_merge_two_non_empty_lists():
    assert mergesort.mergesort([1, 2, 4, 3, 5, 6]) == [1, 2, 3, 4, 5, 6]