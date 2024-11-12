import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from dijkstras import dijkstras

class TestDijkstras:

    def test_shortest_path_case1(self):
        # Test case with a simple graph
        class Vertex:
            def __init__(self, value):
                self.value = value
                self.adjacent = {}
        
        class Graph:
            def __init__(self):
                self.vertices = {}
        
        graph = Graph()
        graph.vertices = {
            'A': Vertex('A'),
            'B': Vertex('B'),
            'C': Vertex('C')
        }
        graph.vertices['A'].adjacent = {'B': 3, 'C': 1}
        graph.vertices['B'].adjacent = {'C': 2}
        
        result = dijkstras(graph, 'A', 'C')
        assert result == ['A', 'C']
    
    def test_shortest_path_case2(self):
        # Test case with a more complex graph
        class Vertex:
            def __init__(self, value):
                self.value = value
                self.adjacent = {}

        class Graph:
            def __init__(self):
                self.vertices = {}
        
        graph = Graph()
        graph.vertices = {
            'A': Vertex('A'),
            'B': Vertex('B'),
            'C': Vertex('C'),
            'D': Vertex('D'),
            'E': Vertex('E')
        }
        graph.vertices['A'].adjacent = {'B': 6, 'D': 1}
        graph.vertices['B'].adjacent = {'D': 2, 'C': 2, 'E': 2}
        graph.vertices['C'].adjacent = {'E': 1}
        graph.vertices['D'].adjacent = {'E': 5}
        
        result = dijkstras(graph, 'A', 'E')
        assert result == ['A', 'D', 'E']