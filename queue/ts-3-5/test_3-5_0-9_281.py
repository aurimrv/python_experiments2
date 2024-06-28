import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from a_queue import Queue

# Test cases for the Queue class

@pytest.fixture
def empty_queue():
    q = Queue()
    return q

@pytest.fixture
def filled_queue():
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    return q

def test_enqueue(empty_queue):
    empty_queue.enqueue(1)
    assert empty_queue.peek() == 1

def test_dequeue(filled_queue):
    assert filled_queue.dequeue() == 1
    assert filled_queue.peek() == 2

def test_peek(filled_queue):
    assert filled_queue.peek() == 1
    filled_queue.dequeue()
    assert filled_queue.peek() == 2

def test_size(empty_queue, filled_queue):
    assert empty_queue.size() == 0
    assert filled_queue.size() == 3

def test_empty_queue():
    q = Queue()
    assert q.peek() is None
    with pytest.raises(IndexError):
        q.dequeue()