import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from a_queue import Queue

@pytest.fixture
def queue():
    return Queue()

def test_enqueue(queue):
    queue.enqueue(1)
    assert queue.peek() == 1
    queue.enqueue(2)
    assert queue.peek() == 1

def test_dequeue(queue):
    queue.enqueue(1)
    queue.enqueue(2)
    assert queue.dequeue() == 1
    assert queue.peek() == 2

def test_peek(queue):
    queue.enqueue(1)
    queue.enqueue(2)
    assert queue.peek() == 1
    queue.dequeue()
    assert queue.peek() == 2

def test_size(queue):
    queue.enqueue(1)
    queue.enqueue(2)
    assert queue.size() == 2
    queue.dequeue()
    assert queue.size() == 1

def test_empty_queue_methods(queue):
    assert queue.peek() is None
    assert queue.size() == 0
    with pytest.raises(IndexError):
        queue.dequeue()