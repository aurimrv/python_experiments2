import os
import sys
from collections import deque

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from breadth_first_search import breadth_first_search, breadth_first_search_graph

def test_breadth_first_search_grid():
    grid = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    assert breadth_first_search(grid, (0, 0), 5) == (1, 1)
    assert breadth_first_search(grid, (2, 2), 1) == (0, 0)
    assert breadth_first_search(grid, (1, 1), 9) == (2, 2)

def test_breadth_first_search_grid_no_target():
    grid = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    assert breadth_first_search(grid, (0, 0), 10) is None
    assert breadth_first_search(grid, (2, 2), 0) is None

def test_breadth_first_search_graph():
    class Node:
        def __init__(self, val):
            self.val = val
            self.adjacent_list = []

    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)

    node1.adjacent_list.append(node2)
    node1.adjacent_list.append(node3)
    node2.adjacent_list.append(node4)

    assert breadth_first_search_graph(node1, 4) == node4
    assert breadth_first_search_graph(node1, 3) == node3
    assert breadth_first_search_graph(node1, 5) is None

def test_breadth_first_search_graph_no_target():
    class Node:
        def __init__(self, val):
            self.val = val
            self.adjacent_list = []

    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)

    node1.adjacent_list.append(node2)
    node1.adjacent_list.append(node3)
    node2.adjacent_list.append(node4)

    assert breadth_first_search_graph(node1, 5) is None
    assert breadth_first_search_graph(node1, 0) is None