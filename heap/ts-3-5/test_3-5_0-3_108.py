import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from heap import Heap

@pytest.fixture
def empty_heap():
    return Heap()

@pytest.fixture
def filled_heap():
    heap = Heap()
    heap.insert(3)
    heap.insert(1)
    heap.insert(5)
    heap.insert(2)
    heap.insert(4)
    return heap

def test_insert(empty_heap):
    empty_heap.insert(5)
    assert empty_heap.min() == 5
    empty_heap.insert(3)
    assert empty_heap.min() == 3

def test_percolate(empty_heap):
    empty_heap.heap_list = [0, 3, 1, 5, 2, 4]
    empty_heap.percolate(5)
    assert empty_heap.heap_list == [0, 1, 3, 5, 2, 4]

def test_sift(filled_heap):
    filled_heap.sift(1)
    assert filled_heap.heap_list == [0, 1, 2, 5, 3, 4]

def test_find_min_child_index(filled_heap):
    assert filled_heap.find_min_child_index(1) == 2
    assert filled_heap.find_min_child_index(2) == 4

def test_min(filled_heap):
    assert filled_heap.min() == 1

def test_delete_min(filled_heap):
    assert filled_heap.delete_min() == 1
    assert filled_heap.delete_min() == 2

def test_build(empty_heap):
    empty_heap.build([3, 1, 5, 2, 4])
    assert empty_heap.heap_list == [0, 1, 2, 5, 3, 4]

def test_size(empty_heap):
    assert empty_heap.size() == 0
    empty_heap.insert(7)
    assert empty_heap.size() == 1