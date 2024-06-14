import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from binheap import Binheap

@pytest.fixture
def empty_heap():
    return Binheap()

def test_push(empty_heap):
    empty_heap.push(5)
    assert empty_heap.container == [None, 5]

def test_push_multiple_values(empty_heap):
    empty_heap.push(5)
    empty_heap.push(10)
    empty_heap.push(3)
    assert empty_heap.container == [None, 10, 5, 3]

def test_pop(empty_heap):
    empty_heap.push(5)
    empty_heap.push(10)
    empty_heap.pop()
    assert empty_heap.container == [None, 5]

def test_display(empty_heap):
    empty_heap.push(5)
    empty_heap.push(10)
    empty_heap.push(3)
    assert empty_heap.display() == ' 10 \n5 3 \n'

def test_push_pop(empty_heap):
    empty_heap.push(5)
    empty_heap.push(10)
    empty_heap.pop()
    empty_heap.push(7)
    assert empty_heap.container == [None, 7, 5]