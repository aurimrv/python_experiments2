import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from dijkstras import dijkstras

class WeightedGraph:
    def __init__(self, vertices):
        self.vertices = vertices

class Vertex:
    def __init__(self, adjacent):
        self.adjacent = adjacent

@pytest.fixture
def weighted_graph():
    vertices = {
        'A': Vertex({'B': 2, 'C': 4}),
        'B': Vertex({'A': 2, 'C': 1, 'D': 7}),
        'C': Vertex({'A': 4, 'B': 1, 'D': 3}),
        'D': Vertex({'B': 7, 'C': 3})
    }
    return WeightedGraph(vertices)

def test_dijkstras_shortest_path(weighted_graph):
    assert dijkstras(weighted_graph, 'A', 'D') == ['A', 'B', 'C', 'D']

def test_dijkstras_no_path(weighted_graph):
    assert dijkstras(weighted_graph, 'A', 'E') == []

def test_dijkstras_same_source_dest(weighted_graph):
    assert dijkstras(weighted_graph, 'A', 'A') == ['A']

def test_dijkstras_path_with_single_edge(weighted_graph):
    assert dijkstras(weighted_graph, 'B', 'D') == ['B', 'D']

def test_dijkstras_path_with_multiple_options(weighted_graph):
    assert dijkstras(weighted_graph, 'C', 'D') == ['C', 'D']

def test_dijkstras_path_with_higher_weight(weighted_graph):
    assert dijkstras(weighted_graph, 'B', 'C') == ['B', 'C']