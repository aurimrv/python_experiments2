import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from heap import Heap

# Test cases for the Heap class

def test_heap_insert():
    h = Heap()
    h.insert(5)
    assert h.heap_list == [0, 5]

    h.insert(3)
    assert h.heap_list == [0, 3, 5]

def test_heap_percolate():
    h = Heap()
    h.heap_list = [0, 5, 3]
    h.percolate(2)
    assert h.heap_list == [0, 3, 5]

def test_heap_sift():
    h = Heap()
    h.heap_list = [0, 3, 5, 8, 10]
    h.sift(1)
    assert h.heap_list == [0, 3, 5, 8, 10]

def test_heap_find_min_child_index():
    h = Heap()
    h.heap_list = [0, 3, 5, 8, 10]
    assert h.find_min_child_index(1) == 2

def test_heap_min():
    h = Heap()
    h.heap_list = [0, 3, 5, 8, 10]
    assert h.min() == 3

def test_heap_delete_min():
    h = Heap()
    h.heap_list = [0, 3, 5, 8, 10]
    assert h.delete_min() == 3

def test_heap_build():
    h = Heap()
    h.build([3, 10, 5, 8])
    assert h.heap_list == [0, 3, 8, 5, 10]

def test_heap_size():
    h = Heap()
    h.heap_list = [0, 3, 5, 8, 10]
    assert h.size() == 4