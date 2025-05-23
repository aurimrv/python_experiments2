import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from breadth_first_search import breadth_first_search, breadth_first_search_graph

# Test cases for breadth_first_search function
def test_bfs_on_2d_grid():
    grid = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8]
    ]
    start = (1, 1)
    target = 5
    assert breadth_first_search(grid, start, target) == (2, 1)

def test_bfs_on_2d_grid_target_not_found():
    grid = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8]
    ]
    start = (0, 0)
    target = 9
    assert breadth_first_search(grid, start, target) is None

# Test cases for breadth_first_search_graph function
class Node:
    def __init__(self, val):
        self.val = val
        self.adjacent_list = []

def test_bfs_graph_node_found():
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    
    node1.adjacent_list = [node2, node3]
    node2.adjacent_list = [node1]
    
    assert breadth_first_search_graph(node1, 3) == node3

def test_bfs_graph_node_not_found():
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    
    node1.adjacent_list = [node2]
    node2.adjacent_list = []
    
    assert breadth_first_search_graph(node1, 3) is None