import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from depth_first_search import depth_first_search

def test_depth_first_search_found():
    grid = [
        [0, 1, 0],
        [0, 0, 0],
        [0, 0, 2]
    ]
    start = (0, 0)
    target = 2
    assert depth_first_search(grid, start, target) == (2, 2)

def test_depth_first_search_not_found():
    grid = [
        [0, 1, 0],
        [0, 0, 0],
        [0, 0, 2]
    ]
    start = (0, 0)
    target = 3
    assert depth_first_search(grid, start, target) == None

def test_depth_first_search_edge_case_empty_grid():
    grid = []
    start = (0, 0)
    target = 1
    assert depth_first_search(grid, start, target) == None

def test_depth_first_search_edge_case_single_element_grid():
    grid = [[3]]
    start = (0, 0)
    target = 3
    assert depth_first_search(grid, start, target) == (0, 0)