import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from priority_queue2 import PriorityQ

import pytest

@pytest.fixture
def empty_priority_queue():
    return PriorityQ()

def test_insert_and_peek(empty_priority_queue):
    empty_priority_queue.insert('task1', 5)
    empty_priority_queue.insert('task2', 3)
    assert empty_priority_queue.peek() == 'task1'

def test_pop_from_empty_queue(empty_priority_queue):
    with pytest.raises(IndexError):
        empty_priority_queue.pop()

def test_insert_and_pop(empty_priority_queue):
    empty_priority_queue.insert('task1', 5)
    empty_priority_queue.insert('task2', 3)
    assert empty_priority_queue.pop() == 'task1'
    assert empty_priority_queue.pop() == 'task2'
    assert empty_priority_queue.peek() is None

def test_insert_with_default_priority(empty_priority_queue):
    empty_priority_queue.insert('task1')
    assert empty_priority_queue.peek() == 'task1'