import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from priority_queue2 import PriorityQ

def test_priorityq_insert():
    pq = PriorityQ()
    pq.insert(5, 1)
    assert pq.peek() == 5

def test_priorityq_pop():
    pq = PriorityQ()
    pq.insert(10, 2)
    pq.insert(20, 1)
    assert pq.pop() == 10
    assert pq.peek() == 20

def test_priorityq_peek_empty():
    pq = PriorityQ()
    assert pq.peek() is None

def test_priorityq_pop_empty():
    pq = PriorityQ()
    with pytest.raises(IndexError):
        pq.pop()

def test_priorityq_insert_multiple():
    pq = PriorityQ()
    pq.insert(30, 3)
    pq.insert(40, 2)
    pq.insert(50, 1)
    assert pq.pop() == 30
    assert pq.pop() == 40
    assert pq.pop() == 50