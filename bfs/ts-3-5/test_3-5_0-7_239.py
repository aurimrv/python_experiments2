import os
import sys
from collections import deque

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from breadth_first_search import breadth_first_search, breadth_first_search_graph


def test_bfs_grid():
    grid = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    start = (0, 0)
    target = 5
    assert breadth_first_search(grid, start, target) == (1, 1)

    start = (2, 2)
    target = 9
    assert breadth_first_search(grid, start, target) == (2, 2)


def test_bfs_grid_not_found():
    grid = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    start = (0, 0)
    target = 10
    assert breadth_first_search(grid, start, target) is None


def test_bfs_graph():
    class Node:
        def __init__(self, val):
            self.val = val
            self.adjacent_list = []

    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)

    node1.adjacent_list = [node2, node3]
    node2.adjacent_list = [node3]

    head = node1
    target = 3
    assert breadth_first_search_graph(head, target) == node3

    target = 2
    assert breadth_first_search_graph(head, target) == node2


def test_bfs_graph_not_found():
    class Node:
        def __init__(self, val):
            self.val = val
            self.adjacent_list = []

    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)

    node1.adjacent_list = [node2, node3]
    node2.adjacent_list = [node3]

    head = node1
    target = 4
    assert breadth_first_search_graph(head, target) is None