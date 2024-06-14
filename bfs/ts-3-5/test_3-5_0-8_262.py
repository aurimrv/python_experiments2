import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from breadth_first_search import breadth_first_search, breadth_first_search_graph

# Test cases for breadth_first_search function

def test_breadth_first_search_start_at_target():
    grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    start = (1, 1)  # Middle of the grid
    target = 5
    assert breadth_first_search(grid, start, target) == start

def test_breadth_first_search_no_target():
    grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    start = (0, 0)  # Top-left corner of the grid
    target = 10
    assert breadth_first_search(grid, start, target) is None

# Test cases for breadth_first_search_graph function

class Node:
    def __init__(self, val):
        self.val = val
        self.adjacent_list = []

def test_breadth_first_search_graph_target_found():
    node_a = Node(1)
    node_b = Node(2)
    node_c = Node(3)
    node_d = Node(4)

    node_a.adjacent_list = [node_b, node_c]
    node_b.adjacent_list = [node_a, node_d]
    node_c.adjacent_list = [node_a]

    target = 4
    assert breadth_first_search_graph(node_a, target) == node_d

def test_breadth_first_search_graph_target_not_found():
    node_a = Node(1)
    node_b = Node(2)
    node_c = Node(3)
    node_d = Node(4)

    node_a.adjacent_list = [node_b, node_c]
    node_b.adjacent_list = [node_a, node_d]
    node_c.adjacent_list = [node_a]

    target = 5
    assert breadth_first_search_graph(node_a, target) is None