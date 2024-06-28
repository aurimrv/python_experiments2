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
    pq.insert('apple', 2)
    assert pq.peek() == 'apple'

def test_pop_empty(pq):
    with pytest.raises(IndexError):
        pq.pop()

def test_pop(pq):
    pq.insert('banana', 3)
    pq.insert('cherry', 1)
    assert pq.pop() == 'banana'
    assert pq.peek() == 'cherry'

def test_peek_empty(pq):
    assert pq.peek() is None

def test_peek(pq):
    pq.insert('date', 5)
    assert pq.peek() == 'date'