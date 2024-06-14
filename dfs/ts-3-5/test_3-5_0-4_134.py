import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from depth_first_search import depth_first_search

def test_depth_first_search():
    # Test case for finding target in a simple 2x2 grid
    grid = [[1, 2], [3, 4]]
    start = (0, 0)
    target = 3
    assert depth_first_search(grid, start, target) == (0, 1)

    # Test case for target not found in a 3x3 grid
    grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    start = (2, 2)
    target = 10
    assert depth_first_search(grid, start, target) is None

    # Test case for target at the start position
    grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    start = (1, 1)
    target = 5
    assert depth_first_search(grid, start, target) == (1, 1)

    # Test case for target at the edge of the grid
    grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    start = (2, 1)
    target = 6
    assert depth_first_search(grid, start, target) == (2, 1)

    # Test case for target not present in a grid with negative numbers
    grid = [[-1, -2, -3], [-4, -5, -6], [-7, -8, -9]]
    start = (0, 0)
    target = 0
    assert depth_first_search(grid, start, target) is None