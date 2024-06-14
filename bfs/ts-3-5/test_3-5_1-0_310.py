import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from breadth_first_search import breadth_first_search, breadth_first_search_graph

# breadth_first_search tests
def test_bfs_grid_found():
    grid = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8]
    ]
    start = (0, 0)
    target = 5
    assert breadth_first_search(grid, start, target) == (2, 1)

def test_bfs_grid_not_found():
    grid = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8]
    ]
    start = (2, 2)
    target = 10
    assert breadth_first_search(grid, start, target) is None

# breadth_first_search_graph tests
class Node:
    def __init__(self, val):
        self.val = val
        self.adjacent_list = []

def test_bfs_graph_found():
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)

    node1.adjacent_list = [node2, node3]
    node2.adjacent_list = [node1, node4]
    node3.adjacent_list = [node1]
    node4.adjacent_list = [node2]

    head = node1
    target = 4

    assert breadth_first_search_graph(head, target) == node4

def test_bfs_graph_not_found():
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)

    node1.adjacent_list = [node2, node3]
    node2.adjacent_list = [node1, node4]
    node3.adjacent_list = [node1]

    head = node1
    target = 5

    assert breadth_first_search_graph(head, target) is None