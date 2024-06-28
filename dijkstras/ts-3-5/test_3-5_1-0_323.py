import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from dijkstras import dijkstras

def test_dijkstras():
    class Vertex:
        def __init__(self, name):
            self.name = name
            self.adjacent = {}

    class WeightedGraph:
        def __init__(self):
            self.vertices = {}

    # Create a sample weighted graph
    graph = WeightedGraph()
    vertex_a = Vertex('A')
    vertex_b = Vertex('B')
    vertex_c = Vertex('C')
    vertex_a.adjacent = {'B': 1, 'C': 4}
    vertex_b.adjacent = {'A': 6, 'C': 2}
    vertex_c.adjacent = {'A': 3, 'B': 5}
    graph.vertices = {'A': vertex_a, 'B': vertex_b, 'C': vertex_c}

    assert dijkstras(graph, 'A', 'C') == ['A', 'B', 'C']
    assert dijkstras(graph, 'B', 'C') == ['B', 'C']
    assert dijkstras(graph, 'C', 'A') == ['C', 'A']

    assert dijkstras(graph, 'A', 'A') == ['A']

    # Add more tests to cover various scenarios and edge cases
