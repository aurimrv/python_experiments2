import os
import sys
import pytest

# Append project directory to sys.path to import fibonacci.py correctly
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from fibonacci import fibonacci_dp, fibonacci_recursive

def test_fibonacci_dp():
    assert fibonacci_dp(0) == 0
    assert fibonacci_dp(1) == 1
    assert fibonacci_dp(2) == 1
    assert fibonacci_dp(3) == 2
    assert fibonacci_dp(4) == 3

def test_fibonacci_dp_negative_input():
    assert fibonacci_dp(-1) == 0

def test_fibonacci_recursive():
    assert fibonacci_recursive(0) == 0
    assert fibonacci_recursive(1) == 1
    assert fibonacci_recursive(2) == 1
    assert fibonacci_recursive(3) == 2
    assert fibonacci_recursive(4) == 3

def test_fibonacci_recursive_negative_input():
    assert fibonacci_recursive(-1) == 0