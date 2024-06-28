import os
import sys
import pytest
from collections import defaultdict, deque

# Importing the file and modules for testing
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from graph1 import Graph, WeightedGraph

# Test cases for Graph class
class TestGraph:
    def test_add_edge(self):
        g = Graph(4)
        g.add_edge(0, 1)
        assert g.graph == {0: [1], 1: []}

    def test_has_cycle_manual(self):
        g = Graph(4)
        g.graph = {0: [1], 1: [2], 2: [3], 3: [0]}
        assert g.has_cycle() == True

    def test_topological_sort(self):
        g = Graph(4)
        g.graph = {0: [1, 2], 1: [3], 2: [3], 3: []}
        assert g.topological_sort() == [0, 2, 1, 3]

# Test cases for WeightedGraph class
class TestWeightedGraph:
    def test_add_vertex(self):
        wg = WeightedGraph()
        wg.add_vertex(1)
        assert 1 in wg.vertices

    def test_add_edge(self):
        wg = WeightedGraph()
        wg.add_edge(1, 2, 5)
        assert wg.vertices[1].adjacent == {2: 5}

    def test_remove_edge(self):
        wg = WeightedGraph()
        wg.add_edge(1, 2, 5)
        wg.remove_edge(1, 2)
        assert 2 not in wg.vertices[1].adjacent

# Run the tests
if __name__ == '__main__':
    pytest.main()