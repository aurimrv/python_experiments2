import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from priority_queue2 import PriorityQ

@pytest.fixture
def priorityq():
    return PriorityQ()

def test_priorityq_insert(priorityq):
    # Test inserting a single value with default priority
    priorityq.insert(5)
    assert priorityq.peek() == 5

    # Test inserting multiple values with different priorities
    priorityq.insert(3, 1)
    priorityq.insert(8, 2)
    assert priorityq.peek() == 8

def test_priorityq_pop(priorityq):
    # Test popping the only element in the queue
    priorityq.insert('test')
    assert priorityq.pop() == 'test'

    # Test popping elements with different priorities
    priorityq.insert('high', 2)
    priorityq.insert('medium', 1)
    priorityq.insert('low', 0)
    assert priorityq.pop() == 'high'
    assert priorityq.pop() == 'medium'
    assert priorityq.pop() == 'low'

def test_priorityq_peek(priorityq):
    # Test peeking an empty queue
    assert priorityq.peek() == None

    # Test peeking with elements in the queue
    priorityq.insert(10)
    assert priorityq.peek() == 10

    priorityq.insert('peek_test', 5)
    assert priorityq.peek() == 'peek_test'