import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from dijkstras import dijkstras

import pytest

@pytest.fixture
def weighted_graph():
    class Vertex:
        def __init__(self, data):
            self.data = data
            self.adjacent = {}

    class Graph:
        def __init__(self):
            self.vertices = {}

        def add_vertex(self, vertex):
            self.vertices[vertex.data] = vertex

        def add_edge(self, vertex1, vertex2, weight):
            self.vertices[vertex1].adjacent[vertex2] = weight
            self.vertices[vertex2].adjacent[vertex1] = weight

    g = Graph()
    v0 = Vertex(0)
    v1 = Vertex(1)
    v2 = Vertex(2)
    v3 = Vertex(3)
    v4 = Vertex(4)
    g.add_vertex(v0)
    g.add_vertex(v1)
    g.add_vertex(v2)
    g.add_vertex(v3)
    g.add_vertex(v4)
    g.add_edge(0, 1, 4)
    g.add_edge(0, 2, 1)
    g.add_edge(1, 3, 1)
    g.add_edge(1, 4, 5)
    g.add_edge(2, 1, 2)
    g.add_edge(2, 3, 5)
    g.add_edge(3, 4, 3)
    return g

def test_dijkstras_path_found(weighted_graph):
    src = 0
    dst = 4
    path = dijkstras(weighted_graph, src, dst)
    assert path == [0, 2, 1, 3, 4]

def test_dijkstras_path_not_found(weighted_graph):
    src = 4
    dst = 0
    path = dijkstras(weighted_graph, src, dst)
    assert path == []

def test_dijkstras_same_source_and_destination(weighted_graph):
    src = 2
    dst = 2
    path = dijkstras(weighted_graph, src, dst)
    assert path == [2]