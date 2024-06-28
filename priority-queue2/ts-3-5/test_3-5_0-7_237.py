import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from priority_queue2 import PriorityQ

@pytest.fixture
def pq():
    return PriorityQ()

def test_insert(pq):
    pq.insert(5)
    assert pq.peek() == 5

def test_insert_priority(pq):
    pq.insert(10, priority=2)
    assert pq.peek() == 10

def test_pop_empty_queue(pq):
    with pytest.raises(IndexError):
        pq.pop()

def test_pop(pq):
    pq.insert(7)
    pq.insert(3)
    assert pq.pop() == 7
    assert pq.pop() == 3

def test_peek_empty_queue(pq):
    assert pq.peek() is None

def test_peek(pq):
    pq.insert(2)
    pq.insert(8)
    assert pq.peek() == 8