import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from priority_queue2 import PriorityQ

@pytest.fixture
def priority_queue():
    return PriorityQ()

def test_insert(priority_queue):
    priority_queue.insert(5, 1)
    assert priority_queue.peek() == 5

    priority_queue.insert(10, 2)
    assert priority_queue.peek() == 10

def test_pop(priority_queue):
    priority_queue.insert(5, 1)
    priority_queue.insert(10, 2)
    assert priority_queue.pop() == 10
    assert priority_queue.pop() == 5

def test_peek_empty(priority_queue):
    assert priority_queue.peek() is None

def test_pop_empty(priority_queue):
    with pytest.raises(IndexError):
        priority_queue.pop()

def test_pop_single_element(priority_queue):
    priority_queue.insert(5, 1)
    assert priority_queue.pop() == 5
    assert priority_queue.peek() is None