import os
import sys
import pytest

# Add project directory to the sys path
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from priority_queue2 import PriorityQ

@pytest.fixture
def priorityq():
    return PriorityQ()

def test_insert(priorityq):
    priorityq.insert(3)
    priorityq.insert(5, 2)
    assert priorityq._container.container[1] == (2, 5)

def test_pop_empty_queue(priorityq):
    with pytest.raises(IndexError):
        priorityq.pop()

def test_pop(priorityq):
    priorityq.insert(3)
    priorityq.insert(5, 2)
    assert priorityq.pop() == 5
    assert priorityq.pop() == 3

def test_peek_empty_queue(priorityq):
    assert priorityq.peek() == None

def test_peek(priorityq):
    priorityq.insert(3)
    priorityq.insert(5, 2)
    assert priorityq.peek() == 5
    priorityq.pop()
    assert priorityq.peek() == 3