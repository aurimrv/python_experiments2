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

def test_insert(priority_q):
    priority_q.insert(5, 1)
    assert priority_q.peek() == 5

def test_pop(priority_q):
    priority_q.insert(7, 2)
    priority_q.insert(12, 1)
    assert priority_q.pop() == 7

def test_peek_empty(priority_q):
    assert priority_q.peek() is None

def test_pop_empty(priority_q):
    with pytest.raises(IndexError):
        priority_q.pop()