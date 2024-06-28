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
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    return queue

def test_enqueue(empty_queue):
    empty_queue.enqueue(1)
    assert empty_queue.size() == 1
    empty_queue.enqueue(2)
    assert empty_queue.size() == 2

def test_dequeue(filled_queue):
    assert filled_queue.dequeue() == 1
    assert filled_queue.size() == 2
    assert filled_queue.dequeue() == 2
    assert filled_queue.size() == 1

def test_peek(empty_queue):
    assert empty_queue.peek() is None
    empty_queue.enqueue(1)
    assert empty_queue.peek() == 1

def test_size(empty_queue, filled_queue):
    assert empty_queue.size() == 0
    assert filled_queue.size() == 3
    filled_queue.dequeue()
    assert filled_queue.size() == 2