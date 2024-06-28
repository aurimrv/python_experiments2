import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from priority_queue2 import PriorityQ

# Test cases for PriorityQ class

def test_insert_method():
    pq = PriorityQ()
    
    pq.insert(5, 1)
    assert len(pq._container.container) == 2
    assert pq._container.container[1] == (1, 5)
    
    pq.insert(10, 2)
    assert len(pq._container.container) == 3
    assert pq._container.container[1] == (2, 10)

def test_pop_method():
    pq = PriorityQ()
    
    pq.insert(5, 1)
    pq.insert(10, 2)
    assert pq.pop() == 10
    
    pq.insert(3, 1)
    assert pq.pop() == 5
    assert pq.pop() == 3
    
    with pytest.raises(IndexError):
        pq.pop()

def test_peek_method():
    pq = PriorityQ()
    
    pq.insert(5, 1)
    pq.insert(10, 2)
    assert pq.peek() == 10
    
    pq.pop()
    assert pq.peek() == 5
    
    pq.pop()
    assert pq.peek() is None