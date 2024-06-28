import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from priority_queue2 import PriorityQ

import pytest

# Testing the PriorityQ class
class TestPriorityQ:
    def test_insert_single(self):
        pq = PriorityQ()
        pq.insert('value1', 1)
        assert pq.peek() == 'value1'

    def test_insert_multiple(self):
        pq = PriorityQ()
        pq.insert('value2', 2)
        pq.insert('value3', 3)
        assert pq.peek() == 'value3'

    def test_pop_single(self):
        pq = PriorityQ()
        pq.insert('value1', 1)
        assert pq.pop() == 'value1'

    def test_pop_multiple(self):
        pq = PriorityQ()
        pq.insert('value2', 2)
        pq.insert('value3', 3)
        assert pq.pop() == 'value3'
        assert pq.pop() == 'value2'

    def test_peek_empty(self):
        pq = PriorityQ()
        assert pq.peek() is None

    def test_pop_empty(self):
        pq = PriorityQ()
        with pytest.raises(IndexError):
            pq.pop()