import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from breadth_first_search import breadth_first_search, breadth_first_search_graph

# Test cases for breadth_first_search function
def test_bfs_grid_found():
    grid = [[1, 2], [3, 4]]
    start = (0, 0)
    target = 2
    assert breadth_first_search(grid, start, target) == (1, 0)

def test_bfs_grid_not_found():
    grid = [[1, 2], [3, 4]]
    start = (0, 0)
    target = 5
    assert breadth_first_search(grid, start, target) is None
    
def test_bfs_graph_found():
    class Node:
        def __init__(self, val):
            self.val = val
            self.adjacent_list = []

    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)

    node1.adjacent_list.append(node2)
    node2.adjacent_list.append(node3)

    target = 3

    assert breadth_first_search_graph(node1, target) == node3

def test_bfs_graph_not_found():
    class Node:
        def __init__(self, val):
            self.val = val
            self.adjacent_list = []

    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)

    node1.adjacent_list.append(node2)

    target = 4

    assert breadth_first_search_graph(node1, target) is None