import os
import sys
from collections import deque

# Add the project directory to sys.path to correctly import the file
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from mergesort import mergesort

def test_mergesort_basic():
    assert mergesort([4, 2, 1, 3]) == [1, 2, 3, 4]

def test_mergesort_empty_list():
    assert mergesort([]) == []

def test_mergesort_already_sorted():
    assert mergesort([1, 2, 3, 4]) == [1, 2, 3, 4]

def test_mergesort_reverse_sorted():
    assert mergesort([4, 3, 2, 1]) == [1, 2, 3, 4]

def test_mergesort_duplicate_elements():
    assert mergesort([3, 1, 4, 2, 1]) == [1, 1, 2, 3, 4]

def test_mergesort_single_element():
    assert mergesort([5]) == [5]

def test_mergesort_large_list():
    assert mergesort([9, 3, 7, 1, 4, 2, 8, 5, 6]) == [1, 2, 3, 4, 5, 6, 7, 8, 9]