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
    heap.insert(4)
    return heap

def test_insert(empty_heap):
    empty_heap.insert(5)
    assert empty_heap.min() == 5

def test_percolate(populated_heap):
    populated_heap.insert(0)
    assert populated_heap.min() == 0

def test_sift(populated_heap):
    populated_heap.delete_min()
    assert populated_heap.min() == 2

def test_find_min_child_index(populated_heap):
    assert populated_heap.find_min_child_index(1) == 2

def test_min(populated_heap):
    assert populated_heap.min() == 1

def test_delete_min(populated_heap):
    min_val = populated_heap.delete_min()
    assert min_val == 1
    assert populated_heap.min() == 2

def test_build(empty_heap):
    empty_heap.build([7, 3, 5, 1, 9])
    assert empty_heap.min() == 1

def test_size(empty_heap, populated_heap):
    assert empty_heap.size() == 0
    assert populated_heap.size() == 5