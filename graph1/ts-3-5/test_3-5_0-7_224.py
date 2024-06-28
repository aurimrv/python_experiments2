import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from graph1 import Graph, WeightedGraph

@pytest.fixture
def create_graph():
    g = Graph(4)
    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    g.add_edge(3, 0)
    return g

def test_add_edge(create_graph):
    assert len(create_graph.graph) == 4
    assert create_graph.graph[0] == [1]
    assert create_graph.graph[1] == [2]
    assert create_graph.graph[2] == [3]
    assert create_graph.graph[3] == [0]

def test_has_cycle(create_graph):
    assert create_graph.has_cycle() == True

def test_topological_sort(create_graph):
    assert create_graph.topological_sort() == [0, 1, 2, 3]

@pytest.fixture
def create_weighted_graph():
    wg = WeightedGraph()
    wg.add_edge(0, 1, 5)
    wg.add_edge(1, 2, 3)
    wg.add_edge(2, 3, 2)
    wg.add_edge(3, 0, 1)
    return wg

def test_weighted_graph_add_edge(create_weighted_graph):
    assert len(create_weighted_graph.vertices) == 4
    assert create_weighted_graph.vertices[0].adjacent[1] == 5
    assert create_weighted_graph.vertices[1].adjacent[2] == 3
    assert create_weighted_graph.vertices[2].adjacent[3] == 2
    assert create_weighted_graph.vertices[3].adjacent[0] == 1

def test_weighted_graph_remove_edge(create_weighted_graph):
    create_weighted_graph.remove_edge(0, 1)
    assert 1 not in create_weighted_graph.vertices[0].adjacent