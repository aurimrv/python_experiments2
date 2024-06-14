import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

import fibonacci

import pytest

# Test cases for fibonacci_dp

def test_fibonacci_dp_with_target_0():
    assert fibonacci.fibonacci_dp(0) == 0

def test_fibonacci_dp_with_target_5():
    assert fibonacci.fibonacci_dp(5) == 5

def test_fibonacci_dp_with_target_negative():
    assert fibonacci.fibonacci_dp(-3) == 0

# Test cases for fibonacci_recursive

def test_fibonacci_recursive_with_target_0():
    assert fibonacci.fibonacci_recursive(0) == 0

def test_fibonacci_recursive_with_target_7():
    assert fibonacci.fibonacci_recursive(7) == 13

def test_fibonacci_recursive_with_target_negative():
    assert fibonacci.fibonacci_recursive(-2) == 0