import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from stack import Stack

import pytest

@pytest.fixture
def stack():
    return Stack()

def test_stack_push(stack):
    stack.push(1)
    assert stack._stack.head.data == 1

def test_stack_multiple_push(stack):
    stack.push(1)
    stack.push(2)
    assert stack._stack.head.next.data == 1
    assert stack._stack.head.data == 2

def test_stack_pop(stack):
    stack.push(1)
    stack.pop()
    assert stack._stack.head is None

def test_stack_multiple_pop(stack):
    stack.push(1)
    stack.push(2)
    stack.pop()
    assert stack._stack.head.data == 1

def test_stack_pop_empty(stack):
    with pytest.raises(IndexError):
        stack.pop()