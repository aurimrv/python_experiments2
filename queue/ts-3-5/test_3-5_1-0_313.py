import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from a_queue import Queue

import pytest

@pytest.fixture
def queue():
    q = Queue()
    return q

def test_initialization(queue):
    assert queue.size() == 0

def test_enqueue(queue):
    queue.enqueue(1)
    assert queue.size() == 1
    assert queue.peek() == 1

def test_multiple_enqueue(queue):
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    assert queue.size() == 3
    assert queue.peek() == 1

def test_dequeue(queue):
    queue.enqueue(1)
    queue.enqueue(2)
    assert queue.dequeue() == 1
    assert queue.size() == 1
    assert queue.peek() == 2

def test_empty_dequeue(queue):
    with pytest.raises(IndexError):
        queue.dequeue()

def test_peek_empty(queue):
    assert queue.peek() == None

def test_size(queue):
    queue.enqueue(1)
    queue.enqueue(2)
    assert queue.size() == 2

def test_size_empty(queue):
    assert queue.size() == 0