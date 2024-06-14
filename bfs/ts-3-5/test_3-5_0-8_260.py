import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from breadth_first_search import breadth_first_search, breadth_first_search_graph

@pytest.fixture
def grid_1():
    return [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]

@pytest.fixture
def graph_node():
    class GraphNode:
        def __init__(self, val):
            self.val = val
            self.adjacent_list = []

    node1 = GraphNode(1)
    node2 = GraphNode(2)
    node3 = GraphNode(3)
    node1.adjacent_list = [node2, node3]
    return node1

def test_breadth_first_search(grid_1):
    assert breadth_first_search(grid_1, (0, 0), 5) == (1, 1)
    assert breadth_first_search(grid_1, (2, 2), 9) == (2, 2)
    assert breadth_first_search(grid_1, (1, 1), 7) == (0, 2)

def test_breadth_first_search_graph(graph_node):
    target_node = breadth_first_search_graph(graph_node, 3)
    assert target_node.val == 3

    target_node = breadth_first_search_graph(graph_node, 2)
    assert target_node.val == 2