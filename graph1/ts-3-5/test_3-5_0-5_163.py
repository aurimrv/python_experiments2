import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from graph1 import Graph, GraphNode, WeightedGraph, WeightedGraphNode

# Test cases for GraphNode class
def test_graph_node_init():
    node = GraphNode(1)
    assert node.val == 1
    assert len(node.adjacent_list) == 0

def test_graph_node_add_remove_adjacent():
    node1 = GraphNode(1)
    node2 = GraphNode(2)
    node1.add_adjacent(node2)
    assert node2 in node1.adjacent_list
    node1.remove_adjacent(node2)
    assert node2 not in node1.adjacent_list

# Test cases for Graph class
def test_graph_init():
    graph = Graph(5)
    assert len(graph.graph) == 0
    assert graph.verticies == 5

def test_graph_add_edge():
    graph = Graph(3)
    graph.add_edge(1, 2)
    assert graph.graph[1] == [2]
    graph.add_edge(2, 3)
    assert graph.graph[2] == [3]
    assert graph.graph[3] == []

def test_graph_has_cycle():
    graph = Graph(4)
    graph.add_edge(0, 1)
    graph.add_edge(1, 2)
    graph.add_edge(2, 3)
    assert not graph.has_cycle()

def test_graph_topological_sort():
    graph = Graph(4)
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(1, 3)
    graph.add_edge(2, 3)
    assert graph.topological_sort() == [0, 2, 1, 3]

# Test cases for WeightedGraphNode class
def test_weighted_graph_node_init():
    node = WeightedGraphNode(1)
    assert node.val == 1
    assert len(node.adjacent) == 0

def test_weighted_graph_node_add_remove_adjacent():
    node1 = WeightedGraphNode(1)
    node2 = WeightedGraphNode(2)
    node1.add_adjacent(node2, 5)
    assert node2 in node1.adjacent
    assert node1.adjacent[node2] == 5
    node1.remove_adjacent(node2)
    assert node2 not in node1.adjacent

# Test cases for WeightedGraph class
def test_weighted_graph_init():
    weighted_graph = WeightedGraph()
    assert len(weighted_graph.vertices) == 0

def test_weighted_graph_add_vertex():
    weighted_graph = WeightedGraph()
    weighted_graph.add_vertex(1)
    assert 1 in weighted_graph.vertices

def test_weighted_graph_add_edge():
    weighted_graph = WeightedGraph()
    weighted_graph.add_edge(1, 2, 3)
    assert 1 in weighted_graph.vertices
    assert 2 in weighted_graph.vertices[1].adjacent
    assert weighted_graph.vertices[1].adjacent[2] == 3

def test_weighted_graph_remove_edge():
    weighted_graph = WeightedGraph()
    weighted_graph.add_edge(1, 2, 3)
    weighted_graph.remove_edge(1, 2)
    assert 2 not in weighted_graph.vertices[1].adjacent