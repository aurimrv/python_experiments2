import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from priority_queue1 import PriorityQueue

@pytest.fixture
def priority_queue():
    return PriorityQueue()

def test_add_task(priority_queue):
    priority_queue.add_task('Task1', 2)
    assert 'Task1' in priority_queue.mapper

    priority_queue.add_task('Task2', 1)
    assert 'Task2' in priority_queue.mapper

def test_remove_task(priority_queue):
    priority_queue.add_task('Task1', 2)
    priority_queue.remove_task('Task1')
    assert 'Task1' not in priority_queue.mapper

def test_set_priority(priority_queue):
    priority_queue.add_task('Task1', 2)
    priority_queue.set_priority('Task1', 1)
    assert priority_queue.mapper['Task1'][0] == 1

def test_pop_task(priority_queue):
    priority_queue.add_task('Task1', 2)
    priority_queue.add_task('Task2', 1)

    popped_task = priority_queue.pop_task()
    assert popped_task == 'Task2'

    popped_task = priority_queue.pop_task()
    assert popped_task == 'Task1'

    with pytest.raises(KeyError):
        priority_queue.pop_task()