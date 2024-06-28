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
def queue_with_values():
    q = Queue()
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    return q

def test_enqueue(empty_queue):
    empty_queue.enqueue(100)
    assert empty_queue.size() == 1

def test_dequeue(queue_with_values):
    assert queue_with_values.dequeue() == 10
    assert queue_with_values.size() == 2

def test_peek(empty_queue, queue_with_values):
    assert empty_queue.peek() is None
    assert queue_with_values.peek() == 10

def test_size(empty_queue, queue_with_values):
    assert empty_queue.size() == 0
    assert queue_with_values.size() == 3

def test_multiple_operations_on_queue(empty_queue):
    empty_queue.enqueue(50)
    empty_queue.enqueue(60)
    empty_queue.dequeue()
    empty_queue.enqueue(70)
    assert empty_queue.size() == 2