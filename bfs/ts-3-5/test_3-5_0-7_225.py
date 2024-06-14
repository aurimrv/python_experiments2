import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from breadth_first_search import breadth_first_search, breadth_first_search_graph

# Test cases for breadth_first_search(grid, start, target)
def test_bfs_grid_target_found():
    grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    start = (0, 0)
    target = 5
    assert breadth_first_search(grid, start, target) == (1, 1)

def test_bfs_grid_target_not_found():
    grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    start = (0, 0)
    target = 10
    assert breadth_first_search(grid, start, target) is None

# Test cases for breadth_first_search_graph(head, target)
class Node:
    def __init__(self, val):
        self.val = val
        self.adjacent_list = []

def test_bfs_graph_target_found():
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    
    node1.adjacent_list.append(node2)
    node2.adjacent_list.append(node3)
    
    assert breadth_first_search_graph(node1, 3) == node3

def test_bfs_graph_target_not_found():
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    
    node1.adjacent_list.append(node2)
    node2.adjacent_list.append(node3)
    
    assert breadth_first_search_graph(node1, 4) is None