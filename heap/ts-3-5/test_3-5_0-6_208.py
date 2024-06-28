import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from heap import Heap

@pytest.fixture
def sample_heap():
    heap = Heap()
    heap.build([9, 6, 5, 2, 3, 1, 8, 7, 4])
    return heap

def test_insert(sample_heap):
    sample_heap.insert(10)
    assert sample_heap.min() == 1

def test_percolate(sample_heap):
    sample_heap.insert(0)
    assert sample_heap.min() == 0

def test_sift(sample_heap):
    assert sample_heap.min() == 1
    sample_heap.delete_min()
    assert sample_heap.min() == 2

def test_find_min_child_index(sample_heap):
    assert sample_heap.find_min_child_index(1) == 2

def test_min(sample_heap):
    assert sample_heap.min() == 1

def test_delete_min(sample_heap):
    assert sample_heap.delete_min() == 1

def test_build():
    heap = Heap()
    heap.build([1, 2, 3, 4, 5])
    assert heap.min() == 1

def test_size(sample_heap):
    assert sample_heap.size() == 9