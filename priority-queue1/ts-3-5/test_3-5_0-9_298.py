import pytest
import os
import sys

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from priority_queue1 import PriorityQueue

@pytest.fixture
def pq():
    return PriorityQueue()

def test_add_task(pq):
    pq.add_task('task1', 1)
    assert 'task1' in pq.mapper
    assert len(pq.pq) == 1

    pq.add_task('task2', 3)
    assert 'task2' in pq.mapper
    assert len(pq.pq) == 2

def test_remove_task(pq):
    pq.add_task('task1', 1)
    pq.remove_task('task1')
    assert 'task1' not in pq.mapper

def test_set_priority(pq):
    pq.add_task('task1', 1)
    pq.add_task('task2', 3)
    pq.set_priority('task1', 2)
    assert pq.mapper['task1'][0] == 2

def test_pop_task(pq):
    pq.add_task('task1', 1)
    pq.add_task('task2', 3)
    popped_task = pq.pop_task()
    assert popped_task in ['task1', 'task2']
    assert popped_task not in pq.mapper