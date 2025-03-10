import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from collections import deque
from breadth_first_search import breadth_first_search, breadth_first_search_graph

def test_breadth_first_search_2d_grid_found():
    grid = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    start = (0, 0)
    target = 5
    assert breadth_first_search(grid, start, target) == (1, 1)

def test_breadth_first_search_2d_grid_not_found():
    grid = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    start = (0, 0)
    target = 10
    assert breadth_first_search(grid, start, target) == None

def test_breadth_first_search_graph_found():
    class Node:
        def __init__(self, val):
            self.val = val
            self.adjacent_list = []

    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node1.adjacent_list = [node2, node3]

    assert breadth_first_search_graph(node1, 3) == node3

def test_breadth_first_search_graph_not_found():
    class Node:
        def __init__(self, val):
            self.val = val
            self.adjacent_list = []

    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node1.adjacent_list = [node2]

    assert breadth_first_search_graph(node1, 4) == None