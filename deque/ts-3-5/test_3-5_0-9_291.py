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

@pytest.fixture
def filled_deque():
    return Deque([1, 2, 3, 4])

def test_init(empty_deque, filled_deque):
    assert empty_deque.size() == 0
    assert filled_deque.size() == 4

def test_append(empty_deque):
    empty_deque.append(5)
    assert empty_deque.size() == 1
    assert empty_deque.peek() == 5

def test_appendleft(empty_deque):
    empty_deque.appendleft(0)
    assert empty_deque.size() == 1
    assert empty_deque.peekleft() == 0

def test_pop(filled_deque):
    popped = filled_deque.pop()
    assert popped == 1
    assert filled_deque.size() == 3

def test_popleft(filled_deque):
    popped_left = filled_deque.popleft()
    assert popped_left == 4
    assert filled_deque.size() == 3

def test_peek(empty_deque):
    assert empty_deque.peek() == None
    empty_deque.append(1)
    assert empty_deque.peek() == 1

def test_peekleft(empty_deque):
    assert empty_deque.peekleft() == None
    empty_deque.appendleft(0)
    assert empty_deque.peekleft() == 0

def test_size(empty_deque, filled_deque):
    assert empty_deque.size() == 0
    assert filled_deque.size() == 4