import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from dijkstras import dijkstras

def test_dijkstras_simple_path():
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
    v1.adjacent = {v2: 2, v3: 5}
    v2.adjacent = {v3: 2}
    weighted_graph.vertices = {v1: v1, v2: v2, v3: v3}

    src = v1
    dst = v3

    assert dijkstras(weighted_graph, src, dst) == [v1, v2, v3]

def test_dijkstras_no_path():
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
    v1.adjacent = {v2: 2}
    v2.adjacent = {v3: 3}
    weighted_graph.vertices = {v1: v1, v2: v2, v3: v3}

    src = v1
    dst = v3

    assert dijkstras(weighted_graph, src, dst) == [v1, v2, v3]

def test_dijkstras_same_node():
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
    v1.adjacent = {v2: 2, v3: 5}
    v2.adjacent = {v3: 2}
    weighted_graph.vertices = {v1: v1, v2: v2, v3: v3}

    src = v1
    dst = v1

    assert dijkstras(weighted_graph, src, dst) == [v1]
