import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from breadth_first_search import breadth_first_search, breadth_first_search_graph

def test_breadth_first_search_grid():
    grid = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    assert breadth_first_search(grid, (0, 0), 5) == (1, 1)
    assert breadth_first_search(grid, (2, 2), 7) == (0, 2)
    assert breadth_first_search(grid, (1, 1), 10) is None

def test_breadth_first_search_graph():
    class Node:
        def __init__(self, val, adjacent_list):
            self.val = val
            self.adjacent_list = adjacent_list

    node1 = Node(1, [])
    node2 = Node(2, [])
    node3 = Node(3, [node1, node2])
    node4 = Node(4, [node3])

    assert breadth_first_search_graph(node4, 1) == node1
    assert breadth_first_search_graph(node4, 2) == node2
    assert breadth_first_search_graph(node4, 5) is None