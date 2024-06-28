import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from heap import Heap

@pytest.fixture
def empty_heap():
    h = Heap()
    return h

@pytest.fixture
def filled_heap():
    h = Heap()
    h.insert(5)
    h.insert(3)
    h.insert(10)
    h.insert(1)
    return h

def test_insert(empty_heap):
    empty_heap.insert(5)
    assert empty_heap.heap_list == [0, 5]

def test_percolate(empty_heap):
    empty_heap.heap_list = [0, 3, 5]
    empty_heap.percolate(2)
    assert empty_heap.heap_list == [0, 3, 5]

def test_sift(filled_heap):
    filled_heap.sift(1)
    assert filled_heap.heap_list == [0, 1, 3, 10, 5]

def test_find_min_child_index(filled_heap):
    assert filled_heap.find_min_child_index(1) == 2

def test_min(filled_heap):
    assert filled_heap.min() == 1

def test_delete_min(filled_heap):
    assert filled_heap.delete_min() == 1
    assert filled_heap.heap_list == [0, 3, 5, 10]

def test_build(empty_heap):
    empty_heap.build([4, 2, 6, 1, 8])
    assert empty_heap.heap_list == [0, 1, 2, 6, 4, 8]

def test_size(filled_heap):
    assert filled_heap.size() == 4