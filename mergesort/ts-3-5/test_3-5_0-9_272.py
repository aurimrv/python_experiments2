import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from mergesort import mergesort

def test_empty_list():
    assert mergesort([]) == []

def test_sorted_list():
    assert mergesort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_reverse_sorted_list():
    assert mergesort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

def test_same_elements():
    assert mergesort([2, 2, 2, 2, 2]) == [2, 2, 2, 2, 2]

def test_negative_elements():
    assert mergesort([-3, -1, -5, -2, -4]) == [-5, -4, -3, -2, -1]

def test_mixed_elements():
    assert mergesort([3, -1, 0, 5, -2, 4, 2, -3]) == [-3, -2, -1, 0, 2, 3, 4, 5]