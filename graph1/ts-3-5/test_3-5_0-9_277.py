import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from graph1 import Graph, WeightedGraph

import pytest

@pytest.fixture
def create_graph():
    graph = Graph(4)
    graph.add_edge(0, 1)
    graph.add_edge(1, 2)
    graph.add_edge(2, 3)
    graph.add_edge(3, 0)
    return graph

def test_graph_add_edge(create_graph):
    assert list(create_graph.graph.keys()) == [0, 1, 2, 3]
    assert create_graph.graph[0] == [1]
    assert create_graph.graph[1] == [2]
    create_graph.add_edge(1, 3)
    assert create_graph.graph[1] == [2, 3]

def test_graph_has_cycle(create_graph):
    assert create_graph.has_cycle() == True

def test_graph_topological_sort(create_graph):
    assert create_graph.topological_sort() == [0, 1, 2, 3]

@pytest.fixture
def create_weighted_graph():
    w_graph = WeightedGraph()
    w_graph.add_edge(0, 1, 5)
    w_graph.add_edge(1, 2, 3)
    w_graph.add_edge(2, 3, 2)
    return w_graph

def test_weighted_graph_add_edge(create_weighted_graph):
    assert len(create_weighted_graph.vertices) == 4
    assert create_weighted_graph.vertices[0].adjacent[1] == 5
    create_weighted_graph.add_edge(0, 2, 4)
    assert create_weighted_graph.vertices[0].adjacent[2] == 4

def test_weighted_graph_remove_edge(create_weighted_graph):
    assert 1 in create_weighted_graph.vertices[0].adjacent
    create_weighted_graph.remove_edge(0, 1)
    assert 1 not in create_weighted_graph.vertices[0].adjacent