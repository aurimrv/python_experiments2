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

def test_peek_empty(priority_q):
    assert priority_q.peek() == None

def test_insert_multiple(priority_q):
    priority_q.insert(15, 1)
    priority_q.insert(25, 3)
    assert priority_q.peek() == 25

def test_pop_multiple(priority_q):
    priority_q.insert(30, 2)
    priority_q.insert(40, 1)
    assert priority_q.pop() == 30
    assert priority_q.pop() == 40

def test_pop_empty(priority_q):
    with pytest.raises(IndexError):
        priority_q.pop()