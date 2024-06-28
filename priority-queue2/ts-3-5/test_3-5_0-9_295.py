import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from priority_queue2 import PriorityQ

import pytest

@pytest.fixture
def priority_queue():
    return PriorityQ()

def test_insert(priority_queue):
    priority_queue.insert('val1', 1)
    assert priority_queue.peek() == 'val1'

def test_pop_empty_queue(priority_queue):
    with pytest.raises(IndexError):
        priority_queue.pop()

def test_pop_non_empty_queue(priority_queue):
    priority_queue.insert('val1', 1)
    priority_queue.insert('val2', 2)
    assert priority_queue.pop() == 'val2'
    assert priority_queue.peek() == 'val1'

def test_peek_empty_queue(priority_queue):
    assert priority_queue.peek() is None

def test_peek_non_empty_queue(priority_queue):
    priority_queue.insert('val1', 1)
    priority_queue.insert('val2', 2)
    assert priority_queue.peek() == 'val2'