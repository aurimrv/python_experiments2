import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from graph1 import Graph, WeightedGraph

@pytest.fixture
def simple_graph():
    graph = Graph(5)
    graph.add_edge(0, 1)
    graph.add_edge(1, 2)
    graph.add_edge(2, 3)
    graph.add_edge(3, 4)
    return graph

@pytest.fixture
def cyclic_graph():
    graph = Graph(4)
    graph.add_edge(0, 1)
    graph.add_edge(1, 2)
    graph.add_edge(2, 3)
    graph.add_edge(3, 0)
    return graph

def test_graph_add_edge(simple_graph):
    simple_graph.add_edge(0, 2)
    assert simple_graph.graph == {0: [1, 2], 1: [2], 2: [3], 3: [4], 4: []}

def test_graph_has_cycle_cyclic(cyclic_graph):
    assert cyclic_graph.has_cycle() == True

def test_graph_has_cycle_acyclic(simple_graph):
    assert simple_graph.has_cycle() == False

def test_graph_topological_sort(simple_graph):
    assert simple_graph.topological_sort() == [0, 1, 2, 3, 4]

@pytest.fixture
def weighted_graph():
    w_graph = WeightedGraph()
    w_graph.add_edge(0, 1, 5)
    w_graph.add_edge(1, 2, 3)
    w_graph.add_edge(2, 3, 2)
    return w_graph

def test_weighted_graph_add_edge(weighted_graph):
    weighted_graph.add_edge(0, 2, 4)
    assert weighted_graph.vertices[0].adjacent == {1: 5, 2: 4}

def test_weighted_graph_remove_edge(weighted_graph):
    weighted_graph.remove_edge(1, 2)
    assert 2 not in weighted_graph.vertices[1].adjacent