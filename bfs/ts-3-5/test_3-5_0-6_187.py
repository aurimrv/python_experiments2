import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from breadth_first_search import breadth_first_search, breadth_first_search_graph

# Test cases for breadth_first_search

def test_bfs_empty_grid():
    grid = []
    start = (0, 0)
    target = 1
    assert breadth_first_search(grid, start, target) is None

def test_bfs_target_at_start():
    grid = [[1, 2], [3, 4]]
    start = (0, 0)
    target = 1
    assert breadth_first_search(grid, start, target) == (0, 0)

def test_bfs_target_in_grid():
    grid = [[1, 2], [3, 4]]
    start = (0, 0)
    target = 4
    assert breadth_first_search(grid, start, target) == (1, 1)

# Test cases for breadth_first_search_graph

class Node:
    def __init__(self, val):
        self.val = val
        self.adjacent_list = []

def test_bfs_graph_target_not_found():
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node1.adjacent_list.append(node2)
    node2.adjacent_list.append(node3)

    target = 4
    assert breadth_first_search_graph(node1, target) is None

def test_bfs_graph_target_found():
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node1.adjacent_list.append(node2)
    node2.adjacent_list.append(node3)

    target = 3
    assert breadth_first_search_graph(node1, target) == node3