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

def test_push(stack):
    stack.push(1)
    assert stack._stack.head.data == 1

def test_multiple_push(stack):
    stack.push(1)
    stack.push(2)
    stack.push(3)
    assert stack._stack.head.data == 3

def test_pop(stack):
    stack.push(1)
    stack.push(2)
    stack.pop()
    assert stack._stack.head.data == 1

def test_pop_empty_stack(stack):
    with pytest.raises(Exception):
        stack.pop()