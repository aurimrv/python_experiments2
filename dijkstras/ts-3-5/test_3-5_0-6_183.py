import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from dijkstras import dijkstras

class TestDijkstras:

    def test_shortest_path_case1(self):
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
        assert dijkstras(weighted_graph, src, dst) == ['A', 'B', 'C', 'D']

    def test_shortest_path_case2(self):
        weighted_graph = WeightedGraph()
        weighted_graph.add_vertex('A')
        weighted_graph.add_vertex('B')
        weighted_graph.add_vertex('C')
        
        weighted_graph.add_edge('A', 'B', 3)
        weighted_graph.add_edge('A', 'C', 1)
        weighted_graph.add_edge('B', 'C', 2)
        
        src = 'A'
        dst = 'C'
        assert dijkstras(weighted_graph, src, dst) == ['A', 'C']

    def test_shortest_path_case3(self):
        weighted_graph = WeightedGraph()
        weighted_graph.add_vertex('A')
        weighted_graph.add_vertex('B')
        weighted_graph.add_vertex('C')
        
        weighted_graph.add_edge('A', 'B', 1)
        weighted_graph.add_edge('B', 'C', 2)
        
        src = 'A'
        dst = 'C'
        assert dijkstras(weighted_graph, src, dst) == ['A', 'B', 'C']

    def test_shortest_path_case4(self):
        weighted_graph = WeightedGraph()
        weighted_graph.add_vertex('A')
        weighted_graph.add_vertex('B')
        weighted_graph.add_vertex('C')
        
        weighted_graph.add_edge('A', 'B', 2)
        weighted_graph.add_edge('B', 'C', 3)
        
        src = 'A'
        dst = 'C'
        assert dijkstras(weighted_graph, src, dst) == ['A', 'B', 'C']

    def test_shortest_path_case5(self):
        weighted_graph = WeightedGraph()
        weighted_graph.add_vertex('A')
        weighted_graph.add_vertex('B')
        weighted_graph.add_vertex('C')
        
        weighted_graph.add_edge('A', 'B', 5)
        weighted_graph.add_edge('A', 'C', 2)
        weighted_graph.add_edge('B', 'C', 1)
        
        src = 'A'
        dst = 'C'
        assert dijkstras(weighted_graph, src, dst) == ['A', 'C']

class WeightedGraph:

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = Vertex(vertex)

    def add_edge(self, start, end, weight):
        if start in self.vertices and end in self.vertices:
            self.vertices[start].adjacent[end] = weight
            self.vertices[end].adjacent[start] = weight

class Vertex:

    def __init__(self, name):
        self.name = name
        self.adjacent = {}