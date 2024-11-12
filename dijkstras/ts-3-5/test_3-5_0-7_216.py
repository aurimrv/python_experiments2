import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from dijkstras import dijkstras

class TestDijkstras:
    def test_dijkstras_shortest_path(self):
        weighted_graph = WeightedGraph()
        weighted_graph.add_vertex(Vertex('A', {'B': 1, 'C': 4}))
        weighted_graph.add_vertex(Vertex('B', {'A': 1, 'C': 2, 'D': 5}))
        weighted_graph.add_vertex(Vertex('C', {'A': 4, 'B': 2, 'D': 1}))
        weighted_graph.add_vertex(Vertex('D', {'B': 5, 'C': 1}))
        
        src = 'A'
        dst = 'D'
        assert dijkstras(weighted_graph, src, dst) == ['A', 'B', 'C', 'D']

    def test_dijkstras_no_path(self):
        weighted_graph = WeightedGraph()
        weighted_graph.add_vertex(Vertex('A', {'B': 1}))
        weighted_graph.add_vertex(Vertex('B', {'A': 1}))
        
        src = 'A'
        dst = 'B'
        assert dijkstras(weighted_graph, src, dst) == ['A', 'B']

    def test_dijkstras_single_node(self):
        weighted_graph = WeightedGraph()
        weighted_graph.add_vertex(Vertex('A', {}))
        
        src = 'A'
        dst = 'A'
        assert dijkstras(weighted_graph, src, dst) == ['A']

    def test_dijkstras_same_source_dest(self):
        weighted_graph = WeightedGraph()
        weighted_graph.add_vertex(Vertex('A', {'B': 1}))
        weighted_graph.add_vertex(Vertex('B', {'A': 1}))
        
        src = 'A'
        dst = 'A'
        assert dijkstras(weighted_graph, src, dst) == ['A']

class WeightedGraph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        self.vertices[vertex.label] = vertex

class Vertex:
    def __init__(self, label, adjacent):
        self.label = label
        self.adjacent = adjacent