import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from priority_queue1 import PriorityQueue

import pytest

@pytest.fixture
def priority_queue():
    return PriorityQueue()

def test_add_task(priority_queue):
    # Test adding a task with default priority
    priority_queue.add_task('task1')
    assert len(priority_queue.pq) == 1

    # Test adding a task with specified priority
    priority_queue.add_task('task2', priority=3)
    assert len(priority_queue.pq) == 2

def test_remove_task(priority_queue):
    # Test removing an existing task
    priority_queue.add_task('task1')
    priority_queue.remove_task('task1')
    assert 'task1' not in priority_queue.mapper

def test_set_priority(priority_queue):
    # Test setting priority to a task
    priority_queue.add_task('task1')
    priority_queue.set_priority('task1', priority=5)
    assert priority_queue.mapper['task1'][0] == 5

def test_pop_task(priority_queue):
    # Test popping a task from non-empty queue
    priority_queue.add_task('task1', priority=2)
    task = priority_queue.pop_task()
    assert task == 'task1'

    # Test popping task from an empty queue
    with pytest.raises(KeyError):
        priority_queue.pop_task()