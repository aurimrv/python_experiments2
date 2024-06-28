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

def test_priorityq_initialization(priority_q):
    assert priority_q

def test_priorityq_insert(priority_q):
    priority_q.insert('A', 5)
    assert priority_q.peek() == 'A'

def test_priorityq_pop(priority_q):
    priority_q.insert('A', 5)
    priority_q.insert('B', 3)
    assert priority_q.pop() == 'A'

def test_priorityq_pop_empty(priority_q):
    with pytest.raises(IndexError):
        priority_q.pop()

def test_priorityq_peek(priority_q):
    priority_q.insert('A', 5)
    priority_q.insert('B', 3)
    assert priority_q.peek() == 'A'

def test_priorityq_peek_empty(priority_q):
    assert priority_q.peek() == None