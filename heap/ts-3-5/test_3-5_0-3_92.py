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
    heap.build([5, 3, 8, 2, 7])
    return heap

def test_insert(empty_heap):
    empty_heap.insert(5)
    assert empty_heap.heap_list == [0, 5]

    empty_heap.insert(3)
    assert empty_heap.heap_list == [0, 3, 5]

def test_percolate(empty_heap):
    empty_heap.heap_list = [0, 5, 3]
    empty_heap.percolate(2)
    assert empty_heap.heap_list == [0, 3, 5]

def test_sift(filled_heap):
    filled_heap.sift(1)
    assert filled_heap.heap_list == [0, 2, 3, 8, 5, 7]

def test_find_min_child_index(filled_heap):
    assert filled_heap.find_min_child_index(1) == 2
    assert filled_heap.find_min_child_index(2) == 4

def test_min(filled_heap):
    assert filled_heap.min() == 2

def test_delete_min(filled_heap):
    min_val = filled_heap.delete_min()
    assert min_val == 2
    assert filled_heap.heap_list == [0, 3, 5, 8, 7]

def test_build(empty_heap):
    empty_heap.build([4, 1, 6, 2])
    assert empty_heap.heap_list == [0, 1, 2, 6, 4]

def test_size(filled_heap):
    assert filled_heap.size() == 5