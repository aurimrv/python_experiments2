import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from priority_queue2 import PriorityQ


def test_priorityq_insert():
    pq = PriorityQ()
    pq.insert(5)
    assert pq.peek() == 5

    pq.insert(10, 2)
    assert pq.peek() == 10

    pq.insert(3, 1)
    assert pq.peek() == 10


def test_priorityq_pop():
    pq = PriorityQ()
    pq.insert(5)
    pq.insert(10, 2)
    pq.insert(3, 1)

    assert pq.pop() == 10
    assert pq.pop() == 3
    assert pq.pop() == 5


def test_priorityq_peek():
    pq = PriorityQ()
    assert pq.peek() is None

    pq.insert(5, 1)
    assert pq.peek() == 5

    pq.insert(10, 2)
    assert pq.peek() == 10