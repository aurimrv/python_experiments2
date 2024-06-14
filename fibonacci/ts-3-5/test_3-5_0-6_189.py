import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

import fibonacci

import pytest

def test_fibonacci_dp():
    assert fibonacci.fibonacci_dp(0) == 0
    assert fibonacci.fibonacci_dp(1) == 1
    assert fibonacci.fibonacci_dp(2) == 1
    assert fibonacci.fibonacci_dp(3) == 2
    assert fibonacci.fibonacci_dp(5) == 5

def test_fibonacci_dp_negative_input():
    assert fibonacci.fibonacci_dp(-1) == 0
    assert fibonacci.fibonacci_dp(-5) == 0

def test_fibonacci_recursive():
    assert fibonacci.fibonacci_recursive(0) == 0
    assert fibonacci.fibonacci_recursive(1) == 1
    assert fibonacci.fibonacci_recursive(2) == 1
    assert fibonacci.fibonacci_recursive(3) == 2
    assert fibonacci.fibonacci_recursive(5) == 5

def test_fibonacci_recursive_negative_input():
    assert fibonacci.fibonacci_recursive(-1) == 0
    assert fibonacci.fibonacci_recursive(-5) == 0