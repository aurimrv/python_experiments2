import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from graph1 import GraphNode, Graph, WeightedGraphNode, WeightedGraph

@pytest.fixture
def sample_graph():
    graph = Graph(4)
    graph.add_edge(0, 1)
    graph.add_edge(1, 2)
    graph.add_edge(2, 3)
    return graph

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

def test_graph_add_edge(sample_graph):
    assert sample_graph.graph == {0: [1], 1: [2], 2: [3], 3: []}

def test_graph_has_cycle():
    graph = Graph(3)
    graph.add_edge(0, 1)
    graph.add_edge(1, 2)
    assert graph.has_cycle() == False

def test_weighted_graph_node_add_adjacent():
    node1 = WeightedGraphNode(1)
    node2 = WeightedGraphNode(2)
    node1.add_adjacent(node2, 5)
    assert node2 in node1.adjacent.keys()

def test_weighted_graph_node_remove_adjacent():
    node1 = WeightedGraphNode(1)
    node2 = WeightedGraphNode(2)
    node1.add_adjacent(node2, 5)
    node1.remove_adjacent(node2)
    assert node2 not in node1.adjacent.keys()

def test_weighted_graph_add_edge():
    weighted_graph = WeightedGraph()
    weighted_graph.add_edge(0, 1, 10)
    assert weighted_graph.vertices[0].adjacent[1] == 10