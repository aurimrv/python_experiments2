import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from priority_queue2 import PriorityQ

@pytest.fixture
def priority_q():
    return PriorityQ()

def test_priority_q_insert(priority_q):
    priority_q.insert(10, 1)
    assert priority_q.peek() == 10

def test_priority_q_pop(priority_q):
    priority_q.insert(20, 2)
    priority_q.insert(30, 3)
    assert priority_q.pop() == 30

def test_priority_q_peek_empty(priority_q):
    assert priority_q.peek() is None

def test_priority_q_pop_empty(priority_q):
    with pytest.raises(IndexError):
        priority_q.pop()

def test_priority_q_multiple_inserts(priority_q):
    priority_q.insert(50, 5)
    priority_q.insert(40, 4)
    priority_q.insert(60, 6)
    assert priority_q.peek() == 60