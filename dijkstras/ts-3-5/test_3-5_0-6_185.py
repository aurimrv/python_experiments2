import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from dijkstras import dijkstras

def test_dijkstras_shortest_path():
    weighted_graph = WeightedGraph()
    weighted_graph.add_vertex('A')
    weighted_graph.add_vertex('B')
    weighted_graph.add_vertex('C')
    weighted_graph.add_vertex('D')
    weighted_graph.add_vertex('E')

    weighted_graph.add_edge('A', 'B', 4)
    weighted_graph.add_edge('A', 'C', 2)
    weighted_graph.add_edge('B', 'C', 5)
    weighted_graph.add_edge('B', 'D', 10)
    weighted_graph.add_edge('C', 'E', 3)
    weighted_graph.add_edge('D', 'E', 7)

    assert dijkstras(weighted_graph, 'A', 'E') == ['A', 'C', 'E']

def test_dijkstras_shortest_path_same_vertex():
    weighted_graph = WeightedGraph()
    weighted_graph.add_vertex('A')

    assert dijkstras(weighted_graph, 'A', 'A') == ['A']

def test_dijkstras_shortest_path_no_path():
    weighted_graph = WeightedGraph()
    weighted_graph.add_vertex('A')
    weighted_graph.add_vertex('B')

    weighted_graph.add_edge('A', 'B', 5)

    assert dijkstras(weighted_graph, 'A', 'B') == ['A', 'B']

class WeightedGraph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = Vertex(vertex)

    def add_edge(self, start_vertex, end_vertex, weight):
        if start_vertex in self.vertices and end_vertex in self.vertices:
            self.vertices[start_vertex].add_neighbor(end_vertex, weight)
            self.vertices[end_vertex].add_neighbor(start_vertex, weight)

class Vertex:
    def __init__(self, vertex):
        self.vertex = vertex
        self.adjacent = {}

    def add_neighbor(self, neighbor, weight):
        self.adjacent[neighbor] = weight