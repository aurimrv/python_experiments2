import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from graph1 import Graph, WeightedGraph

@pytest.fixture
def graph():
    g = Graph(4)
    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    g.add_edge(3, 0)
    return g

def test_graph_add_edge(graph):
    assert graph.graph == {0: [1], 1: [2], 2: [3], 3: [0]}

def test_graph_has_cycle(graph):
    assert graph.has_cycle() == True

def test_graph_topological_sort(graph):
    assert graph.topological_sort() == [0, 1, 2, 3]

@pytest.fixture
def weighted_graph():
    wg = WeightedGraph()
    wg.add_edge(0, 1, 5)
    wg.add_edge(1, 2, 3)
    wg.add_edge(2, 3, 2)
    return wg

def test_weighted_graph_add_edge(weighted_graph):
    assert weighted_graph.vertices[0].adjacent == {1: 5}
    assert weighted_graph.vertices[1].adjacent == {2: 3}
    assert weighted_graph.vertices[2].adjacent == {3: 2}

def test_weighted_graph_remove_edge(weighted_graph):
    weighted_graph.remove_edge(1, 2)
    assert 2 not in weighted_graph.vertices[1].adjacent
