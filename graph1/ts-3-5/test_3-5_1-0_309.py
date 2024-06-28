import pytest
import os
import sys
from collections import defaultdict, deque

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from graph1 import *

# Testing GraphNode class
class TestGraphNode:

    def test_init(self):
        node = GraphNode(1)
        assert node.val == 1
        assert len(node.adjacent_list) == 0

    def test_add_adjacent(self):
        node1 = GraphNode(1)
        node2 = GraphNode(2)
        node1.add_adjacent(node2)
        assert len(node1.adjacent_list) == 1
        assert node2 in node1.adjacent_list

# Testing Graph class
class TestGraph:

    def test_init(self):
        graph = Graph(5)
        assert len(graph.graph) == 0
        assert graph.verticies == 5

    def test_add_edge(self):
        graph = Graph(5)
        graph.add_edge(1, 2)
        assert len(graph.graph) == 2
        assert graph.graph[1] == [2]
        assert graph.graph[2] == []

    def test_has_cycle(self):
        graph = Graph(3)
        graph.add_edge(0, 1)
        graph.add_edge(1, 2)
        assert not graph.has_cycle()

        graph.add_edge(2, 0)
        assert graph.has_cycle()

    def test_topological_sort(self):
        graph = Graph(4)
        graph.add_edge(0, 1)
        graph.add_edge(1, 2)
        graph.add_edge(1, 3)
        graph.add_edge(2, 3)
        assert graph.topological_sort() == [0, 1, 2, 3]


# Testing WeightedGraphNode class
class TestWeightedGraphNode:

    def test_init(self):
        w_node = WeightedGraphNode(10)
        assert w_node.val == 10
        assert len(w_node.adjacent) == 0

    def test_add_adjacent(self):
        w_node1 = WeightedGraphNode(10)
        w_node2 = WeightedGraphNode(20)
        w_node1.add_adjacent(w_node2, 5)
        assert len(w_node1.adjacent) == 1
        assert w_node1.adjacent[w_node2] == 5

    def test_remove_adjacent(self):
        w_node1 = WeightedGraphNode(10)
        w_node2 = WeightedGraphNode(20)
        w_node1.add_adjacent(w_node2, 5)
        w_node1.remove_adjacent(w_node2)
        assert len(w_node1.adjacent) == 0


# Testing WeightedGraph class
class TestWeightedGraph:

    def test_init(self):
        w_graph = WeightedGraph()
        assert len(w_graph.vertices) == 0

    def test_add_edge(self):
        w_graph = WeightedGraph()
        w_graph.add_edge(1, 2, 5)
        assert len(w_graph.vertices) == 2
        assert 2 in w_graph.vertices[1].adjacent
        assert w_graph.vertices[1].adjacent[2] == 5

    def test_remove_edge(self):
        w_graph = WeightedGraph()
        w_graph.add_edge(1, 2, 5)
        w_graph.remove_edge(1, 2)
        assert 2 not in w_graph.vertices[1].adjacent