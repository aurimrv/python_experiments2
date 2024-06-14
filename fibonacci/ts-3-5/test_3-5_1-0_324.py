import os
import sys

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

import pytest
import fibonacci

def test_fibonacci_dp_negative_input():
    assert fibonacci.fibonacci_dp(-5) == 0

def test_fibonacci_dp_zero():
    assert fibonacci.fibonacci_dp(0) == 0

def test_fibonacci_dp_positive_input():
    assert fibonacci.fibonacci_dp(6) == 8

def test_fibonacci_recursive_negative_input():
    assert fibonacci.fibonacci_recursive(-3) == 0

def test_fibonacci_recursive_zero():
    assert fibonacci.fibonacci_recursive(0) == 0

def test_fibonacci_recursive_positive_input():
    assert fibonacci.fibonacci_recursive(5) == 5