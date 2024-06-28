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
def heap_with_elements():
    heap = Heap()
    heap.insert(3)
    heap.insert(6)
    heap.insert(2)
    heap.insert(8)
    return heap

def test_insert(empty_heap):
    assert empty_heap.heap_list == [0]
    empty_heap.insert(5)
    assert empty_heap.heap_list == [0, 5]

def test_percolate(empty_heap):
    empty_heap.heap_list = [0, 3, 2, 5, 6]
    empty_heap.percolate(4)
    assert empty_heap.heap_list == [0, 2, 3, 5, 6]

def test_sift(heap_with_elements):
    heap_with_elements.sift(1)
    assert heap_with_elements.heap_list == [0, 2, 6, 3, 8]

def test_find_min_child_index(empty_heap):
    empty_heap.heap_list = [0, 3, 6, 2, 8]
    assert empty_heap.find_min_child_index(1) == 3

def test_min(empty_heap):
    empty_heap.heap_list = [0, 4, 7, 3]
    assert empty_heap.min() == 4

def test_delete_min(heap_with_elements):
    min_val = heap_with_elements.delete_min()
    assert min_val == 2
    assert heap_with_elements.heap_list == [0, 3, 6, 8]

def test_build(empty_heap):
    empty_heap.build([5, 3, 8, 4, 2])
    assert empty_heap.heap_list == [0, 2, 3, 8, 4, 5]

def test_size(empty_heap, heap_with_elements):
    assert empty_heap.size() == 0
    assert heap_with_elements.size() == 4