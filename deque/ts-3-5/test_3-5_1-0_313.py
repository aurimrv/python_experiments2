import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from deque import Deque

import pytest

@pytest.fixture
def deque():
    return Deque()

def test_append(deque):
    deque.append(1)
    assert deque.peek() == 1

def test_appendleft(deque):
    deque.appendleft(2)
    assert deque.peekleft() == 2

def test_pop(deque):
    deque.append(3)
    assert deque.pop() == 3

def test_popleft(deque):
    deque.appendleft(4)
    assert deque.popleft() == 4

def test_peek_empty(deque):
    assert deque.peek() is None

def test_peekleft_empty(deque):
    assert deque.peekleft() is None

def test_size_empty(deque):
    assert deque.size() == 0

def test_multiple_add_remove(deque):
    deque.append(5)
    deque.append(6)
    deque.appendleft(7)
    deque.appendleft(8)
    assert deque.pop() == 6
    assert deque.popleft() == 8
    assert deque.size() == 2