import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from deque import Deque

@pytest.fixture
def new_deque():
    return Deque()

def test_init():
    deque = Deque()
    assert deque.size() == 0

def test_append(new_deque):
    new_deque.append(5)
    assert new_deque.size() == 1
    assert new_deque.peek() == 5

def test_appendleft(new_deque):
    new_deque.appendleft(3)
    assert new_deque.size() == 1
    assert new_deque.peekleft() == 3

def test_pop(new_deque):
    new_deque.append(2)
    assert new_deque.pop() == 2
    assert new_deque.size() == 0

def test_popleft(new_deque):
    new_deque.appendleft(10)
    assert new_deque.popleft() == 10
    assert new_deque.size() == 0

def test_peek_with_empty_deque(new_deque):
    assert new_deque.peek() is None

def test_peekleft_with_empty_deque(new_deque):
    assert new_deque.peekleft() is None

def test_size_with_empty_deque(new_deque):
    assert new_deque.size() == 0