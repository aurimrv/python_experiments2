import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from depth_first_search import depth_first_search

def test_depth_first_search_found():
    # Test case for finding target in a simple 3x3 grid
    grid = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8]
    ]
    start = (1, 1)
    target = 4
    assert depth_first_search(grid, start, target) == (1, 1)

def test_depth_first_search_not_found():
    # Test case for target not found in a 3x3 grid
    grid = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8]
    ]
    start = (0, 0)
    target = 9
    assert depth_first_search(grid, start, target) == None

def test_depth_first_search_corner_case():
    # Test case for target at the edge of a 2x2 grid
    grid = [
        [1, 2],
        [3, 4]
    ]
    start = (1, 1)
    target = 4
    assert depth_first_search(grid, start, target) == (1, 1)

def test_depth_first_search_empty_grid():
    # Test case for an empty grid, should return None
    grid = []
    start = (0, 0)
    target = 1
    assert depth_first_search(grid, start, target) == None

def test_depth_first_search_target_at_start():
    # Test case for target value already at the starting position
    grid = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8]
    ]
    start = (2, 1)
    target = 5
    assert depth_first_search(grid, start, target) == (2, 1)

def test_depth_first_search_target_not_in_grid():
    # Test case for target value not present in the grid
    grid = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8]
    ]
    start = (0, 0)
    target = 9
    assert depth_first_search(grid, start, target) == None