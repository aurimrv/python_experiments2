# test_fibonacci.py

import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from fibonacci import fibonacci_dp, fibonacci_recursive

import pytest

def test_fibonacci_dp():
    # Test cases for fibonacci_dp function
    assert fibonacci_dp(0) == 0
    assert fibonacci_dp(1) == 1
    assert fibonacci_dp(2) == 1
    assert fibonacci_dp(5) == 5
    assert fibonacci_dp(10) == 55

def test_fibonacci_recursive():
    # Test cases for fibonacci_recursive function
    assert fibonacci_recursive(0) == 0
    assert fibonacci_recursive(1) == 1
    assert fibonacci_recursive(2) == 1
    assert fibonacci_recursive(5) == 5
    assert fibonacci_recursive(10) == 55