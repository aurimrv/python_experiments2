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
    heap.insert(4)
    heap.insert(1)
    return heap

def test_insert(empty_heap):
    empty_heap.insert(7)
    assert empty_heap.size() == 1
    assert empty_heap.min() == 7

def test_percolate(populated_heap):
    populated_heap.insert(2)
    assert populated_heap.min() == 1

def test_sift(populated_heap):
    populated_heap.insert(3)
    assert populated_heap.min() == 1

def test_find_min_child_index(empty_heap):
    assert empty_heap.find_min_child_index(1) is None

def test_min(populated_heap):
    assert populated_heap.min() == 1

def test_delete_min(populated_heap):
    min_val = populated_heap.delete_min()
    assert min_val == 1
    assert populated_heap.min() == 4

def test_build(empty_heap):
    lst = [9, 3, 6, 1, 7]
    empty_heap.build(lst)
    assert empty_heap.min() == 1
    assert empty_heap.size() == 5

def test_size(populated_heap):
    assert populated_heap.size() == 2