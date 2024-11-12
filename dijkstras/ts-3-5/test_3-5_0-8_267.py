# test_dijkstras.py

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

def test_dijkstras():
    # Test case 1: Shortest path between two directly connected vertices
    vertex_a = Vertex({"B": 5})
    vertex_b = Vertex({})
    graph = WeightedGraph({"A": vertex_a, "B": vertex_b})
    assert dijkstras(graph, "A", "B") == ["A", "B"]

    # Test case 2: Shortest path with multiple vertices and edges
    vertex_a = Vertex({"B": 5, "C": 3})
    vertex_b = Vertex({"D": 7})
    vertex_c = Vertex({"D": 2})
    vertex_d = Vertex({})
    graph = WeightedGraph({"A": vertex_a, "B": vertex_b, "C": vertex_c, "D": vertex_d})
    assert dijkstras(graph, "A", "D") == ["A", "C", "D"]

    # Test case 3: Shortest path with circular dependency
    vertex_a = Vertex({"B": 5})
    vertex_b = Vertex({"C": 3})
    vertex_c = Vertex({"A": 2})
    graph = WeightedGraph({"A": vertex_a, "B": vertex_b, "C": vertex_c})
    assert dijkstras(graph, "A", "C") == ["A", "B", "C"]