import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from fibonacci import fibonacci_dp, fibonacci_recursive

import pytest

# Fibonacci Dynamic Programming tests
def test_fibonacci_dp_zero_input():
    assert fibonacci_dp(0) == 0

def test_fibonacci_dp_first_fibonacci():
    assert fibonacci_dp(1) == 1

def test_fibonacci_dp_sequence():
    assert fibonacci_dp(6) == 8

# Fibonacci Recursive tests
def test_fibonacci_recursive_zero_input():
    assert fibonacci_recursive(0) == 0

def test_fibonacci_recursive_first_fibonacci():
    assert fibonacci_recursive(1) == 1

def test_fibonacci_recursive_sequence():
    assert fibonacci_recursive(6) == 8