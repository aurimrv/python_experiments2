import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from dijkstras import dijkstras

class Vertex:
    def __init__(self):
        self.adjacent = {}

class Graph:
    def __init__(self):
        self.vertices = {}

@pytest.fixture
def weighted_graph():
    vertices = {
        'A': Vertex(),
        'B': Vertex(),
        'C': Vertex(),
        'D': Vertex(),
        'E': Vertex()
    }

    vertices['A'].adjacent = {'B': 1, 'C': 4}
    vertices['B'].adjacent = {'A': 1, 'C': 2, 'D': 5}
    vertices['C'].adjacent = {'A': 4, 'B': 2, 'D': 1}
    vertices['D'].adjacent = {'B': 5, 'C': 1, 'E': 3}
    vertices['E'].adjacent = {'D': 3}

    graph = Graph()
    graph.vertices = vertices
    return graph

def test_dijkstras_shortest_path(weighted_graph):
    assert dijkstras(weighted_graph, 'A', 'E') == ['A', 'C', 'D', 'E']
    assert dijkstras(weighted_graph, 'B', 'E') == ['B', 'C', 'D', 'E']

def test_dijkstras_no_path(weighted_graph):
    assert dijkstras(weighted_graph, 'D', 'A') == []

def test_dijkstras_same_source_dest(weighted_graph):
    assert dijkstras(weighted_graph, 'E', 'E') == ['E']

def test_dijkstras_invalid_source(weighted_graph):
    with pytest.raises(KeyError):
        dijkstras(weighted_graph, 'F', 'A')

def test_dijkstras_invalid_destination(weighted_graph):
    with pytest.raises(KeyError):
        dijkstras(weighted_graph, 'A', 'F')