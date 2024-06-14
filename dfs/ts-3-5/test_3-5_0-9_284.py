import os
import sys

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from depth_first_search import depth_first_search

def test_start_target_same():
    grid = [[1, 2], [3, 4]]
    start = (0, 0)
    target = 1
    assert depth_first_search(grid, start, target) == start

def test_target_not_found():
    grid = [[1, 2], [3, 4]]
    start = (0, 0)
    target = 5
    assert depth_first_search(grid, start, target) is None

def test_target_found_in_path():
    grid = [[1, 2], [3, 4]]
    start = (0, 0)
    target = 4
    assert depth_first_search(grid, start, target) == (1, 1)

def test_large_grid():
    grid = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    start = (0, 0)
    target = 9
    assert depth_first_search(grid, start, target) == (2, 2)

def test_empty_grid():
    grid = []
    start = (0, 0)
    target = 1
    assert depth_first_search(grid, start, target) is None

def test_target_found_at_edge():
    grid = [[1, 2, 3], [4, 5, 6]]
    start = (0, 0)
    target = 6
    assert depth_first_search(grid, start, target) == (2, 1)