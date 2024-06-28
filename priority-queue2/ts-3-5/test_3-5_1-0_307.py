import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from priority_queue2 import PriorityQ

@pytest.fixture
def create_priorityq():
    q = PriorityQ()
    return q

def test_insert(create_priorityq):
    q = create_priorityq
    q.insert(10, 2)
    assert q.peek() == 10

def test_pop(create_priorityq):
    q = create_priorityq
    q.insert(10, 2)
    q.insert(20, 1)
    assert q.pop() == 10

def test_pop_empty_queue(create_priorityq):
    q = create_priorityq
    with pytest.raises(IndexError):
        q.pop()

def test_peek(create_priorityq):
    q = create_priorityq
    q.insert(10, 2)
    assert q.peek() == 10

def test_peek_empty_queue(create_priorityq):
    q = create_priorityq
    assert q.peek() is None