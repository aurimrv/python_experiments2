import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from priority_queue1 import PriorityQueue

def test_add_task():
    pq = PriorityQueue()
    pq.add_task('task1', 1)
    assert len(pq.mapper) == 1
    assert len(pq.pq) == 1

def test_remove_task():
    pq = PriorityQueue()
    pq.add_task('task1', 1)
    pq.remove_task('task1')
    assert len(pq.mapper) == 0
    assert len(pq.pq) == 0

def test_set_priority():
    pq = PriorityQueue()
    pq.add_task('task1', 1)
    pq.set_priority('task1', 2)
    assert pq.mapper['task1'][0] == 2

def test_pop_task():
    pq = PriorityQueue()
    pq.add_task('task1', 1)
    task_popped = pq.pop_task()
    assert task_popped == 'task1'

def test_pop_task_empty_queue():
    pq = PriorityQueue()
    with pytest.raises(KeyError):
        pq.pop_task()