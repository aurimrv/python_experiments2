import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from priority_queue2 import PriorityQ

import pytest

@pytest.fixture
def priorityq():
    return PriorityQ()

def test_insert(priorityq):
    priorityq.insert(5, 2)
    assert priorityq.peek() == 5

def test_insert_multiple(priorityq):
    priorityq.insert(10, 1)
    priorityq.insert(20, 3)
    assert priorityq.peek() == 20

def test_pop(priorityq):
    priorityq.insert(15, 1)
    assert priorityq.pop() == 15

def test_pop_exception(priorityq):
    with pytest.raises(IndexError):
        priorityq.pop()

def test_peek_empty_queue(priorityq):
    assert priorityq.peek() is None

def test_peek(priorityq):
    priorityq.insert(30, 5)
    assert priorityq.peek() == 30