import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from graph2 import Graph

@pytest.fixture
def graph():
    return Graph()

def test_add_node(graph):
    graph.add_node(1)
    assert 1 in graph.nodes()

def test_add_edge(graph):
    graph.add_node(1)
    graph.add_node(2)
    graph.add_edge(1, 2)
    assert 2 in graph.neighbors(1)

def test_del_node(graph):
    graph.add_node(1)
    graph.del_node(1)
    assert not graph.has_node(1)

def test_del_edge(graph):
    graph.add_node(1)
    graph.add_node(2)
    graph.add_edge(1, 2)
    graph.del_edge(1, 2)
    assert not graph.adjacent(1, 2)

def test_has_node(graph):
    graph.add_node(1)
    assert graph.has_node(1)

def test_neighbors(graph):
    graph.add_node(1)
    graph.add_node(2)
    graph.add_edge(1, 2)
    assert 2 in graph.neighbors(1)

def test_adjacent(graph):
    graph.add_node(1)
    graph.add_node(2)
    graph.add_edge(1, 2)
    assert graph.adjacent(1, 2)