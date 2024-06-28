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
    heap.build([4, 7, 1, 9, 3])
    return heap

def test_insert(empty_heap):
    empty_heap.insert(5)
    assert empty_heap.size() == 1
    assert empty_heap.min() == 5

def test_percolate(empty_heap):
    empty_heap.heap_list = [0, 3, 7, 1, 9, 4]
    empty_heap.percolate(5)
    assert empty_heap.heap_list == [0, 3, 4, 1, 9, 7]

def test_sift(filled_heap):
    filled_heap.sift(1)
    assert filled_heap.heap_list == [0, 1, 3, 4, 9, 7]

def test_find_min_child_index(filled_heap):
    assert filled_heap.find_min_child_index(1) == 2

def test_min(filled_heap):
    assert filled_heap.min() == 1

def test_delete_min(filled_heap):
    min_val = filled_heap.delete_min()
    assert min_val == 1
    assert filled_heap.size() == 4

def test_build(empty_heap):
    empty_heap.build([8, 2, 6, 5])
    assert empty_heap.size() == 4
    assert empty_heap.min() == 2

def test_size(filled_heap):
    assert filled_heap.size() == 5