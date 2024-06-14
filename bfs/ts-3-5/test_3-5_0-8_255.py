import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from breadth_first_search import breadth_first_search, breadth_first_search_graph

def test_breadth_first_search():
    grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    start = (0, 0)
    target = 5
    assert breadth_first_search(grid, start, target) == (1, 1)

    grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    start = (2, 0)
    target = 7
    assert breadth_first_search(grid, start, target) == (0, 2)

def test_breadth_first_search_graph():
    class Node:
        def __init__(self, val):
            self.val = val
            self.adjacent_list = []

    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)

    node1.adjacent_list = [node2, node3]
    node2.adjacent_list = [node1, node4]
    node3.adjacent_list = [node1]
    node4.adjacent_list = [node2]

    target = 4
    assert breadth_first_search_graph(node1, target) == node4

    target = 3
    assert breadth_first_search_graph(node1, target) == node3