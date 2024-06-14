import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from breadth_first_search import breadth_first_search, breadth_first_search_graph

# Test cases for breadth_first_search function

def test_breadth_first_search_grid_found():
    grid = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8]
    ]
    start = (1, 1)
    target = 4
    assert breadth_first_search(grid, start, target) == (1, 1)

def test_breadth_first_search_grid_not_found():
    grid = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8]
    ]
    start = (0, 0)
    target = 9
    assert breadth_first_search(grid, start, target) == None

# Test cases for breadth_first_search_graph function

class Node:
    def __init__(self, val):
        self.val = val
        self.adjacent_list = []

def test_breadth_first_search_graph_found():
    node_a = Node('A')
    node_b = Node('B')
    node_c = Node('C')

    node_a.adjacent_list.append(node_b)
    node_b.adjacent_list.append(node_c)

    head = node_a
    target = 'C'

    assert breadth_first_search_graph(head, target) == node_c

def test_breadth_first_search_graph_not_found():
    node_a = Node('A')
    node_b = Node('B')
    node_c = Node('C')

    node_a.adjacent_list.append(node_b)

    head = node_a
    target = 'D'

    assert breadth_first_search_graph(head, target) == None