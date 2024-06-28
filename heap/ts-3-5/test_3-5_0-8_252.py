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
    heap.insert(5)
    heap.insert(3)
    heap.insert(7)
    return heap

def test_insert(empty_heap):
    empty_heap.insert(5)
    assert empty_heap.size() == 1
    assert empty_heap.min() == 5

def test_percolate(populated_heap):
    populated_heap.insert(2)
    assert populated_heap.min() == 2

def test_sift(populated_heap):
    populated_heap.insert(2)
    popped_val = populated_heap.delete_min()
    assert popped_val == 2

def test_find_min_child_index(populated_heap):
    index = populated_heap.find_min_child_index(1)
    assert index == 2

def test_min(populated_heap):
    assert populated_heap.min() == 3

def test_delete_min(populated_heap):
    min_val = populated_heap.delete_min()
    assert min_val == 3
    assert populated_heap.min() == 5

def test_build():
    heap = Heap()
    heap.build([4, 2, 6, 1, 3])
    assert heap.min() == 1
    assert heap.size() == 5