import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from priority_queue2 import PriorityQ

@pytest.fixture
def empty_priority_q():
    return PriorityQ()

def test_initialize_priority_q(empty_priority_q):
    assert empty_priority_q.peek() is None

def test_insert_and_peek(empty_priority_q):
    empty_priority_q.insert('task1', 5)
    empty_priority_q.insert('task2', 3)
    empty_priority_q.insert('task3', 7)
    assert empty_priority_q.peek() == 'task3'

def test_pop(empty_priority_q):
    empty_priority_q.insert('task1', 5)
    empty_priority_q.insert('task2', 3)
    empty_priority_q.insert('task3', 7)
    assert empty_priority_q.pop() == 'task3'
    assert empty_priority_q.pop() == 'task1'

def test_pop_empty_queue(empty_priority_q):
    with pytest.raises(IndexError):
        empty_priority_q.pop()

def test_peek_empty_queue(empty_priority_q):
    assert empty_priority_q.peek() is None