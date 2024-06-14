import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from deque import Deque

# Test Deque class methods
def test_append():
    dq = Deque()
    dq.append(1)
    assert dq.peek() == 1

def test_append_multiple():
    dq = Deque()
    dq.append(1)
    dq.append(2)
    assert dq.size() == 2

def test_appendleft():
    dq = Deque()
    dq.appendleft(5)
    assert dq.pop() == 5

def test_pop():
    dq = Deque()
    dq.append(3)
    assert dq.pop() == 3

def test_popleft():
    dq = Deque()
    dq.appendleft(7)
    assert dq.popleft() == 7

def test_peek():
    dq = Deque()
    dq.append(9)
    assert dq.peek() == 9

def test_peekleft():
    dq = Deque()
    dq.append(3)
    assert dq.peekleft() == 3

def test_size():
    dq = Deque([1, 2, 3])
    assert dq.size() == 3

def test_size_empty():
    dq = Deque()
    assert dq.size() == 0