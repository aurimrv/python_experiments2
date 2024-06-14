import os
import sys
import pytest
from collections import deque

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from breadth_first_search import breadth_first_search, breadth_first_search_graph

# Test Cases for breadth_first_search(grid, start, target)
def test_bfs_grid_target_found():
    grid = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    start = (0, 0)
    target = 5
    assert breadth_first_search(grid, start, target) == (1, 1)

def test_bfs_grid_target_not_found():
    grid = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    start = (0, 0)
    target = 10
    assert breadth_first_search(grid, start, target) is None

# Test Cases for breadth_first_search_graph(head, target)
class Node:
    def __init__(self, val):
        self.val = val
        self.adjacent_list = []

def test_bfs_graph_target_found():
    node_a = Node(1)
    node_b = Node(2)
    node_c = Node(3)
    
    node_a.adjacent_list.append(node_b)
    node_b.adjacent_list.append(node_c)
    
    assert breadth_first_search_graph(node_a, 3) == node_c

def test_bfs_graph_target_not_found():
    node_a = Node(1)
    node_b = Node(2)
    node_c = Node(3)
    
    node_a.adjacent_list.append(node_b)
    
    assert breadth_first_search_graph(node_a, 4) is None