import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from deque import Deque

@pytest.fixture
def deque():
    return Deque()

def test_append(deque):
    deque.append(1)
    assert deque.size() == 1
    deque.append(2)
    assert deque.size() == 2

def test_appendleft(deque):
    deque.appendleft(1)
    assert deque.size() == 1
    deque.appendleft(2)
    assert deque.size() == 2

def test_pop(deque):
    deque.append(1)
    deque.append(2)
    assert deque.pop() == 2
    assert deque.size() == 1

def test_popleft(deque):
    deque.append(1)
    deque.append(2)
    assert deque.popleft() == 1
    assert deque.size() == 1

def test_peek(deque):
    assert deque.peek() == None
    deque.append(1)
    assert deque.peek() == 1

def test_peekleft(deque):
    assert deque.peekleft() == None
    deque.append(1)
    assert deque.peekleft() == 1

def test_size(deque):
    assert deque.size() == 0
    deque.append(1)
    assert deque.size() == 1
    deque.appendleft(2)
    assert deque.size() == 2