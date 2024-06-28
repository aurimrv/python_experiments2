import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from priority_queue2 import PriorityQ

import pytest

@pytest.fixture
def pq():
    return PriorityQ()

def test_priorityq_insert(pq):
    pq.insert(5, 0)
    assert pq.peek() == 5
    pq.insert(10, 1)
    assert pq.peek() == 10

def test_priorityq_pop(pq):
    pq.insert(5, 0)
    pq.insert(10, 1)
    assert pq.pop() == 10
    assert pq.pop() == 5

def test_priorityq_empty_pop(pq):
    with pytest.raises(IndexError):
        pq.pop()

def test_priorityq_peek(pq):
    pq.insert(5, 0)
    pq.insert(10, 1)
    assert pq.peek() == 10

def test_priorityq_empty_peek(pq):
    assert pq.peek() == None