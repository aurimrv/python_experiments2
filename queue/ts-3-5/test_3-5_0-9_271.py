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
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    return q

def test_enqueue(empty_queue):
    assert empty_queue.size() == 0
    empty_queue.enqueue(1)
    assert empty_queue.size() == 1
    empty_queue.enqueue(2)
    assert empty_queue.size() == 2

def test_dequeue(queue_with_values):
    assert queue_with_values.dequeue() == 1
    assert queue_with_values.size() == 2
    assert queue_with_values.dequeue() == 2
    assert queue_with_values.dequeue() == 3
    assert queue_with_values.size() == 0

def test_peek(queue_with_values):
    assert queue_with_values.peek() == 1
    queue_with_values.dequeue()
    assert queue_with_values.peek() == 2
    queue_with_values.dequeue()
    assert queue_with_values.peek() == 3
    queue_with_values.dequeue()
    assert queue_with_values.peek() == None

def test_size(empty_queue, queue_with_values):
    assert empty_queue.size() == 0
    assert queue_with_values.size() == 3
    empty_queue.enqueue(1)
    empty_queue.enqueue(2)
    assert empty_queue.size() == 2