import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from graph1 import GraphNode, Graph, WeightedGraphNode, WeightedGraph

@pytest.fixture
def sample_graph():
    g = Graph(5)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 4)
    return g

def test_graph_node():
    node1 = GraphNode(1)
    node2 = GraphNode(2)
    
    node1.add_adjacent(node2)
    assert node2 in node1.adjacent_list
    
    node1.remove_adjacent(node2)
    assert node2 not in node1.adjacent_list

def test_graph_add_edge(sample_graph):
    assert sample_graph.graph == {0: [1, 2], 1: [3], 2: [4], 3: [], 4: []}

def test_graph_has_cycle(sample_graph):
    assert not sample_graph.has_cycle()

def test_graph_topological_sort(sample_graph):
    assert sample_graph.topological_sort() == [0, 2, 4, 1, 3]

def test_weighted_graph_node():
    w_node = WeightedGraphNode('A')
    w_node.add_adjacent('B', 5)
    assert w_node.adjacent == {'B': 5}

    w_node.remove_adjacent('B')
    assert 'B' not in w_node.adjacent

def test_weighted_graph():
    w_graph = WeightedGraph()
    w_graph.add_edge('A', 'B', 3)
    w_graph.add_edge('B', 'C', 2)
    
    assert str(w_graph) == "A adjacent: ['B'], B adjacent: ['C'], C adjacent: []"
    
    w_graph.remove_edge('A', 'B')
    assert str(w_graph) == "A adjacent: [], B adjacent: ['C'], C adjacent: []"