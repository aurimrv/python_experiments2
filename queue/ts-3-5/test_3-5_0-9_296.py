import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from a_queue import Queue

@pytest.fixture
def setup_queue():
    q = Queue()
    return q

def test_enqueue(setup_queue):
    q = setup_queue
    q.enqueue(1)
    assert q.size() == 1

def test_enqueue_multiple(setup_queue):
    q = setup_queue
    q.enqueue(1)
    q.enqueue(2)
    assert q.size() == 2

def test_dequeue(setup_queue):
    q = setup_queue
    q.enqueue(1)
    result = q.dequeue()
    assert result == 1
    assert q.size() == 0

def test_peek_empty_queue(setup_queue):
    q = setup_queue
    assert q.peek() is None

def test_peek_non_empty_queue(setup_queue):
    q = setup_queue
    q.enqueue(1)
    assert q.peek() == 1

def test_size_empty_queue(setup_queue):
    q = setup_queue
    assert q.size() == 0

def test_size_non_empty_queue(setup_queue):
    q = setup_queue
    q.enqueue(1)
    q.enqueue(2)
    assert q.size() == 2