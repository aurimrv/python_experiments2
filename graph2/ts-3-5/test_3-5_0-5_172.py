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
    graph.add_node('A')
    assert graph.has_node('A') == True

def test_add_edge(graph):
    graph.add_node('A')
    graph.add_node('B')
    graph.add_edge('A', 'B')
    assert graph.adjacent('A', 'B') == True

def test_del_node(graph):
    graph.add_node('A')
    graph.del_node('A')
    assert graph.has_node('A') == False

def test_del_edge(graph):
    graph.add_node('A')
    graph.add_node('B')
    graph.add_edge('A', 'B')
    graph.del_edge('A', 'B')
    assert graph.adjacent('A', 'B') == False

def test_has_node(graph):
    graph.add_node('A')
    assert graph.has_node('A') == True

def test_neighbors(graph):
    graph.add_node('A')
    graph.add_node('B')
    graph.add_edge('A', 'B')
    assert graph.neighbors('A') == {'B'}

def test_adjacent(graph):
    graph.add_node('A')
    graph.add_node('B')
    graph.add_edge('A', 'B')
    assert graph.adjacent('A', 'B') == True