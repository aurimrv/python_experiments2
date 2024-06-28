import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from a_queue import Queue

@pytest.fixture
def empty_queue():
    return Queue()

@pytest.fixture
def filled_queue():
    queue = Queue()
    for i in range(5):
        queue.enqueue(i)
    return queue

def test_enqueue(empty_queue):
    empty_queue.enqueue(10)
    assert empty_queue.peek() == 10

def test_dequeue(filled_queue):
    assert filled_queue.dequeue() == 0
    assert filled_queue.peek() == 1

def test_peek(empty_queue, filled_queue):
    assert empty_queue.peek() is None
    assert filled_queue.peek() == 0

def test_size(empty_queue, filled_queue):
    assert empty_queue.size() == 0
    assert filled_queue.size() == 5

def test_enqueue_dequeue_mix(empty_queue):
    empty_queue.enqueue(100)
    empty_queue.enqueue(200)
    assert empty_queue.size() == 2
    assert empty_queue.dequeue() == 100
    assert empty_queue.dequeue() == 200
    assert empty_queue.size() == 0