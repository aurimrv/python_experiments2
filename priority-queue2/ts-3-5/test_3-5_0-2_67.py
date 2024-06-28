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
    priority_q.insert(5, 1)
    assert priority_q.peek() == 5

def test_pop(priority_q):
    priority_q.insert(10, 2)
    priority_q.insert(20, 1)
    assert priority_q.pop() == 10

def test_peek_empty_queue(priority_q):
    assert priority_q.peek() is None

def test_pop_empty_queue(priority_q):
    with pytest.raises(IndexError):
        priority_q.pop()

def test_insert_multiple_values(priority_q):
    priority_q.insert(100, 3)
    priority_q.insert(200, 2)
    priority_q.insert(300, 1)
    assert priority_q.peek() == 100
    assert priority_q.pop() == 100
    assert priority_q.pop() == 200
    assert priority_q.pop() == 300
    assert priority_q.peek() is None