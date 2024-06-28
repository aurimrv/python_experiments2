import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from dijkstras import dijkstras

def test_dijkstras_basic():
    class WeightedGraph:
        def __init__(self, vertices):
            self.vertices = vertices

    class Vertex:
        def __init__(self, adjacent):
            self.adjacent = adjacent

    vertices = {
        'A': Vertex({'B': 2, 'C': 4}),
        'B': Vertex({'A': 2, 'C': 1, 'D': 7}),
        'C': Vertex({'A': 4, 'B': 1, 'D': 3}),
        'D': Vertex({'B': 7, 'C': 3})
    }

    weighted_graph = WeightedGraph(vertices)
    src = 'A'
    dst = 'D'

    assert dijkstras(weighted_graph, src, dst) == ['A', 'B', 'C', 'D']

def test_dijkstras_no_path():
    class WeightedGraph:
        def __init__(self, vertices):
            self.vertices = vertices

    class Vertex:
        def __init__(self, adjacent):
            self.adjacent = adjacent

    vertices = {
        'A': Vertex({'B': 2, 'C': 4}),
        'B': Vertex({'A': 2, 'C': 1, 'D': 7}),
        'C': Vertex({'A': 4, 'B': 1, 'D': 3}),
        'D': Vertex({'B': 7, 'C': 3})
    }

    weighted_graph = WeightedGraph(vertices)
    src = 'A'
    dst = 'E'

    assert dijkstras(weighted_graph, src, dst) == []

def test_dijkstras_same_source_and_destination():
    class WeightedGraph:
        def __init__(self, vertices):
            self.vertices = vertices

    class Vertex:
        def __init__(self, adjacent):
            self.adjacent = adjacent

    vertices = {
        'A': Vertex({'B': 2, 'C': 4}),
        'B': Vertex({'A': 2, 'C': 1, 'D': 7}),
        'C': Vertex({'A': 4, 'B': 1, 'D': 3}),
        'D': Vertex({'B': 7, 'C': 3})
    }

    weighted_graph = WeightedGraph(vertices)
    src = 'A'
    dst = 'A'

    assert dijkstras(weighted_graph, src, dst) == ['A']
