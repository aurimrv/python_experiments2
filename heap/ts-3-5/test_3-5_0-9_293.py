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

def test_heap_insert(heap):
    heap.insert(5)
    assert heap.heap_list == [0, 5]

    heap.insert(3)
    assert heap.heap_list == [0, 3, 5]

def test_heap_percolate(heap):
    heap.heap_list = [0, 3, 5]
    heap.percolate(2)
    assert heap.heap_list == [0, 3, 5]

    heap.heap_list = [0, 5, 3]
    heap.percolate(2)
    assert heap.heap_list == [0, 3, 5]

def test_heap_sift(heap):
    heap.heap_list = [0, 3, 5]
    heap.sift(1)
    assert heap.heap_list == [0, 3, 5]

    heap.heap_list = [0, 5, 3]
    heap.sift(1)
    assert heap.heap_list == [0, 3, 5]

def test_heap_find_min_child_index(heap):
    heap.heap_list = [0, 3, 5, 7]
    assert heap.find_min_child_index(1) == 2

    heap.heap_list = [0, 5, 3, 7]
    assert heap.find_min_child_index(1) == 2

def test_heap_min(heap):
    heap.heap_list = [0, 3, 5]
    assert heap.min() == 3

    heap.heap_list = [0]
    assert heap.min() == None

def test_heap_delete_min(heap):
    heap.heap_list = [0, 3, 5]
    assert heap.delete_min() == 3
    assert heap.heap_list == [0, 5]

    heap.heap_list = [0]
    assert heap.delete_min() == None

def test_heap_build(heap):
    lst = [3, 5, 1, 7, 2]
    heap.build(lst)
    assert heap.heap_list == [0, 1, 2, 3, 7, 5]

def test_heap_size(heap):
    heap.heap_list = [0, 3, 5, 7]
    assert heap.size() == 3

    heap.heap_list = [0]
    assert heap.size() == 0