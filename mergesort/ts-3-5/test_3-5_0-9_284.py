import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from mergesort import mergesort

def test_mergesort_basic():
    assert mergesort([]) == []
    assert mergesort([1]) == [1]
    assert mergesort([3, 2, 1]) == [1, 2, 3]

def test_mergesort_duplicates():
    assert mergesort([5, 5, 5, 5]) == [5, 5, 5, 5]
    assert mergesort([4, 3, 3, 2, 2, 1, 1]) == [1, 1, 2, 2, 3, 3, 4]

def test_mergesort_negative_numbers():
    assert mergesort([-3, -2, -1]) == [-3, -2, -1]
    assert mergesort([-5, -2, -1, -4]) == [-5, -4, -2, -1]

def test_mergesort_mixed_numbers():
    assert mergesort([4, -2, 0, 5, -1]) == [-2, -1, 0, 4, 5]
    assert mergesort([-6, 3, -7, 8, 1]) == [-7, -6, 1, 3, 8]