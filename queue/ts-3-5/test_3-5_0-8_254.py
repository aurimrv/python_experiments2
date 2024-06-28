import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from a_queue import Queue

import pytest

@pytest.fixture
def queue():
    return Queue()

def test_enqueue(queue):
    queue.enqueue(1)
    assert queue.peek() == 1

def test_dequeue(queue):
    queue.enqueue(1)
    assert queue.dequeue() == 1

def test_peek_empty(queue):
    assert queue.peek() is None

def test_size_empty(queue):
    assert queue.size() == 0

def test_size(queue):
    queue.enqueue(1)
    queue.enqueue(2)
    assert queue.size() == 2

def test_enqueue_dequeue(queue):
    queue.enqueue(1)
    queue.enqueue(2)
    assert queue.dequeue() == 1
    assert queue.dequeue() == 2

def test_peek(queue):
    queue.enqueue(1)
    queue.enqueue(2)
    assert queue.peek() == 1
    queue.dequeue()
    assert queue.peek() == 2