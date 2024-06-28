import os
import sys
import pytest
from collections import defaultdict, deque

# Append project directory to sys.path
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from graph1 import GraphNode, Graph, WeightedGraphNode, WeightedGraph

def test_graph_node():
    node1 = GraphNode(1)
    node2 = GraphNode(2)
    
    node1.add_adjacent(node2)
    assert node2 in node1.adjacent_list

    node1.remove_adjacent(node2)
    assert node2 not in node1.adjacent_list

def test_graph_add_edge():
    g = Graph(3)
    
    g.add_edge(1, 2)
    assert g.graph == {1: [2], 2: []}

    g.add_edge(2, 3)
    assert g.graph == {1: [2], 2: [3], 3: []}

def test_graph_has_cycle():
    g = Graph(4)
    g.graph = {0: [1], 1: [2], 2: [3], 3: [0]}
    
    assert g.has_cycle() == True

    g.graph = {0: [1], 1: [2], 2: [3], 3: []}
    assert g.has_cycle() == False

def test_graph_topological_sort():
    g = Graph(4)
    g.graph = {0: [1, 2], 1: [3], 2: [3], 3: []}

    assert g.topological_sort() == [0, 2, 1, 3]

def test_weighted_graph_node():
    w_node1 = WeightedGraphNode(1)
    w_node2 = WeightedGraphNode(2)
    
    w_node1.add_adjacent(w_node2, 5)
    assert w_node2 in w_node1.adjacent
    assert w_node1.adjacent[w_node2] == 5

    w_node1.remove_adjacent(w_node2)
    assert w_node2 not in w_node1.adjacent

def test_weighted_graph_add_edge():
    wg = WeightedGraph()
    wg.add_edge(1, 2, 5)
    
    assert wg.vertices[1].adjacent == {2: 5}

    wg.add_edge(2, 3, 3)
    assert wg.vertices[2].adjacent == {3: 3}

def test_weighted_graph_remove_edge():
    wg = WeightedGraph()
    wg.add_edge(1, 2, 5)
    wg.remove_edge(1, 2)
    
    assert 2 not in wg.vertices[1].adjacent