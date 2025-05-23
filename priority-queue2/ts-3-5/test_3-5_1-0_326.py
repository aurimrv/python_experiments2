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
    priority_q.insert('A', 2)
    assert priority_q.peek() == 'A'
    priority_q.insert('B', 1)
    assert priority_q.peek() == 'A'

def test_pop(priority_q):
    priority_q.insert('A', 2)
    priority_q.insert('B', 1)
    assert priority_q.pop() == 'A'
    assert priority_q.peek() == 'B'
    assert priority_q.pop() == 'B'
    assert priority_q.peek() is None

def test_peek_empty_queue(priority_q):
    assert priority_q.peek() is None

def test_pop_empty_queue(priority_q):
    with pytest.raises(IndexError):
        priority_q.pop()