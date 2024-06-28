import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from heap import Heap

# Test cases for Heap class methods

@pytest.fixture
def new_heap():
    return Heap()

def test_heap_insert(new_heap):
    new_heap.insert(5)
    assert new_heap.heap_list == [0, 5]

def test_heap_percolate_single_element(new_heap):
    new_heap.heap_list = [0, 5]
    new_heap.percolate(1)
    assert new_heap.heap_list == [0, 5]

def test_heap_percolate_multiple_elements(new_heap):
    new_heap.heap_list = [0, 3, 5, 8, 10]
    new_heap.percolate(4)
    assert new_heap.heap_list == [0, 3, 5, 8, 10]

def test_heap_sift_single_element(new_heap):
    new_heap.heap_list = [0, 5]
    new_heap.sift(1)
    assert new_heap.heap_list == [0, 5]

def test_heap_sift_multiple_elements(new_heap):
    new_heap.heap_list = [0, 10, 8, 5]
    new_heap.sift(1)
    assert new_heap.heap_list == [0, 5, 8, 10]

def test_find_min_child_index_left_child(new_heap):
    new_heap.heap_list = [0, 3, 5, 8]
    assert new_heap.find_min_child_index(1) == 2

def test_find_min_child_index_right_child(new_heap):
    new_heap.heap_list = [0, 3, 8, 5]
    assert new_heap.find_min_child_index(1) == 3

def test_find_min_child_index_no_child(new_heap):
    new_heap.heap_list = [0, 3]
    assert new_heap.find_min_child_index(1) is None

def test_min_empty_heap(new_heap):
    assert new_heap.min() is None

def test_min_non_empty_heap(new_heap):
    new_heap.heap_list = [0, 5, 10, 3]
    assert new_heap.min() == 5

def test_delete_min_empty_heap(new_heap):
    assert new_heap.delete_min() is None

def test_delete_min_single_element(new_heap):
    new_heap.heap_list = [0, 5]
    assert new_heap.delete_min() == 5
    assert new_heap.heap_list == [0]

def test_delete_min_multiple_elements(new_heap):
    new_heap.heap_list = [0, 3, 5, 10, 8]
    assert new_heap.delete_min() == 3
    assert new_heap.heap_list == [0, 5, 8, 10]

def test_build(new_heap):
    new_heap.build([3, 8, 5])
    assert new_heap.heap_list == [0, 3, 8, 5]

def test_size_empty_heap(new_heap):
    assert new_heap.size() == 0

def test_size_non_empty_heap(new_heap):
    new_heap.heap_list = [0, 3, 5, 8]
    assert new_heap.size() == 3