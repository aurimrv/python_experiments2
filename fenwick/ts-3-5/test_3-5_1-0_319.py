import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from fenwick_tree import FenwickTree

def test_update_single_index():
    ft = FenwickTree([1, 2, 3, 4, 5])
    ft.update(2, 8)
    assert ft.sum_of_range(2, 2) == 8

def test_update_multiple_indices():
    ft = FenwickTree([1, 2, 3, 4, 5])
    ft.update(1, 10)
    ft.update(3, 6)
    assert ft.sum_of_range(1, 3) == 19

def test_sum_of_n():
    ft = FenwickTree([1, 2, 3, 4, 5])
    assert ft.sum_of_n(3) == 10

def test_sum_of_range_full():
    ft = FenwickTree([1, 2, 3, 4, 5])
    assert ft.sum_of_range(0, 4) == 15

def test_sum_of_range_partial():
    ft = FenwickTree([1, 2, 3, 4, 5])
    assert ft.sum_of_range(1, 3) == 9