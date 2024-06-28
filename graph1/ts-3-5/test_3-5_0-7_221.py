import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from graph1 import Graph, WeightedGraph

def test_graph_add_edge():
    g = Graph(4)
    g.add_edge(0, 1)
    assert g.graph == {0: [1], 1: []}

def test_graph_has_cycle():
    g = Graph(4)
    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    assert g.has_cycle() is False

def test_graph_topological_sort():
    g = Graph(4)
    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    assert g.topological_sort() == [0, 1, 2, 3]

def test_weighted_graph_add_vertex():
    wg = WeightedGraph()
    wg.add_vertex(0)
    assert len(wg.vertices) == 1

def test_weighted_graph_add_edge():
    wg = WeightedGraph()
    wg.add_edge(0, 1, 5)
    assert wg.vertices[0].adjacent == {1: 5}

def test_weighted_graph_remove_edge():
    wg = WeightedGraph()
    wg.add_edge(0, 1, 5)
    wg.remove_edge(0, 1)
    assert wg.vertices[0].adjacent == {}
