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
def example_heap():
    heap = Heap()
    heap.insert(5)
    heap.insert(3)
    heap.insert(8)
    heap.insert(2)
    heap.insert(7)
    return heap

def test_insert(empty_heap):
    empty_heap.insert(5)
    assert empty_heap.size() == 1
    assert empty_heap.min() == 5

def test_percolate(example_heap):
    example_heap.insert(1)
    assert example_heap.min() == 1

def test_sift(example_heap):
    example_heap.delete_min()
    assert example_heap.min() == 3

def test_find_min_child_index(example_heap):
    assert example_heap.find_min_child_index(1) == 2

def test_min(example_heap):
    assert example_heap.min() == 2

def test_delete_min(example_heap):
    deleted_val = example_heap.delete_min()
    assert deleted_val == 2
    assert example_heap.min() == 3

def test_build():
    heap = Heap()
    heap.build([4, 6, 1, 9, 5])
    assert heap.size() == 5
    assert heap.min() == 1