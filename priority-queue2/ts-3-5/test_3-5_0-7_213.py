import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from priority_queue2 import PriorityQ

@pytest.fixture
def empty_priorityq():
    return PriorityQ()

@pytest.fixture
def filled_priorityq():
    pq = PriorityQ()
    pq.insert(10, 2)
    pq.insert(20, 1)
    pq.insert(30, 3)
    return pq

def test_init(empty_priorityq):
    assert empty_priorityq is not None

def test_insert(empty_priorityq):
    empty_priorityq.insert(100, 5)
    assert empty_priorityq.peek() == 100

def test_pop(filled_priorityq):
    assert filled_priorityq.pop() == 30
    assert filled_priorityq.pop() == 10

def test_peek(filled_priorityq):
    assert filled_priorityq.peek() == 30
    filled_priorityq.pop()
    assert filled_priorityq.peek() == 10