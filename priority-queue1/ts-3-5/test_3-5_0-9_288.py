# test_priority_queue1.py

import os
import sys
import pytest

# Add project directory to the path
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from priority_queue1 import PriorityQueue

@pytest.fixture
def priority_queue():
    return PriorityQueue()

def test_add_task(priority_queue):
    priority_queue.add_task('Task1', 5)
    assert len(priority_queue.pq) == 1

def test_remove_task(priority_queue):
    priority_queue.add_task('Task1', 5)
    priority_queue.remove_task('Task1')
    assert 'Task1' not in priority_queue.mapper

def test_set_priority(priority_queue):
    priority_queue.add_task('Task1', 5)
    priority_queue.set_priority('Task1', 10)
    assert priority_queue.mapper['Task1'][0] == 10

def test_pop_task(priority_queue):
    priority_queue.add_task('Task1', 5)
    task = priority_queue.pop_task()
    assert task == 'Task1'
    assert 'Task1' not in priority_queue.mapper