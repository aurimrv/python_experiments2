import os
import sys

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from dijkstras import dijkstras

class TestDijkstras:
    
    def test_dijkstras_shortest_path(self):
        weighted_graph = WeightedGraph()
        weighted_graph.add_vertex('A')
        weighted_graph.add_vertex('B')
        weighted_graph.add_vertex('C')
        weighted_graph.add_vertex('D')
        weighted_graph.add_edge('A', 'B', 1)
        weighted_graph.add_edge('A', 'C', 4)
        weighted_graph.add_edge('B', 'C', 2)
        weighted_graph.add_edge('B', 'D', 5)
        weighted_graph.add_edge('C', 'D', 1)
        
        src = 'A'
        dst = 'D'
        
        shortest_path = dijkstras(weighted_graph, src, dst)
        assert shortest_path == ['A', 'B', 'C', 'D']
        
    def test_dijkstras_no_path(self):
        weighted_graph = WeightedGraph()
        weighted_graph.add_vertex('A')
        weighted_graph.add_vertex('B')
        weighted_graph.add_vertex('C')
        
        weighted_graph.add_edge('A', 'B', 1)
        weighted_graph.add_edge('B', 'C', 2)
        
        src = 'A'
        dst = 'C'
        
        shortest_path = dijkstras(weighted_graph, src, dst)
        assert shortest_path == ['A', 'B', 'C']
        
    def test_dijkstras_same_node(self):
        weighted_graph = WeightedGraph()
        weighted_graph.add_vertex('A')
        weighted_graph.add_vertex('B')
        
        weighted_graph.add_edge('A', 'B', 3)
        
        src = 'A'
        dst = 'A'
        
        shortest_path = dijkstras(weighted_graph, src, dst)
        assert shortest_path == ['A']

    def test_dijkstras_single_vertex(self):
        weighted_graph = WeightedGraph()
        weighted_graph.add_vertex('A')
        
        src = 'A'
        dst = 'A'
        
        shortest_path = dijkstras(weighted_graph, src, dst)
        assert shortest_path == ['A']

class WeightedGraph:
    def __init__(self):
        self.vertices = {}
        
    def add_vertex(self, key):
        self.vertices[key] = Vertex(key)
        
    def add_edge(self, key1, key2, weight):
        self.vertices[key1].add_neighbor(self.vertices[key2], weight)
        self.vertices[key2].add_neighbor(self.vertices[key1], weight)

class Vertex:
    def __init__(self, key):
        self.key = key
        self.adjacent = {}
        
    def add_neighbor(self, neighbor, weight):
        self.adjacent[neighbor.key] = weight