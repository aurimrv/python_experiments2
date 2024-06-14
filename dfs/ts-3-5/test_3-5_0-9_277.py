import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from depth_first_search import depth_first_search

def test_empty_grid():
    grid = []
    start = (0, 0)
    target = 1
    assert depth_first_search(grid, start, target) is None

def test_starting_at_target():
    grid = [[1, 2], [3, 4]]
    start = (0, 0)
    target = 1
    assert depth_first_search(grid, start, target) == (0, 0)

def test_target_not_in_grid():
    grid = [[1, 2], [3, 4]]
    start = (1, 1)
    target = 5
    assert depth_first_search(grid, start, target) is None

def test_basic_search():
    grid = [[1, 2], [3, 4]]
    start = (0, 0)
    target = 2
    assert depth_first_search(grid, start, target) == (1, 0)

def test_out_of_bounds_search():
    grid = [[1, 2], [3, 4]]
    start = (1, 0)
    target = 3
    assert depth_first_search(grid, start, target) == (0, 1)

def test_search_in_larger_grid():
    grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    start = (2, 1)
    target = 8
    assert depth_first_search(grid, start, target) == (1, 2)