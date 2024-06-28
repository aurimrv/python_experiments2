import os
import sys
import pytest

# Add project directory to sys.path
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

# Import the Queue class for testing
from a_queue import Queue

def test_queue_initialization():
    q = Queue()
    assert q.size() == 0

def test_enqueue():
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    assert q.size() == 2
    assert q.peek() == 1

def test_dequeue():
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    assert q.dequeue() == 1
    assert q.size() == 1
    assert q.dequeue() == 2
    assert q.size() == 0

def test_peek_empty_queue():
    q = Queue()
    assert q.peek() is None

def test_size_empty_queue():
    q = Queue()
    assert q.size() == 0

def test_size_non_empty_queue():
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    assert q.size() == 2

def test_enqueue_multiple_values():
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    assert q.size() == 3
    assert q.peek() == 1

def test_dequeue_empty_queue():
    q = Queue()
    with pytest.raises(IndexError):
        q.dequeue()