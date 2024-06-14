import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from depth_first_search import depth_first_search

@pytest.fixture
def grid():
    return [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

def test_depth_first_search_target_at_start(grid):
    start = (0, 0)
    target = 1
    assert depth_first_search(grid, start, target) == start

def test_depth_first_search_target_at_end(grid):
    start = (2, 2)
    target = 9
    assert depth_first_search(grid, start, target) == start

def test_depth_first_search_target_not_in_grid(grid):
    start = (1, 1)
    target = 10
    assert depth_first_search(grid, start, target) is None

def test_depth_first_search_empty_grid():
    grid = []
    start = (0, 0)
    target = 1
    assert depth_first_search(grid, start, target) is None

def test_depth_first_search_large_grid():
    grid = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]
    start = (0, 0)
    target = 15
    assert depth_first_search(grid, start, target) == (2, 3)