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

def test_insert(priority_q):
    # Test inserting a single value with priority
    priority_q.insert(5, 1)
    assert priority_q.peek() == 5

    # Test inserting multiple values
    priority_q.insert(10, 2)
    priority_q.insert(15, 3)
    assert priority_q.peek() == 15

def test_pop(priority_q):
    # Test popping the only element in the queue
    priority_q.insert(20)
    assert priority_q.pop() == 20
    assert priority_q.peek() is None

    # Test popping multiple elements
    priority_q.insert(25, 2)
    priority_q.insert(30, 1)
    assert priority_q.pop() == 25
    assert priority_q.peek() == 30

def test_peek(priority_q):
    # Test peeking an empty queue
    assert priority_q.peek() is None

    # Test peeking after inserting multiple values
    priority_q.insert(35, 1)
    priority_q.insert(40, 3)
    priority_q.insert(45, 2)
    assert priority_q.peek() == 40