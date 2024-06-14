import os
import sys
from collections import deque

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from breadth_first_search import breadth_first_search, breadth_first_search_graph

# Test cases for breadth_first_search

def test_breadth_first_search_empty_grid():
    grid = []
    start = (0, 0)
    target = 1
    assert breadth_first_search(grid, start, target) is None

def test_breadth_first_search_target_at_start():
    grid = [[1, 2], [3, 4]]
    start = (0, 0)
    target = 1
    assert breadth_first_search(grid, start, target) == (0, 0)

def test_breadth_first_search_target_not_found():
    grid = [[1, 2], [3, 4]]
    start = (0, 0)
    target = 5
    assert breadth_first_search(grid, start, target) is None

# Test cases for breadth_first_search_graph

class Node:
    def __init__(self, val, adjacent_list):
        self.val = val
        self.adjacent_list = adjacent_list

def test_breadth_first_search_graph_target_not_found():
    node1 = Node(1, [])
    node2 = Node(2, [])
    node3 = Node(3, [])
    node4 = Node(4, [])
    
    node1.adjacent_list = [node2, node3]
    node2.adjacent_list = [node1, node4]
    node3.adjacent_list = [node1, node4]
    node4.adjacent_list = [node2, node3]

    head = node1
    target = 5
    assert breadth_first_search_graph(head, target) is None

def test_breadth_first_search_graph_target_found():
    node1 = Node(1, [])
    node2 = Node(2, [])
    node3 = Node(3, [])
    node4 = Node(4, [])
    
    node1.adjacent_list = [node2, node3]
    node2.adjacent_list = [node1, node4]
    node3.adjacent_list = [node1, node4]
    node4.adjacent_list = [node2, node3]

    head = node1
    target = 4
    assert breadth_first_search_graph(head, target) == node4