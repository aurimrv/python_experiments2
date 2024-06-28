import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from graph1 import Graph, WeightedGraph

# Tests for Graph class
def test_graph_add_edge():
    graph = Graph(5)
    graph.add_edge(0, 1)
    assert 1 in graph.graph[0]
    assert graph.graph[1] == []

def test_graph_has_cycle():
    graph = Graph(3)
    graph.add_edge(0, 1)
    graph.add_edge(1, 2)
    graph.add_edge(2, 0)
    assert graph.has_cycle() == True

    graph = Graph(3)
    graph.add_edge(0, 1)
    graph.add_edge(1, 2)
    assert graph.has_cycle() == False

def test_graph_topological_sort():
    graph = Graph(4)
    graph.add_edge(0, 1)
    graph.add_edge(1, 2)
    graph.add_edge(2, 3)
    assert graph.topological_sort() == [0, 1, 2, 3]

# Tests for WeightedGraph class
def test_weighted_graph_add_edge():
    w_graph = WeightedGraph()
    w_graph.add_edge(0, 1, 5)
    assert w_graph.vertices[0].adjacent[1] == 5

def test_weighted_graph_remove_edge():
    w_graph = WeightedGraph()
    w_graph.add_edge(0, 1, 3)
    w_graph.remove_edge(0, 1)
    assert 1 not in w_graph.vertices[0].adjacent

def test_weighted_graph_add_vertex():
    w_graph = WeightedGraph()
    w_graph.add_vertex(0)
    assert 0 in w_graph.vertices

def test_weighted_graph_str():
    w_graph = WeightedGraph()
    w_graph.add_vertex(0)
    w_graph.add_vertex(1)
    w_graph.add_edge(0, 1, 2)
    assert str(w_graph) == "0 adjacent: [1], 1 adjacent: []"
