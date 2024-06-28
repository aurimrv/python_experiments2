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

    def test_has_cycle(self):
        graph = Graph(4)
        graph.add_edge(0, 1)
        graph.add_edge(1, 2)
        graph.add_edge(2, 3)
        graph.add_edge(3, 0)
        assert graph.has_cycle() == True

    def test_topological_sort(self):
        graph = Graph(4)
        graph.add_edge(0, 1)
        graph.add_edge(0, 2)
        graph.add_edge(1, 3)
        graph.add_edge(2, 3)
        assert graph.topological_sort() == [0, 2, 1, 3]

# Test cases for WeightedGraph class
class TestWeightedGraph:
    def test_add_vertex(self):
        w_graph = WeightedGraph()
        w_graph.add_vertex(1)
        assert len(w_graph.vertices) == 1

    def test_add_edge(self):
        w_graph = WeightedGraph()
        w_graph.add_edge(1, 2, 5)
        assert w_graph.vertices[1].adjacent == {2: 5}

    def test_remove_edge(self):
        w_graph = WeightedGraph()
        w_graph.add_edge(1, 2, 5)
        w_graph.remove_edge(1, 2)
        assert w_graph.vertices[1].adjacent == {}