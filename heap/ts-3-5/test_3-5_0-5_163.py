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
def filled_heap():
    h = Heap()
    h.insert(5)
    h.insert(3)
    h.insert(8)
    h.insert(2)
    return h

def test_insert(empty_heap):
    empty_heap.insert(5)
    assert empty_heap.size() == 1
    assert empty_heap.min() == 5

def test_percolate(empty_heap):
    empty_heap.insert(5)
    empty_heap.insert(3)
    assert empty_heap.size() == 2
    assert empty_heap.min() == 3

def test_sift(filled_heap):
    filled_heap.insert(1)
    assert filled_heap.size() == 5
    assert filled_heap.min() == 1

def test_find_min_child_index(filled_heap):
    assert filled_heap.find_min_child_index(1) == 2

def test_min(empty_heap, filled_heap):
    assert empty_heap.min() is None
    assert filled_heap.min() == 2

def test_delete_min(empty_heap, filled_heap):
    assert empty_heap.delete_min() is None
    assert filled_heap.delete_min() == 2
    assert filled_heap.size() == 3

def test_build(empty_heap):
    empty_heap.build([5, 2, 7, 1, 9])
    assert empty_heap.size() == 5
    assert empty_heap.min() == 1