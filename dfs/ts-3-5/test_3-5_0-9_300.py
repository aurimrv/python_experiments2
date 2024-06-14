import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from depth_first_search import depth_first_search

def test_depth_first_search():
    grid = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8]
    ]
    start = (0, 0)
    target = 4
    assert depth_first_search(grid, start, target) == (1, 1)

    grid = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8]
    ]
    start = (2, 0)
    target = 8
    assert depth_first_search(grid, start, target) == (2, 2)

    grid = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8]
    ]
    start = (1, 2)
    target = 0
    assert depth_first_search(grid, start, target) == (0, 0)
    
    grid = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8]
    ]
    start = (2, 2)
    target = 9
    assert depth_first_search(grid, start, target) == None