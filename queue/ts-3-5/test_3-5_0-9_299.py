import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from a_queue import Queue

@pytest.fixture
def queue_empty():
    return Queue()

@pytest.fixture
def queue_with_values():
    queue = Queue()
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    return queue

def test_enqueue(queue_empty, queue_with_values):
    assert queue_empty.size() == 0
    queue_empty.enqueue(5)
    assert queue_empty.size() == 1

    assert queue_with_values.size() == 3
    queue_with_values.enqueue(40)
    assert queue_with_values.size() == 4

def test_dequeue(queue_empty, queue_with_values):
    with pytest.raises(Exception):
        queue_empty.dequeue()

    assert queue_with_values.dequeue() == 10
    assert queue_with_values.size() == 2

def test_peek(queue_empty, queue_with_values):
    assert queue_empty.peek() == None
    queue_empty.enqueue(5)
    assert queue_empty.peek() == 5

    assert queue_with_values.peek() == 10
    queue_with_values.dequeue()
    assert queue_with_values.peek() == 20

def test_size(queue_empty, queue_with_values):
    assert queue_empty.size() == 0
    queue_empty.enqueue(5)
    assert queue_empty.size() == 1

    assert queue_with_values.size() == 3
    queue_with_values.enqueue(40)
    assert queue_with_values.size() == 4