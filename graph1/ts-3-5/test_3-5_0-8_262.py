import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from graph1 import Graph, WeightedGraph

# Tests for Graph class
class TestGraph:
    
    def test_add_edge(self):
        g = Graph(5)
        g.add_edge(0, 1)
        assert g.graph == {0: [1], 1: []}
        
    def test_has_cycle(self):
        g = Graph(3)
        g.add_edge(0, 1)
        g.add_edge(1, 2)
        g.add_edge(2, 1)
        assert g.has_cycle() == True
    
    def test_topological_sort(self):
        g = Graph(4)
        g.add_edge(0, 1)
        g.add_edge(0, 2)
        g.add_edge(1, 3)
        g.add_edge(2, 3)
        assert g.topological_sort() == [0, 2, 1, 3]

# Tests for WeightedGraph class
class TestWeightedGraph:
    
    def test_add_vertex(self):
        wg = WeightedGraph()
        wg.add_vertex('A')
        assert 'A' in wg.vertices
    
    def test_add_edge(self):
        wg = WeightedGraph()
        wg.add_edge('A', 'B', 5)
        assert 'A' in wg.vertices and 'B' in wg.vertices['A'].adjacent
    
    def test_remove_edge(self):
        wg = WeightedGraph()
        wg.add_edge('A', 'B', 5)
        wg.remove_edge('A', 'B')
        assert 'B' not in wg.vertices['A'].adjacent