import pytest
from breadth_first_search import breadth_first_search

def make_simple_grid():
    return [
        [1,0,3,4],
        [5,6,2,6],
        [8,8,1,3],
    ]

def make_complex_grid():
    return [
        [1,0,3,4,7,12,4,111],
        [5,6,2,6,0,1,54,3],
        [8,8,1,3,2,6,8,22],
        [8,8,1,3,4,0,77,1],
        [8,8,1,3,-1,4,2,9],
    ]

def test_bfs_basic():
    assert (1,2) == breadth_first_search(make_simple_grid(), (3, 0), 8)
    assert (3,2) == breadth_first_search(make_simple_grid(), (0, 2), 3)
    assert (2,0) == breadth_first_search(make_simple_grid(), (0, 0), 3)

def test_bfs_complex():
    assert (7,0) == breadth_first_search(make_complex_grid(), (7, 4), 111)
    assert (0,4) == breadth_first_search(make_complex_grid(), (0, 4), 8)

def test_bfs_empty():
    assert None == breadth_first_search([], (0,1), 0)

def test_bfs_not_found():
    assert None == breadth_first_search(make_simple_grid(), (0,0), -1)

