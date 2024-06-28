import pytest
import os
import sys

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from priority_queue2 import PriorityQ

@pytest.fixture
def priorityq():
    return PriorityQ()

def test_priorityq_insert(priorityq):
    priorityq.insert(5)
    assert priorityq.peek() == 5

def test_priorityq_insert_multiple(priorityq):
    priorityq.insert(3, priority=1)
    priorityq.insert(7, priority=2)
    assert priorityq.peek() == 7

def test_priorityq_pop(priorityq):
    priorityq.insert(10)
    assert priorityq.pop() == 10

def test_priorityq_pop_empty(priorityq):
    with pytest.raises(IndexError):
        priorityq.pop()

def test_priorityq_peek(priorityq):
    priorityq.insert(1)
    assert priorityq.peek() == 1

def test_priorityq_peek_empty(priorityq):
    assert priorityq.peek() is None