import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from dijkstras import dijkstras

class TestDijkstras:

    def test_dijkstras_basic_case(self):
        weighted_graph = WeightedGraph()
        weighted_graph.add_vertex('A')
        weighted_graph.add_vertex('B')
        weighted_graph.add_vertex('C')
        weighted_graph.add_vertex('D')
        weighted_graph.add_edge('A', 'B', 1)
        weighted_graph.add_edge('B', 'C', 2)
        weighted_graph.add_edge('C', 'D', 3)

        result = dijkstras(weighted_graph, 'A', 'D')
        assert result == ['A', 'B', 'C', 'D']

    def test_dijkstras_same_source_destination(self):
        weighted_graph = WeightedGraph()
        weighted_graph.add_vertex('X')

        result = dijkstras(weighted_graph, 'X', 'X')
        assert result == ['X']

    def test_dijkstras_unreachable_destination(self):
        weighted_graph = WeightedGraph()
        weighted_graph.add_vertex('P')
        weighted_graph.add_vertex('Q')
        weighted_graph.add_edge('P', 'Q', 5)

        result = dijkstras(weighted_graph, 'P', 'Q')
        assert result == ['P', 'Q']


# Mock WeightedGraph class for testing purposes
class WeightedGraph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        self.vertices[vertex] = Vertex(vertex)

    def add_edge(self, start, end, weight):
        self.vertices[start].add_adjacent(end, weight)


class Vertex:
    def __init__(self, label):
        self.label = label
        self.adjacent = {}

    def add_adjacent(self, vertex, weight):
        self.adjacent[vertex] = weight