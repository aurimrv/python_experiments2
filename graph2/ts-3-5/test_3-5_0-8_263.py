import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from graph2 import Graph

# Test Graph class initialization
def test_graph_init():
    g = Graph([1, 2, 3])
    assert len(g.nodes()) == 3

# Test add_node method
def test_add_node():
    g = Graph()
    g.add_node(1)
    assert 1 in g.nodes()

# Test add_edge method
def test_add_edge():
    g = Graph()
    g.add_node(1)
    g.add_node(2)
    g.add_edge(1, 2)
    assert g.adjacent(1, 2) is True

# Test del_node method
def test_del_node():
    g = Graph()
    g.add_node(1)
    g.del_node(1)
    assert 1 not in g.nodes()

# Test del_edge method
def test_del_edge():
    g = Graph()
    g.add_node(1)
    g.add_node(2)
    g.add_edge(1, 2)
    g.del_edge(1, 2)
    assert g.adjacent(1, 2) is False

# Test has_node method
def test_has_node():
    g = Graph()
    g.add_node(1)
    assert g.has_node(1) is True

# Test neighbors method
def test_neighbors():
    g = Graph()
    g.add_node(1)
    g.add_node(2)
    g.add_edge(1, 2)
    assert 2 in g.neighbors(1)

# Test adjacent method
def test_adjacent():
    g = Graph()
    g.add_node(1)
    g.add_node(2)
    g.add_edge(1, 2)
    assert g.adjacent(1, 2) is True