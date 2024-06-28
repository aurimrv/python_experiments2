import os
import sys
import pytest

# Import the file and modules being tested
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from a_queue import Queue

@pytest.fixture
def empty_queue():
    return Queue()

@pytest.fixture
def filled_queue():
    q = Queue()
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    return q

def test_enqueue(empty_queue):
    empty_queue.enqueue(5)
    assert empty_queue.size() == 1

    empty_queue.enqueue(10)
    assert empty_queue.size() == 2

def test_dequeue(filled_queue):
    assert filled_queue.dequeue() == 10
    assert filled_queue.size() == 2

    assert filled_queue.dequeue() == 20
    assert filled_queue.size() == 1

def test_peek(empty_queue):
    assert empty_queue.peek() is None

    empty_queue.enqueue(1)
    empty_queue.enqueue(2)
    assert empty_queue.peek() == 1

def test_size(empty_queue, filled_queue):
    assert empty_queue.size() == 0

    filled_queue.enqueue(100)
    assert filled_queue.size() == 4

    filled_queue.dequeue()
    filled_queue.dequeue()
    assert filled_queue.size() == 2