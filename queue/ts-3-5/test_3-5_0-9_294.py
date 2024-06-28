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
def queue_with_elements():
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    return q

def test_enqueue(empty_queue):
    empty_queue.enqueue(1)
    assert empty_queue.size() == 1

def test_dequeue(queue_with_elements):
    assert queue_with_elements.dequeue() == 1
    assert queue_with_elements.size() == 2

def test_peek_empty_queue(empty_queue):
    assert empty_queue.peek() == None

def test_peek_non_empty_queue(queue_with_elements):
    assert queue_with_elements.peek() == 1

def test_size_empty_queue(empty_queue):
    assert empty_queue.size() == 0

def test_size_non_empty_queue(queue_with_elements):
    assert queue_with_elements.size() == 3