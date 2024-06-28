import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from a_queue import Queue

def test_enqueue():
    queue = Queue()
    queue.enqueue(1)
    assert queue.peek() == 1

def test_dequeue():
    queue = Queue()
    queue.enqueue(1)
    assert queue.dequeue() == 1

def test_peek_empty_queue():
    queue = Queue()
    assert queue.peek() is None

def test_size_empty_queue():
    queue = Queue()
    assert queue.size() == 0

def test_size_after_enqueue():
    queue = Queue()
    queue.enqueue(1)
    assert queue.size() == 1

def test_multiple_enqueue_dequeue():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    assert queue.dequeue() == 1
    assert queue.dequeue() == 2
    assert queue.size() == 0

def test_dequeue_empty_queue():
    queue = Queue()
    with pytest.raises(IndexError):
        queue.dequeue()

def test_peek_non_empty_queue():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    assert queue.peek() == 1
    assert queue.size() == 2