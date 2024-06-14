import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from fibonacci import fibonacci_dp, fibonacci_recursive

# Test cases for fibonacci_dp

def test_fibonacci_dp_negative_input():
    assert fibonacci_dp(-1) == 0

def test_fibonacci_dp_zero_input():
    assert fibonacci_dp(0) == 0

def test_fibonacci_dp_first_fibonacci():
    assert fibonacci_dp(1) == 1

def test_fibonacci_dp_fifth_fibonacci():
    assert fibonacci_dp(5) == 5

def test_fibonacci_dp_tenth_fibonacci():
    assert fibonacci_dp(10) == 55

# Test cases for fibonacci_recursive

def test_fibonacci_recursive_negative_input():
    assert fibonacci_recursive(-1) == 0

def test_fibonacci_recursive_zero_input():
    assert fibonacci_recursive(0) == 0

def test_fibonacci_recursive_first_fibonacci():
    assert fibonacci_recursive(1) == 1

def test_fibonacci_recursive_fifth_fibonacci():
    assert fibonacci_recursive(5) == 5

def test_fibonacci_recursive_tenth_fibonacci():
    assert fibonacci_recursive(10) == 55