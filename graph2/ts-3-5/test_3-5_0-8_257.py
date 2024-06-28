import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from graph2 import Graph

# Test cases for Graph class methods

def test_nodes_empty_graph():
    g = Graph()
    assert len(g.nodes()) == 0

def test_nodes_with_data():
    data = [1, 2, 3]
    g = Graph(data)
    assert len(g.nodes()) == len(data)

def test_edges_empty_graph():
    g = Graph()
    assert len(g.edges()) == 0

def test_edges_with_edges():
    g = Graph()
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    assert len(g.edges()) == 2

def test_add_node():
    g = Graph()
    g.add_node(1)
    assert 1 in g.nodes()

def test_add_edge():
    g = Graph()
    g.add_node(1)
    g.add_node(2)
    g.add_edge(1, 2)
    assert g.adjacent(1, 2)

def test_del_node():
    g = Graph()
    g.add_node(1)
    g.del_node(1)
    assert 1 not in g.nodes()

def test_del_edge():
    g = Graph()
    g.add_node(1)
    g.add_node(2)
    g.add_edge(1, 2)
    g.del_edge(1, 2)
    assert not g.adjacent(1, 2)

def test_has_node():
    g = Graph()
    g.add_node(1)
    assert g.has_node(1)

def test_neighbors():
    g = Graph()
    g.add_node(1)
    g.add_node(2)
    g.add_edge(1, 2)
    assert 2 in g.neighbors(1)

def test_adjacent():
    g = Graph()
    g.add_node(1)
    g.add_node(2)
    g.add_edge(1, 2)
    assert g.adjacent(1, 2)
