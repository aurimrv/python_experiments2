import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from graph1 import Graph, WeightedGraph

# Test cases for Graph class
class TestGraph:

    def test_add_edge(self):
        graph = Graph(5)
        graph.add_edge(0, 1)
        assert graph.graph == {0: [1], 1: []}
        graph.add_edge(2, 3)
        assert graph.graph == {0: [1], 1: [], 2: [3], 3: []}

    def test_has_cycle(self):
        graph = Graph(4)
        graph.add_edge(0, 1)
        graph.add_edge(1, 2)
        graph.add_edge(2, 3)
        assert graph.has_cycle() == False
        graph.add_edge(3, 0)
        assert graph.has_cycle() == True

    def test_topological_sort(self):
        graph = Graph(4)
        graph.add_edge(0, 1)
        graph.add_edge(1, 2)
        graph.add_edge(2, 3)
        assert graph.topological_sort() == [0, 1, 2, 3]

# Test cases for WeightedGraph class
class TestWeightedGraph:

    def test_add_edge(self):
        weighted_graph = WeightedGraph()
        weighted_graph.add_edge('A', 'B', 5)
        assert weighted_graph.vertices['A'].adjacent == {'B': 5}
        weighted_graph.add_edge('B', 'C', 3)
        assert weighted_graph.vertices['B'].adjacent == {'C': 3}

    def test_remove_edge(self):
        weighted_graph = WeightedGraph()
        weighted_graph.add_edge('X', 'Y', 2)
        weighted_graph.add_edge('Y', 'Z', 4)
        weighted_graph.remove_edge('X', 'Y')
        assert 'Y' not in weighted_graph.vertices['X'].adjacent