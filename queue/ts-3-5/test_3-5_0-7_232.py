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

def test_peek(filled_queue):
    assert filled_queue.peek() == 1

def test_size_empty(empty_queue):
    assert empty_queue.size() == 0

def test_size_filled(filled_queue):
    assert filled_queue.size() == 3

def test_enqueue_dequeue_single(empty_queue):
    empty_queue.enqueue(5)
    assert empty_queue.dequeue() == 5

def test_enqueue_multiple_dequeue_all(empty_queue):
    empty_queue.enqueue(1)
    empty_queue.enqueue(2)
    empty_queue.enqueue(3)
    assert empty_queue.dequeue() == 1
    assert empty_queue.dequeue() == 2
    assert empty_queue.dequeue() == 3

def test_peek_empty(empty_queue):
    assert empty_queue.peek() is None

def test_peek_after_dequeue(filled_queue):
    filled_queue.dequeue()
    assert filled_queue.peek() == 2
