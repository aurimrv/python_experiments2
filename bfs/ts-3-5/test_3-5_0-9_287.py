import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from breadth_first_search import breadth_first_search, breadth_first_search_graph

# Tests for breadth_first_search method
def test_breadth_first_search_empty_grid():
    assert breadth_first_search([], (0, 0), 1) == None

def test_breadth_first_search_target_at_start():
    grid = [[1, 2], [3, 4]]
    assert breadth_first_search(grid, (0, 0), 1) == (0, 0)

def test_breadth_first_search_target_not_found():
    grid = [[1, 2], [3, 4]]
    assert breadth_first_search(grid, (0, 0), 5) == None

# Tests for breadth_first_search_graph method
class Node:
    def __init__(self, val):
        self.val = val
        self.adjacent_list = []

def test_breadth_first_search_graph_target_not_found():
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)

    node1.adjacent_list.extend([node2, node3])

    assert breadth_first_search_graph(node1, 4) == None

def test_breadth_first_search_graph_target_found():
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)

    node1.adjacent_list.extend([node2, node3])

    assert breadth_first_search_graph(node1, 3) == node3