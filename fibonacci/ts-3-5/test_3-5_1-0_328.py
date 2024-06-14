import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from fibonacci import fibonacci_dp, fibonacci_recursive

# Test cases for fibonacci_dp function
def test_fibonacci_dp_zero_input():
    assert fibonacci_dp(0) == 0

def test_fibonacci_dp_first_fibonacci_number():
    assert fibonacci_dp(1) == 1

def test_fibonacci_dp_next_fibonacci_number():
    assert fibonacci_dp(6) == 8

def test_fibonacci_dp_large_input():
    assert fibonacci_dp(10) == 55


# Test cases for fibonacci_recursive function
def test_fibonacci_recursive_zero_input():
    assert fibonacci_recursive(0) == 0

def test_fibonacci_recursive_first_fibonacci_number():
    assert fibonacci_recursive(1) == 1

def test_fibonacci_recursive_next_fibonacci_number():
    assert fibonacci_recursive(6) == 8

def test_fibonacci_recursive_large_input():
    assert fibonacci_recursive(10) == 55