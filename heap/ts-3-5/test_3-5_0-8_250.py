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
    assert heap.size() == 1
    assert heap.min() == 5

def test_percolate(heap):
    heap.heap_list = [0, 3, 2, 1]
    heap.percolate(3)
    assert heap.heap_list == [0, 1, 2, 3]

def test_sift(heap):
    heap.heap_list = [0, 2, 3, 1]
    heap.sift(1)
    assert heap.heap_list == [0, 1, 3, 2]

def test_find_min_child_index(heap):
    heap.heap_list = [0, 3, 2, 1]
    assert heap.find_min_child_index(1) == 3

def test_min(heap):
    heap.heap_list = [0, 4, 7, 2]
    assert heap.min() == 4

def test_delete_min(heap):
    heap.heap_list = [0, 4, 7, 2]
    assert heap.delete_min() == 4
    assert heap.size() == 2

def test_build(heap):
    lst = [4, 7, 2]
    heap.build(lst)
    assert heap.size() == 3
    assert heap.min() == 2

def test_size(heap):
    heap.heap_list = [0, 3, 2, 1]
    assert heap.size() == 3