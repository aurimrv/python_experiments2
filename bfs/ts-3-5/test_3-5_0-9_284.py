import os
import sys
from collections import deque

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from breadth_first_search import breadth_first_search, breadth_first_search_graph

# Test cases for breadth_first_search method
def test_bfs_1():
    grid = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]
    start = (0, 0)
    target = 5
    assert breadth_first_search(grid, start, target) == (1, 1)

def test_bfs_2():
    grid = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]
    start = (2, 2)
    target = 9
    assert breadth_first_search(grid, start, target) == (2, 2)

# Test cases for breadth_first_search_graph method
class Node:
    def __init__(self, val):
        self.val = val
        self.adjacent_list = []

def test_bfs_graph_1():
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)

    node1.adjacent_list = [node2, node3]
    node2.adjacent_list = [node1, node4]
    node3.adjacent_list = [node1]
    node4.adjacent_list = [node2]

    assert breadth_first_search_graph(node1, 4) == node4

def test_bfs_graph_2():
    node1 = Node(1)
    node2 = Node(2)
    
    node1.adjacent_list = [node2]
    node2.adjacent_list = [node1]

    assert breadth_first_search_graph(node1, 3) == None