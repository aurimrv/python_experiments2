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
    # Test adding a single value to the queue
    queue.enqueue(5)
    assert queue.size() == 1

    # Test adding multiple values to the queue
    queue.enqueue(10)
    queue.enqueue(15)
    assert queue.size() == 3


def test_dequeue(queue):
    # Test dequeueing from an empty queue
    with pytest.raises(IndexError):
        queue.dequeue()

    # Test dequeueing a single item from the queue
    queue.enqueue(5)
    assert queue.dequeue() == 5

    # Test dequeueing multiple items from the queue
    queue.enqueue(10)
    queue.enqueue(15)
    assert queue.dequeue() == 10
    assert queue.dequeue() == 15
    assert queue.size() == 0


def test_peek(queue):
    # Test peeking from an empty queue
    assert queue.peek() is None

    # Test peeking at the next value in the queue
    queue.enqueue(5)
    queue.enqueue(10)
    assert queue.peek() == 5
    queue.dequeue()
    assert queue.peek() == 10


def test_size(queue):
    # Test getting the size of an empty queue
    assert queue.size() == 0

    # Test getting the size after adding elements to the queue
    queue.enqueue(5)
    queue.enqueue(10)
    queue.enqueue(15)
    assert queue.size() == 3