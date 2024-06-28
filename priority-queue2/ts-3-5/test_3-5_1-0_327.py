import pytest
import os
import sys

# Add project directory to sys.path
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from priority_queue2 import PriorityQ

@pytest.fixture
def priorityq():
    return PriorityQ()

def test_priorityq_insert(priorityq):
    priorityq.insert(5, 2)
    assert priorityq.peek() == 5

def test_priorityq_insert_multiple(priorityq):
    priorityq.insert(10, 1)
    priorityq.insert(15, 3)
    priorityq.insert(8, 2)
    assert priorityq.peek() == 15

def test_priorityq_pop(priorityq):
    priorityq.insert(10, 1)
    priorityq.insert(15, 3)
    assert priorityq.pop() == 15

def test_priorityq_peek_empty(priorityq):
    assert priorityq.peek() is None

def test_priorityq_pop_empty(priorityq):
    with pytest.raises(IndexError):
        priorityq.pop()

def test_priorityq_pop_last_value(priorityq):
    priorityq.insert(5, 1)
    assert priorityq.pop() == 5
    assert priorityq.peek() is None