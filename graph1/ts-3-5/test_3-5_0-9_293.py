import sys
import os
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from graph1 import Graph, WeightedGraph

# Test cases for Graph class
def test_add_edge():
    graph = Graph(5)
    graph.add_edge(1, 2)
    assert graph.graph == {1: [2], 2: []}

def test_has_cycle_no_cycle():
    graph = Graph(3)
    graph.add_edge(0, 1)
    graph.add_edge(1, 2)
    assert graph.has_cycle() == False

def test_has_cycle_with_cycle():
    graph = Graph(4)
    graph.add_edge(0, 1)
    graph.add_edge(1, 2)
    graph.add_edge(2, 3)
    graph.add_edge(3, 0)
    assert graph.has_cycle() == True

def test_topological_sort():
    graph = Graph(4)
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(1, 3)
    graph.add_edge(2, 3)
    assert graph.topological_sort() == [0, 2, 1, 3]

# Test cases for WeightedGraph class
def test_add_edge():
    wgraph = WeightedGraph()
    wgraph.add_edge(1, 2, 5)
    assert wgraph.vertices[1].adjacent[2] == 5

def test_remove_edge():
    wgraph = WeightedGraph()
    wgraph.add_edge(1, 2, 5)
    wgraph.remove_edge(1, 2)
    assert 2 not in wgraph.vertices[1].adjacent

def test_add_vertex():
    wgraph = WeightedGraph()
    wgraph.add_vertex(1)
    assert 1 in wgraph.vertices

def test_remove_vertex():
    wgraph = WeightedGraph()
    wgraph.add_vertex(1)
    del wgraph.vertices[1]
    assert 1 not in wgraph.vertices

def test_str():
    wgraph = WeightedGraph()
    wgraph.add_vertex(1)
    wgraph.add_vertex(2)
    wgraph.add_edge(1, 2, 3)
    assert wgraph.__str__() == "1 adjacent: [2], 2 adjacent: []"