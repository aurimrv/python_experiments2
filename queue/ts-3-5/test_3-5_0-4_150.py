import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from a_queue import Queue

import pytest

@pytest.fixture
def empty_queue():
    return Queue()

@pytest.fixture
def queue_with_values():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    return queue

def test_enqueue(empty_queue):
    empty_queue.enqueue(1)
    assert empty_queue.peek() == 1

def test_dequeue(queue_with_values):
    assert queue_with_values.dequeue() == 1
    assert queue_with_values.size() == 2

def test_peek(empty_queue):
    assert empty_queue.peek() is None

def test_size(empty_queue, queue_with_values):
    assert empty_queue.size() == 0
    assert queue_with_values.size() == 3