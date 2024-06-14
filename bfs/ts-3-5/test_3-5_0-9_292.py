import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from breadth_first_search import breadth_first_search, breadth_first_search_graph

# Test Cases for breadth_first_search

def test_bfs_search_returns_start_if_target_is_start():
    grid = [[1, 2], [3, 4]]
    start = (0, 0)
    target = 1
    assert breadth_first_search(grid, start, target) == start

def test_bfs_search_returns_correct_coordinates():
    grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    start = (0, 0)
    target = 5
    assert breadth_first_search(grid, start, target) == (1, 1)

# Test Cases for breadth_first_search_graph

class Node:
    def __init__(self, val, adjacent_list=[]):
        self.val = val
        self.adjacent_list = adjacent_list

def test_bfs_graph_search_returns_none_if_target_not_found():
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3, [node1, node2])

    assert breadth_first_search_graph(node3, 4) == None

def test_bfs_graph_search_returns_correct_node():
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3, [node1, node2])

    assert breadth_first_search_graph(node3, 2) == node2