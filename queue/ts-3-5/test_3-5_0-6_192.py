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

def test_empty_queue_size(empty_queue):
    assert empty_queue.size() == 0

def test_queue_size(queue_with_values):
    assert queue_with_values.size() == 3

def test_empty_queue_peek(empty_queue):
    assert empty_queue.peek() is None

def test_queue_peek(queue_with_values):
    assert queue_with_values.peek() == 1

def test_enqueue(empty_queue):
    empty_queue.enqueue(5)
    assert empty_queue.size() == 1
    assert empty_queue.peek() == 5

def test_dequeue(queue_with_values):
    value = queue_with_values.dequeue()
    assert value == 1
    assert queue_with_values.size() == 2

def test_dequeue_empty_queue(empty_queue):
    with pytest.raises(IndexError):
        empty_queue.dequeue()