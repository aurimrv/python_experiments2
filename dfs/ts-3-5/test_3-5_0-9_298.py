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
    assert depth_first_search(grid, start, target) == None

def test_depth_first_search_target_not_found():
    grid = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    start = (0, 0)
    target = 1
    assert depth_first_search(grid, start, target) == None

def test_depth_first_search_target_found_at_start():
    grid = [
        [1, 0],
        [0, 0]
    ]
    start = (0, 0)
    target = 1
    assert depth_first_search(grid, start, target) == (0, 0)

def test_depth_first_search_target_found_in_grid():
    grid = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]
    start = (0, 0)
    target = 1
    assert depth_first_search(grid, start, target) == (1, 1)

def test_depth_first_search_target_not_found_in_grid():
    grid = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]
    start = (0, 0)
    target = 1
    assert depth_first_search(grid, start, target) == None

def test_depth_first_search_target_on_edge():
    grid = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 1]
    ]
    start = (0, 0)
    target = 1
    assert depth_first_search(grid, start, target) == (2, 2)