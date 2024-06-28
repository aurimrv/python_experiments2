import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from graph1 import Graph, WeightedGraph

def test_graph_add_edge():
    g = Graph(3)
    g.add_edge(0, 1)
    assert g.graph == {0: [1], 1: []}

    g.add_edge(1, 2)
    assert g.graph == {0: [1], 1: [2], 2: []}

def test_graph_has_cycle():
    g = Graph(4)
    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    g.add_edge(3, 0)
    assert g.has_cycle() == True

    g = Graph(3)
    g.add_edge(0, 1)
    g.add_edge(1, 2)
    assert g.has_cycle() == False

def test_graph_topological_sort():
    g = Graph(4)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 3)
    assert g.topological_sort() == [0, 2, 1, 3]

def test_weighted_graph_add_edge():
    wg = WeightedGraph()
    wg.add_edge('A', 'B', 5)
    assert wg.vertices['A'].adjacent == {'B': 5}

    wg.add_edge('B', 'C', 3)
    assert wg.vertices['B'].adjacent == {'C': 3}

def test_weighted_graph_remove_edge():
    wg = WeightedGraph()
    wg.add_edge('A', 'B', 5)
    wg.add_edge('B', 'C', 3)
    wg.remove_edge('A', 'B')
    assert 'B' not in wg.vertices['A'].adjacent

    wg.remove_edge('B', 'C')
    assert 'C' not in wg.vertices['B'].adjacent