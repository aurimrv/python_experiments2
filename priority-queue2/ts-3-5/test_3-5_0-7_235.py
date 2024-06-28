import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from priority_queue2 import PriorityQ

def test_insert():
    pq = PriorityQ()
    pq.insert(5, 10)
    assert pq.peek() == 5

def test_pop():
    pq = PriorityQ()
    pq.insert(3, 20)
    pq.insert(7, 15)
    assert pq.pop() == 3

def test_peek():
    pq = PriorityQ()
    pq.insert(2, 10)
    pq.insert(8, 5)
    assert pq.peek() == 2

def test_empty_pop():
    pq = PriorityQ()
    with pytest.raises(IndexError):
        pq.pop()

def test_empty_peek():
    pq = PriorityQ()
    assert pq.peek() is None