import os
import sys
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
    # Test case 1 - Shortest path when source equals destination
    vertices = {
        'A': Vertex({'B': 1, 'C': 2}),
        'B': Vertex({'A': 1, 'C': 3}),
        'C': Vertex({'A': 2, 'B': 3})
    }
    weighted_graph = WeightedGraph(vertices)
    src = 'A'
    dst = 'A'
    assert dijkstras(weighted_graph, src, dst) == ['A']

    # Test case 2 - Shortest path when source to destination is direct
    src = 'A'
    dst = 'C'
    assert dijkstras(weighted_graph, src, dst) == ['A', 'C']

    # Test case 3 - Shortest path when there are multiple possible paths
    vertices = {
        'A': Vertex({'B': 1, 'C': 2}),
        'B': Vertex({'A': 1, 'C': 1}),
        'C': Vertex({'A': 2, 'B': 1})
    }
    weighted_graph = WeightedGraph(vertices)
    src = 'A'
    dst = 'C'
    assert dijkstras(weighted_graph, src, dst) == ['A', 'B', 'C']

    # Test case 4 - Shortest path in a more complex graph
    vertices = {
        'A': Vertex({'B': 2, 'D': 5}),
        'B': Vertex({'A': 2, 'C': 3, 'D': 2}),
        'C': Vertex({'B': 3, 'E': 4}),
        'D': Vertex({'A': 5, 'B': 2, 'E': 1}),
        'E': Vertex({'C': 4, 'D': 1})
    }
    weighted_graph = WeightedGraph(vertices)
    src = 'A'
    dst = 'E'
    assert dijkstras(weighted_graph, src, dst) == ['A', 'B', 'D', 'E']

    # Add more test cases here to cover all branches in the dijkstras function