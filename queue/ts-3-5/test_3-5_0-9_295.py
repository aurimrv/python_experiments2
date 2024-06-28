import os
import sys
import pytest

# Add project directory to sys.path
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from a_queue import Queue

@pytest.fixture
def queue_empty():
    return Queue()

@pytest.fixture
def queue_with_values():
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    return q

def test_enqueue(queue_empty):
    queue_empty.enqueue(1)
    assert queue_empty.size() == 1
    queue_empty.enqueue(2)
    assert queue_empty.size() == 2

def test_dequeue(queue_with_values):
    assert queue_with_values.dequeue() == 1
    assert queue_with_values.size() == 2
    assert queue_with_values.dequeue() == 2
    assert queue_with_values.size() == 1

def test_peek_empty(queue_empty):
    assert queue_empty.peek() is None

def test_peek(queue_with_values):
    assert queue_with_values.peek() == 1

def test_size(queue_empty):
    assert queue_empty.size() == 0
    queue_empty.enqueue(1)
    assert queue_empty.size() == 1
    queue_empty.enqueue(2)
    assert queue_empty.size() == 2