import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from graph1 import GraphNode, Graph, WeightedGraphNode, WeightedGraph

# GraphNode Tests
def test_graph_node_add_adjacent():
    node1 = GraphNode(1)
    node2 = GraphNode(2)
    node1.add_adjacent(node2)
    assert node2 in node1.adjacent_list

def test_graph_node_remove_adjacent():
    node1 = GraphNode(1)
    node2 = GraphNode(2)
    node1.add_adjacent(node2)
    node1.remove_adjacent(node2)
    assert node2 not in node1.adjacent_list

# Graph Tests
def test_graph_add_edge():
    graph = Graph(3)
    graph.add_edge(1, 2)
    assert graph.graph[1] == [2]

def test_graph_has_cycle():
    graph = Graph(4)
    graph.graph = {0: [1], 1: [2], 2: [3], 3: [0]}
    assert graph.has_cycle() == True

def test_graph_topological_sort():
    graph = Graph(4)
    graph.graph = {0: [1, 2], 1: [3], 2: [3], 3: []}
    assert graph.topological_sort() == [0, 2, 1, 3]

# WeightedGraphNode Tests
def test_weighted_graph_node_add_adjacent():
    node1 = WeightedGraphNode(1)
    node2 = WeightedGraphNode(2)
    node1.add_adjacent(node2, 5)
    assert node1.adjacent[node2] == 5

def test_weighted_graph_node_remove_adjacent():
    node1 = WeightedGraphNode(1)
    node2 = WeightedGraphNode(2)
    node1.add_adjacent(node2, 5)
    node1.remove_adjacent(node2)
    assert node2 not in node1.adjacent

# WeightedGraph Tests
def test_weighted_graph_add_edge():
    weighted_graph = WeightedGraph()
    weighted_graph.add_edge(1, 2, 5)
    assert weighted_graph.vertices[1].adjacent[2] == 5

def test_weighted_graph_remove_edge():
    weighted_graph = WeightedGraph()
    weighted_graph.add_edge(1, 2, 5)
    weighted_graph.remove_edge(1, 2)
    assert 2 not in weighted_graph.vertices[1].adjacent
