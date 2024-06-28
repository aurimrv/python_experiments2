import sys
import os
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from priority_queue2 import PriorityQ

import pytest

@pytest.fixture
def pq():
    return PriorityQ()

def test_priorityq_insert(pq):
    pq.insert(5, 1)
    assert pq.peek() == 5

def test_priorityq_pop(pq):
    pq.insert(7, 2)
    pq.insert(3, 1)
    assert pq.pop() == 7

def test_priorityq_peek_empty(pq):
    assert pq.peek() is None

def test_priorityq_pop_empty(pq):
    with pytest.raises(IndexError):
        pq.pop()