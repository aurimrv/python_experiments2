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

def test_insert(pq):
    pq.insert(5, 1)
    assert pq.peek() == 5

def test_pop(pq):
    pq.insert(10, 2)
    pq.insert(20, 1)
    assert pq.pop() == 10

def test_peek_empty(pq):
    assert pq.peek() is None

def test_pop_empty(pq):
    with pytest.raises(IndexError):
        pq.pop()

def test_insert_multiple(pq):
    pq.insert(100)
    pq.insert(200, 2)
    pq.insert(300, 1)
    assert pq.peek() == 200

def test_pop_multiple(pq):
    pq.insert(100)
    pq.insert(200, 2)
    pq.insert(300, 1)
    assert pq.pop() == 200
    assert pq.pop() == 300
    assert pq.pop() == 100
