import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from priority_queue2 import PriorityQ

def test_insert():
    pq = PriorityQ()
    pq.insert(5, 2)
    assert pq.peek() == 5

def test_pop():
    pq = PriorityQ()
    pq.insert(10, 1)
    pq.insert(20, 2)
    assert pq.pop() == 20

def test_peek_empty_queue():
    pq = PriorityQ()
    assert pq.peek() is None

def test_pop_empty_queue():
    pq = PriorityQ()
    with pytest.raises(IndexError):
        pq.pop()

def test_multiple_inserts_and_pops():
    pq = PriorityQ()
    pq.insert(100, 3)
    pq.insert(200, 1)
    pq.insert(300, 2)
    assert pq.pop() == 100
    assert pq.pop() == 300
    assert pq.pop() == 200