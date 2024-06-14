import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from breadth_first_search import breadth_first_search, breadth_first_search_graph

def test_breadth_first_search():
    grid = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]

    start = (0, 0)
    target = 5
    assert breadth_first_search(grid, start, target) == (1, 1)

    start = (2, 2)
    target = 7
    assert breadth_first_search(grid, start, target) == (0, 2)

def test_breadth_first_search_graph():
    class Node:
        def __init__(self, val):
            self.val = val
            self.adjacent_list = []

        def add_adjacent(self, node):
            self.adjacent_list.append(node)

    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)

    node1.add_adjacent(node2)
    node1.add_adjacent(node3)
    node2.add_adjacent(node4)
    node3.add_adjacent(node5)

    head = node1
    target = 5
    assert breadth_first_search_graph(head, target) == node5

    target = 4
    assert breadth_first_search_graph(head, target) == node4