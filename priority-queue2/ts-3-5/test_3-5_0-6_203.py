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

def test_priorityq_init(priority_q):
    assert isinstance(priority_q, PriorityQ)

def test_priorityq_insert(priority_q):
    priority_q.insert('A', 2)
    assert priority_q.peek() == 'A'

def test_priorityq_pop(priority_q):
    priority_q.insert('A', 2)
    priority_q.insert('B', 1)
    assert priority_q.pop() == 'A'

def test_priorityq_peek_empty(priority_q):
    assert priority_q.peek() == None

def test_priorityq_peek(priority_q):
    priority_q.insert('A', 2)
    priority_q.insert('B', 1)
    assert priority_q.peek() == 'A'