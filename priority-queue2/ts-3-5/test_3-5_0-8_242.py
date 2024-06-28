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

def test_pop_empty_queue(priorityq):
    with pytest.raises(IndexError):
        priorityq.pop()

def test_pop_and_peek(priorityq):
    priorityq.insert('a', 3)
    priorityq.insert('b', 1)
    assert priorityq.pop() == 'a'
    assert priorityq.peek() == 'b'

def test_pop_from_empty_queue(priorityq):
    with pytest.raises(IndexError):
        priorityq.pop()

def test_peek_from_empty_queue(priorityq):
    assert priorityq.peek() is None