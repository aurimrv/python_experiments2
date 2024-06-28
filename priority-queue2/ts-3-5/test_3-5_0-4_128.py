import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from priority_queue2 import PriorityQ

import pytest

@pytest.fixture
def priorityq():
    return PriorityQ()

def test_insert_single_element(priorityq):
    priorityq.insert(5)
    assert priorityq.peek() == 5

def test_insert_multiple_elements(priorityq):
    priorityq.insert(10, 2)
    priorityq.insert(20, 1)
    priorityq.insert(30, 3)
    assert priorityq.peek() == 30

def test_pop_single_element(priorityq):
    priorityq.insert(5)
    assert priorityq.pop() == 5

def test_pop_multiple_elements(priorityq):
    priorityq.insert(10, 2)
    priorityq.insert(20, 1)
    priorityq.insert(30, 3)
    assert priorityq.pop() == 30
    assert priorityq.pop() == 10

def test_peek_empty_queue(priorityq):
    assert priorityq.peek() == None

def test_pop_empty_queue(priorityq):
    with pytest.raises(IndexError):
        priorityq.pop()