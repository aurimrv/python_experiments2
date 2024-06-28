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
    priority_q.insert(5)
    assert priority_q.peek() == 5

def test_priority_q_insert_with_priority(priority_q):
    priority_q.insert(10, 2)
    assert priority_q.peek() == 10

def test_priority_q_pop(priority_q):
    priority_q.insert(3)
    assert priority_q.pop() == 3

def test_priority_q_pop_empty_queue(priority_q):
    with pytest.raises(IndexError):
        priority_q.pop()

def test_priority_q_peek(priority_q):
    priority_q.insert(7)
    assert priority_q.peek() == 7

def test_priority_q_peek_empty_queue(priority_q):
    assert priority_q.peek() is None