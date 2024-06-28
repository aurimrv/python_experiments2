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

def test_priorityq_insert(priority_queue):
    priority_queue.insert(5, 2)
    assert priority_queue.peek() == 5

def test_priorityq_insert_multiple(priority_queue):
    priority_queue.insert(10, 1)
    priority_queue.insert(20, 3)
    assert priority_queue.peek() == 20

def test_priorityq_pop(priority_queue):
    priority_queue.insert(15, 2)
    assert priority_queue.pop() == 15

def test_priorityq_pop_empty_queue(priority_queue):
    with pytest.raises(IndexError):
        priority_queue.pop()

def test_priorityq_peek(priority_queue):
    priority_queue.insert(25, 3)
    assert priority_queue.peek() == 25

def test_priorityq_peek_empty_queue(priority_queue):
    assert priority_queue.peek() is None