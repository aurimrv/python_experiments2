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

def test_pop_empty_queue(priority_q):
    with pytest.raises(IndexError):
        priority_q.pop()

def test_pop_non_empty_queue(priority_q):
    priority_q.insert(20, 2)
    priority_q.insert(30, 3)
    assert priority_q.pop() == 30
    assert priority_q.peek() == 20

def test_peek_empty_queue(priority_q):
    assert priority_q.peek() is None

def test_peek_non_empty_queue(priority_q):
    priority_q.insert(40, 4)
    priority_q.insert(50, 5)
    assert priority_q.peek() == 50