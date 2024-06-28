import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from priority_queue2 import PriorityQ

@pytest.fixture
def priority_q():
    pq = PriorityQ()
    yield pq

def test_insert_method(priority_q):
    priority_q.insert(5, 1)
    assert priority_q.peek() == 5

def test_insert_multiple_values(priority_q):
    priority_q.insert(10, 1)
    priority_q.insert(20, 2)
    priority_q.insert(30, 3)
    assert priority_q.peek() == 30

def test_pop_method(priority_q):
    priority_q.insert(5, 1)
    assert priority_q.pop() == 5

def test_pop_empty_queue_raises_error(priority_q):
    with pytest.raises(IndexError):
        priority_q.pop()

def test_peek_method(priority_q):
    priority_q.insert(5, 1)
    assert priority_q.peek() == 5

def test_peek_empty_queue_returns_none(priority_q):
    assert priority_q.peek() is None