import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from a_queue import Queue

import pytest

@pytest.fixture
def sample_queue():
    q = Queue()
    return q

def test_enqueue(sample_queue):
    sample_queue.enqueue(1)
    assert sample_queue.size() == 1
    sample_queue.enqueue(2)
    assert sample_queue.size() == 2

def test_dequeue_empty_queue(sample_queue):
    # Dequeue from an empty queue should raise an error
    with pytest.raises(IndexError):
        sample_queue.dequeue()

def test_dequeue(sample_queue):
    sample_queue.enqueue(1)
    sample_queue.enqueue(2)
    assert sample_queue.dequeue() == 1
    assert sample_queue.size() == 1
    assert sample_queue.dequeue() == 2
    assert sample_queue.size() == 0

def test_peek_empty_queue(sample_queue):
    assert sample_queue.peek() is None

def test_peek(sample_queue):
    sample_queue.enqueue(1)
    sample_queue.enqueue(2)
    assert sample_queue.peek() == 1
    assert sample_queue.size() == 2

def test_size_empty_queue(sample_queue):
    assert sample_queue.size() == 0

def test_size(sample_queue):
    sample_queue.enqueue(1)
    sample_queue.enqueue(2)
    assert sample_queue.size() == 2