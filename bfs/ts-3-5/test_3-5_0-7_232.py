import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from breadth_first_search import breadth_first_search, breadth_first_search_graph

# Test cases for breadth_first_search function

def test_bfs_search_target_exists():
    grid = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    start = (0, 0)
    target = 5
    assert breadth_first_search(grid, start, target) == (1, 1)

def test_bfs_search_target_not_exists():
    grid = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    start = (0, 0)
    target = 10
    assert breadth_first_search(grid, start, target) is None

# Test cases for breadth_first_search_graph function

class Node:
    def __init__(self, val):
        self.val = val
        self.adjacent_list = []

def test_bfs_graph_search_target_exists():
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)

    node1.adjacent_list = [node2, node3]
    node2.adjacent_list = [node1]
    node3.adjacent_list = [node2]

    target = 3
    assert breadth_first_search_graph(node1, target) == node3

def test_bfs_graph_search_target_not_exists():
    node1 = Node(1)
    node2 = Node(2)

    node1.adjacent_list = [node2]
    target = 3
    assert breadth_first_search_graph(node1, target) is None