import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from dijkstras import dijkstras

class TestDijkstras:
    def test_shortest_path_case1(self):
        class Vertex:
            def __init__(self):
                self.adjacent = {}
        
        class WeightedGraph:
            def __init__(self):
                self.vertices = {}
        
        weighted_graph = WeightedGraph()
        
        v1 = Vertex()
        v2 = Vertex()
        v3 = Vertex()
        
        v1.adjacent = {v2: 2, v3: 4}
        v2.adjacent = {v3: 1}
        
        weighted_graph.vertices = {v1: v1, v2: v2, v3: v3}
        
        src = v1
        dst = v3
        
        assert dijkstras(weighted_graph, src, dst) == [v1, v2, v3]

    def test_shortest_path_case2(self):
        class Vertex:
            def __init__(self):
                self.adjacent = {}
        
        class WeightedGraph:
            def __init__(self):
                self.vertices = {}
        
        weighted_graph = WeightedGraph()
        
        v1 = Vertex()
        v2 = Vertex()
        v3 = Vertex()
        v4 = Vertex()
        
        v1.adjacent = {v2: 2, v3: 4}
        v2.adjacent = {v3: 1, v4: 3}
        v3.adjacent = {v4: 2}
        
        weighted_graph.vertices = {v1: v1, v2: v2, v3: v3, v4: v4}
        
        src = v1
        dst = v4
        
        assert dijkstras(weighted_graph, src, dst) == [v1, v2, v3, v4]