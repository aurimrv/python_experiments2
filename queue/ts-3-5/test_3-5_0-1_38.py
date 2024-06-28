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
    assert queue.size() == 1
    queue.enqueue(2)
    assert queue.size() == 2

def test_dequeue(queue):
    queue.enqueue(1)
    queue.enqueue(2)
    assert queue.dequeue() == 1
    assert queue.size() == 1
    assert queue.dequeue() == 2
    assert queue.size() == 0

def test_peek(queue):
    queue.enqueue(1)
    queue.enqueue(2)
    assert queue.peek() == 1
    assert queue.size() == 2
    queue.dequeue()
    assert queue.peek() == 2
    queue.dequeue()
    assert queue.peek() == None

def test_size(queue):
    assert queue.size() == 0
    queue.enqueue(1)
    assert queue.size() == 1
    queue.enqueue(2)
    assert queue.size() == 2
    queue.dequeue()
    assert queue.size() == 1
    queue.dequeue()
    assert queue.size() == 0