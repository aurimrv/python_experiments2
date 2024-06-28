import os
import sys
import pytest

# Add the project directory to the sys path for correct imports
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from priority_queue2 import PriorityQ

@pytest.fixture
def empty_priority_q():
    return PriorityQ()

def test_insert(empty_priority_q):
    empty_priority_q.insert(5)
    assert empty_priority_q.peek() == 5

def test_pop(empty_priority_q):
    empty_priority_q.insert(10)
    empty_priority_q.insert(20)
    assert empty_priority_q.pop() == 20
    assert empty_priority_q.pop() == 10

def test_peek(empty_priority_q):
    assert empty_priority_q.peek() == None
    empty_priority_q.insert(30)
    assert empty_priority_q.peek() == 30

def test_insert_with_priority(empty_priority_q):
    empty_priority_q.insert(100, priority=1)
    empty_priority_q.insert(200, priority=2)
    assert empty_priority_q.pop() == 200
    assert empty_priority_q.pop() == 100

def test_pop_empty_queue(empty_priority_q):
    with pytest.raises(IndexError):
        empty_priority_q.pop()