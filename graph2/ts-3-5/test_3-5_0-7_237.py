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

def test_add_node(empty_graph):
    empty_graph.add_node(1)
    assert empty_graph.has_node(1) == True

def test_add_edge(empty_graph):
    empty_graph.add_node(1)
    empty_graph.add_node(2)
    empty_graph.add_edge(1, 2)
    assert empty_graph.adjacent(1, 2) == True

def test_del_node(empty_graph):
    empty_graph.add_node(1)
    empty_graph.del_node(1)
    assert empty_graph.has_node(1) == False

def test_del_edge(empty_graph):
    empty_graph.add_node(1)
    empty_graph.add_node(2)
    empty_graph.add_edge(1, 2)
    empty_graph.del_edge(1, 2)
    assert empty_graph.adjacent(1, 2) == False

def test_has_node(empty_graph):
    empty_graph.add_node(1)
    assert empty_graph.has_node(1) == True

def test_neighbors(empty_graph):
    empty_graph.add_node(1)
    empty_graph.add_node(2)
    empty_graph.add_edge(1, 2)
    assert empty_graph.neighbors(1) == {2}

def test_adjacent(empty_graph):
    empty_graph.add_node(1)
    empty_graph.add_node(2)
    empty_graph.add_edge(1, 2)
    assert empty_graph.adjacent(1, 2) == True