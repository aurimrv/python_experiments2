import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from graph1 import Graph, WeightedGraph

@pytest.fixture
def graph():
    return Graph(4)

def test_add_edge(graph):
    graph.add_edge(0, 1)
    assert graph.graph == {0: [1], 1: []}
    
    graph.add_edge(1, 2)
    assert graph.graph == {0: [1], 1: [2], 2: []}

def test_has_cycle(graph):
    graph.add_edge(0, 1)
    graph.add_edge(1, 2)
    graph.add_edge(2, 3)
    assert not graph.has_cycle()
    
    graph.add_edge(3, 0)  # introduce cycle
    assert graph.has_cycle()

def test_topological_sort(graph):
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(1, 3)
    graph.add_edge(2, 3)
    
    result = graph.topological_sort()
    assert result == [0, 2, 1, 3]

@pytest.fixture
def weighted_graph():
    return WeightedGraph()

def test_weighted_graph_add_edge(weighted_graph):
    weighted_graph.add_edge('A', 'B', 5)
    weighted_graph.add_edge('B', 'C', 3)
    
    assert weighted_graph.vertices['A'].adjacent == {'B': 5}
    assert weighted_graph.vertices['B'].adjacent == {'C': 3}

def test_weighted_graph_remove_edge(weighted_graph):
    weighted_graph.add_edge('A', 'B', 5)
    weighted_graph.add_edge('B', 'C', 3)
    
    weighted_graph.remove_edge('A', 'B')
    assert 'B' not in weighted_graph.vertices['A'].adjacent