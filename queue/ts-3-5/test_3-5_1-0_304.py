import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from a_queue import Queue

@pytest.fixture
def new_queue():
    return Queue()

def test_initialization():
    queue = Queue()
    assert queue.size() == 0

def test_enqueue(new_queue):
    new_queue.enqueue(1)
    assert new_queue.size() == 1
    new_queue.enqueue(2)
    assert new_queue.size() == 2

def test_dequeue(new_queue):
    new_queue.enqueue(1)
    new_queue.enqueue(2)
    assert new_queue.dequeue() == 1
    assert new_queue.size() == 1
    assert new_queue.dequeue() == 2
    assert new_queue.size() == 0

def test_peek_empty_queue(new_queue):
    assert new_queue.peek() is None

def test_peek(new_queue):
    new_queue.enqueue(1)
    new_queue.enqueue(2)
    assert new_queue.peek() == 1
    assert new_queue.size() == 2