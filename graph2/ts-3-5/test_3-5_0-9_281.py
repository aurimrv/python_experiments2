import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from graph2 import Graph

@pytest.fixture
def empty_graph():
    return Graph()

@pytest.fixture
def graph_with_data():
    return Graph(['A', 'B', 'C', 'D'])

def test_nodes_empty_graph(empty_graph):
    assert empty_graph.nodes() == []

def test_edges_empty_graph(empty_graph):
    assert empty_graph.edges() == []

def test_add_node(empty_graph):
    empty_graph.add_node('A')
    assert 'A' in empty_graph.nodes()

def test_add_edge(empty_graph):
    empty_graph.add_node('A')
    empty_graph.add_node('B')
    empty_graph.add_edge('A', 'B')
    assert 'B' in empty_graph.neighbors('A')

def test_del_node(graph_with_data):
    graph_with_data.del_node('A')
    assert 'A' not in graph_with_data.nodes()

def test_del_edge(graph_with_data):
    with pytest.raises(KeyError):
        graph_with_data.del_edge('B', 'C')

def test_has_node(graph_with_data):
    assert graph_with_data.has_node('D') == True

def test_neighbors(graph_with_data):
    assert graph_with_data.neighbors('B') == set()

def test_adjacent(graph_with_data):
    assert graph_with_data.adjacent('A', 'B') == False