import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from priority_queue2 import PriorityQ

import pytest

# Test cases for PriorityQ class

def test_insert():
    pq = PriorityQ()
    pq.insert(5, 2)
    assert pq.peek() == 5

def test_pop():
    pq = PriorityQ()
    pq.insert(10, 1)
    pq.insert(20, 2)
    pq.insert(30, 3)
    assert pq.pop() == 30
    assert pq.pop() == 20

def test_peek():
    pq = PriorityQ()
    pq.insert(7, 3)
    pq.insert(3, 1)
    pq.insert(5, 2)
    assert pq.peek() == 7
    pq.pop()
    assert pq.peek() == 5
    pq.pop()
    pq.pop()
    assert pq.peek() is None