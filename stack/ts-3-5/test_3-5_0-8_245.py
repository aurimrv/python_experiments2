import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from stack import Stack

@pytest.fixture
def stack():
    stack = Stack()
    return stack

def test_init(stack):
    assert stack._stack.head is None

def test_push(stack):
    stack.push(5)
    assert stack._stack.head.data == 5

def test_pop(stack):
    stack.push(10)
    stack.push(20)
    stack.pop()
    assert stack._stack.head.data == 10

def test_pop_empty(stack):
    with pytest.raises(Exception):
        stack.pop()

def test_push_multiple(stack):
    stack.push(1)
    stack.push(2)
    stack.push(3)
    assert stack._stack.head.data == 3
    assert stack._stack.head.next.data == 2
    assert stack._stack.head.next.next.data == 1

def test_pop_multiple(stack):
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.pop()
    assert stack._stack.head.data == 2
    stack.pop()
    assert stack._stack.head.data == 1
