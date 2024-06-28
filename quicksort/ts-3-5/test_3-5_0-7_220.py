import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)
sys.setrecursionlimit(15000)

from quicksort import quicksort

def test_quicksort_empty_list():
    input_list = []
    assert quicksort(input_list) == []

def test_quicksort_sorted_list():
    input_list = [1, 2, 3, 4, 5]
    assert quicksort(input_list) == [1, 2, 3, 4, 5]

def test_quicksort_reversed_list():
    input_list = [5, 4, 3, 2, 1]
    assert quicksort(input_list) == [1, 2, 3, 4, 5]

def test_quicksort_duplicate_elements():
    input_list = [4, 2, 1, 3, 4, 2]
    assert quicksort(input_list) == [1, 2, 2, 3, 4, 4]

def test_quicksort_negative_numbers():
    input_list = [-5, -2, -1, -3, -4]
    assert quicksort(input_list) == [-5, -4, -3, -2, -1]

def test_quicksort_mixed_numbers():
    input_list = [5, -4, 0, 2, -1]
    assert quicksort(input_list) == [-4, -1, 0, 2, 5]