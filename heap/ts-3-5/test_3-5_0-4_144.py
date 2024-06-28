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
def sample_heap():
    heap = Heap()
    heap.heap_list = [0, 3, 7, 10, 15, 12, 19]
    return heap

def test_insert(empty_heap):
    empty_heap.insert(5)
    assert empty_heap.heap_list == [0, 5]

def test_percolate(empty_heap):
    empty_heap.heap_list = [0, 5, 3]
    empty_heap.percolate(2)
    assert empty_heap.heap_list == [0, 3, 5]

def test_sift(sample_heap):
    sample_heap.sift(1)
    assert sample_heap.heap_list == [0, 3, 7, 10, 15, 12, 19]

def test_find_min_child_index(sample_heap):
    assert sample_heap.find_min_child_index(1) == 2

def test_min(sample_heap):
    assert sample_heap.min() == 3

def test_delete_min(sample_heap):
    assert sample_heap.delete_min() == 3
    assert sample_heap.heap_list == [0, 7, 12, 10, 15, 19]

def test_build(empty_heap):
    empty_heap.build([3, 7, 10, 15, 12, 19])
    assert empty_heap.heap_list == [0, 3, 7, 10, 15, 12, 19]

def test_size(sample_heap):
    assert sample_heap.size() == 6