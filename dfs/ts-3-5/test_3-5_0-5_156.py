import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from depth_first_search import depth_first_search

def test_depth_first_search():
    # Test case 1: Target found at start position
    grid = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]
    start = (0, 0)
    target = 1
    assert depth_first_search(grid, start, target) == (0, 0)

    # Test case 2: Target found at a different position
    grid = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]
    start = (1, 1)
    target = 5
    assert depth_first_search(grid, start, target) == (1, 1)

    # Test case 3: Target not found in the grid
    grid = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]
    start = (2, 2)
    target = 10
    assert depth_first_search(grid, start, target) is None

    # Test case 4: Target found at the edge of the grid
    grid = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]
    start = (2, 1)
    target = 6
    assert depth_first_search(grid, start, target) == (2, 1)

    # Test case 5: Target found diagonally
    grid = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]
    start = (0, 0)
    target = 5
    assert depth_first_search(grid, start, target) == (1, 1)