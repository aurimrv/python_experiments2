import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from priority_queue2 import PriorityQ

@pytest.fixture
def priorityq():
    return PriorityQ()

def test_insert(priorityq):
    priorityq.insert(5, 1)
    assert priorityq.peek() == 5

def test_pop(priorityq):
    priorityq.insert(10, 2)
    priorityq.insert(20, 1)
    assert priorityq.pop() == 10
    assert priorityq.peek() == 20

def test_peek_empty_queue(priorityq):
    assert priorityq.peek() is None

def test_pop_empty_queue(priorityq):
    with pytest.raises(IndexError):
        priorityq.pop()

def test_insert_multiple_values(priorityq):
    priorityq.insert(100, 3)
    priorityq.insert(200, 2)
    priorityq.insert(300, 1)
    assert priorityq.pop() == 100
    assert priorityq.pop() == 200
    assert priorityq.pop() == 300