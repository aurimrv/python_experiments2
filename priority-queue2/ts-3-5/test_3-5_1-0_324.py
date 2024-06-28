import pytest
import os
import sys

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from priority_queue2 import PriorityQ

@pytest.fixture
def priority_q_instance():
    return PriorityQ()

def test_insert_method(priority_q_instance):
    priority_q_instance.insert(5)
    assert priority_q_instance.peek() == 5

    priority_q_instance.insert(10, 2)
    assert priority_q_instance.peek() == 10

def test_pop_method(priority_q_instance):
    priority_q_instance.insert('alpha', 3)
    priority_q_instance.insert('beta', 1)
    priority_q_instance.insert('gamma', 5)

    assert priority_q_instance.pop() == 'gamma'
    assert priority_q_instance.pop() == 'alpha'
    assert priority_q_instance.pop() == 'beta'

def test_peek_method_empty_queue(priority_q_instance):
    assert priority_q_instance.peek() is None

def test_peek_method(priority_q_instance):
    priority_q_instance.insert('apple', 4)
    assert priority_q_instance.peek() == 'apple'

    priority_q_instance.insert('banana', 6)
    assert priority_q_instance.peek() == 'banana'