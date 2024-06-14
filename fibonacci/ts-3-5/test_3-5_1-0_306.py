import os
import sys

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from fibonacci import fibonacci_dp, fibonacci_recursive

import pytest

# Test cases for fibonacci_dp function
def test_fibonacci_dp_with_positive_input():
    assert fibonacci_dp(0) == 0
    assert fibonacci_dp(1) == 1
    assert fibonacci_dp(2) == 1
    assert fibonacci_dp(3) == 2
    assert fibonacci_dp(4) == 3

def test_fibonacci_dp_with_negative_input():
    assert fibonacci_dp(-1) == 0
    assert fibonacci_dp(-5) == 0

def test_fibonacci_dp_with_large_input():
    assert fibonacci_dp(10) == 55
    assert fibonacci_dp(15) == 610
    assert fibonacci_dp(20) == 6765

# Test cases for fibonacci_recursive function
def test_fibonacci_recursive_with_positive_input():
    assert fibonacci_recursive(0) == 0
    assert fibonacci_recursive(1) == 1
    assert fibonacci_recursive(2) == 1
    assert fibonacci_recursive(3) == 2
    assert fibonacci_recursive(4) == 3

def test_fibonacci_recursive_with_negative_input():
    assert fibonacci_recursive(-1) == 0
    assert fibonacci_recursive(-5) == 0

def test_fibonacci_recursive_with_large_input():
    assert fibonacci_recursive(10) == 55
    assert fibonacci_recursive(15) == 610
    assert fibonacci_recursive(20) == 6765