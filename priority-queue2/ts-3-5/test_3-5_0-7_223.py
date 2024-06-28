import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from priority_queue2 import PriorityQ

def test_insert():
    pq = PriorityQ()
    pq.insert(5, 1)
    assert pq.peek() == 5

def test_pop():
    pq = PriorityQ()
    pq.insert(10, 2)
    pq.insert(20, 1)
    assert pq.pop() == 10
    assert pq.pop() == 20

def test_peek_empty():
    pq = PriorityQ()
    assert pq.peek() == None

def test_insert_no_priority():
    pq = PriorityQ()
    pq.insert(100)
    assert pq.peek() == 100

def test_pop_empty_queue():
    pq = PriorityQ()
    with pytest.raises(IndexError):
        pq.pop()

def test_pop_single_element_queue():
    pq = PriorityQ()
    pq.insert(50, 3)
    assert pq.pop() == 50
    assert pq.peek() == None