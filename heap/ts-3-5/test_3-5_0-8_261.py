import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from heap import Heap

@pytest.fixture
def heap():
    return Heap()

def test_insert(heap):
    heap.insert(5)
    assert heap.heap_list == [0, 5]

    heap.insert(3)
    assert heap.heap_list == [0, 3, 5]

    heap.insert(7)
    assert heap.heap_list == [0, 3, 5, 7]

def test_percolate(heap):
    heap.heap_list = [0, 5, 3]
    heap.percolate(2)
    assert heap.heap_list == [0, 3, 5]

def test_sift(heap):
    heap.heap_list = [0, 3, 5, 7, 9]
    heap.sift(1)
    assert heap.heap_list == [0, 3, 5, 7, 9]

def test_find_min_child_index(heap):
    heap.heap_list = [0, 3, 5, 7, 9]
    assert heap.find_min_child_index(1) == 2

def test_min(heap):
    heap.heap_list = [0, 3, 5, 7, 9]
    assert heap.min() == 3

def test_delete_min(heap):
    heap.heap_list = [0, 3, 5, 7, 9]
    assert heap.delete_min() == 3
    assert heap.heap_list == [0, 5, 9, 7]

def test_build(heap):
    heap.build([3, 2, 4, 1])
    assert heap.heap_list == [0, 1, 2, 4, 3]

def test_size(heap):
    heap.heap_list = [0, 3, 5, 7, 9]
    assert heap.size() == 4