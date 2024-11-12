import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

import pytest
from priority_queue1 import PriorityQueue

@pytest.fixture
def empty_priority_queue():
    return PriorityQueue()

def test_add_task(empty_priority_queue):
    empty_priority_queue.add_task('task1', 1)
    assert len(empty_priority_queue.pq) == 1

def test_remove_task(empty_priority_queue):
    empty_priority_queue.add_task('task1', 1)
    empty_priority_queue.remove_task('task1')
    assert 'task1' not in empty_priority_queue.mapper

def test_set_priority(empty_priority_queue):
    empty_priority_queue.add_task('task1', 1)
    empty_priority_queue.set_priority('task1', 2)
    assert empty_priority_queue.mapper['task1'][0] == 2

def test_pop_task(empty_priority_queue):
    empty_priority_queue.add_task('task1', 1)
    task = empty_priority_queue.pop_task()
    assert task == 'task1'