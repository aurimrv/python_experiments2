import os
import sys
import pytest

# Add the project directory to the sys.path
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from priority_queue2 import PriorityQ

@pytest.fixture
def empty_priorityq():
    return PriorityQ()

@pytest.fixture
def populated_priorityq():
    pq = PriorityQ()
    pq.insert("Task A", 2)
    pq.insert("Task B", 1)
    pq.insert("Task C", 3)
    return pq

def test_insert(empty_priorityq):
    empty_priorityq.insert("Task D", 2)
    assert empty_priorityq.peek() == "Task D"

    empty_priorityq.insert("Task E", 3)
    assert empty_priorityq.peek() == "Task E"

def test_pop(populated_priorityq):
    assert populated_priorityq.pop() == "Task C"
    assert populated_priorityq.pop() == "Task A"

def test_peek(empty_priorityq):
    assert empty_priorityq.peek() is None

    empty_priorityq.insert("Task F", 1)
    assert empty_priorityq.peek() == "Task F"

    empty_priorityq.pop()
    assert empty_priorityq.peek() is None