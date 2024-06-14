import os
import sys
from collections import deque

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from breadth_first_search import breadth_first_search, breadth_first_search_graph

def test_breadth_first_search_empty_grid():
    grid = []
    start = (0, 0)
    target = 1
    assert breadth_first_search(grid, start, target) is None

def test_breadth_first_search_found_target():
    grid = [[0, 1],
            [2, 3]]
    start = (0, 0)
    target = 1
    assert breadth_first_search(grid, start, target) == (1, 0)

def test_breadth_first_search_not_found():
    grid = [[0, 1],
            [2, 3]]
    start = (0, 0)
    target = 5
    assert breadth_first_search(grid, start, target) is None

def test_breadth_first_search_graph_found_target():
    class Node:
        def __init__(self, val):
            self.val = val
            self.adjacent_list = []

    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)

    node1.adjacent_list = [node2, node3]

    head = node1
    target = 3

    assert breadth_first_search_graph(head, target) == node3

def test_breadth_first_search_graph_not_found():
    class Node:
        def __init__(self, val):
            self.val = val
            self.adjacent_list = []

    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)

    node1.adjacent_list = [node2, node3]

    head = node1
    target = 5

    assert breadth_first_search_graph(head, target) is None