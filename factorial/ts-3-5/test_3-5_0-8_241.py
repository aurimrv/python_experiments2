import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from factorial import factorial

import pytest

@pytest.mark.parametrize("n, expected", [
    (0, 0),
    (1, 1),
    (5, 120),
    (10, 3628800)
])
def test_factorial_valid_input(n, expected):
    assert factorial(n) == expected

def test_factorial_negative_input():
    assert factorial(-5) == 0

def test_factorial_large_input():
    assert factorial(20) == 2432902008176640000