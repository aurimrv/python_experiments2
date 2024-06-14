import os
import sys
import pytest

# Add the project directory to the sys.path
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from breadth_first_search import breadth_first_search, breadth_first_search_graph

# Test cases for breadth_first_search function
def test_breadth_first_search_empty_grid():
    grid = []
    start = (0, 0)
    target = 1
    assert breadth_first_search(grid, start, target) == None

def test_breadth_first_search_target_found():
    grid = [[0, 1], [2, 3]]
    start = (0, 0)
    target = 1
    assert breadth_first_search(grid, start, target) == (1, 0)

def test_breadth_first_search_target_not_found():
    grid = [[0, 1], [2, 3]]
    start = (0, 0)
    target = 5
    assert breadth_first_search(grid, start, target) == None

# Test cases for breadth_first_search_graph function
class Node:
    def __init__(self, val):
        self.val = val
        self.adjacent_list = []
    
    def add_adjacent(self, node):
        self.adjacent_list.append(node)

def test_breadth_first_search_graph_target_found():
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    
    node1.add_adjacent(node2)
    node2.add_adjacent(node3)
    
    target = 3
    assert breadth_first_search_graph(node1, target) == node3

def test_breadth_first_search_graph_target_not_found():
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    
    node1.add_adjacent(node2)
    node2.add_adjacent(node3)
    
    target = 4
    assert breadth_first_search_graph(node1, target) == None