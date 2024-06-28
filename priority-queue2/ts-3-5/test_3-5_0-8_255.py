import os
import sys
import pytest

# Add project directory to sys.path
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from priority_queue2 import PriorityQ

# Test cases for PriorityQ class methods

def test_insert():
    pq = PriorityQ()
    pq.insert(5)
    assert pq.peek() == 5
    
    pq.insert(10, priority=2)
    assert pq.peek() == 10

def test_pop():
    pq = PriorityQ()
    pq.insert(5)
    pq.insert(10, priority=2)
    
    assert pq.pop() == 10
    assert pq.pop() == 5

    with pytest.raises(IndexError):
        pq.pop()

def test_peek():
    pq = PriorityQ()
    assert pq.peek() is None
    
    pq.insert(5)
    assert pq.peek() == 5
    
    pq.insert(10, priority=2)
    assert pq.peek() == 10