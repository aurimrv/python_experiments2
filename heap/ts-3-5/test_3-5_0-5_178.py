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
def prepopulated_heap():
    heap = Heap()
    heap.heap_list = [0, 3, 6, 9, 12, 15]
    return heap

def test_insert(empty_heap):
    empty_heap.insert(5)
    assert empty_heap.heap_list == [0, 5]

def test_percolate(empty_heap):
    empty_heap.heap_list = [0, 3, 6, 9, 12, 15]
    empty_heap.percolate(5)
    assert empty_heap.heap_list == [0, 3, 6, 9, 12, 15]

def test_sift(prepopulated_heap):
    prepopulated_heap.sift(1)
    assert prepopulated_heap.heap_list == [0, 3, 6, 9, 12, 15]

def test_find_min_child_index(prepopulated_heap):
    assert prepopulated_heap.find_min_child_index(1) == 2

def test_min(prepopulated_heap):
    assert prepopulated_heap.min() == 3

def test_delete_min(prepopulated_heap):
    assert prepopulated_heap.delete_min() == 3

def test_build(empty_heap):
    empty_heap.build([4, 7, 10, 13])
    assert empty_heap.heap_list == [0, 4, 7, 10, 13]

def test_size(prepopulated_heap):
    assert prepopulated_heap.size() == 5