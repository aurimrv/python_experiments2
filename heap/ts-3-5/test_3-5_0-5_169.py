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
def heap_with_values():
    h = Heap()
    h.heap_list = [0, 5, 9, 11, 14, 18, 19, 21, 33, 17, 27]
    return h

def test_insert(empty_heap):
    empty_heap.insert(10)
    assert empty_heap.heap_list == [0, 10]

def test_percolate(empty_heap):
    empty_heap.heap_list = [0, 5, 9, 11, 14]
    empty_heap.percolate(4)
    assert empty_heap.heap_list == [0, 5, 9, 11, 14]

def test_sift(heap_with_values):
    heap_with_values.sift(2)
    assert heap_with_values.heap_list == [0, 5, 9, 11, 14, 18, 19, 21, 33, 17, 27]

def test_find_min_child_index(heap_with_values):
    assert heap_with_values.find_min_child_index(2) == 4

def test_min(heap_with_values):
    assert heap_with_values.min() == 5

def test_delete_min(heap_with_values):
    assert heap_with_values.delete_min() == 5
    assert heap_with_values.heap_list == [0, 9, 14, 11, 17, 18, 19, 21, 33, 27]

def test_build(empty_heap):
    empty_heap.build([3, 7, 2, 11, 9, 10])
    assert empty_heap.heap_list == [0, 2, 7, 3, 11, 9, 10]

def test_size(empty_heap):
    assert empty_heap.size() == 0