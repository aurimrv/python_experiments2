import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from priority_queue2 import PriorityQ

import pytest

@pytest.fixture
def priority_queue():
    return PriorityQ()

def test_insert(priority_queue):
    priority_queue.insert(5)
    assert priority_queue.peek() == 5

def test_pop(priority_queue):
    priority_queue.insert(3)
    priority_queue.insert(7)
    assert priority_queue.pop() == 7

def test_peek_empty(priority_queue):
    assert priority_queue.peek() is None

def test_pop_empty_queue(priority_queue):
    with pytest.raises(IndexError):
        priority_queue.pop()

def test_insert_multiple_elements(priority_queue):
    priority_queue.insert(10, 2)
    priority_queue.insert(20, 1)
    priority_queue.insert(30, 3)
    assert priority_queue.peek() == 30

def test_pop_until_empty(priority_queue):
    priority_queue.insert(5, 1)
    priority_queue.insert(10, 2)
    priority_queue.pop()
    priority_queue.pop()
    assert priority_queue.peek() is None