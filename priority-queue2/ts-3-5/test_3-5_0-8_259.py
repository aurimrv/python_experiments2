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
    priorityq.insert(5)
    assert priorityq.peek() == 5

    priorityq.insert(10, 2)
    assert priorityq.peek() == 10

def test_pop(priorityq):
    priorityq.insert(5)
    priorityq.insert(10, 2)
    
    assert priorityq.pop() == 10
    assert priorityq.pop() == 5

def test_peek(priorityq):
    assert priorityq.peek() is None

    priorityq.insert(3)
    assert priorityq.peek() == 3

    priorityq.pop()
    assert priorityq.peek() is None