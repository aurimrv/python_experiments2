import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from depth_first_search import depth_first_search

def test_depth_first_search_empty_grid():
    grid = []
    start = (0, 0)
    target = 1
    assert depth_first_search(grid, start, target) is None

def test_depth_first_search_target_at_start():
    grid = [[5, 3, 2], [4, 1, 6], [7, 8, 9]]
    start = (1, 1)
    target = 1
    assert depth_first_search(grid, start, target) == start

def test_depth_first_search_no_target_found():
    grid = [[5, 3, 2], [4, 1, 6], [7, 8, 9]]
    start = (0, 0)
    target = 10
    assert depth_first_search(grid, start, target) is None

def test_depth_first_search_target_in_grid():
    grid = [[5, 3, 2], [4, 1, 6], [7, 8, 9]]
    start = (1, 1)
    target = 6
    assert depth_first_search(grid, start, target) == (2, 1)

def test_depth_first_search_target_not_in_grid():
    grid = [[5, 3, 2], [4, 1, 6], [7, 8, 9]]
    start = (1, 1)
    target = 10
    assert depth_first_search(grid, start, target) is None