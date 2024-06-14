import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from depth_first_search import depth_first_search

def test_depth_first_search_start_at_target():
    grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    start = (1, 1)
    target = 5
    assert depth_first_search(grid, start, target) == (1, 1)

def test_depth_first_search_target_not_found():
    grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    start = (0, 0)
    target = 10
    assert depth_first_search(grid, start, target) is None

def test_depth_first_search_edge_case_empty_grid():
    grid = []
    start = (0, 0)
    target = 1
    assert depth_first_search(grid, start, target) is None

def test_depth_first_search_edge_case_single_element_grid():
    grid = [[1]]
    start = (0, 0)
    target = 1
    assert depth_first_search(grid, start, target) == (0, 0)

def test_depth_first_search_edge_case_large_grid():
    grid = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    start = (0, 0)
    target = 11
    assert depth_first_search(grid, start, target) == (2, 2)