import os
import sys
import pytest

# Add the project directory to the system path for correct imports
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from depth_first_search import depth_first_search

def test_depth_first_search_found():
    grid = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]
    start = (0, 0)
    target = 1
    assert depth_first_search(grid, start, target) == (1, 1)

def test_depth_first_search_not_found():
    grid = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    start = (2, 2)
    target = 1
    assert depth_first_search(grid, start, target) == None

def test_depth_first_search_start_target_same():
    grid = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]
    start = (1, 1)
    target = 1
    assert depth_first_search(grid, start, target) == (1, 1)

def test_depth_first_search_edge_case():
    grid = []
    start = (0, 0)
    target = 1
    assert depth_first_search(grid, start, target) == None

def test_depth_first_search_large_grid():
    grid = [
        [1, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]
    start = (0, 0)
    target = 1
    assert depth_first_search(grid, start, target) == (0, 0)