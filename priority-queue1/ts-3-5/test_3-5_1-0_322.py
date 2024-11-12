import os
import sys
import itertools
from heapq import heappush, heappop

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from priority_queue1 import PriorityQueue

def test_priority_queue_init():
    pq = PriorityQueue()
    assert pq is not None

def test_add_task():
    pq = PriorityQueue()
    pq.add_task('task1', 10)
    assert pq.mapper['task1'][0] == 10

def test_remove_task():
    pq = PriorityQueue()
    pq.add_task('task1', 5)
    pq.remove_task('task1')
    assert 'task1' not in pq.mapper

def test_set_priority():
    pq = PriorityQueue()
    pq.add_task('task1', 5)
    pq.set_priority('task1', 10)
    assert pq.mapper['task1'][0] == 10

def test_pop_task():
    pq = PriorityQueue()
    pq.add_task('task1', 10)
    assert pq.pop_task() == 'task1'

def test_pop_task_empty_queue():
    pq = PriorityQueue()
    try:
        pq.pop_task()
    except KeyError as e:
        assert str(e) == "'task1'"