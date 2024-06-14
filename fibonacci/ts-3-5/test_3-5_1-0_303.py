import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from fibonacci import fibonacci_dp, fibonacci_recursive

import pytest

# Test cases for fibonacci_dp

def test_fibonacci_dp_with_zero_input():
    result = fibonacci_dp(0)
    assert result == 0

def test_fibonacci_dp_with_positive_input():
    result = fibonacci_dp(5)
    assert result == 5

def test_fibonacci_dp_with_large_input():
    result = fibonacci_dp(10)
    assert result == 55

# Test cases for fibonacci_recursive

def test_fibonacci_recursive_with_zero_input():
    result = fibonacci_recursive(0)
    assert result == 0

def test_fibonacci_recursive_with_positive_input():
    result = fibonacci_recursive(5)
    assert result == 5

def test_fibonacci_recursive_with_large_input():
    result = fibonacci_recursive(10)
    assert result == 55