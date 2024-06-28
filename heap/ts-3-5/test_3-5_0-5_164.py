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
    heap = Heap()
    heap.insert(3)
    heap.insert(1)
    heap.insert(5)
    heap.insert(2)
    heap.insert(4)
    return heap

def test_insert(empty_heap):
    empty_heap.insert(3)
    assert empty_heap.heap_list == [0, 3]

    empty_heap.insert(1)
    assert empty_heap.heap_list == [0, 1, 3]

def test_percolate(empty_heap):
    empty_heap.heap_list = [0, 3, 1, 5, 2, 4]
    empty_heap.percolate(5)
    assert empty_heap.heap_list == [0, 1, 3, 5, 2, 4]

def test_sift(heap_with_values):
    heap_with_values.sift(1)
    assert heap_with_values.heap_list == [0, 1, 2, 5, 3, 4]

def test_find_min_child_index(heap_with_values):
    assert heap_with_values.find_min_child_index(1) == 2

def test_min(empty_heap, heap_with_values):
    assert empty_heap.min() is None
    assert heap_with_values.min() == 1

def test_delete_min(heap_with_values):
    min_val = heap_with_values.delete_min()
    assert min_val == 1
    assert heap_with_values.heap_list == [0, 2, 3, 5, 4]

def test_build(empty_heap):
    empty_heap.build([3, 1, 5, 2, 4])
    assert empty_heap.heap_list == [0, 1, 2, 5, 3, 4]

def test_size(empty_heap, heap_with_values):
    assert empty_heap.size() == 0
    assert heap_with_values.size() == 5