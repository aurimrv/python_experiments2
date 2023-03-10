import pytest
from depth_first_search import depth_first_search


class TestDFS:
    def make_simple_grid(self):
        return [
            [1, 0, 3, 4],
            [5, 6, 2, 6],
            [8, 8, 1, 3],
        ]

    def make_complex_grid(self):
        return [
            [1, 0, 3, 4, 7, 12, 4, 111],
            [5, 6, 2, 6, 0, 1, 54, 3],
            [8, 8, 1, 3, 2, 6, 8, 22],
            [8, 8, 1, 3, 4, 0, 77, 1],
            [8, 8, 1, 3, -1, 4, 2, 9],
        ]

    def test_dfs_basic(self):
        assert depth_first_search(self.make_simple_grid(), (3, 0), 8) == (1, 2)

    def test_find_farther_first(self):
        assert depth_first_search(self.make_simple_grid(), (0, 2), 3) == (3, 2)

    def test_dfs_complex(self):
        assert depth_first_search(self.make_complex_grid(), (7, 4), 111) == (7, 0)
        assert depth_first_search(self.make_complex_grid(), (0, 4), 8) == (0, 4)

    def test_dfs_empty(self):
        assert depth_first_search([], (0, 1), 0) is None

    def test_dfs_not_found(self):
        assert depth_first_search(self.make_simple_grid(), (0, 0), -1) is None

