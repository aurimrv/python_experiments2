import pytest
import os
import sys

# Add project directory to sys.path for correct import
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from heap import Heap

# Test case for Heap.insert method
def test_insert():
    h = Heap()
    h.insert(5)
    assert h.size() == 1
    assert h.min() == 5

    h.insert(3)
    assert h.size() == 2
    assert h.min() == 3

# Test case for Heap.percolate method
def test_percolate():
    h = Heap()
    h.heap_list = [0, 5, 3]
    h.percolate(2)
    assert h.heap_list == [0, 3, 5]

# Test case for Heap.sift method
def test_sift():
    h = Heap()
    h.heap_list = [0, 3, 5]
    h.sift(1)
    assert h.heap_list == [0, 3, 5]

# Test case for Heap.find_min_child_index method
def test_find_min_child_index():
    h = Heap()
    h.heap_list = [0, 3, 5]
    assert h.find_min_child_index(1) == 2

# Test case for Heap.min method
def test_min():
    h = Heap()
    h.heap_list = [0, 3, 5]
    assert h.min() == 3

# Test case for Heap.delete_min method
def test_delete_min():
    h = Heap()
    h.heap_list = [0, 3, 5]
    assert h.delete_min() == 3
    assert h.size() == 1

# Test case for Heap.build method
def test_build():
    h = Heap()
    h.build([5, 3, 7, 2])
    assert h.size() == 4
    assert h.min() == 2