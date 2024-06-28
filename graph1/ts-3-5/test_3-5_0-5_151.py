import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from graph1 import Graph, WeightedGraph

@pytest.fixture
def sample_graph():
    g = Graph(5)
    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    g.add_edge(3, 4)
    return g

def test_graph_add_edge(sample_graph):
    sample_graph.add_edge(4, 0)
    assert sample_graph.graph[4] == [0]

def test_graph_has_cycle(sample_graph):
    assert not sample_graph.has_cycle()

def test_graph_topological_sort(sample_graph):
    assert sample_graph.topological_sort() == [0, 1, 2, 3, 4]

@pytest.fixture
def sample_weighted_graph():
    wg = WeightedGraph()
    wg.add_edge('A', 'B', 5)
    wg.add_edge('B', 'C', 3)
    wg.add_edge('C', 'D', 2)
    return wg

def test_weighted_graph_add_edge(sample_weighted_graph):
    sample_weighted_graph.add_edge('D', 'A', 1)
    assert sample_weighted_graph.vertices['D'].adjacent['A'] == 1

def test_weighted_graph_remove_edge(sample_weighted_graph):
    sample_weighted_graph.remove_edge('B', 'C')
    assert 'C' not in sample_weighted_graph.vertices['B'].adjacent