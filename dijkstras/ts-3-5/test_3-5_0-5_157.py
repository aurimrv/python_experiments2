import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from dijkstras import dijkstras

class TestDijkstras:
    def test_shortest_path_case1(self):
        weighted_graph = WeightedGraph()
        # Add vertices and edges to the weighted_graph
        src = 'A'
        dst = 'D'
        assert dijkstras(weighted_graph, src, dst) == ['A', 'B', 'D']

    def test_shortest_path_case2(self):
        weighted_graph = WeightedGraph()
        # Add vertices and edges to the weighted_graph
        src = 'B'
        dst = 'C'
        assert dijkstras(weighted_graph, src, dst) == ['B', 'C']

    def test_shortest_path_case3(self):
        weighted_graph = WeightedGraph()
        # Add vertices and edges to the weighted_graph
        src = 'A'
        dst = 'C'
        assert dijkstras(weighted_graph, src, dst) == ['A', 'B', 'C']

    def test_shortest_path_case4(self):
        weighted_graph = WeightedGraph()
        # Add vertices and edges to the weighted_graph
        src = 'A'
        dst = 'E'
        assert dijkstras(weighted_graph, src, dst) == ['A', 'B', 'D', 'E']

    def test_shortest_path_case5(self):
        weighted_graph = WeightedGraph()
        # Add vertices and edges to the weighted_graph
        src = 'C'
        dst = 'D'
        assert dijkstras(weighted_graph, src, dst) == ['C', 'B', 'D']

class WeightedGraph:
    def __init__(self):
        self.vertices = {
            'A': Vertex('A', {'B': 1, 'D': 3}),
            'B': Vertex('B', {'A': 1, 'C': 1, 'D': 1}),
            'C': Vertex('C', {'B': 1, 'D': 2}),
            'D': Vertex('D', {'A': 3, 'B': 1, 'C': 2, 'E': 1}),
            'E': Vertex('E', {'D': 1})
        }

class Vertex:
    def __init__(self, name, adjacent):
        self.name = name
        self.adjacent = adjacent