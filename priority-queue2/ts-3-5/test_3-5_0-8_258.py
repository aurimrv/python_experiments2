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
    priority_q.insert(10, 1)
    assert priority_q.peek() == 10
    priority_q.insert(20, 2)
    priority_q.insert(30)  # Testing without specifying priority
    assert priority_q.peek() == 20

def test_pop(priority_q):
    priority_q.insert(10, 1)
    priority_q.insert(20, 2)
    priority_q.insert(30, 3)
    assert priority_q.pop() == 30
    assert priority_q.pop() == 20
    assert priority_q.pop() == 10
    with pytest.raises(IndexError):
        priority_q.pop()

def test_peek_empty(priority_q):
    assert priority_q.peek() is None

def test_peek_non_empty(priority_q):
    priority_q.insert(10, 1)
    assert priority_q.peek() == 10