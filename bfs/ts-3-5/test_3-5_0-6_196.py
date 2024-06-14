import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from collections import deque
from breadth_first_search import breadth_first_search, breadth_first_search_graph

# Test cases for breadth_first_search function

def test_bfs_empty_grid():
    grid = []
    start = (0, 0)
    target = 1
    assert breadth_first_search(grid, start, target) == None

def test_bfs_target_at_start():
    grid = [[1, 0], [0, 0]]
    start = (0, 0)
    target = 1
    assert breadth_first_search(grid, start, target) == (0, 0)

def test_bfs_target_not_found():
    grid = [[1, 0], [0, 0]]
    start = (0, 0)
    target = 2
    assert breadth_first_search(grid, start, target) == None

# Test cases for breadth_first_search_graph function

class Node:
    def __init__(self, val):
        self.val = val
        self.adjacent_list = []

def test_bfs_graph_target_found():
    head = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    head.adjacent_list = [node2, node3]
    target = 3
    assert breadth_first_search_graph(head, target) == node3

def test_bfs_graph_target_not_found():
    head = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    head.adjacent_list = [node2, node3]
    target = 4
    assert breadth_first_search_graph(head, target) == None