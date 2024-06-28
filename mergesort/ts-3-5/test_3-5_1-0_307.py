import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from mergesort import mergesort

def test_empty_list():
    assert mergesort([]) == []

def test_single_element():
    assert mergesort([5]) == [5]

def test_already_sorted_list():
    assert mergesort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_reverse_sorted_list():
    assert mergesort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

def test_duplicate_elements():
    assert mergesort([3, 2, 4, 1, 2]) == [1, 2, 2, 3, 4]

def test_negative_numbers():
    assert mergesort([-5, 10, 0, -3, 8]) == [-5, -3, 0, 8, 10]