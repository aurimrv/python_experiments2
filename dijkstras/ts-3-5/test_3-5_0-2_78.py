import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from dijkstras import dijkstras

class TestDijkstras:
    def test_shortest_path_case1(self):
        weighted_graph = WeightedGraph()
        # Add vertices and edges to weighted_graph
        src = 'A'
        dst = 'D'
        assert dijkstras(weighted_graph, src, dst) == ['A', 'B', 'D']

    def test_shortest_path_case2(self):
        weighted_graph = WeightedGraph()
        # Add vertices and edges to weighted_graph
        src = 'A'
        dst = 'C'
        assert dijkstras(weighted_graph, src, dst) == ['A', 'C']

    def test_shortest_path_case3(self):
        weighted_graph = WeightedGraph()
        # Add vertices and edges to weighted_graph
        src = 'B'
        dst = 'D'
        assert dijkstras(weighted_graph, src, dst) == ['B', 'D']

    def test_shortest_path_case4(self):
        weighted_graph = WeightedGraph()
        # Add vertices and edges to weighted_graph
        src = 'C'
        dst = 'A'
        assert dijkstras(weighted_graph, src, dst) == ['C', 'A']

    def test_shortest_path_case5(self):
        weighted_graph = WeightedGraph()
        # Add vertices and edges to weighted_graph
        src = 'D'
        dst = 'B'
        assert dijkstras(weighted_graph, src, dst) == ['D', 'B']

    def test_shortest_path_case6(self):
        weighted_graph = WeightedGraph()
        # Add vertices and edges to weighted_graph
        src = 'A'
        dst = 'A'
        assert dijkstras(weighted_graph, src, dst) == ['A']

    def test_shortest_path_case7(self):
        weighted_graph = WeightedGraph()
        # Add vertices and edges to weighted_graph
        src = 'B'
        dst = 'B'
        assert dijkstras(weighted_graph, src, dst) == ['B']

    def test_shortest_path_case8(self):
        weighted_graph = WeightedGraph()
        # Add vertices and edges to weighted_graph
        src = 'C'
        dst = 'C'
        assert dijkstras(weighted_graph, src, dst) == ['C']

    def test_shortest_path_case9(self):
        weighted_graph = WeightedGraph()
        # Add vertices and edges to weighted_graph
        src = 'D'
        dst = 'D'
        assert dijkstras(weighted_graph, src, dst) == ['D']

class WeightedGraph:
    def __init__(self):
        self.vertices = {
            'A': Vertex('A', {'B': 1, 'C': 4}),
            'B': Vertex('B', {'A': 1, 'D': 2}),
            'C': Vertex('C', {'A': 4, 'D': 5}),
            'D': Vertex('D', {'B': 2, 'C': 5})
        }

class Vertex:
    def __init__(self, name, adjacent):
        self.name = name
        self.adjacent = adjacent