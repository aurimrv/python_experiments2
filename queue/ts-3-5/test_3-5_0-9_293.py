import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from a_queue import Queue

@pytest.fixture
def sample_queue():
    q = Queue()
    for i in range(1, 6):
        q.enqueue(i)
    return q

def test_enqueue(sample_queue):
    assert sample_queue.size() == 5
    sample_queue.enqueue(6)
    assert sample_queue.size() == 6

def test_dequeue(sample_queue):
    assert sample_queue.dequeue() == 1
    assert sample_queue.size() == 4

def test_peek(sample_queue):
    assert sample_queue.peek() == 1
    sample_queue.dequeue()
    assert sample_queue.peek() == 2

def test_size(sample_queue):
    assert sample_queue.size() == 5
    sample_queue.dequeue()
    sample_queue.dequeue()
    assert sample_queue.size() == 3