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
def heap_with_values():
    heap = Heap()
    heap.insert(5)
    heap.insert(3)
    heap.insert(8)
    heap.insert(2)
    heap.insert(6)
    return heap

def test_insert(empty_heap):
    empty_heap.insert(5)
    assert empty_heap.size() == 1
    assert empty_heap.min() == 5

def test_percolate(heap_with_values):
    heap_with_values.insert(1)
    assert heap_with_values.min() == 1

def test_sift(heap_with_values):
    heap_with_values.insert(1)
    assert heap_with_values.min() == 1

def test_find_min_child_index(heap_with_values):
    assert heap_with_values.find_min_child_index(1) == 2

def test_min(heap_with_values):
    assert heap_with_values.min() == 2

def test_delete_min(heap_with_values):
    min_val = heap_with_values.delete_min()
    assert min_val == 2
    assert heap_with_values.size() == 4

def test_build():
    heap = Heap()
    heap.build([7, 4, 1, 9, 2])
    assert heap.size() == 5
    assert heap.min() == 1