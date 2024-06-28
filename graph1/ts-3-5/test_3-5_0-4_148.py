import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from graph1 import Graph, WeightedGraph

# Test cases for Graph class
class TestGraph:
    def test_add_edge(self):
        g = Graph(3)
        g.add_edge(0, 1)
        assert g.graph == {0: [1], 1: []}

    def test_has_cycle(self):
        g = Graph(3)
        g.add_edge(0, 1)
        g.add_edge(1, 2)
        assert g.has_cycle() == False

    def test_topological_sort(self):
        g = Graph(4)
        g.add_edge(0, 1)
        g.add_edge(0, 2)
        g.add_edge(1, 3)
        g.add_edge(2, 3)
        assert g.topological_sort() == [0, 2, 1, 3]

# Test cases for WeightedGraph class
class TestWeightedGraph:
    def test_add_vertex(self):
        wg = WeightedGraph()
        wg.add_vertex(1)
        assert wg.vertices == {1: wg.vertices[1]}

    def test_add_edge(self):
        wg = WeightedGraph()
        wg.add_edge(1, 2, 5)
        assert wg.vertices[1].adjacent == {2: 5}

    def test_remove_edge(self):
        wg = WeightedGraph()
        wg.add_edge(1, 2, 5)
        wg.remove_edge(1, 2)
        assert 2 not in wg.vertices[1].adjacent

    def test_remove_edge_invalid(self):
        wg = WeightedGraph()
        wg.add_edge(1, 2, 5)
        wg.remove_edge(2, 1)
        assert 2 in wg.vertices[1].adjacent
