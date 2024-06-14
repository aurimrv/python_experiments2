import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from fibonacci import fibonacci_dp, fibonacci_recursive

import pytest

def test_fibonacci_dp():
    # Test case for target = 0
    assert fibonacci_dp(0) == 0

    # Test case for target = 1
    assert fibonacci_dp(1) == 1

    # Test case for target = 5
    assert fibonacci_dp(5) == 5

    # Test case for target = 10
    assert fibonacci_dp(10) == 55

def test_fibonacci_recursive():
    # Test case for target = 0
    assert fibonacci_recursive(0) == 0

    # Test case for target = 1
    assert fibonacci_recursive(1) == 1

    # Test case for target = 5
    assert fibonacci_recursive(5) == 5

    # Test case for target = 10
    assert fibonacci_recursive(10) == 55

    # Test case for negative target
    assert fibonacci_recursive(-5) == 0