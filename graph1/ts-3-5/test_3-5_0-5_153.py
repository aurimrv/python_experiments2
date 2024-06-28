import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from graph1 import GraphNode, Graph, WeightedGraphNode, WeightedGraph

# Tests for GraphNode class
class TestGraphNode:
    def test_add_adjacent(self):
        node1 = GraphNode(1)
        node2 = GraphNode(2)
        node1.add_adjacent(node2)
        assert node2 in node1.adjacent_list

    def test_remove_adjacent(self):
        node1 = GraphNode(1)
        node2 = GraphNode(2)
        node1.add_adjacent(node2)
        node1.remove_adjacent(node2)
        assert node2 not in node1.adjacent_list

# Tests for Graph class
class TestGraph:
    def test_add_edge(self):
        graph = Graph(3)
        graph.add_edge(0, 1)
        assert graph.graph == {0: [1], 1: []}

    def test_has_cycle(self):
        graph = Graph(3)
        graph.add_edge(0, 1)
        graph.add_edge(1, 2)
        graph.add_edge(2, 0)
        assert graph.has_cycle() == True

    def test_topological_sort(self):
        graph = Graph(3)
        graph.add_edge(0, 1)
        graph.add_edge(0, 2)
        graph.add_edge(1, 2)
        assert graph.topological_sort() == [0, 1, 2]

# Tests for WeightedGraphNode class
class TestWeightedGraphNode:
    def test_add_adjacent(self):
        node1 = WeightedGraphNode(1)
        node2 = WeightedGraphNode(2)
        node1.add_adjacent(node2, 5)
        assert node2 in node1.adjacent and node1.adjacent[node2] == 5

    def test_remove_adjacent(self):
        node1 = WeightedGraphNode(1)
        node2 = WeightedGraphNode(2)
        node1.add_adjacent(node2, 5)
        node1.remove_adjacent(node2)
        assert node2 not in node1.adjacent

# Tests for WeightedGraph class
class TestWeightedGraph:
    def test_add_edge(self):
        weighted_graph = WeightedGraph()
        weighted_graph.add_edge(0, 1, 10)
        assert weighted_graph.vertices[0].adjacent[1] == 10

    def test_remove_edge(self):
        weighted_graph = WeightedGraph()
        weighted_graph.add_edge(0, 1, 10)
        weighted_graph.remove_edge(0, 1)
        assert 1 not in weighted_graph.vertices[0].adjacent