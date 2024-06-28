import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from graph1 import Graph, WeightedGraph

@pytest.fixture
def graph():
    g = Graph(5)
    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    g.add_edge(3, 4)
    return g

def test_graph_add_edge(graph):
    assert graph.graph == {0: [1], 1: [2], 2: [3], 3: [4], 4: []}

def test_graph_has_cycle_no_cycle(graph):
    assert not graph.has_cycle()

def test_graph_has_cycle_with_cycle():
    g = Graph(3)
    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    assert g.has_cycle()

def test_graph_topological_sort(graph):
    assert graph.topological_sort() == [0, 1, 2, 3, 4]

@pytest.fixture
def weighted_graph():
    wg = WeightedGraph()
    wg.add_edge('A', 'B', 5)
    wg.add_edge('B', 'C', 3)
    wg.add_edge('C', 'D', 2)
    return wg

def test_weighted_graph_add_edge(weighted_graph):
    assert weighted_graph.vertices['A'].adjacent == {'B': 5}
    assert weighted_graph.vertices['B'].adjacent == {'C': 3}
    assert weighted_graph.vertices['C'].adjacent == {'D': 2}

def test_weighted_graph_remove_edge(weighted_graph):
    weighted_graph.remove_edge('B', 'C')
    assert 'C' not in weighted_graph.vertices['B'].adjacent
