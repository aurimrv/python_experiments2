import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from breadth_first_search import breadth_first_search, breadth_first_search_graph

# Tests for breadth_first_search function

def test_breadth_first_search_empty_grid():
    grid = []
    start = (0, 0)
    target = 5
    assert breadth_first_search(grid, start, target) == None

def test_breadth_first_search_target_at_start():
    grid = [[3, 4, 5], [6, 7, 8], [9, 10, 11]]
    start = (0, 0)
    target = 3
    assert breadth_first_search(grid, start, target) == (0, 0)

def test_breadth_first_search_target_in_grid():
    grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    start = (1, 0)
    target = 8
    assert breadth_first_search(grid, start, target) == (1, 2)

# Tests for breadth_first_search_graph function

class Node:
    def __init__(self, val):
        self.val = val
        self.adjacent_list = []

def test_breadth_first_search_graph_target_not_found():
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    
    node1.adjacent_list.append(node2)
    node2.adjacent_list.append(node3)
    
    target = 5
    assert breadth_first_search_graph(node1, target) == None

def test_breadth_first_search_graph_target_at_node():
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    
    node1.adjacent_list.append(node2)
    node2.adjacent_list.append(node3)
    
    target = 3
    assert breadth_first_search_graph(node1, target) == node3

def test_breadth_first_search_graph_multiple_paths_to_target():
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    
    node1.adjacent_list.append(node2)
    node1.adjacent_list.append(node3)
    node3.adjacent_list.append(node4)
    
    target = 4
    assert breadth_first_search_graph(node1, target) == node4