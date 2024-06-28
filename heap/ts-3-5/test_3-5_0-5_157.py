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
def populated_heap():
    heap = Heap()
    heap.insert(3)
    heap.insert(1)
    heap.insert(5)
    heap.insert(2)
    return heap

def test_insert(empty_heap):
    empty_heap.insert(3)
    assert empty_heap.heap_list == [0, 3]

def test_percolate(empty_heap):
    empty_heap.heap_list = [0, 3, 1, 5, 2]
    empty_heap.percolate(4)
    assert empty_heap.heap_list == [0, 1, 3, 5, 2]

def test_sift(populated_heap):
    populated_heap.sift(1)
    assert populated_heap.heap_list == [0, 1, 2, 5, 3]

def test_find_min_child_index(populated_heap):
    result = populated_heap.find_min_child_index(1)
    assert result == 2

def test_min(populated_heap):
    result = populated_heap.min()
    assert result == 1

def test_delete_min(populated_heap):
    result = populated_heap.delete_min()
    assert result == 1
    assert populated_heap.heap_list == [0, 2, 3, 5]

def test_build(empty_heap):
    empty_heap.build([4, 2, 6, 1, 5])
    assert empty_heap.heap_list == [0, 1, 2, 6, 4, 5]

def test_size(populated_heap):
    result = populated_heap.size()
    assert result == 4