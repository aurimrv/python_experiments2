import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from stack import Stack

import pytest

@pytest.fixture
def initialized_stack():
    return Stack()

def test_stack_push(initialized_stack):
    initialized_stack.push(1)
    assert initialized_stack._stack.head.data == 1

def test_stack_push_multiple_values(initialized_stack):
    initialized_stack.push(1)
    initialized_stack.push(2)
    initialized_stack.push(3)
    assert initialized_stack._stack.head.data == 3

def test_stack_pop(initialized_stack):
    initialized_stack.push(1)
    initialized_stack.push(2)
    initialized_stack.pop()
    assert initialized_stack._stack.head.data == 1

def test_stack_pop_empty_stack(initialized_stack):
    with pytest.raises(Exception):
        initialized_stack.pop()