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
    heap.build([5, 3, 8, 2, 7, 4])
    return heap

def test_insert(empty_heap):
    empty_heap.insert(5)
    assert empty_heap.heap_list == [0, 5]

    empty_heap.insert(3)
    assert empty_heap.heap_list == [0, 3, 5]

def test_percolate(empty_heap):
    empty_heap.heap_list = [0, 3, 5]
    empty_heap.percolate(2)
    assert empty_heap.heap_list == [0, 3, 5]

    empty_heap.heap_list = [0, 5, 3]
    empty_heap.percolate(2)
    assert empty_heap.heap_list == [0, 3, 5]

def test_sift(heap_with_elements):
    heap_with_elements.sift(1)
    assert heap_with_elements.heap_list == [0, 2, 3, 4, 5, 7, 8]

    heap_with_elements.sift(2)
    assert heap_with_elements.heap_list == [0, 2, 3, 4, 5, 7, 8]

def test_find_min_child_index(heap_with_elements):
    assert heap_with_elements.find_min_child_index(1) == 2
    assert heap_with_elements.find_min_child_index(2) == 4

def test_min(heap_with_elements):
    assert heap_with_elements.min() == 2

def test_delete_min(heap_with_elements):
    assert heap_with_elements.delete_min() == 2
    assert heap_with_elements.delete_min() == 3

def test_build(empty_heap):
    empty_heap.build([5, 3, 8, 2, 7, 4])
    assert empty_heap.heap_list == [0, 2, 3, 4, 5, 7, 8]

def test_size(heap_with_elements):
    assert heap_with_elements.size() == 6