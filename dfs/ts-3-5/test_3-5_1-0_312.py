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
    start = (0, 0) # Value at this coordinate: 1
    target = 5
    assert depth_first_search(grid, start, target) == (1, 1)

def test_depth_first_search_not_found():
    grid = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    start = (0, 0) # Value at this coordinate: 1
    target = 10 # Value not in the grid
    assert depth_first_search(grid, start, target) == None

def test_depth_first_search_target_at_start():
    grid = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    start = (1, 1) # Value at this coordinate: 5
    target = 5
    assert depth_first_search(grid, start, target) == (1, 1)

def test_depth_first_search_target_in_corner():
    grid = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    start = (0, 0) # Value at this coordinate: 1
    target = 9
    assert depth_first_search(grid, start, target) == (2, 2)