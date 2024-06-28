import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from priority_queue2 import PriorityQ

@pytest.fixture
def empty_priorityq():
    return PriorityQ()

def test_insert(empty_priorityq):
    empty_priorityq.insert(5, 2)
    assert empty_priorityq.peek() == 5

def test_pop(empty_priorityq):
    empty_priorityq.insert(10, 1)
    empty_priorityq.insert(20, 3)
    assert empty_priorityq.pop() == 20

def test_peek(empty_priorityq):
    empty_priorityq.insert(7, 2)
    assert empty_priorityq.peek() == 7
    empty_priorityq.pop()
    assert empty_priorityq.peek() is None