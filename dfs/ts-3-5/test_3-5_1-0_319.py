import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

import depth_first_search

def test_depth_first_search():
    grid = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    start = (0, 0)
    target = 5
    assert depth_first_search.depth_first_search(grid, start, target) == (1, 1)

def test_depth_first_search_target_not_found():
    grid = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    start = (0, 0)
    target = 10
    assert depth_first_search.depth_first_search(grid, start, target) == None

def test_depth_first_search_start_at_target():
    grid = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    start = (1, 1)
    target = 5
    assert depth_first_search.depth_first_search(grid, start, target) == (1, 1)

def test_depth_first_search_empty_grid():
    grid = []
    start = (0, 0)
    target = 2
    assert depth_first_search.depth_first_search(grid, start, target) == None

def test_depth_first_search_edge_case():
    grid = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    start = (2, 2)
    target = 1
    assert depth_first_search.depth_first_search(grid, start, target) == (0, 0)