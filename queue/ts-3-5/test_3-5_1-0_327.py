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
    for i in range(1, 4):
        q.enqueue(i)
    return q

def test_enqueue(empty_queue):
    empty_queue.enqueue(1)
    assert empty_queue.peek() == 1

def test_dequeue(queue_with_values):
    assert queue_with_values.dequeue() == 1

def test_peek(empty_queue):
    assert empty_queue.peek() is None

def test_size(empty_queue):
    assert empty_queue.size() == 0

def test_queue_size_after_enqueue(empty_queue):
    empty_queue.enqueue(1)
    assert empty_queue.size() == 1

def test_multiple_enqueue_and_dequeue():
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    assert q.dequeue() == 1
    q.enqueue(3)
    assert q.dequeue() == 2
    assert q.dequeue() == 3
    assert q.size() == 0