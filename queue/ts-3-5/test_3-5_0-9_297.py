import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from a_queue import Queue

# Test cases for Queue class methods

def test_enqueue():
    queue = Queue()
    queue.enqueue(1)
    assert queue.size() == 1

def test_dequeue():
    queue = Queue()
    queue.enqueue(1)
    assert queue.dequeue() == 1

def test_peek_with_elements():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    assert queue.peek() == 1

def test_peek_empty_queue():
    queue = Queue()
    assert queue.peek() == None

def test_size_with_elements():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    assert queue.size() == 2

def test_size_empty_queue():
    queue = Queue()
    assert queue.size() == 0