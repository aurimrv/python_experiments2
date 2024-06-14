import os
import sys
from collections import deque

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from breadth_first_search import breadth_first_search, breadth_first_search_graph

def test_breadth_first_search_grid():
    # Test for finding target in a grid
    grid = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]
    start = (1, 1)  # Start in the middle
    target = 5  # Target value to find
    assert breadth_first_search(grid, start, target) == (1, 1)

    # Test for target not found in grid
    assert breadth_first_search(grid, start, 99) is None

def test_breadth_first_search_graph():
    class Node:
        def __init__(self, val):
            self.val = val
            self.adjacent_list = []

    # Create a simple graph for testing
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    
    node1.adjacent_list = [node2, node3]
    node2.adjacent_list = [node4]
    node3.adjacent_list = [node4]
    
    # Test for finding target in the graph
    head = node1
    target = 4
    assert breadth_first_search_graph(head, target) == node4

    # Test for target not found in the graph
    target = 99
    assert breadth_first_search_graph(head, target) is None