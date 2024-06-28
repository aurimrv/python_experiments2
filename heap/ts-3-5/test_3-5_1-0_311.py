import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from heap import Heap

@pytest.fixture
def empty_heap():
    heap = Heap()
    return heap

def test_insert(empty_heap):
    empty_heap.insert(5)
    assert empty_heap.size() == 1
    assert empty_heap.min() == 5

def test_percolate(empty_heap):
    empty_heap.heap_list = [0, 3, 5]
    empty_heap.percolate(2)
    assert empty_heap.heap_list == [0, 3, 5]

def test_sift(empty_heap):
    empty_heap.heap_list = [0, 5, 3]
    empty_heap.sift(1)
    assert empty_heap.heap_list == [0, 3, 5]

def test_find_min_child_index(empty_heap):
    empty_heap.heap_list = [0, 3, 5, 8]
    assert empty_heap.find_min_child_index(1) == 2

def test_min(empty_heap):
    empty_heap.heap_list = [0, 2, 5]
    assert empty_heap.min() == 2
    
def test_delete_min(empty_heap):
    empty_heap.heap_list = [0, 2, 5]
    assert empty_heap.delete_min() == 2
    assert empty_heap.size() == 1

def test_build(empty_heap):
    empty_heap.build([3, 6, 2, 8])
    assert empty_heap.size() == 4
    assert empty_heap.min() == 2