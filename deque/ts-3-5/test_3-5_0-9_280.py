import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from deque import Deque

@pytest.fixture
def empty_deque():
    return Deque()

def test_append(empty_deque):
    empty_deque.append(1)
    assert empty_deque.size() == 1
    assert empty_deque.peek() == 1

def test_appendleft(empty_deque):
    empty_deque.appendleft(2)
    empty_deque.appendleft(3)
    assert empty_deque.size() == 2
    assert empty_deque.peek() == 3

def test_pop(empty_deque):
    empty_deque.append(1)
    assert empty_deque.pop() == 1
    assert empty_deque.size() == 0

def test_popleft(empty_deque):
    empty_deque.appendleft(2)
    assert empty_deque.popleft() == 2
    assert empty_deque.size() == 0

def test_peek_empty_deque(empty_deque):
    assert empty_deque.peek() == None

def test_peekleft_empty_deque(empty_deque):
    assert empty_deque.peekleft() == None

def test_size_empty_deque(empty_deque):
    assert empty_deque.size() == 0