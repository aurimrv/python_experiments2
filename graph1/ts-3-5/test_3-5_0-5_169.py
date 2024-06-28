import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from graph1 import Graph, WeightedGraph

# Test cases for Graph class
def test_graph_add_edge():
    graph = Graph(3)
    graph.add_edge(0, 1)
    assert graph.graph == {0: [1], 1: []}

def test_graph_has_cycle_no_cycle():
    graph = Graph(3)
    graph.add_edge(0, 1)
    graph.add_edge(1, 2)
    assert not graph.has_cycle()

def test_graph_has_cycle_with_cycle():
    graph = Graph(3)
    graph.add_edge(0, 1)
    graph.add_edge(1, 2)
    graph.add_edge(2, 0)
    assert graph.has_cycle()

def test_graph_topological_sort():
    graph = Graph(4)
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(1, 3)
    graph.add_edge(2, 3)
    assert graph.topological_sort() == [0, 2, 1, 3]

# Test cases for WeightedGraph class
def test_weighted_graph_add_edge():
    weighted_graph = WeightedGraph()
    weighted_graph.add_edge(0, 1, 5)
    assert weighted_graph.vertices[0].adjacent == {1: 5}

def test_weighted_graph_remove_edge():
    weighted_graph = WeightedGraph()
    weighted_graph.add_edge(0, 1, 5)
    weighted_graph.remove_edge(0, 1)
    assert weighted_graph.vertices[0].adjacent == {}

def test_weighted_graph_str():
    weighted_graph = WeightedGraph()
    weighted_graph.add_edge(0, 1, 5)
    weighted_graph.add_edge(1, 2, 3)
    assert str(weighted_graph) == "0 adjacent: [1], 1 adjacent: [2], 2 adjacent: []"