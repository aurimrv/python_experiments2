import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from fibonacci import fibonacci_dp, fibonacci_recursive

import pytest

@pytest.mark.parametrize("input, expected", [
    (0, 0),
    (1, 1),
    (2, 1),
    (3, 2),
    (4, 3),
    (5, 5),
    (6, 8),
    (7, 13),
    (8, 21),
    (9, 34)
])
def test_fibonacci_dp(input, expected):
    result = fibonacci_dp(input)
    assert result == expected

@pytest.mark.parametrize("input, expected", [
    (0, 0),
    (1, 1),
    (2, 1),
    (3, 2),
    (4, 3),
    (5, 5),
    (6, 8),
    (7, 13),
    (8, 21),
    (9, 34)
])
def test_fibonacci_recursive(input, expected):
    result = fibonacci_recursive(input)
    assert result == expected

@pytest.mark.parametrize("input, expected", [
    (10, 55),
    (15, 610),
    (20, 6765),
    (25, 75025)
])
def test_fibonacci_both(input, expected):
    result_dp = fibonacci_dp(input)
    result_rec = fibonacci_recursive(input)
    assert result_dp == expected
    assert result_rec == expected