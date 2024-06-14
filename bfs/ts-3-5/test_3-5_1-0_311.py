import os
import sys

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from breadth_first_search import breadth_first_search, breadth_first_search_graph

def test_bfs_search_2d_grid():
    grid = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8]
    ]
    assert breadth_first_search(grid, (0, 0), 8) == (2, 2)
    assert breadth_first_search(grid, (1, 1), 5) == (2, 1)

def test_bfs_search_2d_grid_not_found():
    grid = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8]
    ]
    assert breadth_first_search(grid, (0, 0), 9) is None
    assert breadth_first_search(grid, (1, 1), 10) is None

def test_bfs_search_graph():
    class Node:
        def __init__(self, val):
            self.val = val
            self.adjacent_list = []
    
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    
    node1.adjacent_list = [node2, node3]
    node2.adjacent_list = [node1]
    
    assert breadth_first_search_graph(node1, 3) == node3
    assert breadth_first_search_graph(node1, 2) == node2

def test_bfs_search_graph_not_found():
    class Node:
        def __init__(self, val):
            self.val = val
            self.adjacent_list = []
    
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    
    node1.adjacent_list = [node2, node3]
    node2.adjacent_list = [node1]
    
    assert breadth_first_search_graph(node1, 4) is None
    assert breadth_first_search_graph(node1, 5) is None
