import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from a_queue import Queue

@pytest.fixture
def queue_with_values():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    return queue

def test_enqueue():
    queue = Queue()
    queue.enqueue(1)
    assert queue.size() == 1

def test_dequeue(queue_with_values):
    value = queue_with_values.dequeue()
    assert value == 1
    assert queue_with_values.size() == 1

def test_peek_empty_queue():
    queue = Queue()
    assert queue.peek() is None

def test_peek(queue_with_values):
    assert queue_with_values.peek() == 1

def test_size_empty_queue():
    queue = Queue()
    assert queue.size() == 0

def test_size(queue_with_values):
    assert queue_with_values.size() == 2