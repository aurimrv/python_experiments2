import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from a_queue import Queue

@pytest.fixture
def empty_queue():
    return Queue()

@pytest.fixture
def queue_with_values():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    return queue

def test_enqueue(empty_queue):
    empty_queue.enqueue(1)
    assert empty_queue.size() == 1
    assert empty_queue.peek() == 1

def test_dequeue(queue_with_values):
    assert queue_with_values.dequeue() == 1
    assert queue_with_values.size() == 1

def test_peek(queue_with_values):
    assert queue_with_values.peek() == 1
    queue_with_values.dequeue()
    assert queue_with_values.peek() == 2

def test_size(empty_queue, queue_with_values):
    assert empty_queue.size() == 0
    assert queue_with_values.size() == 2

def test_dequeue_empty(empty_queue):
    with pytest.raises(IndexError):
        empty_queue.dequeue()

def test_peek_empty(empty_queue):
    assert empty_queue.peek() is None