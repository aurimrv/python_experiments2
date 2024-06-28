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
    priorityq.insert(5, 2)
    assert priorityq.peek() == 5

def test_pop(priorityq):
    priorityq.insert(10, 1)
    priorityq.insert(20, 2)
    assert priorityq.pop() == 20

def test_peek_empty(priorityq):
    assert priorityq.peek() is None

def test_pop_empty(priorityq):
    with pytest.raises(IndexError):
        priorityq.pop()