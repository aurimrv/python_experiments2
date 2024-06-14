import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from depth_first_search import depth_first_search

def test_depth_first_search_found():
    grid = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    start = (0, 0)
    target = 5
    assert depth_first_search(grid, start, target) == (1, 1)

def test_depth_first_search_not_found():
    grid = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    start = (0, 0)
    target = 10
    assert depth_first_search(grid, start, target) is None

def test_depth_first_search_edge_case():
    grid = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    start = (2, 2)
    target = 9
    assert depth_first_search(grid, start, target) == (2, 2)

def test_depth_first_search_empty_grid():
    grid = []
    start = (0, 0)
    target = 5
    assert depth_first_search(grid, start, target) is None

def test_depth_first_search_single_element_grid():
    grid = [[5]]
    start = (0, 0)
    target = 5
    assert depth_first_search(grid, start, target) == (0, 0)