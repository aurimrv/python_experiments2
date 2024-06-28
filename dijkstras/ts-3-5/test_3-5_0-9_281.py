import os
import sys

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from dijkstras import dijkstras

def test_dijkstras():
    class Vertex:
        def __init__(self):
            self.adjacent = {}

    class WeightedGraph:
        def __init__(self):
            self.vertices = {}

    # Setup weighted graph
    graph = WeightedGraph()
    graph.vertices = {
        'A': Vertex(),
        'B': Vertex(),
        'C': Vertex(),
        'D': Vertex(),
        'E': Vertex()
    }
    graph.vertices['A'].adjacent = {'B': 4, 'C': 2}
    graph.vertices['B'].adjacent = {'A': 4, 'C': 5, 'D': 10}
    graph.vertices['C'].adjacent = {'A': 2, 'B': 5, 'D': 3}
    graph.vertices['D'].adjacent = {'B': 10, 'C': 3, 'E': 7}
    graph.vertices['E'].adjacent = {'D': 7}

    # Test cases
    assert dijkstras(graph, 'A', 'E') == ['A', 'C', 'D', 'E']
    assert dijkstras(graph, 'A', 'B') == ['A', 'B']
    assert dijkstras(graph, 'B', 'E') == ['B', 'D', 'E']
    assert dijkstras(graph, 'C', 'D') == ['C', 'D']
    assert dijkstras(graph, 'D', 'A') == ['D', 'C', 'A']