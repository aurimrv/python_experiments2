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

def test_insert(priorityq):
    priorityq.insert(10, 1)
    assert priorityq.peek() == 10

    priorityq.insert(20, 2)
    assert priorityq.peek() == 20

def test_pop(priorityq):
    priorityq.insert(10, 1)
    priorityq.insert(20, 2)

    assert priorityq.pop() == 20
    assert priorityq.pop() == 10

def test_peek(priorityq):
    assert priorityq.peek() is None

    priorityq.insert(10, 1)
    priorityq.insert(20, 2)

    assert priorityq.peek() == 20