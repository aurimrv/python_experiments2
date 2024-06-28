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
def populated_queue():
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    return q

def test_enqueue(empty_queue):
    empty_queue.enqueue(1)
    assert empty_queue.peek() == 1
    assert empty_queue.size() == 1

def test_dequeue(populated_queue):
    assert populated_queue.dequeue() == 1
    assert populated_queue.size() == 2

def test_peek(empty_queue, populated_queue):
    assert empty_queue.peek() == None
    assert populated_queue.peek() == 1

def test_size(empty_queue, populated_queue):
    assert empty_queue.size() == 0
    assert populated_queue.size() == 3

def test_enqueue_dequeue_combo():
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    assert q.dequeue() == 1
    q.enqueue(3)
    assert q.dequeue() == 2
    assert q.size() == 1
    assert q.dequeue() == 3
    assert q.size() == 0
