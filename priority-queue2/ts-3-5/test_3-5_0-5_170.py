import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from priority_queue2 import PriorityQ

import pytest

@pytest.fixture
def priority_q():
    return PriorityQ()

def test_priorityq_insert(priority_q):
    priority_q.insert(5, 2)
    assert priority_q.peek() == 5

def test_priorityq_pop(priority_q):
    priority_q.insert(10, 1)
    priority_q.insert(20, 2)
    assert priority_q.pop() == 20

def test_priorityq_peek_empty(priority_q):
    assert priority_q.peek() is None

def test_priorityq_peek(priority_q):
    priority_q.insert(15, 3)
    assert priority_q.peek() == 15

def test_priorityq_pop_empty(priority_q):
    with pytest.raises(IndexError):
        priority_q.pop()