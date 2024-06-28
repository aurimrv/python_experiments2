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
    priority_q.insert(5)
    assert priority_q.peek() == 5

    priority_q.insert(10, 2)
    assert priority_q.peek() == 10

def test_pop(priority_q):
    priority_q.insert(5)
    priority_q.insert(10, 2)

    assert priority_q.pop() == 10
    assert priority_q.pop() == 5

def test_peek_empty_queue(priority_q):
    assert priority_q.peek() is None

def test_pop_empty_queue_raises_error(priority_q):
    with pytest.raises(IndexError):
        priority_q.pop()